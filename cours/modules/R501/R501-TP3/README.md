# R501-TP3 - WPA Entreprise et WPA3-SAE

## 1 - Sécurité WPA-Entreprise/802.1X

1. Valider   sur  le  Raspberry   avec   l’outil  eapol_test-2.10-arm64  (fourni   sur   l’ENT)  les
  méthodes d’authentification EAP-MSCHAPv2, EAP-PEAP-EAP-MSCHAPV2, EAP-TTLS-PAP,
  EAP-TTLS-CHAP,   EAP-TTLS-MSCHAP,   EAP-TTLS-MSCHAPv2,   EAP-TTLS-EAP-
  MSCHAPv2 et EAP-TLS (voir fichiers de configuration fournis sur l’ENT) sur serveur RADIUS
  indiqué par l’enseignant.

      On fait la commande suivante:

      ```sh
      ./eapol_test-2.10-arm64 -c <ficher-configuration> -a <RADIUS-server-IP> -p 1812 -s <password>
      ```

     - `EAP-MSCHAPv2`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-PEAP-EAP-MSCHAPV2`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-TTLS-PAP`

        - Première tentative: Authentification échouée due à une erreur d'invalidité du certificat
        - Deuxième tentative:

          Après la commande suivante, Authentification réussie:

          ```sh
          sudo date --set "19 SEP 2024 10:21:00"
          ```

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-TTLS-CHAP`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > [!NOTE] \
        > Il faut tout de même mettre à jour la date de la machine.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-TTLS-MSCHAP`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > [!NOTE] \
        > Il faut tout de même mettre à jour la date de la machine.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-TTLS-MSCHAPv2`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > [!NOTE] \
        > Il faut tout de même mettre à jour la date de la machine.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-TTLS-EAP-MSCHAPv2`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > [!NOTE] \
        > Il faut tout de même mettre à jour la date de la machine.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

     - `EAP-TLS`

        Authentification réussie, on a pu accéder au serveur RADIUS avec les bons paramètres.

        > [!NOTE] \
        > Il faut tout de même mettre à jour la date de la machine.

        > ![NOTE] \
        > Voir la sortie de la commande, disponible [ici](./src/exit-question1/ms-chapv2.txt).

2. Paramétrer alors le point d’accès en mode « Entreprise » 802.1x avec ce serveur RADIUS
  (voir Annexe). Afficher la configuration complète de l’AP (sh run) et vérifier par un scan sur le RPI,
  le paramétrage du point d’accès.

      Configuration de l'AP:

      ```cisco
      conf t
      interface bvi1
      ip address 10.205.6.100 255.255.0.0
      exit
      ip radius source-interface BVI1
      aaa new-model
      radius-server host 10.205.20.1 auth-port 1812 acct-port 1813 key 0 testing123
      radius-server vsa send accounting
      aaa group server radius rad_eap
      server 10.205.20.1 auth-port 1812 acct-port 1813
      exit
      aaa group server radius rad_acct
      exit
      aaa authentication login eap_methods group rad_eap
      aaa accounting network acct_methods start-stop group rad_acct
      dot11 ssid test-os
      authentication open eap eap_methods
      authentication network-eap eap_methods
      authentication key-management wpa
      guest-mode
      exit
      interface Dot11Radio0
      encryption mode ciphers aes-ccm
      ssid test-os
      channel 2412
      power local cck -1
      power local ofdm -1
      no shutdown
      exit
      ```

      > [!NOTE] \
      > Pour voir la configuration, disponible [ici](./src/conf-ap-cisco-mode-entreprise.conf)

      Comme vu ci-dessous, on peut voir que l'AP est bien configuré:

      ```txt
      BSS 00:3a:9a:f4:2c:d0(on wlan0)
        last seen: 4515.078s [boottime]
        TSF: 0 usec (0d, 00:00:00)
        freq: 2412
        beacon interval: 100 TUs
        capability: ESS Privacy ShortPreamble ShortSlotTime (0x0431)
        signal: -50.00 dBm
        last seen: 0 ms ago
        SSID: test-os
        Supported rates: 1.0* 2.0* 5.5* 6.0 9.0 11.0* 12.0 18.0 
        DS Parameter set: channel 1
        ERP: <no flags>
        RSN:   * Version: 1
           * Group cipher: CCMP
           * Pairwise ciphers: CCMP
           * Authentication suites: IEEE 802.1X
           * Capabilities: 4-PTKSA-RC 4-GTKSA-RC (0x0028)
        Extended supported rates: 24.0 36.0 48.0 54.0 
        WMM:   * Parameter version 1
           * u-APSD
           * BE: CW 15-1023, AIFSN 3
           * BK: CW 15-1023, AIFSN 7
           * VI: CW 7-15, AIFSN 2, TXOP 6016 usec
           * VO: CW 3-7, AIFSN 2, TXOP 3264 usec
      ```

3. Connecter le Raspberry sur le point d’accès en adaptant une des configurations du § 1.1
  (ajouter les directives ssid, auth_alg, proto, key_mgmt, pairwise et group).

    Configuration du Raspberry Pi:

    ```sh
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US

    network={
      ssid="test-os"
      scan_ssid=1
      key_mgmt=WPA-EAP
      eap=PEAP
      identity="bob"
      password="hello"
      phase1="peaplabel=0"
      phase2="autheap=MSCHAPV2"
    }
    ```

4. Capturer les trames Wifi entre le Raspberry et le point d’accès et vérifier que l’on a pas accès aux
  trames RADIUS mais que le trafic d’authentification est bien encapsulé avec EAP.

    On voit avec notre capture wireshark, [accessible ici](./src/rasp-cisco-eap-tls.pcapng), que notre traffic est bien encapsulé avec EAP et que toutes les
    trames RADIUS sont chifrées avec du TLS.

5. Vérifier   que   l’on   peut   bien   déchiffrer   le   trafic   en   utilisant   la(es)   clé(s)   indiquée(s)   par
  wpa_supplicant avec les options -d et -K.

    La clé est:

    ```sh
    24 4a e5 c3 db 31 e4 5b 66 85 35 6b 2b a7 cd 14 00 38 df b6 b1 87 c1 72 7c ea 56 c1 f3 6b e8 01
    ```

## 2 - Sécurité WPA3-SAE

1. Vérifier que les points d’accès fournis ne supportent pas WPA3/SAE

    Selon la documention associé a la borne wifi, elle ne supporte pas la communication WPA3/SAE

2. La carte Wifi intégrée du Raspberry ne supporte pas non plus SAE, mais vérifier que la carte Wifi
  USB possède bien les fonctionnalités SAE (voir la sortie standard de iw phy).

    Avec la commande iw phy nous avons le retour [accessible ici](./src/retoure_iw_phy.txt) de tout les carte réseaux disponible, aprés avoir trouvé la bonne on peut voir quelle est compatible avec le protocol SAE (ligne 198 du fiché donnée).

3. Mettre alors en place sur le Raspberry PI, un point d’accès WPA3/SAE en utilisant l’outil
  hostapd (voir hostapd.conf.sample)

4. Capturer les trames de connexion d’un autre Raspberry PI client de ce réseau Wifi

5. Mettre en évidence les 4 trames d’authentification SAE avant les trames EAPOL

6. Pour décrypter le trafic WPA3, il faut les clés TK et/ou GTK.
  Utiliser à nouveau les options -d et -K  de  wpa_supplicant ou
  de hostapd pour obtenir dans les traces, les clés de déchiffrement.

    s
