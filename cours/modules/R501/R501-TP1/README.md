---
Author:
    - Lucas Simpol Augeray
    - Alexis Opolka
CreationDate: 11/09/2024
Copyright: All Rights Reserved
----

# R501-TP1

1. Commandes Linux pour le Wifi

    1. On désire utiliser le Raspberry PI comme client WIFI (IP : 10.205.x.2/16, utilisateur pi, mot de passe raspberry). \
     Afficher les paramètres de la carte Wifi intégrée (iw phy), puis scanner les réseaux Wifi visibles avec la commande iw wlan0 scan.

       - `iw phy`: Pour voir le rendu de la commande, voir le fichier [iw-phy.txt](./src/iw-phy.txt).
       - `iw wlan0 scan`: Pour voir le rendu de la commande, voir le fichier [scan.sh](./src/scan.sh).

    2. Quels canaux sont disponibles ?

       ```sh
       iw phy | grep frequencies
       ```

        nous donne :

        ```sh
        Frequencies:
          * 2412 MHz [1] (20.0 dBm)
          * 2417 MHz [2] (20.0 dBm)
          * 2422 MHz [3] (20.0 dBm)
          * 2427 MHz [4] (20.0 dBm)
          * 2432 MHz [5] (20.0 dBm)
          * 2437 MHz [6] (20.0 dBm)
          * 2442 MHz [7] (20.0 dBm)
          * 2447 MHz [8] (20.0 dBm)
          * 2452 MHz [9] (20.0 dBm)
          * 2457 MHz [10] (20.0 dBm)
          * 2462 MHz [11] (20.0 dBm)
          * 2467 MHz [12] (disabled)
          * 2472 MHz [13] (disabled)
          * 2484 MHz [14] (disabled)
        ```

        Il y a donc 14 canaux utilisables.

    3. Peut-on utiliser les canaux dans la bande des 5 GHz ?

        La carte wifi de notre raspberry n'est pas compatible avec la gamme de fréquence 5GHz

    4. Brancher maintenant la carte Wifi USB sur le PC et comparer les résultats avec la carte Wifi intégrée aux RPI.

        Nous avons utilisé la carte wifi d'un ordinateur portable afin de voir tous les canaux disponibles, voir le rendu disponible : [1.3-conf.sh](./src/1.3-conf.sh).

        Comme on peut le voir sur le fichier, la carte réseau de l'ordinateur portable est capable d'utiliser les canaux suivants :
       
        | Fréquence (en MHz) | Supporté           |
        |--------------------|--------------------|
        | 2.4                | :white_check_mark: |
        | 5                  | :white_check_mark: |
        | 6                  | :white_check_mark: |


2. Sécurité WEP40-OPEN :
    1. Paramétrer maintenant un point d’accès CISCO (Faire un Reset pendant 3 seconde après alimentation – lumière orange,
      et utiliser le mot de passe Cisco) en WEP40 authentification OPEN, puissance d’émission au minimum (Voir annexe ou Cisco-1130AG-ios1243.pdf). \
      Choisir un des canaux trouvés au § 1.2.

        Nous nous sommes connectés avec PuTTY, un baud de `9600 8N1` et le port `/dev/ttyS0`.
        Puis l'on se connecte avec les identifiants suivants :

        | Username | Password |
        |----------|----------|
        | N/A      | Cisco    |

        Nous utilisons la configuration suivante :

        ```cisco
        conf t
        dot11 ssid test-os
        guest-mode
        authentication open
        exit
        interface Dot11Radio0
        no encryption mode ciphers
        encryption mode wep mandatory
        encryption key 1 size 40bit 11111111111 transmit-key
        ssid test-os
        channel 2412
        power local cck -1
        power local ofdm -1
        no shutdown
        exit
        exit
        ```

        Pour vérifier notre SSID, nous faisons :

        ```cisco
        show dot11 bssid
        ```

        ![cisco-ap-bssid](./src/img/cisco-ap-bssid.png)

        Pour vérifier si nous avons une bonne association avec un appareil en wifi sur une interface, nous faisons:

        ```cisco
        show dot11 associations
        ```

        ![cisco-ap-assos](./src/img/cisco-ap-assocations.png)

        > [!NOTE]
        > Afin d'obtenir une adresse IP, vous devez avoir une connexion Ethernet sur l'AP en question.

    2. Vérifier que votre réseau wifi est bien visible avec un scan sur le RPI/PC ou bien utiliser (par exemple) une application comme « Wifi Analyser » sur votre smartphone pour voir les canaux Wifi...

        ![vue_reseau_wifi](./src/img/vue_reseau_wifi.png)

    3. Utiliser ensuite wpa_supplicant dans un terminal sur le RPI pour se connecter au point d’accès. \
      Créer le fichier de configuration `wep40-open.conf` avec les directives _ssid_, _auth_alg_, _key_mgmt_, _wep*_. \
      Voir fichiers d’exemples dans `/usr/share/doc/wpa_supplicant/examples/`.

        Lancez le programme avec la commande :

        ```bash
        wpa_supplicant -i wlan0 -c wep40-open.conf
        ```

        > [!NOTE]
        > Voir la configuration dans le fichier [wep40-open.conf](./src/wep40-open.conf).

    4. Tester ensuite dans une autre console, la connectivité Wifi (iw wlan0 link).

        ```sh
        iw wlan0 link
        ```

        nous donne:

        ```sh
        Connected to 00:3a:99:2b:59:b0 (on wlan0)
          SSID: test-os
          freq: 2412
          RX: 24134 bytes (251 packets)
          TX: 0 bytes (0 packets)
          signal: -68 dBm
          rx bitrate: 54.0 MBit/s

          bss flags:	short-preamble short-slot-time
          dtim period:	2
          beacon int:	100
        ```

    5. Ajouter sur l’AP une adresse IP dans l’interface BVI1, et paramétrer votre RPI dans le même réseau. Tester la connectivité IP avec un ping.

        ```sh
        ping 10.203.0.144 
        ```

        ```sh
        PING 10.203.0.144 (10.203.0.144) 56(84) bytes of data.
        64 bytes from 10.203.0.144: icmp_seq=1 ttl=255 time=6.71 ms
        64 bytes from 10.203.0.144: icmp_seq=2 ttl=255 time=4.47 ms
        --- 10.203.0.144 ping statistics ---
        2 packets transmitted, 2 received, 0% packet loss, time 1002ms
        rtt min/avg/max/mdev = 4.470/5.589/6.708/1.119 ms
        ```

    6. Capturer les trames Wifi de ce réseau sur le PC avec la carte Wifi USB en mode monitor (voir commande iw). Détailler la procédure (Attention au canal utilisé !).

        ```sh
        iwconfig <wireless-adapter> mode monitor
        ```

    7. Mettre en évidence, le chiffrement WEP dans la capture sur les trames DATA/QoS DATA et vérifier que l’on peut bien déchiffrer les trames avec wireshark, si on connaît la clé WEP.
    8. Sauvegarder la capture dans le fichier wep40-open.pcap.

2. Sécurité WEP104-SHARED :
    1. Configurer maintenant l’AP et le Raspberry pour avoir une clé WEP de 104 bits et une authentification SHARED. Vérifier cela avec une nouvelle capture de trames.
    2. Sauvegarder la capture dans le fichier wep104-shared.pcap

3. Sécurité WPA-PSK/TKIP :
    1. Paramétrer maintenant le point d’accès en WPA-PSK/TKIP en mode PSK authentification OPEN avec une clé de seulement 8 digits (uniquement des chiffres) et sans doublons (soit 1814400 possibilités = 10*9*8*7*6*5*4*3).
    2. Réaliser la connexion depuis le Raspberry PI (ficher wpa-psk-tkip.conf avec les directives : ssid, auth_alg, proto, key_mgmt, pairwise, group, psk) et capturer les trames Wifi en parallèle sur le PC pour mettre en évidence le chiffrement TKIP et aussi les 4 trames EAPOL de l’échange de clé.
    3. Sauvegarder la capture dans le fichier wpa1-psk-tkip.pcap.
    4. Peut-on déchiffrer les trames avec wireshark ?

4. Sécurité WPA2-PSK/CCMP :
    1. Passer ensuite en WPA2-PSK/CCMP avec une autre clé (toujours de 8 digits sans doublons).
    2. Capturer les trames de connexion du Raspberry PI (fichier wpa-psk-ccmp.conf) sur ce réseau Wifi et vérifier que le chiffrement est bien en CCMP.
    3. Sauvegarder la capture dans le fichier wpa2-psk-ccmp.pcap.
    4. Peut-on déchiffrer les trames s’il n’y a pas les 4 trames EAPOL dans la capture ?

5. annexe

    1. Commandes cisco IOS WEP :

        ```cisco
        conf t
        dot11 ssid XXXXXXX
        guest-mode
        ===> authentication open
        ===> authentication shared
        exit
        interface Dot11Radio0
        no encryption mode ciphers
        encryption mode wep mandatory
        ===> encryption key X size 40bit ZZZZZZZZZZ transmit-key
        ===> encryption key X size 128bit ZZZZZZZZZZZZZZZZZZZZZZZZZZ transmit-key
        ssid XXXXXXX
        channel NNNN
        power local cck -1
        power local ofdm -1
        no shutdown
        exit
        exit
        ```

    1. Commandes cisco IOS WPA-PSK TKIP/CCMP :

        ```cisco
        conf t
        dot11 ssid XXXXXXX
        guest-mode
        authentication open
        authentication key-management wpa
        wpa-psk ascii 0 ZZZZZZZZ
        exit
        interface Dot11Radio0
        ===> encryption mode ciphers tkip
        ===> encryption mode ciphers aes-ccm
        ssid XXXXXXX
        channel NNNN
        power local cck -1
        power local ofdm -1
        no shutdown
        exit
        exit
        ```

        > [!NOTE] 
        > Le `===>` indique un choix entre les propositions.
