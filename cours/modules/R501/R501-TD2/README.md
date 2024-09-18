# R501 - TD2

## 1 - Introduction

1. ### 1.1 - Paramètres radios

     - Trame 1

       ![1.1-params-radios](./src/img/1-1-params-radio.png)

     - Trame 99

       ![1.99-params-radios](./src/img/1-99-params-radio.png)

     | Trame N° | Canal       | Débit binaire | type de réseau | qualité de signal | modulation utilisée |
     |----------|-------------|---------------|----------------|-------------------|---------------------|
     | Trame 1  | 1 (2.4 GHz) | 1 Mb/s        | 11b            | 84                | CCK                 |
     | Trame 99 | 1 (2.4 GHz) | 54 Mb/s       | 11g            | 100               | OFDM                |

     - Donner les valeurs et la signification des 3 adresses MAC de la trame 1 (partie Beacon Frame).

       Dans la trame 1, nous avons un broadcast de l'AP.

       - Receiver address: `Broadcast (ff:ff:ff:ff:ff:ff)`
       - Destination address: `Broadcast (ff:ff:ff:ff:ff:ff)`
       - Transmitter address: `CiscoLinksys_82:b2:55 (00:0c:41:82:b2:55)`

     - Donner les valeurs et la signification des adresses MAC de la trame 99 à partir des drapeaux ToDS et FromDS

       Dans la trame 99, nous avons une communication d'une STA à une DS via un AP, donc d'un appareil client
       à un AP Wifi.

       - Receiver address: `Cisco-Li_82:b2:55 (00:0c:41:82:b2:55)`
       - Transmitter address: `Apple_82:36:3a (00:0d:93:82:36:3a)`
       - Destination address: `Broadcast (ff:ff:ff:ff:ff:ff)`

2. ### 1.2 - Trames `BEACON`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0x8
    ```

    - Quel(s) est(sont) le(s) SSID utilisé(s) ?

        En appliquant le filtre donné, nous obtenons les SSID suivants:

        - Coherer

    - Quel est l'intervalle entre 2 trames BEACON pour chaque AP ? (Donner le champ de la trame contenant la valeur)

      L'intervalle entre 2 trames se situe, dans une trame management (IEEE 802.11 Wireless Management), dans la partie Fixed Parameters.

      On sait donc qu'une trame `BEACON` sera envoyée toutes les `0.102400` secondes.

      ![frame-intervals](./src/img/2-frame-intervals.png)

    - Quels sont les débits supportés par le(s) point(s) d'accès ? (Où sont ils précisés ?)

      Les débits supportés par le point d'accès sont précisés dans le champ `Tag` `Supported Rates` et `Extended Supported Rates` de la trame
      IEEE 802.11 Wireless Management, en l'occurence les débits sont (Mbit/s):

      - 1
      - 2
      - 5.5
      - 6
      - 11
      - 12
      - 18
      - 24
      - 36
      - 48
      - 54

      ![ap-supported-rates](./src/img/2-supported-ap-rates.png)

    - Quels protocoles de sécurité utilise(nt) il(s) ?

      L'AP peut utiliser le protocole WEP:

      ![2-ap-security-protocols](./src/img/2-proto-security.png)

3. ### 1.3 - Trames `PROBE REQUEST`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0x4
    ```

    - Combien de trames la capture contient elle ?

      Elle contient 13 trames.

    - Quelles sont les adresses MAC des machines émettant des trames PROBE REQUEST ?

      Les adresses MAC sont:

      - 00:0d:93:82:36:3a
      - 00:0f:66:16:94:73

    - Que contiennent ces trames et à quoi servent-elles ?

      Ces trames permettent aux STA de découvrir les appareils à proximité avec lesquelles elles peuvent
      communiquer. Voir: [802.11-2012.pdf#G10.29301](./src/802.11-2012.pdf#G10.29301).

4. ### 1.4 - Trames `PROBE RESPONSE`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0x5
    ```

    - Combien de trames la capture contient elle ?

      Elle contient 26 trames.

    - Quelle est l'adresses MAC de l'AP émettant des trames PROBE RESPONSE ?

      Les adresses MAC sont:

      - 00:0c:41:82:b2:55

    - Que contiennent ces trames et à quoi servent-elles ?

      Ces trames contiennent des BSSID permettant aux émetteurs de trames `PROBE REQUEST`
      de connaître le réseau en question.

5. ### 1.5 - Trames `AUTHENTICATION`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0xb
    ```

    - Combien il y a-t-il de demande d'authentification dans toute la capture ?

      Il y a 2 demandes d'authentification.

    - Quel est le type d'algorithme utilisé (Open System ou Shared key) ?

      Le type d'algorithme utilisé est `Open System`.

    - Donner les 6 octets de la partie fixe de « 802.11 wireless LAN management frame » pour chaque trame.

      | Trame N° | Partie fixe       |
      | -------- | ----------------- |
      | 80       | 00 00 02 00 00 00 |
      | 78       | 00 00 01 00 00 00 |

    - Combien  il  y  a-t-il  d'authentifications  réussies  (cf.  Norme  802.11  § 8.28 « Authentication frame body » page 434, § 8.28
      « Presence of fields and elements in Authentication frames » et § 8.37 « Status codes » page 446) ?

      Il y a 2 authentifications réussies.

6. ### 1.6 - Trames `ASSOCIATION REQUEST`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0x0
    ```

    - Combien il y a-t-il de demande d'association dans toute la capture ?

      Il y a 1 demande d'association.

    - Quelles informations sont transportées dans ces trames ?

7. ### 1.7 - Trames `ASSOCIATION RESPONSE`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0x1
    ```

    - Quelle est l'adresses MAC de la station ayant réussi l'association ?

      L'adresse MAC est:

      - 00:0d:93:82:36:3a

    - Quel est le code d'état de l'association et l'identifiant de l'association ?

8. ### 1.8 - Trames `DATA`

    En utilisant le filtre suivant:

    ```sh
    wlan.fc.type_subtype == 0x2
    ```

    - Quels sont les 2 protocoles de chiffrement utilisés dans la capture ? Noter où se trouvent les IV
    - Combien il y a-t-il d’échanges de clé EAPOL dans la capture ? Est-ce la même station que celle trouvée au point précédent ?

## 2 - Déchiffrement de trames WPA

  - Sachant que le mot de passe utilisé dans la capture est « Induction », paramétrer wireshark pour déchiffrer les trames IEEE 802.11 Data. (cf. <http://wiki.wireshark.org/HowToDecrypt802.11>)
  - Quel est alors le protocole de la trame 99 ?

    La trame 99 a pour protocole DHCP.

    ![trame-99-proto](./src/img/2-trame-99-proto.png)
