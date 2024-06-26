---
Author: Alexis Opolka
Subject: Infrastructure de sécurité
---

# R401 - Infrastructure de sécurité

## À propos

Ce compte rendu comprend tous les TP de R401 en un seul fichier.

## Sommaire

- [R401 - Infrastructure de sécurité](#r401---infrastructure-de-sécurité)
  - [À propos](#à-propos)
  - [Sommaire](#sommaire)
  - [TP 1 - Cryptographie](#tp-1---cryptographie)
    - [Fonctions de Hachage](#fonctions-de-hachage)
  - [TP 2: VPN](#tp-2-vpn)
    - [1 - Questions Préliminaires](#1---questions-préliminaires)
    - [2 - Premiers tests](#2---premiers-tests)
    - [3 - Ajout d'une clé de chiffrement partagée](#3---ajout-dune-clé-de-chiffrement-partagée)
    - [4 - Finalisation](#4---finalisation)
    - [5 - Utilisation de TLS et PKI](#5---utilisation-de-tls-et-pki)
    - [6 - Pontage (bridge)](#6---pontage-bridge)
    - [Annexes TP 2](#annexes-tp-2)
      - [Configurations Réseau NetworkManager](#configurations-réseau-networkmanager)
        - [Passerelle](#passerelle)
      - [Configurations DNSMASQ](#configurations-dnsmasq)
        - [00-use-dnsmasq.conf](#00-use-dnsmasqconf)
        - [01-DNS-lan.conf](#01-dns-lanconf)
        - [02-DHCP-lan.conf](#02-dhcp-lanconf)
        - [03-DNS-iut.conf](#03-dns-iutconf)
        - [04-DHCP-iut.conf](#04-dhcp-iutconf)
  - [TP 3: Proxy](#tp-3-proxy)
    - [1 - Questions Préliminaires](#1---questions-préliminaires-1)
    - [2 - Proxy direct](#2---proxy-direct)
    - [3 - Proxy reverse](#3---proxy-reverse)
    - [Annexes TP 3](#annexes-tp-3)
      - [Configuration Squid](#configuration-squid)
      - [Configuration Nginx Proxy Inverse](#configuration-nginx-proxy-inverse)
        - [nginx.conf](#nginxconf)
        - [proxy\_params](#proxy_params)
  - [TP 4 - NAT et filtrage](#tp-4---nat-et-filtrage)

## TP 1 - Cryptographie

> [!NOTE]
> Vu que ce TP a été fait en ratrapage avec l'accord de M. Comby, je suis seul à faire la manipulation.

### Fonctions de Hachage

1. #### Calcul d'un condensé à l'aide de MD5

    1. Quel hash obtenez vous ?

        On fait:

        ```sh
        md5sum md5-checksum.txt
        ```

        Ce qui nous donne:

        ```sh
        e59ff97941044f85df5297e1c302d260  md5-checksum.txt
        ```

        où `e59ff97941044f85df5297e1c302d260` est le hash de notre fichier.

    1. Combien de condensés différents sont possibles ?
    1. La dernière propriété mathématique énoncée dans Wikipédia est-elle possible en pratique.

1. #### Vérification des propriétés de condensé

    1. Reprenez le fichier précédent et renommez-le. \
        Calculez son hash. Que remarquez-vous ?

        On renomme notre fichier `md5-checksum-modified.txt` puis on calcule notre hash:

        ```sh
        md5sum md5-checksum-modified.txt
        ```

        Ce qui nous donne:

        ```sh
        e59ff97941044f85df5297e1c302d260  md5-checksum-modified.txt
        ```

        On peut voir que le hash n'a pas changé.

    2. Modifiez maintenant le contenu du fichier. Recalculez le hash. Que remarquez-vous ?

        Après avoir changé le contenu du fichier, on obtient:

        ```sh
        b0b894e9da826be633b074417da4fd79  md5-checksum-modified.txt
        ```

        On peut voir que le hash a bien changé.

    3. Peut-on calculer le hash d'un fichier binaire (un executable par exemple) ? \
        Vérifiez votre réponse.

        On peut en effet calculer le hash d'un fichier binaire, par exemple le hash du binaire Bash:

        ```sh
        6c9105164270542e8b8b79ef790beee1  /bin/bash
        ```

1. #### Clefs de chiffrement

    1. Génération des clefs

        On fait:

        ```sh
        gpg --gen-key
        ```

        ou

        ```sh
        gpg --full-generate-key
        ```

        Ce qui nous donne:

        ```sh
        gpg: directory '~/.gnupg/openpgp-revocs.d' created
        gpg: revocation certificate stored as '~/.gnupg/openpgp-revocs.d/E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18.rev'
        public and secret key created and signed.

        pub   ed25519 2024-06-17 [SC] [expires: 2027-06-17]
            E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
        uid                      Alexis Opolka <contact@alexis-opolka.dev>
        sub   cv25519 2024-06-17 [E] [expires: 2027-06-17]
        ```

        1. Vérifiez que votre trousseau numérique contient bien votre clef publique avec la commande suivante:

            ```sh
            gpg --list-keys
            ```

            Quels sont les différents champs ?

            ---

            On peut voir notre clé dans notre trousseau:

            ```sh
            [keyboxd]
            ---------
            pub   ed25519 2024-06-17 [SC] [expires: 2027-06-17]
                E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
            uid           [ultimate] Alexis Opolka <contact@alexis-opolka.dev>
            sub   cv25519 2024-06-17 [E] [expires: 2027-06-17]
            ```

            Les différents champs sont:

            - `pub`
            - `uid`
            - `sub`

        1. Quelle commande permet de lister les clefs privées présentes sur votre machine ? \
            Comment peut-on savoir comment relier la clef publique et la clef privée ?

            La commande qui permet de lister les clefs privées est:

            ```sh
            gpg --list-secret-keys
            ```

            Nous avons, une empreinte similaire pour la clé privée et sa clé publique, dans notre cas nous avons:

            - empreinte clé privée: `E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18`
            - empreinte clé publique: `E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18`

            Vu qu'elles sont similaires, nous savons que la clé privée et la clé publique sont correspondantes.

    1. Diffusion de la clef publique

        On exporte notre clé:

        ```sh
        gpg --export --armor > gpg-pub-key.key
        ```

        1. Quel est le contenu de votre fichier ?

            Le contenu du fichier est:

            ```sh
            -----BEGIN PGP PUBLIC KEY BLOCK-----

            mDMEZnBSkxYJKwYBBAHaRw8BAQdA7t57Tjn0Vck11chnRKOtHn8Q489FHtTJcF3q
            0NyDOa+0KUFsZXhpcyBPcG9sa2EgPGNvbnRhY3RAYWxleGlzLW9wb2xrYS5kZXY+
            iJkEExYKAEEWIQTmEZtbcnz8ilyX5f0fWTbJZ/+6GAUCZnBSkwIbAwUJBaOagAUL
            CQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAKCRAfWTbJZ/+6GHOmAP42W/toxiJz
            adfMtVupXlaftvNmBV4XIfxqTMAumewKcwEAkKBowiNYmCk9LCsZWWIzjkD/7nTp
            KAL+fCe+AsIpvAe4OARmcFKTEgorBgEEAZdVAQUBAQdA0dKLR6lmZ2DSW430roUk
            dQku6u5Gqas718rsYPSYHSIDAQgHiH4EGBYKACYWIQTmEZtbcnz8ilyX5f0fWTbJ
            Z/+6GAUCZnBSkwIbDAUJBaOagAAKCRAfWTbJZ/+6GA2pAPwOUWp//mwPKiOtKKs/
            kLwVwjdmwqMVn+ZsCf7UkMjP2QEAkszkWxP3XQJk4BGj4OawB2NzZ/ydKvNl9Hg3
            WBEACgg=
            =J9Ep
            -----END PGP PUBLIC KEY BLOCK-----
            ```

            Comme nous pouvons le voir, nous avons exporté notre clé publique.

        1. Il est également possible d'exporter sa clef privée pour la mettre sur son ordinateur (si on ne l'a pas créée sur son ordinateur). \
            Pour cela, on utilise la commande suivante:

            ```sh
            gpg --export-secret-keys --armor > gpg-private-key.key
            ```

1. #### Chiffrement d'un fichier

   1. Pour envoyer un message chiffré à votre binôme, quelle clef faut-il utiliser pour chiffrer le message ?
      Pour cela, soit on la récupère sur un site de dépôt de lcef soit on l'importe à partir d'un fichier reçu.

      ```sh
      gpg --import gpg-pub-key.key
      ```

   1. Vérifier que la clef est importée sur votre trousseau numérique.

      On fait à nouveau:

      ```sh
      gpg --list-keys
      ```

      ce qui nous donne:

      ```sh
      [keyboxd]
      ---------
      pub   ed25519 2024-06-17 [SC] [expires: 2027-06-17]
          E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
      uid           [ultimate] Alexis Opolka <contact@alexis-opolka.dev>
      sub   cv25519 2024-06-17 [E] [expires: 2027-06-17]
      ```

      On peut voir que nous avons bien importé la clé publique.

   1. Générer un fichier texte `toto.txt` et chiffrez le avec la commande suivante:

      ```sh
      gpg --armor --recipient alexis.opolka@etu.umontpellier.fr --encrypt toto.txt
      ```

      Quel est le fichier généré qui correspond à la version chiffrée de `toto.txt` ?

      Le déchiffrage du fichier se fera avec la clé privée du destinaire. \
      La commande utilisée pour faire cela est:

      ```sh
      gpg --decrypt toto.txt.asc > toto.txt
      ```

      ---

      Le fichier qui correspond à la version chiffrée de `toto.txt` est `toto.txt.asc` avec le contenu suivant:

      ```sh
      -----BEGIN PGP MESSAGE-----

      hF4DtUDPdHXa7z4SAQdAM2ry0pUJ5DEQdGzqRU4Q12dg8RMlwVAd27IGU2OA4CUw
      L53oZ5qFgeGVgo/GHMgjQOptm+3x7pTy33np3s0+dlT6PnVyuRySYAhqmWxh+FVJ
      1HoBCQIQDPXb8QhUJTisHp4LjNg4KIia+UNikQVsuubKBvQxQ0ugVGRLoAGjapx8
      flNaC/D52Xsk66n87b76/G0qk30tvCWvcKiHq/rnnuAtUqrcADqCo//J0k3q3gjy
      a05KDYksA3tbZg6yvDnfCOc3r9tY/srYcr3Grg==
      =jItP
      -----END PGP MESSAGE-----
      ```

      On déchiffre le contenu du fichier, ce qui nous donne:

      ```sh
      This file has been encrypted with my GPG key
      ```

   1. Vérifier que le fichier déchiffré est équivalent au fichier initial.

      Le contenu du fichier initial est:

      ```txt
      This file has been encrypted with my GPG key
      ```

      et le contenu du fichier déchiffré est:

      ```txt
      This file has been encrypted with my GPG key
      ```

      Le fichier déchiffré est donc bien équivalent au fichier initial.

1. #### Signature numérique

   1. Signature d'un fichier

      1. Tester les commandes ci-dessus et vérifier leurs résultat.

          Pour vérifier la signature on peut utiliser la commande suivante:

          ```sh
          gpg --verify <fichier.gpg>
          ```

          ---

          - Signature avec Compression

              On fait:

              ```sh
              gpg --sign toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.gpg`.

              Où:

              ```sh
              gpg --verify toto.txt.gpg
              ```

              donne:

              ```sh
              gpg: Signature made Mon 17 Jun 2024 06:15:45 PM CEST
              gpg:                using EDDSA key E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
              gpg: Good signature from "Alexis Opolka <contact@alexis-opolka.dev>" [ultimate]
              ```

          - Signature sans Compression

              On fait:

              ```sh
              gpg --clearsign toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.asc`.

          - Export de la signature

              On fait:

              ```sh
              gpg --detach-sign toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.sig`.

              Où:

              ```sh
              gpg --verify toto.txt.sig
              ```

              donne:

              ```sh
              gpg: assuming signed data in 'toto.txt'
              gpg: Signature made Mon 17 Jun 2024 06:18:34 PM CEST
              gpg:                using EDDSA key E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
              gpg: Good signature from "Alexis Opolka <contact@alexis-opolka.dev>" [ultimate]
              ```

          - Signature et Chiffrement

              On fait:

              ```sh
              gpg -r contact@alexis-opolka.dev --armor --sign --encrypt toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.asc` avec le contenu suivant:

              ```sh
              -----BEGIN PGP MESSAGE-----

              hF4DtUDPdHXa7z4SAQdApAJZP75gr7EFGuQX3l4bn7lc+XngCUwm9IVqTGCKcCEw
              bti4GK7FeEfQi68YxF2eogQXCUop3mCrG8OXTvdrQHbfb8grMmEtcXEIItPCFA6o
              1MA3AQkCELfrQpFxSyCETvwSW03vnHaHgRnRlivrNyOoiycEFR97RiSTMdm9wx1z
              yoyji4Qggf6uZtebKLaSNSlXgQ22KFhwiK7MreYtfB0uCkpKQ4BLY4MPhmFEtEkb
              mh4IKp4I9H/SJq4jmJW7fWVCWbZmZ7t3j/zZTNJzqCO6Mb2dEOtQy7XbnHPXDMm4
              n0Hc5GhbKjDRhHcPBufk8Oq1BVm/lRxabnNaG18x1OpUpEhbDkTwHySurxae6/a5
              JwIMRIex4zXIxQqyCzDN7LlnQM8NvXNbtzIcXOK3Feh213hCbceCEEnITTBYbK8t
              jO6t6fMGYc34Ng==
              =VQo/
              -----END PGP MESSAGE-----
              ```

   1. Signature d'une clef publique

      1. Signer la clef de votre binôme avec la commande suivante:

          ```sh
          gpg --sign-key <id-clef>
          ```

          > [!NOTE]
          > Dans mon cas, je ne peux signer une autre clef que la mienne, je signe donc la clé GPG de [Fedora Project](https://fedoraproject.org) pour
          > la version 40 de la distribution linux Fedora.

          ---

          On fait:

          ```sh
          gpg --sign-key 115DF9AEF857853EE8445D0A0727707EA15B79CC
          ```

          > [!NOTE]
          > La clé GPG publique de Fedora pour la version 40 de la distribution a ces informations:
          >
          > ```sh
          > pub   rsa4096 2023-01-24 [SCE]
          >     115DF9AEF857853EE8445D0A0727707EA15B79CC
          > uid           [ unknown] Fedora (40) <fedora-40-primary@fedoraproject.org>
          > ```

          Ce qui nous donne:

          ```sh
          pub  rsa4096/0727707EA15B79CC
              created: 2023-01-24  expires: never       usage: SCE
              trust: unknown       validity: unknown
          [ unknown] (1). Fedora (40) <fedora-40-primary@fedoraproject.org>

          pub  rsa4096/0727707EA15B79CC
              created: 2023-01-24  expires: never       usage: SCE
              trust: unknown       validity: unknown
          Primary key fingerprint: 115D F9AE F857 853E E844  5D0A 0727 707E A15B 79CC

              Fedora (40) <fedora-40-primary@fedoraproject.org>

          Are you sure that you want to sign this key with your
          key "Alexis Opolka <contact@alexis-opolka.dev>" (1F5936C967FFBA18)
          ```

          Maintenant, lorsque l'on regarde la clé dans notre trousseau:

          ```sh
          pub   rsa4096 2023-01-24 [SCE]
              115DF9AEF857853EE8445D0A0727707EA15B79CC
          uid           [  full  ] Fedora (40) <fedora-40-primary@fedoraproject.org>
          ```

          On peut voir que nous avons une confiance totale à la clef puisque nous venons de la signer.

1. #### Utilisation d'un certificat

   - Nous installons OpenSSL:

      ```sh
      dnf install openssl
      ```

   - On génère sa clef:

      ```sh
      openssl genrsa -aes256 -out my-key.key 4096
      ```

   - On génère un certificat "débloqué":

      ```sh
      mv my-key.key my-key.key.lock
      openssl rsa -in my-key.key.lock -out my-key.key
      ```

   - On génère le fichier de demande de signature de notre clef et renseigner tous les champs demandés:

      ```sh
      openssl req -new -key my-key.key.lock -out certificat.csr
      ```

   - On auto-signe son certificat X509:

      ```sh
      openssl x509 -req -days 365 -in certificat.csr -signkey my-key.key.lock -out certificat.crt
      ```

   - On active Apache2

      ```sh
      systemctl start httpd
      ```

   - On active le module SSL sur le serveur Apache

      ```sh
      dnf install mod_ssl -y
      ```

   1. Effectuer la configuration sur le serveur. Faut-il prévoir quelque chose sur le client ? \
      Vérifier si le trafic est chiffré lors de l'envoi de la page web.

      Vu que l'on utilise Fedora au lieu d'une distribution Ubuntu/Debian, nous devons faire plusieurs actions en plus d'une simple
      configuration.

      - Configuration serveur

        - Création des répertoires `/etc/httpd/sites-available` et `/etc/ssl/www`

            On fait:

            ```sh
            mdkir /etc/httpd/sites-available /etc/ssl/www
            ```

        - Copie des certificats dans le répertoire

            On fait:

            ```sh
            cp certificat.crt /etc/ssl/www/
            cp my-key.key /etc/ssl/www/
            ```

        - Création du fichier de configuration `/etc/httpd/sites-available/centaurustasie.fr.conf`

            On fait:

            ```sh
            touch /etc/httpd/sites-available/centaurustasie.fr.conf
            ```

            Avec le contenu suivant:

            ```apacheconf
            <VirtualHost *:80>
                    ServerName      centaurustasie.fr
                    # On redirige le port HTTP vers le port HTTPS
                    Redirect / <https://centaurustasie.fr>
            </VirtualHost>
            <VirtualHost>
                    ServerName      centaurustasie.fr
                    DocumentRoot    /var/www/test

                    SSLEngine on
                    SSLCertificateFile      /etc/ssl/www/certificat.crt
                    SSLCertificateKeyFile   /etc/ssl/www/my-key.key
                    SSLProtocol all -SSLv2 -SSLv3
                    SSLHonorCipherOrder on
            </VirtualHost>
            ```

        - On inclue ensuite le fichier dans la configuration

            On ajoute à la fin du fichier `/etc/httpd/conf/httpd.conf`

            ```ini
            include sites-available/
            ```

      - Configuration Client

          On ajoute notre FQDN dans le fichier `/etc/hosts`:

          ```ini
          127.0.0.1 centaurustasie.fr
          ```

      On peut maintenant cURL le FQDN en HTTPS:

      ```sh
      curl -k https://centaurustasie.fr
      ```

      ce qui nous donne:

      ```html
      <!DOCTYPE html>
      <html lang="en">
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>SAE 401 - Test Page</title>
          </head>
          <body>
              Hello World, I'm not dead (yet)!
          </body>
      </html>
      ```

      On constate que l'on arrive bien à accéder à la page en HTTPS.

      Si l'on rend cURL un peu plus verbeux lors de la requête HTTPS, cela nous donne:

      ```sh
      - Host centaurustasie.fr:443 was resolved.
      - IPv6: (none)
      - IPv4: 127.0.0.1
      - Trying 127.0.0.1:443...
      - Connected to centaurustasie.fr (127.0.0.1) port 443
      - ALPN: curl offers h2,http/1.1
      - TLSv1.3 (OUT), TLS handshake, Client hello (1):
      - TLSv1.3 (IN), TLS handshake, Server hello (2):
      - TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
      - TLSv1.3 (IN), TLS handshake, Certificate (11):
      - TLSv1.3 (IN), TLS handshake, CERT verify (15):
      - TLSv1.3 (IN), TLS handshake, Finished (20):
      - TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
      - TLSv1.3 (OUT), TLS handshake, Finished (20):
      - SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / x25519 / RSASSA-PSS
      - ALPN: server accepted http/1.1
      - Server certificate:
      - subject: C=FR; ST=Occitanie; L=Béziers; O=IUT Béziers; OU=R&T; CN=centaurustasie.fr; emailAddress=<contact@centaurustasie.fr>
      - start date: Jun 17 17:32:42 2024 GMT
      - expire date: Jun 17 17:32:42 2025 GMT
      - issuer: C=FR; ST=Occitanie; L=Béziers; O=IUT Béziers; OU=R&T; CN=centaurustasie.fr; emailAddress=<contact@centaurustasie.fr>
      - SSL certificate verify result: self-signed certificate (18), continuing anyway.
      - Certificate level 0: Public key type RSA (4096/152 Bits/secBits), signed using sha256WithRSAEncryption
      - using HTTP/1.x

      > GET / HTTP/1.1
      > Host: centaurustasie.fr
      > User-Agent: curl/8.6.0
      > Accept: */*
      >
      - TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
      - TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
      - old SSL session ID is stale, removing
      < HTTP/1.1 200 OK
      < Date: Mon, 17 Jun 2024 19:51:57 GMT
      < Server: Apache/2.4.59 (Fedora Linux) OpenSSL/3.2.1
      < Last-Modified: Mon, 17 Jun 2024 19:44:25 GMT
      < ETag: "f0-61b1b31519b73"
      < Accept-Ranges: bytes
      < Content-Length: 240
      < Content-Type: text/html; charset=UTF-8
      <

      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SAE 401 - Test Page</title>
      </head>
      <body>
        Hello World, I'm not dead (yet)!
      </body>
      * Connection #0 to host centaurustasie.fr left intact
      ```

      On peut voir que l'on a bien une interaction SSL qui s'effectue lors de la requête HTTPS GET.

      Aussi visible sur cette prise sous Wireshark:

      ![ssl-centaurustasie.fr](./src/img/ssl-centaurustasie.fr.png)

   1. Quels sont d'après vous les risques pour un administrateur réseau d'avoir des utilisateurs qui utilisent principalement des sites en HTTPS ?

      Un risque qu'il pourrait y avoir, c'est d'être incapable de connaître les informations reçues et envoyées, ou bien les actions menées
      par les utilisateurs puisque le traffic est chiffré.

1. #### Client mail

    1. Installer et configurer sur votre machine le client Email Thunderbird. \
        Envoyez à votre binôme un courrier à la fois chiffré et signé.

        Nous n'avons qu'à importer notre clé GPG dans Thunderbird:

        ![thunderbird-key-import](./src/img/thunderbird-key-import.png)

        > [!NOTE]
        > Nous importons une autre clé que celle de la boîte mail en question car j'avais déjà
        > une clé présente, au lieu de générer à nouveau une clé PGP, j'ai préféré importer la clé
        > utilisée lors des manipulations plus en haut.

        Nous voyons que l'email que l'on a envoyé a été signé et crypté.

        ![thunderbird-encrypted-signed-email](./src/img/thunderbird-encrypted-signed-email.png)

## TP 2: VPN

### 1 - Questions Préliminaires

1. Configurer la passerelle de sorte que le client interne ait accès à la partie Internet.
    Il s'agira de mettre du NAT en place.

    En premiers lieux, on configure la passerelle afin de pouvoir avoir un schéma fonctionnel. \
    On installe `dnsmasq` et `firewalld` afin de permettre à notre routeur de faire DNS et DHCP.

    - On configure les interfaces réseaux afin que le service `NetworkManager-wait-online.service` ne tourne pas en essayant d'alimenter une
        adresse IP sur nos trois interfaces.

        - On change d'abord leur nom:

            Vu que l'on a ajouté deux interfaces en plus, elles sont nommées par défaut en `Wired connection X` où X correspond à l'interface. \
            Cela ne nous permet pas de distinguer facilement leur attaches via `nmcli`, nous les renommons alors:

            ```sh
            nmcli con modify "Wired connection 1" connection.id "iut-net eth1"
            nmcli con modify "Wired connection 2" connection.id "internal-net eth2"
            ```

        Nous allons ensuite dans le répertoire `/etc/NetworkManager/system-connections/` afin de configurer "en dur" la configuration:

        - Pour `eth1`:

            ```ini
            [connection]
            id=iut-net eth1
            uuid=c1682d93-6910-3916-a30f-71675e5d0508
            type=ethernet
            autoconnect-priority=-999
            interface-name=eth1
            timestamp=1719335741

            [ethernet]

            [ipv4]
            address1=10.202.255.254/16
            method=manual

            [ipv6]
            addr-gen-mode=default
            method=auto

            [proxy]
            ```

        - Pour `eth2`:

            ```ini
            [connection]
            id=internal-net eth2
            uuid=6e55c895-cba4-358e-9932-eba3fb9c3c8f
            type=ethernet
            autoconnect-priority=-999
            interface-name=eth2
            timestamp=1719335741

            [ethernet]

            [ipv4]
            address1=192.168.1.254/24
            method=manual

            [ipv6]
            addr-gen-mode=default
            method=auto

            [proxy]
            ```

    - On installe les paquets:

        ```sh
        dnf install dnsmasq firewalld
        ```

    - Nous devons dire à NetworkManager d'utiliser dnsmasq, pour cela on crée le fichier [`00-use-dnsmasq.conf`](#00-use-dnsmasqconf) avec le contenu suivant:

        ```ini
        [main]
        dns=dnsmasq
        ```

    - Nous avons deux réseaux qu'il va falloir définir, le réseau IUT et le réseau interne

        Nous configurons alors `dnsmasq` en créant les fichiers suivants: [`01-DNS-lan.conf`](#01-dns-lanconf), [`02-DHCP-lan.conf`](#02-dhcp-lanconf),
        [`03-DNS-iut.conf`](#03-dns-iutconf) et [`04-DHCP-iut.conf`](#04-dhcp-iutconf).

    - Nous devons maintenant ouvrir le firewall, pour cela nous faisons:

        ```sh
        firewall-cmd --set-default-zone FedoraServer
        firewall-cmd --get-services
        firewall-cmd --zone=FedoraServer --permanent --add-service=dhcp
        firewall-cmd --zone=FedoraServer --permanent --add-service=dns
        firewall-cmd --reload
        ```

    - Coté clients, nous devons modifier le fichier de connections NetworkManager

        Sur le client IUT et le client réseau interne, nous modifions le fichier `cloud-init-eth0.nmconnection`
        pour que la ligne:

        ```ini
        [ipv4]
        may-fail=false
        method=link-local
        ```

        devienne:

        ```ini
        [ipv4]
        may-fail=false
        method=auto
        ```

    Après cela, nous configurons le NAT afin de pouvoir accéder à Internet:

    > [!NOTE]
    > Dans le cas où `nft` renverrait une erreur de commande inconnue, veuillez installer `nftables` comme ci-dessous:
    >
    > ```sh
    > dnf install nftables
    > ```

    ```sh
    nft add table nat
    nft -- add chain nat prerouting { type nat hook prerouting priority -100 \; }
    nft add chain nat postrouting { type nat hook postrouting priority 100 \; }
    nft add rule nat postrouting oifname "eth0" masquerade
    nft add rule nat postrouting oifname "eth1" snat to 10.202.255.254
    ```

    N'oublions pas d'activer temporairement le routage IPv4:

    ```sh
    sudo echo "1" > /proc/sys/net/ipv4/ip_forward
    ```

    Comme l'on peut le voir, cela nous permet d'accéder à Internet:

    - Du client IUT

        - ![client-passerelle](./src/img/interne-internet-client-passerelle.png)
        - ![passerelle-internet](./src/img/interne-internet-passerelle-internet.png)

    On peut aussi accéder du réseau interne au réseau de l'IUT:

    - Du client interne

        - ![client-passerelle](./src/img/interne-iut-client-passerelle.png)
        - ![passerelle-iut](./src/img/interne-iut-iut-passerelle.png)

1. Donner la configuration (adresses, masques, routes, iptables) de chacun des équipements.

    | Machine                          | IP                                  |
    | -------------------------------- | ----------------------------------- |
    | Client IUT                       | 10.202.1.1/16 (Bail DHCP Statique)  |
    | Passerelle - Pate réseau IUT     | 10.202.255.254/16                   |
    | Passerelle - Pate Internet       | 192.168.124.130                     |
    | Passerelle - Pate Réseau Interne | 192.168.1.254/24                    |
    | Client Réseau Interne            | 192.168.1.1/24 (Bail DHCP Statique) |

    Voir les fichiers de configuration en [annexes](#annexes-tp-2) afin de voir en détail la configuration.

1. Installer OpenVPN et la librairie `lzo` sur la passerellle et sur le client

    Nous installons OpenVPN sur la passerelle et sur le client:

        On fait:

        ```sh
        dnf install openvpn lzo
        ```

### 2 - Premiers tests

1. Vérifier dans un premier temps la liste des interfaces réseau sur votre machine.
    Ensuite, on cherche à vérifier si OpenVPN peut être lancé à la main. \
    Sur la passerelle, exécuter la commande suivante:

    ```sh
    openvpn --dev tun0 --ifconfig 192.168.10.1 192.168.10.2
    ```

    Et sur le client OpenVPN celle indiquée ci-dessous:

    ```sh
    openvpn --remote <ip-passerelle> --dev tun0 --ifconfig 192.168.10.2 192.168.10.1
    ```

    ---

    Avant tout, nous devons ouvrir les ports du firewall afin que le port `1194` soit ouvert à la communication
    entre les deux machines:

    Sur le client:

    ```sh
    firewall-cmd --add-port=1194/udp
    ```

    et sur la passerelle:

    ```sh
    firewall-cmd --zone FedoraServer --add-port=1194/udp
    ```

    > [!NOTE]
    > Il semblerait que sur Fedora, ce port ne soit pas ouvert par défaut, d'où le besoin
    > de l'ouvrir manuellement.

    Sur la passerelle, nous faisons:

    ```sh
    openvpn --dev tun0 --ifconfig 192.168.10.1 192.168.10.2 --proto udp4
    ```

    > [!NOTE]
    > Sur Fedora, il semblerait être nécessaire d'ajouter `--proto udp4` afin qu'ils puissent communiquer ensembles.
    > Sinon, la passerelle ne semblait pas vouloir communiquer en IPV4.

    et sur le client nous faisons:

    ```sh
    openvpn --remote 192.168.1.254 --dev tun0 --ifconfig 192.168.10.2 192.168.10.1
    ```

    Ce qui nous donne:

    - Pour le client:

        ```sh
        2024-06-25 19:48:08 DEPRECATION: No tls-client or tls-server option in configuration detected. OpenVPN 2.7 will remove the functionality to run a VPN without TLS. See the examples section in the manual page for examples of a similar quick setup with peer-fingerprint.
        2024-06-25 19:48:08 OpenVPN 2.6.9 x86_64-redhat-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] [DCO]
        2024-06-25 19:48:08 library versions: OpenSSL 3.1.1 30 May 2023, LZO 2.10
        2024-06-25 19:48:08 DCO version: N/A
        2024-06-25 19:48:08 ******* WARNING *******: '--cipher none' was specified. This means NO encryption will be performed and tunnelled data WILL be transmitted in clear text over the network! PLEASE DO RECONSIDER THIS SETTING!
        2024-06-25 19:48:08 ******* WARNING *******: '--auth none' was specified. This means no authentication will be performed on received packets, meaning you CANNOT trust that the data received by the remote side have NOT been manipulated. PLEASE DO RECONSIDER THIS SETTING!
        2024-06-25 19:48:08 ******* WARNING *******: All encryption and authentication features disabled -- All data will be tunnelled as clear text and will not be protected against man-in-the-middle changes. PLEASE DO RECONSIDER THIS CONFIGURATION!
        2024-06-25 19:48:08 TUN/TAP device tun0 opened
        2024-06-25 19:48:08 net_iface_mtu_set: mtu 1500 for tun0
        2024-06-25 19:48:08 net_iface_up: set tun0 up
        2024-06-25 19:48:08 net_addr_ptp_v4_add: 192.168.10.2 peer 192.168.10.1 dev tun0
        2024-06-25 19:48:08 TCP/UDP: Preserving recently used remote address: [AF_INET]192.168.1.254:1194
        2024-06-25 19:48:08 UDPv4 link local (bound): [AF_INET][undef]:1194
        2024-06-25 19:48:08 UDPv4 link remote: [AF_INET]192.168.1.254:1194
        2024-06-25 19:48:12 Peer Connection Initiated with [AF_INET]192.168.1.254:1194
        2024-06-25 19:48:13 Initialization Sequence Completed
        ```

    - Pour le serveur:

        ```sh
        2024-06-25 19:47:52 DEPRECATION: No tls-client or tls-server option in configuration detected. OpenVPN 2.7 will remove the functionality to run a VPN without TLS. See the examples section in the manual page for examples of a similar quick setup with peer-fingerprint.
        2024-06-25 19:47:52 OpenVPN 2.6.9 x86_64-redhat-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] [DCO]
        2024-06-25 19:47:52 library versions: OpenSSL 3.1.1 30 May 2023, LZO 2.10
        2024-06-25 19:47:52 DCO version: N/A
        2024-06-25 19:47:52 ******* WARNING *******: '--cipher none' was specified. This means NO encryption will be performed and tunnelled data WILL be transmitted in clear text over the network! PLEASE DO RECONSIDER THIS SETTING!
        2024-06-25 19:47:52 ******* WARNING *******: '--auth none' was specified. This means no authentication will be performed on received packets, meaning you CANNOT trust that the data received by the remote side have NOT been manipulated. PLEASE DO RECONSIDER THIS SETTING!
        2024-06-25 19:47:52 ******* WARNING *******: All encryption and authentication features disabled -- All data will be tunnelled as clear text and will not be protected against man-in-the-middle changes. PLEASE DO RECONSIDER THIS CONFIGURATION!
        2024-06-25 19:47:52 TUN/TAP device tun0 opened
        2024-06-25 19:47:52 net_iface_mtu_set: mtu 1500 for tun0
        2024-06-25 19:47:52 net_iface_up: set tun0 up
        2024-06-25 19:47:52 net_addr_ptp_v4_add: 192.168.10.1 peer 192.168.10.2 dev tun0
        2024-06-25 19:47:52 UDPv4 link local (bound): [AF_INET][undef]:1194
        2024-06-25 19:47:52 UDPv4 link remote: [AF_UNSPEC]
        2024-06-25 19:48:08 Peer Connection Initiated with [AF_INET]192.168.1.24:1194
        2024-06-25 19:48:10 Initialization Sequence Completed
        ```

1. Vérifiez que la connexion est correctement effectuée en réalisant un ping judicieux.

    Vu que l'on a établi une connexion VPN en Peer to Peer, nous pouvons simplement ping notre pair et voir s'il répond.

    Du client, on fait:

    ```sh
    ping 192.168.10.1
    ```

    ce qui nous donne:

    ```sh
    PING 192.168.10.1 (192.168.10.1) 56(84) bytes of data.
    64 bytes from 192.168.10.1: icmp_seq=1 ttl=64 time=1.85 ms
    64 bytes from 192.168.10.1: icmp_seq=2 ttl=64 time=2.01 ms
    64 bytes from 192.168.10.1: icmp_seq=3 ttl=64 time=1.39 ms
    64 bytes from 192.168.10.1: icmp_seq=4 ttl=64 time=6.80 ms
    64 bytes from 192.168.10.1: icmp_seq=5 ttl=64 time=1.28 ms
    --- 192.168.10.1 ping statistics ---
    5 packets transmitted, 5 received, 0% packet loss, time 4006ms
    rtt min/avg/max/mdev = 1.280/2.665/6.801/2.085 ms
    ```

1. Lister les interfaces présentes sur vos machines. Que constatez-vous ?

    Lorsque l'on liste les interfaces, on peut voir l'arrivée d'une interface `tun0`:

    ```sh
    lo               UNKNOWN        127.0.0.1/8 ::1/128
    eth0             UP             192.168.1.24/16
    tun0             UNKNOWN        192.168.10.2 peer 192.168.10.1/32 fe80::3dab:715a:2dbd:9b8b/64
    ```

    Cette interface correspond bien au nom que l'on a donné lors de la commande openvpn et est
    bien sur une connection P2P.

1. Pendant que le ping fonctionne, capturez une trame à l'aide de wireshark sur chacune des deux interfaces du client openvpn. \
    Que constatez-vous ? Expliquez et détaillez l'encapsulation du paquet capturé sur l'interface réseau ethernet de votre machine.

    - ![openvpn-capture-1](./src/img/openvpn-capture-1.png)

    Comme l'on peut le voir au dessus, une transmission VPN avec notre configuration actuelle fait apparaitre
    des paquets `P_CONTROL_HARD_RESET_SERVER_V2`, toute fois, la stack d'une communication VPN avec OpenVPN
    est:

    - ![openvpn-net-stack](./src/img/openvpn-net-stack.png)

    Donc avec l'encapsulation suivante:

    - Ethernet
    - IP
    - UDP/TCP
    - OpenVPN

    où UDP peut être interchangé avec TCP selon la configuration et OpenVPN étant de la couche applicative permettant de
    transmettre les informations propres à la discussion VPN, dans notre cas, notre ping.

1. Démarrez un service non chiffré quelconque sur la passerelle (telnet, ftp, etc.). \
    Capturer les paquets échangés sur l'interface ethernet. Sont-ils chiffrés ?

    Nous devons tout d'abord installer un serveur FTP sur la passerelle:

    ```sh
    dnf install vsftpd
    ```

    puis nous le démarrons et configurons le firewall:

    ```sh
    systemctl start vsftpd
    firewall-cmd --add-service=ftp
    ```

    Du client, nous essayons d'accéder au serveur FTP:

    ```sh
    ftp -p 192.168.10.1 21
    ```

    ce qui nous donne:

    ```sh
    Connected to 192.168.10.1 (192.168.10.1).
    220 (vsFTPd 3.0.5)
    Name (192.168.10.1:root): fedora
    331 Please specify the password.
    Password:
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp>
    ```

    Et comme l'on peut le voir ci-dessous, les paquets sont transmis en clair sur le réseau:

    - ![openvpn-ftp-clear](./src/img/openvpn-ftp-clear-communication.png)

### 3 - Ajout d'une clé de chiffrement partagée

Créer une clée partagée sur le serveur à l'aide de la commande suivante:

```sh
openvpn --genkey --secret static.key
```

 >[!NOTE]
 > Au vu d'une note de `deprecation`, nous faisons la commande suivante:
 >
 > ```sh
 > openvpn --genkey secret static.key
 > ```

1. Que contient le fichier `static.key` ?

    Le fichier contient une clé statique OpenVPN:

    ```txt
    #
    # 2048 bit OpenVPN static key
    #

    -----BEGIN OpenVPN Static key V1-----
    8f4b73735fd63db512ef282c706b6aab
    0dc024fdc78e5927f75bde1d1cdc632a
    7940362235bcf7fdb67af0ee4979543b
    079a95e8f988c6f1c9170b02a5647e9e
    74a5e4dbaefeee7aab4516d18c9f4514
    051773c056b6f492d06aa8d62481dcc5
    03d3e22fee5852a8b6e3d628f265c1a7
    e6111edcefba8ee584f642ebeb642d68
    21190b702b256d80cdd767b5f3dfb823
    8ec031081dfc307b572585d7d8c24267
    9f85c20b3bb4f5167dbd60960e434ade
    5ccfe9705ce7ac8eaa32052b4a0f3de7
    358de9e39eb63c4ec607e185c10cd105
    86cb23b81bbbc396606bca790cb609d6
    9073105e4e0e5770ea01f3a3bf4c8e67
    61cbe953e0f307312a39d611dd31fe1e
    -----END OpenVPN Static key V1-----
    ```

1. De quel type de clé s'agit-il ?

    Selon la documentation de openvpn, accessible [ici](https://openvpn.net/community-resources/openvpn-cryptographic-layer/),
    la clé static est composée de quatres clés indépendantes: `HMAC send`, `HMAC receive`, `encrypt` et `decrypt`.

1. Quelle est sa longueur ?

    Elle fait 2048 bits de longueur.

1. Il faut maintenant transférer cette clé de façon sécurisée sur le client. Comment procéder ?

    Relancez le VPN entre les deux machines en concaténant aux commandes précédentes la directive suivante:

    ```sh
    --secret /chemin/vers/votre/clef
    ```

    ---

    On peut transmettre de façon sécurisée la clef symmétrique via SFTP.

    On se connecte maintenant, en faisant:

    - Sur le client:

        ```sh
        openvpn --remote 192.168.1.254 --dev tun0 --ifconfig 192.168.10.2 192.168.10.1 --proto udp4 --secret static.key --cipher AES-256-CBC
        ```

    - Sur la passerelle:

        ```sh
        openvpn --dev tun0 --ifconfig 192.168.10.1 192.168.10.2 --proto udp4 --secret static.key --cipher AES-256-CBC
        ```

    > [!NOTE]
    > Nous devons préciser l'option `cipher` avec la valeur `AES-256-CBC` car par défaut, OpenVPN essaie d'utiliser `BF-CBC` qui est
    > déprécié pour des raisons de sécurité sur les versions 3.X+ de OpenSSL.

1. Vérifier le bon fonctionnement du réseau.

    On peut toujours ping notre pair:

    ```sh
    ping -c 4 192.168.10.1
    ```

    ce qui nous donne:

    ```sh
    PING 192.168.10.1 (192.168.10.1) 56(84) bytes of data.
    64 bytes from 192.168.10.1: icmp_seq=1 ttl=64 time=1.17 ms
    64 bytes from 192.168.10.1: icmp_seq=2 ttl=64 time=1.13 ms
    64 bytes from 192.168.10.1: icmp_seq=3 ttl=64 time=1.71 ms
    64 bytes from 192.168.10.1: icmp_seq=4 ttl=64 time=1.85 ms

    --- 192.168.10.1 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3005ms
    rtt min/avg/max/mdev = 1.132/1.465/1.853/0.321 ms
    ```

1. Montrez que vos communications au travers du vpn sont maintenant chiffrés.

    Pour gagner de la bande passante, vous pouvez également ajouter la directive suivante aux commandes précédentes.

    ```sh
    --comp-lzo --keepalive 10 60 --float
    ```

    ---

    - ![openvpn-symmetric-key-network-encrypted](./src/img/openvpn-symmetric-key-network-crypted.png)

    On peut voir que notre traffic est bien chiffré.

1. Tester et expliquer

### 4 - Finalisation

Pour se simplifier la vie, il est préférable de mettre au point un fichier de configuration.
Le démarrage d’openvpn se fera alors de la façon suivante:

```sh
openvpn /path/to/pc.conf
```

Avec le fichier de configuration suivante (pour le client):

```ini
dev tun
remote ip_passerelle
ifconfig 192.168.10.2 192.168.10.1
secret /etc/openvpn/static.key
comp-lzo
keepalive 10 60
float
```

1. Créer le fichier de configuration du serveur, et tester le bon fonctionnement du tout.

    On crée le fichier de confiuuration serveur:

    ```ini
    dev tun
    ifconfig 192.168.10.1 192.168.10.2
    secret /etc/openvpn/static.key
    comp-lzo
    keepalive 10 60
    float
    cipher AES-256-CBC
    ```

    Comme on peut le voir des logs vpn clients, nous accédons bien à initialiser
    la connexion VPN avec le serveur:

    ```sh
    2024-06-26 12:04:50 DEPRECATED OPTION: The option --secret is deprecated.
    2024-06-26 12:04:50 WARNING: Compression for receiving enabled. Compression has been used in the past to break encryption. Sent packets are not compressed unless "allow-compression yes" is also set.
    2024-06-26 12:04:50 DEPRECATION: No tls-client or tls-server option in configuration detected. OpenVPN 2.7 will remove the functionality to run a VPN without TLS. See the examples section in the manual page for examples of a similar quick setup with peer-fingerprint.
    2024-06-26 12:04:50 OpenVPN 2.6.9 x86_64-redhat-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] [DCO]
    2024-06-26 12:04:50 library versions: OpenSSL 3.1.1 30 May 2023, LZO 2.10
    2024-06-26 12:04:50 DCO version: N/A
    2024-06-26 12:04:50 TUN/TAP device tun0 opened
    2024-06-26 12:04:50 net_iface_mtu_set: mtu 1500 for tun0
    2024-06-26 12:04:50 net_iface_up: set tun0 up
    2024-06-26 12:04:50 net_addr_ptp_v4_add: 192.168.10.2 peer 192.168.10.1 dev tun0
    2024-06-26 12:04:50 TCP/UDP: Preserving recently used remote address: [AF_INET]192.168.1.254:1194
    2024-06-26 12:04:50 UDPv4 link local (bound): [AF_INET][undef]:1194
    2024-06-26 12:04:50 UDPv4 link remote: [AF_INET]192.168.1.254:1194
    2024-06-26 12:04:52 Peer Connection Initiated with [AF_INET]192.168.1.254:1194
    2024-06-26 12:04:52 Initialization Sequence Completed
    ```

### 5 - Utilisation de TLS et PKI

1. À l’aide de votre moteur de recherche préféré, expliquez en quelques phrases ce qu’est TLS.

    La première étape pour obtenir une véritable configuration est de construire une PKI (public key infrastructure), qui consiste en :

    - ▷Un certificat séparé (clef publique) et une clé privée pour le serveur et pour chaque client.
    - ▷Une autorité de certification qui signe les certificats précédents.

    On construit d’abord l’autorité de certification (CA) au moyen des scripts fournis et distribués dans le paquet : **easy-rsa**

    ---

    Selon la définition de Cloudflare, accessible [ici](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/),
    le protocole TLS a été développé par l'IETF et est dérivé du protocole SSL version 3.1 développé par Netscape.

    TLS est principalement utilisé pour garantir la confidentialité et la sécurité des communications sur Internet. \
    On connait principalement TLS avec son implémentation dans le protocole HTTPS afin de garantir la sécurité des
    communications web.

    On installe le paquet `easy-rsa`:

    ```sh
    dnf install easy-rsa
    ```

1. Que signifie X509 ? Suivre la procédure pour générer les clefs, les certificats et les procédures d’échange de clefs indiquée
    à l’adresse suivante [community.openvpn.net](https://community.openvpn.net/openvpn/wiki/EasyRSA3-OpenVPN-Howto)

    X509 est un standard utilisé pour définir les clés publiques, notamment des protocoles SSL/TLS.

1. Vous pouvez copier le fichier "vars.exemple" dans un fichier nommé "vars".
    Ensuite, mettez à jour les informations du certificat X509 (fichier vars).

    Réaliser l’initialisation de la PKI sur le CA : générer les paires de clefs ainsi que le certificat à l’aide les commandes suivantes :

    ```sh
    /usr/share/easy-rsa/ ./easyrsa init-pki
    /usr/share/easy-rsa/ ./easyrsa build-ca
    ```

1. Où sont stockées les clefs ? À quoi correspondent les différents fichiers ?

    Les clefs sont stockées dans le répertoire `./pki/private/`.

1. Sur le client et le serveur, générer une paire de clef ainsi que la requête pour l’échange à l’aide des commandes suivantes :

    ```sh
    ./easyrsa init-pki
    ./easyrsa gen-req PASSERELLE nopass
    ```

    ```sh
    ./easyrsa init-pki
    ./easyrsa gen-req CLIENTEXTERNE
    ```

1. Envoyer les requêtes du serveur et du client sur le CA, puis importez-les à l’aide de la commande:

    ```sh
    ./easyrsa import-req Chemin/vers/les/fichiers/req PASSERELLE
    ./easyrsa import-req Chemin/vers/les/fichiers/req CLIENT
    ```

    ce qui nous donne:

    ```sh
    Notice
    ------
    Request successfully imported with short-name: test-client
    This request is now ready to be signed.
    ```

1. Signer les clefs publiques pour la passerelle et le client avec les commandes

    ```sh
    ./easyrsa sign-req client CLIENT
    ./easyrsa sign-req server PASSERELLE
    ```

    ce qui nous donne:

    ```sh
    Please check over the details shown below for accuracy. Note that this request
    has not been cryptographically verified. Please be sure it came from a trusted
    source or that you have verified the request checksum with the sender.
    You are about to sign the following certificate:

    Requested CN:   'test-client'
    Requested type: 'client'
    Valid for:      '825' days

    subject=
        commonName                = test-client

    Type the word 'yes' to continue, or any other input to abort.
    Confirm request details: yes

    Using configuration from /usr/share/easy-rsa/3.2.0/pki/1d3e8354/temp.0.1
    Enter pass phrase for /usr/share/easy-rsa/3.2.0/pki/private/ca.key:
    Check that the request matches the signature
    Signature ok
    The Subject's Distinguished Name is as follows
    commonName            :ASN.1 12:'test-client'
    Certificate is to be certified until Sep 29 13:42:09 2026 GMT (825 days)

    Write out database with 1 new entries
    Data Base Updated

    Notice
    ------
    Certificate created at:
    * /usr/share/easy-rsa/3.2.0/pki/issued/test-client.crt
    ```

1. Qu’est-ce qu’un échange de Diffie-Hellman ?

    Selon l'article [wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange), un échange Diffie-Hellman est un échange
    de clé cryptographiques sécurisé dans un espace de communication publique.

1. Construire ensuite les paramètres de l’échange de clés par Diffie-Helmann avec la commande suivante :

    ```sh
    ./easyrsa gen-dh
    ```

    Après un temps d'attente, nous obtenons:

    ```sh
    DH parameters appear to be ok.

    Notice
    ------

    DH parameters of size 2048 created at:
    - /usr/share/easy-rsa/3.2.0/pki/dh.pem
    ```

1. Tester votre configuration, et faire valider par l’enseignant que cela fonctionne.

### 6 - Pontage (bridge)

Maintenant que votre VPN est en place, il reste à configurer votre serveur afin que :

- ▷Les deux clients puissent communiquer sans problème.
- ▷Les deux clients accèdent à internet par la passerelle

Montrez comment, avec l’utilitaire bridge-utils, vous pouvez procéder

1. Faites valider par l’enseignant que cela fonctionne.

### Annexes TP 2

#### Configurations Réseau NetworkManager

##### Passerelle

- `eth1`:

    ```ini
    [connection]
    id=iut-net eth1
    uuid=c1682d93-6910-3916-a30f-71675e5d0508
    type=ethernet
    autoconnect-priority=-999
    interface-name=eth1
    timestamp=1719335741

    [ethernet]

    [ipv4]
    address1=10.202.255.254/16
    method=manual

    [ipv6]
    addr-gen-mode=default
    method=auto

    [proxy]
    ```

- `eth2`:

    ```ini
    [connection]
    id=internal-net eth2
    uuid=6e55c895-cba4-358e-9932-eba3fb9c3c8f
    type=ethernet
    autoconnect-priority=-999
    interface-name=eth2
    timestamp=1719335741

    [ethernet]

    [ipv4]
    address1=192.168.1.254/24
    method=manual

    [ipv6]
    addr-gen-mode=default
    method=auto

    [proxy]
    ```

#### Configurations DNSMASQ

##### 00-use-dnsmasq.conf

```ini
[main]
dns=dnsmasq
```

##### 01-DNS-lan.conf

```ini
### local domain
local=/centaurustasie.dev/

### Hostname mapping
addn-hosts=/etc/dnsmasq.hosts

domain-needed
bogus-priv

expand-hosts

### Interfaces to listen on
interface=lo
interface=eth2

### Upstream public net DNS server
no-poll
server=1.1.1.1
server=8.8.8.8
```

##### 02-DHCP-lan.conf

```ini
### The domain the DHCP is responsible for:
### The local FQDN, the internal network and the local network
domain=centaurustasie.dev,192.168.1.0/24

### Interface to listen on
interface=eth2

### DHCP configuration

dhcp-authoritative
dhcp-option=1,255.255.255.0
dhcp-option=3,192.168.1.254
dhcp-option=6,192.168.1.254

### Assign fixed IP addresses base on MAC address
dhcp-host=0c:bf:be:51:00:00,InternalClient,192.168.1.1,infinite

dhcp-range=tag:eth2,192.168.1.10,192.168.1.200,4h
```

##### 03-DNS-iut.conf

```ini
### local domain
local=/iutbeziers.fr/

### Hostname mapping
addn-hosts=/etc/dnsmasq.hosts

domain-needed
bogus-priv

expand-hosts

### Interfaces to listen on
interface=eth1

### Upstream public net DNS server
no-poll
server=1.1.1.1
server=8.8.8.8
```

##### 04-DHCP-iut.conf

```ini
### The domain the DHCP is responsible for:
### The IUT network
domain=iutbeziers.fr,10.202.0.0/16

### Interface to listen on
interface=eth1

### DHCP configuration

dhcp-authoritative
dhcp-option=1,255.255.0.0
dhcp-option=3,10.202.255.254
dhcp-option=6,10.202.255.254

### Assign fixed IP addresses base on MAC address
dhcp-host=0c:40:f6:0c:00:00,IUTClient,10.202.1.1,infinite

dhcp-range=tag:eth1,10.202.0.1,10.202.0.253,4h
```

## TP 3: Proxy

### 1 - Questions Préliminaires

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

### 2 - Proxy direct

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

    | Machine                       | IP                 |
    | ----------------------------- | ------------------ |
    | Serveur WEB                   | 10.10.10.1/24      |
    | Routeur - Pate Réseau Externe | 10.10.10.254/24    |
    | Routeur - Pate Réseau Interne | 172.168.100.254/24 |
    | Routeur - Pate Réseau NAT     | 192.168.124.254/24 |
    | Serveur Proxy                 | 172.168.100.100/24 |
    | Client                        | 172.168.100.1/24   |

    Ce qui nous donne ce schéma réseau suivant:

    ![tp-proxy-reseau-1](./src/img/tp-proxy-reseau-1.png)

    - #### Configuration du routeur

        On configure notre routeur qui va nous permettre d'accéder à internet ainsi que d'accéder à nos deux réseaux:

        ```ini
        conf t

        ### Configuration du routage
        ip routing
        ip route 0.0.0.0 0.0.0.0 192.168.124.1 # Routeur de la machine hôte

        ### Configuration des interfaces
        int F0/0 # Interface Interne
        ip address 172.168.100.254 255.255.255.0
        no shut
        ip nat inside
        exit
        int F1/0 # Interface NAT
        ip address 192.168.124.254 255.255.255.0
        no shut
        ip nat outside
        exit
        int F0/1 # Interface Externe
        ip address 10.10.10.254 255.255.255.0
        ip nat inside
        no shut
        exit

        ### Configuration du NAT
        access-list 1 permit 172.168.100.0 0.0.0.255
        access-list 1 permit 10.10.10.0 0.0.0.255
        ip nat inside source list 1 interface F1/0 overload # NAT pour internet

        ### Enregistrement de la configuration
        do wr mem
        ```

1. Modifier le fichier de configuration de squid pour que le trafic de votre réseau local seulement soit capté par le serveur proxy.
    Squid permet également de mettre en cache les pages web visitées.
    On pourra modifier la valeur par défaut

    On modifie le fichier de configuration de squid avec les instructions suivantes:

    ```squidconf
    acl localnet src 172.168.100.0/24
    http_access allow localnet
    cache_dir ufs /var/spool/squid 100 16 256
    ```

1. Configurez le navigateur du client web pour qu'il utilise le serveur proxy que vous avez configuré (adresse IP et port d'écoute).

    On configure le navigateur afin qu'il utilise le proxy:

    ![firefox-proxy-configuration](./src/img/firefox-proxy-configuration.png)

    On peut voir que la requête `HTTP GET` est envoyée au proxy et traitée:

    ![proxy-access-1](./src/img/proxy-access-1.png)
    ![proxy-access-2](./src/img/proxy-access-2.png)

1. une fois la configuration opérationnelle, on bloquera tout autre trafic.
    Prévoir la règle nftable ou la politique par défaut qui permet de réaliser cela.

    Sur notre routeur Cisco, nous créons à nouveau l'ACL 1 qui nous permet de contrôler le trafic sortant:

    ```ini
    access-list 1 permit 172.168.100.100 0.0.0.0
    access-list 1 permit 10.10.10.0 0.0.0.255
    ip nat inside source list 1 interface F1/0 overload
    ```

1. Vérifier le fonctionnement de la mise en cache en proposant des captures de trames judicieuses.

    Nous capturons le traffic TCP et HTTP entre le client et le proxy et entre le routeur et le serveur web afin de voir si lorsque
    l'on requête le serveur web, nous retrouvons une requête HTTP liée:

    > [!NOTE]
    > Nous allons utiliser `watch` afin de ne pas avoir à s'encombrer de relancer une requête via firefox.

    On fait:

    ```sh
    watch -n 5 curl -x http://172.168.100.100:3128 http://10.10.10.1/index.html
    ```

    > [!WARNING]
    > Squid ne cache pas les requêtes avec des codes de statut 3XX, 4XX, 5XX. \
    > Si la requête se résout sous un de ces statuts, Squid indiquera un CACHE_MISS.
    > Si la requête est effectuée en HTTPS, Squid ne cache pas non plus la requête.

    On peut voir que nous avons une réponse directement sans passer par le serveur web:

    ![proxy-cache](./src/img/proxy-cache.png)

    On peut aussi voir avec les logs d'accès de Squid:

    ```sh
    tail -f /var/log/squid/access.log
    ```

    ce qui nous donne:

    ```sh
    1718783702.696      0 172.168.100.1 TCP_MEM_HIT/200 360 HEAD http://10.10.10.1/index.html - HIER_NONE/- text/html
    ```

    On tombe bien sur une page web qui a été cachée et est donc retournée du disque du serveur proxy et non du serveur web.

1. Prévoir une procédure de test pour illustrer que le trafic est bien capturé par le serveur proxy. \
    Vous analyserez également les logs qui sont situés dans `/var/log/squid/`. \
    Une description des logs possibles se trouve [ici](https://wiki.squid-cache.org/SquidFaq/SquidLogs).

    De la même manière que l'on a fait, nous capturons le trafic entre le client et le proxy et le proxy et le serveur web,
    si à chaque requête HTTP, nous avons du trafic HTTP et TCP entre le proxy et le serveur web, tout est bon.

    Si à chaque requête HTTP, nous avons du trafic HTTP et TCP entre le client et le serveur web, alors le proxy ne capture pas tout le trafic.

    On peut aussi voir les logs d'accès situés dans le fichier `/var/log/squid/access.log`, si l'on retrouve une entrée correspondante à la requête
    du client alors le proxy capture le trafic de celui-ci.

1. Quel peut-être, à votre avis, une des difficultés rencontrée avec squid pour la navigation sur le WEB ?

    Une des difficultés rencontrée avec squid peut être une atteinte à la vie privée des personnes étant sur le réseau capturé
    par le proxy.

    On peut aussi avoir le problème du "Single Point of Failure", si nous arrivons à surcharger le proxy, nous ne pouvons plus
    accéder à Internet puisque c'est une étape obligatoire d'accès.

1. Afin que la sécurité soit assurée (utilisation du proxy obligatoire pour sortir) que faudrait-il prévoir au niveau de la configuration des postes client ?

    il faudrait configurer les postes clients de manière à s'assurer que toutes leurs requêtes passent par le proxy.

### 3 - Proxy reverse

1. Dans un premier temps, on va monter l’infrastructure réseau simplifiée pour tester notre proxy inverse. Réaliser le montage de la figure 2.

    On crée le réseau suivant:

    ![tp-proxy-reseau-2](./src/img/tp-proxy-reseau-2.png)

    où:

    | Machine                                          | IP                 |
    | ------------------------------------------------ | ------------------ |
    | Serveur WEB Apache                               | 192.168.1.120/24   |
    | Serveur WEB Nginx                                | 192.168.1.130/24   |
    | Routeur - Pate Réseau Interne                    | 172.168.100.254/24 |
    | Routeur - Pate Réseau NAT                        | 192.168.124.254/24 |
    | Serveur Proxy Inverse - Pate Réseau client       | 172.168.100.100/24 |
    | Serveur Proxy Inverse - Pate Réseau Serveurs Web | 192.168.1.254/24   |
    | Client                                           | 172.168.100.1/24   |

1. Installer Nginx sur le serveur proxy inverse et tester son fonctionnement. Attention si vous avez un apache2 qui tourne sur la même machine, il risque d’y avoir des conflits

    Quand on fait un cURL, nous voyons que nous accédons bien au serveur Nginx:

    ```sh
    curl -I 127.0.0.1
    ```

    nous donne:

    ```sh
    HTTP/1.1 200 OK
    Server: nginx/1.26.1
    Date: Wed, 19 Jun 2024 12:15:17 GMT
    Content-Type: text/html
    Content-Length: 59
    Last-Modified: Wed, 19 Jun 2024 12:06:08 GMT
    Connection: keep-alive
    ETag: "6672c9b0-3b"
    Accept-Ranges: bytes
    ```

1. Installer un serveur web sur les 2 machines qui font office de serveur web (apache ou Nginx) on différenciera les 2 page web pour bien arriver à faire la différence au moment de l’accès à ces pages web.

    On installe un serveur apache et un serveur Nginx.

    Vu que sous Fedora les deux serveurs ont la même page d'accueil, nous créons ces pages-ci:

    - Nginx:

        ```html
        <html>
            <body>
                This is the Nginx server
            </body>
        </html>
        ```

    - Apache:

        ```html
        <html>
            <body>
                This is the Apache server
            </body>
        </html>
        ```

1. On se servira d’une machine avec une interface graphique pour faire le client.
    Configurer le plan d’adressage du schéma pour que cela fonctionne.
    Configurer le fichier /etc/hosts sur le client web pour que le nom de domaine que vous choisirez soit associé à votre
    serveur proxy inverse (cela remplacera le fonctionnement du DNS).

    On ajoute dans `/etc/hosts`:

    ```inimynetwork
    172.168.100.100 centaurustasie.fr
    ```

1. Configurer le serveur proxy inverse pour que tout le trafic provenant du client web
    à destination du nom de site que vous avez renseigné dans le `/etc/hosts` soit redirigé alternativement vers l’un ou l’autre des serveurs web.

    On crée un fichier de configuration `centaurustasie.fr.conf` dans le dossier `/etc/nginx/sites-available` que nous venons de créer.

    ```nginxconf
    upstream backend {
        server 192.168.1.120:80 weight=1 max_fails=3 fail_timeout=30s;
        server 192.168.1.130:80 weight=1 max_fails=3 fail_timeout=30s;
    }

    server {
        listen 80;
        listen [::]:80;

        server_name centaurustasie.fr www.centaurustasie.fr;

        location / {
            proxy_pass http://backend;
            include proxy_params;
        }
    }
    ```

    Nous l'ajoutons ensuite dans le fichier de configurations `nginx.conf`

    > [!NOTE]
    > Si nous tombons sur une erreur `502: Bad Gateway`, une solution peut être
    > de paramétrer SELinux:
    >
    > ```sh
    > setsebool -P httpd_can_network_connect 1
    > ```

    En effectuant un cURL plusieurs fois, nous pouvons voir que notre Reverse Proxy et notre Load Balancing fonctionnent:

    - Requête 1:

        ```html
        <html>
            <body>
                This is the Apache server
            </body>
        </html>
        ```

    - Requête 2:

        ```html
        <html>
            <body>
                This is the Nginx server
            </body>
        </html>
        ```

### Annexes TP 3

#### Configuration Squid

```squidconf
#
# Recommended minimum configuration:
#

acl localnet src 172.168.100.0/24

acl SSL_ports port 443
acl Safe_ports port 80  # http
acl Safe_ports port 21  # ftp
acl Safe_ports port 443  # https
acl Safe_ports port 70  # gopher
acl Safe_ports port 210  # wais
acl Safe_ports port 1025-65535 # unregistered ports
acl Safe_ports port 280  # http-mgmt
acl Safe_ports port 488  # gss-http
acl Safe_ports port 591  # filemaker
acl Safe_ports port 777  # multiling http

#
# Recommended minimum Access Permission configuration:
#
# Deny requests to certain unsafe ports
http_access deny !Safe_ports

# Deny CONNECT to other than secure SSL ports
http_access deny CONNECT !SSL_ports

# Only allow cachemgr access from localhost
http_access allow localhost manager
http_access deny manager

# This default configuration only allows localhost requests because a more
# permissive Squid installation could introduce new attack vectors into the
# network by proxying external TCP connections to unprotected services.
http_access allow localhost

# The two deny rules below are unnecessary in this default configuration
# because they are followed by a "deny all" rule. However, they may become
# critically important when you start allowing external requests below them.

# Protect web applications running on the same server as Squid. They often
# assume that only local usersmynetwork can access them at "localhost" ports.
http_access deny to_localhost

# Protect cloud servers that provide local users with sensitive info about
# their server via certain well-known link-local (a.k.a. APIPA) addresses.
http_access deny to_linklocal

# For example, to allow access from your local networks, you may uncomment the
# following rule (and/or add rules that match your definition of "local"):
http_access allow localnet

# And finally deny all other access to this proxy
http_access deny all

# Squid normally listens to port 3128
http_port 3128
mynetwork
# Uncomment and adjust the following to add a disk cache directory.
cache_dir ufs /var/spool/squid 100 16 256

# Leave coredumps in the first cache dir
coredump_dir /var/spool/squid

#
# Add any of your own refresh_pattern entries above these.
#
refresh_pattern ^ftp:  1440 20% 10080
refresh_pattern -i (/cgi-bin/|\?) 0 0% 0
refresh_pattern .  0 20% 4320
```

#### Configuration Nginx Proxy Inverse

##### nginx.conf

```nginxconf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log notice;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '

                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    include sites-enabled/*.conf;

}
```

##### proxy_params

```nginxconf
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

## TP 4 - NAT et filtrage


