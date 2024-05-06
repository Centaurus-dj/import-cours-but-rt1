---
Author: Alexis Opolka
Subject: Infrastructure de sécurité
---

# R401 - Infrastructure de sécurité

## TP 3 - Proxy

1. ### - Questions Préliminaires

    1. Rappelez quel est le rôle d'un proxy direct

        Le rôle d'un proxy direct est d'authentifier le traffic
        de clients du réseau comme étant originel de son adresse IP.

        Cela permet de masquer l'adresse des machines utilisateurs sur
        le traffic internet.

    2. Quelle différence faites-vous avec le proxy inverse ?

        Le proxy inverse est principalement utilisé pour sécuriser des connexions
        serveurs. Il est utilisé comme machine hôte du traffic serveur-client
        afin d'empêcher d'exposer sur internet le serveur en question.

    3. Citez quelques exemples de solutions permettant de réaliser ces fonctions.

        Nginx, Apache et tout serveur web permettant de gérer du traffic entrant et sortant.

1. ### Proxy direct

    On met en place l'infrastructure nécessaire au TP:

    1. Installer le paquet `apache2` sur le serveur web. On gardera la configuration de base du serveur.

        > [!NOTE]
        > Vu que l'on utilise une VM `fedora`, nous allons devoir utiliser
        > le paquet `httpd` qui se trouve être le serveur Apache mais pour les distributions `RPM`.

        On fait:

        ```sh
        dnf install httpd
        ```

    1. Installer squid sur le serveur proxy.  
        Le fichier de configuration est dans `/etc/squid/squid.conf`.  
        Faire une copie de sauvegarde de ce fichier (`/etc/squid/squid.conf.bak`) avant de le modifier.

        On fait:

        ```sh
        dnf install squid
        cp /etc/squid/squid.conf{, .bak}
        ```

    1. Déterminer le plan d’adressage pour que le montage soit fonctionnel.

        Configurer les routes et les règles `nftables` pour que le poste client puisse joindre le serveur web et vice-versa.  
        On s’arrangera pour que le serveur WEB soit sur le plan d’adressage de la salle de TP.  
        Le serveur Proxy et le client Web pourront être des machines virtuelles.  
        Attention, il faut que le client web ait une interface graphique pour pouvoir utiliser un navigateur Web.

        On décide d'utiliser des machines virtuelles afin de "nous simplifier" les manipulations.  
        Ayant plus l'habitude de manipuler des machines sous Fedora, j'utiliserais donc des images [Fedora Cloud](https://fedoraproject.org/cloud/).

        | Machine                     | IP              |
        | --------------------------- | --------------- |
        | Serveur WEB                 | 172.168.1.1     |
        | Routeur Pate NAT            | 192.168.124.232 |
        | Routeur Pate Réseau Interne | 172.168.255.254 |
        | Serveur Proxy               | 192.168.124.130 |

        Ce qui nous donne ce schéma réseau suivant:

        ![tp-proxy-reseau-1](./src/img/tp-proxy-reseau-1.png)

        - #### Installation & Configuration du routeur sous Fedora

            On installe les paquets `nftables`:

            ```sh
            dnf install nftables
            ```

            puis on configure le NAT masquerade avec du port forwarding sur le serveur web:

            ```sh
            nft add table ip nat
            nft -- add chain ip nat prerouting { type nat hook prerouting priority -100 \; }
            nft add chain ip nat postrouting { type nat hook postrouting priority 100 \; }
            nft add rule ip nat prerouting tcp dport 80 dnat to 172.168.1.1
            nft add rule ip nat postrouting ip daddr 172.168.1.1 masquerade
            echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/95-IPv4-forwarding.conf
            sysctl -p /etc/sysctl.d/95-IPv4-forwarding.conf
            ```

            > [!NOTE]
            > On peut aussi spécifier des addresses IP statiques comme suit:
            >
            > ```sh
            > sudo nmcli con modify '<interface-name>' ifname <interface> ipv4.method manual ipv4.addresses <ip-address>/<netmask> gw4 <gateway-address>
            > ```

    1. Modifier le fichier de configuration de squid pour que le trafic de votre réseau local seulement soit capté par le serveur proxy.  
        Squid permet également de mettre en cache les pages web visitées.  
        On pourra modifier la valeur par défaut

        On
