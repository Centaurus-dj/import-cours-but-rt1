# R501 - TD2

## Introduction

1. ### 1.1 Paramètres radios

  - Trame 1

    ![1.1-params-radios](./src/img/1-1-params-radio.png)

  - Trame 99

    ![1.99-params-radios](./src/img/1-99-params-radio.png)

  | Trame N° | Canal       | Débit binaire | type de réseau | qualité de signal | modulation utilisée |
  |----------|-------------|---------------|----------------|-------------------|---------------------|
  | Trame 1  | 1 (2.4 GHz) | 1 Mb/s        | 11b            | 84                | CCK                 |
  | Trame 99 | 1 (2.4 GHz) | 54 Mb/s       | 11g            | 100               | OFDM                |

  - Donner les valeurs et la signification des 3 adresses MAC de la trame 1 (partie Beacon Frame).
  - Donner les valeurs et la signification des adresses MAC de la trame 99 à partir des drapeaux ToDS et FromDS

    Dans la trame 99, nous avons une communication d'une STA à une DS via un AP, donc d'un appareil client
    à un AP Wifi.

    - Receiver address: `Cisco-Li_82:b2:55 (00:0c:41:82:b2:55)`
    - Transmitter address: `Apple_82:36:3a (00:0d:93:82:36:3a)`
    - Destination address: `Broadcast (ff:ff:ff:ff:ff:ff)`
