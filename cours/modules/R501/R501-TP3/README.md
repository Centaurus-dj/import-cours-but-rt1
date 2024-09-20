# R501-TP3 - WPA Entreprise et WPA3-SAE

## 1 - Sécurité WPA-Entreprise/802.1X

1. Valider   sur  le  Raspberry   avec   l’outil  eapol_test-2.10-arm64  (fourni   sur   l’ENT)  les
  méthodes d’authentification EAP-MSCHAPv2, EAP-PEAP-EAP-MSCHAPV2, EAP-TTLS-PAP,
  EAP-TTLS-CHAP,   EAP-TTLS-MSCHAP,   EAP-TTLS-MSCHAPv2,   EAP-TTLS-EAP-
  MSCHAPv2 et EAP-TLS (voir fichiers de configuration fournis sur l’ENT) sur serveur RADIUS
  indiqué par l’enseignant.

     - `EAP-MSCHAPv2`
     - `EAP-PEAP-EAP-MSCHAPV2`
     - `EAP-TTLS-PAP`
     - `EAP-TTLS-CHAP`
     - `EAP-TTLS-MSCHAP`
     - `EAP-TTLS-MSCHAPv2`
     - `EAP-TTLS-EAP-MSCHAPv2`
     - `EAP-TLS`

2. Paramétrer alors le point d’accès en mode « Entreprise » 802.1x avec ce serveur RADIUS
  (voir Annexe). Afficher la configuration complète de l’AP (sh run) et vérifier par un scan sur le RPI,
  le paramétrage du point d’accès.

3. Connecter le Raspberry sur le point d’accès en adaptant une des configurations du § 1.1 (ajouter
  les directives ssid, auth_alg, proto, key_mgmt, pairwise et group).

4. Capturer les trames Wifi entre le Raspberry et le point d’accès et vérifier que l’on a pas accès aux
  trames RADIUS mais que le trafic d’authentification est bien encapsulé avec EAP.

5. Vérifier   que   l’on   peut   bien   déchiffrer   le   trafic   en   utilisant   la(es)   clé(s)   indiquée(s)   par
  wpa_supplicant avec les options -d et -K.

## 2 - Sécurité WPA3-SAE

1. Vérifier que les points d’accès fournis ne supportent pas WPA3/SAE

2. La carte Wifi intégrée du Raspberry ne supporte pas non plus SAE, mais vérifier que la carte Wifi
  USB possède bien les fonctionnalités SAE (voir la sortie standard de iw phy).

3. Mettre alors en place sur le Raspberry PI, un point d’accès WPA3/SAE en utilisant l’outil
  hostapd (voir hostapd.conf.sample)

4. Capturer les trames de connexion d’un autre Raspberry PI client de ce réseau Wifi

5. Mettre en évidence les 4 trames d’authentification SAE avant les trames EAPOL

6. Pour décrypter le trafic WPA3, il faut les clés TK et/ou GTK.
  Utiliser à nouveau les options -d et -K  de  wpa_supplicant ou
  de hostapd pour obtenir dans les traces, les clés de déchiffrement.

    s
