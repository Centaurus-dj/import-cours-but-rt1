---
Author:
  - Alexis Opolka
  - Mathys Domergue
Company: IUT de Béziers
Subject: Analyse de trames 2G
Copyright: All Rights Reserved
---

# R404 - TP2 - Analyse de trames 2G

1. ## Applications "réseau"

    - Sur ANDROID:

        Chercher sur le site de « google play » les applications permettant de récupérer les informations sur la cellule serveuse
        2G/3G/4G utilisée par votre mobile (MCC, MNC, LAC, ARFCN, ... ).  
        Par exemple G-NetTrack, G-Mon, Network Cell Info, Net Monitor, ...  
        Tester les sur votre mobile.

    - Sur IOS: Il faut activer le « Field Test mode » en tapant `*3001#12345#*`

        Voici les informations que nous avons pu récupérer sur l'un de nos deux téléphone:

        ![ios-cell-tracking](./src/img/tp2/ios-tracking.jpg)

1. ## Etude des niveaux de signal

    1. Lancer le programme `Nemo Outdoor` (après avoir branché le dongle USB) et ouvrir le fichier de capture réalisé par l'enseignant (`Nemo-14-11-28.nmf`).
    1. Afficher le graphique `Parameter Grid : Band and System Information` et jouer sur le curseur temporel.
        Vérifier que l'on est bien sur une bande de fréquence 2G. Quelles sont les identifiants des 2 cellules ?

        ![neo-2g-cell-1](./src/img/tp2/neo-2g-cell-1.png)
        ![neo-2g-cell-2](./src/img/tp2/neo-2g-cell-2.png)

    1. Afficher le graphique `Line Graph : GSM/UMTS Pilot Levels`.

        - Faire défiler le temps et noter les 2 cellules serveuses utilisées (RAC, CI, LAC, MNC et MCC) ?

            ![3-1-cell-1-info](./src/img/tp2/2-3-1-cell-1-info.png)
            ![3-1-cell-2-info](./src/img/tp2/2-3-1-cell-2-info.png)

        - Quels sont les canaux utilisés sur ces cellules (ARFCN) ?

            Les cannaux utilisés sont les canaux 8 et 16.  

        - A quel(s) instant(s) a-t-on changé de cellule, de canal ?  

            Le canal change de cellule à `10:47:11` et à `10:48`.  

        - A l'instant `10:45:50`, quel est le niveau de réception en dBm et le code BSIC de la BTS ?

            A  l'instant `10:45:50`, le BSCI n'est pas disponible, et pour le BTS, il est égale à `-94` dbm.

        - Idem, à l'instant `10:48:20`.

            Pour `10:48:20`:

            | Recherché | Valeur (dBm) |
            | --------- | ------------ |
            | BSCI      | 26           |
            | BTS       | -96          |

        - Cliquer sur le bouton droite de la souris dans la partie `Values` et ajouter les informations GSM `Hopping status, Hopping channels, Timing advance et TMSI`.  
            Faire défiler le temps et noter à quels instants les valeurs changent.

            Les valeurs changent dans un premier temps à `10:47:12` et `10:47:59`.  

        - Qu'indique les valeurs des canaux de la liste `Hopping channels` ?  

            Les valeurs indiquent les canaux disponibles pour le téléphone dans le cas où il voudrait changer de canal.

        - En utilisant la valeur du `TA`, à quelle distance approximative se trouve la BTS (faire un calcul) ?

            > [!NOTE]
            > Pour le GSM, le TA est de 554.

            Donc le BTS est à :

            $$
                554 x 10 = 5540 = 5.54 \text{ km}
            $$  

    1. Afficher le graphique `Line Graph: GSM serving cell and neighbor RX levels` ou bien `Bar Graph: GSM RX levels...`.  
        Quelles sont les fréquences voisines au temps `10:47:15` ?

    1. Afficher le graphique `Line Graph : GSM serving cell RF parameters`.

        - Chercher la signification du terme AMR sur internet.

            > [!NOTE]
            > AMR signifie `Adaptive Multi-Rate`[^1].

            [^1]: See: [en.wikipedia.org/wiki/Adaptive_Multi-Rate_audio_codec](https://en.wikipedia.org/wiki/Adaptive_Multi-Rate_audio_codec)

        - En déduire les instants pendant lesquels le mobile était en communication.  

            | Debut    | Fin      |
            | -------- | -------- |
            | 10:47:12 | 10:47:22 |
            | 10:47:23 | 10:47:23 |
            | 10:47:23 | 10:47:26 |
            | 10:47:27 | 10:47:29 |
            | 10:47:30 | 10:47:37 |
            | 10:47:38 | 10:47:58 |

        - Qu'indique le graphique C/I average ?

            C'est le rapport signal sur bruit pour les cellules

    1. Afficher le graphique `Events Grid : GSM L1 problems`.  
        Quels sont les différents messages utilisés ?

        1. Les différents messages utilisés sont:

           - Cell measurement
           - Carrier per interface
           - RX quality

        2. &nbsp;
           - Afficher le détail d'un message `Cell mesurement`.  
                A qui et à quoi servent ces messages ?

                ![2-6-message-details-1](./src/img/tp2/2-6-message-details-1.png)
                ![2-6-message-details-2](./src/img/tp2/2-6-message-details-2.png)

                Ces messages servent à <réponse>.

           - A partir de quels moments a-t-on des messages `RX quality` ?

                On peut voir qu'à partir de `10:47:12`, nous avons des messages `RX quality`.

    1. Afficher le graphique `Events Grid : Handover Events`.  
        Qu'est-ce qu'un Handover ?

        > [!NOTE]
        > Le handover désigne l'ensemble des opérations mises en œuvre pour permettre qu'un téléphone mobile
        > ou un smartphone puisse changer de cellule radio sans interruption de la conversation ou du transfert des données
        >
        > Source: [fr.wikipedia.org/wiki/Handover](https://fr.wikipedia.org/wiki/Handover)

    1. Quel type de handover a été demandé par le réseau (donner les propriétés courantes et demandées) ?

        ![2-8-handover-events-graph](./src/img/tp2/2-8-handover-events-graph.png)

    1. Afficher le graphique `Events Grid : Neighbor List` et en déduire comment le mobile détermine les canaux des cellules voisines utilisées au §1.4.

1. ## Messages de la couche 3

    1. Afficher le tableau « Events Grid : Call events » et retrouver les instants notés au §1.3.

        - Quel est le numéro appelé ?

            ![3-1-events-grid-call-events.png](./src/img/tp2/3-1-events-grid-call-events.png)

    2. Afficher le tableau « Events Grid : Layer 3 messages »

        - Noter pour les 6 messages IMMEDIATE ASSIGNMENT à partir de 10:46:36.138, les valeurs du numéro de slot, le numéro de séquence d'apprentissage, le numéro de canal et le timing advance.  
            Faire un schéma récapitulatif.
        - Qu'indique le message CM_SERVICE_REQUEST. Quelle est la valeur du TMSI envoyée par le MS ?
        - Dans quelle trame qui suit, trouve-t-on l'IMSI du mobile ? Quelle est sa valeur ? Retrouver alors le MCC et le MNC.
        - Qu'indique selon-vous les trames CIPHERING_MODE_COMMAND et CIPHERING_MODE_COMPLETE ?
        - Retrouver le numéro d'appel dans la trame SETUP. Comment est-il codé (hex. Data) ?
        - Qu'indique la trame CALL_PROCEEDING ?
        - Qu'indique selon-vous les trames ASSIGNEMENT_COMMAND et ASSIGNEMENT_COMPLETE ? Sur quel slot vont être envoyé les données à partir de là ?
        - Qu'indique selon-vous les trames CONNECT et CONNECT_ACKNOLEDGE ?
        - Qu'indique les 2 messages PHYSICAL_INFORMATION qui suivent ?
        - Quelle(s)   information(s)   peut-on   déduire   sur   les   actions   de   l'utilisateur   à   partir   des   trames   START_DTMF, START_DTMF_ACKNOLEDGE, STOP_DTMF et STOP_DTMF_ACKNOLEDGE ?
        - Enfin, quelles trames indiquent la fin de la communication et qui (du mobile ou du réseau) en est à l'initiative ?

3. ## Analyse de traces

    - Déterminer les actions de l’utilisateur en utilisant la trace Nemo-15-01-19-1.nmf
