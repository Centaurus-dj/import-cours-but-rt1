---
Author:
  - Alexis Opolka
  - Mathys Domergue
---

# R404 - TP3 - Analyse de trames 3G/4G

1. ## Etude des niveaux de signal 3G

    1. Installer et lancer le programme `Nemo Outdoor` (après avoir branché le dongle USB).
    2. Ouvrir le fichier de capture réalisé par l'enseignant (`Nemo-15-01-12.nmf`).
    3. Afficher le graphique `Parameter Grid : Band and System Information` et jouer sur le curseur temporel.

         - Vérifier que l'on est bien sur une bande de fréquence 3G

            Nous sommes bien sur une bande de fréquence 3G, car nous utilisons les bandes de fréquences UMTS.

            > [!NOTE]
            > Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/UMTS_frequency_bands).

         - Quelles sont les identifiants des 2 cellules ?

            | Nom       | Identifiant |
            | --------- | ----------- |
            | Cellule 1 | 25657241    |
            | Cellule 2 | 25641988    |

    4. Afficher les graphiques `Parameter Grid : UMTS Active Set Cell Information`et `Table Grid : UMTS Active Set Information`

       - Qu'indiquent les valeurs Ec/N0 et RSCP ?

          | Valeur   | Signification                 |
          | -------- | ----------------------------- |
          | $E_c/N0$ | Rapport signal sur bruit      |
          | $RSCP$   | Qualité du signal en recption |

       - Donner les valeurs du numéro de canal et du code de `scrambling` utilisés au temps `10:23:20`

          | Valeur                          | Je sais pas |
          | ------------------------------- | ----------- |
          | $\textbf{Numéro du canal}$      | 10836       |
          | $\textbf{Code de 'scrambling'}$ | 274         |

    5. Afficher les graphiques `Line Graph : Ec/N0 (active & monitored)`, `Bar Graph : Ec/N0 (active & monitored)`,
      `Bar Graph : GSM/UMTS Pilote Levels` et en déduire la signification des appellations `active` et `monitored` (jouer sur le curseur temporel).

    6. Afficher le graphique `Line Graph : UMTS Radio parameters` et déterminer à quels instants le contrôle de puissance
      d'émission du téléphone a été activé

          | instant de début | Instant de fin |
          | :--------------: | :------------: |
          |     10:23:29     |    10:23:42    |
          |     10:23:43     |    10:23:44    |

         - Que signifie le terme `BLER` ?

            Le terme `BLER` signifie ***Block Error Rate/Ratio***.

            > [!NOTE]
            > Source: [telecompedia.net](https://telecompedia.net/block-error-rate-in-lte/).

2. ## Messages réseau

    1. Afficher les tableaux `Events Grid : Call Events` et `Events Grid : Layer 3 Messages` et en déduire les actions de l'utilisateur sur le téléphone

        - A quoi sert le premier message (qu'indique-t-il) ? Quel est le TMSI du mobile ?

          Le premier message permer de savoir quelle cellule est disponible pour que lors de l'apelle il puisse si connecter.  
          La valeur du TMSI est de 1401f406.

        - Quel est le numéro appelant ?  
            Comment est-il codé dans les données hexadécimales ?

            - Le numéro de l'appelant est le `0467116000`.  
            - Son code en hexadecimal : `33641761 00f0`.

    2. Les messages de paging et d'information envoyés par le système (cf. TP n° 02) ne sont pas visibles en 3G dans cette
      fenêtre mais dans plutôt dans la liste des messages RRC. Chercher sur internet la signification de ce terme et la norme
      UMTS qui spécifie ce protocole de transport.

        `RRC` : Radio Ressource Control, protocol utilisé entre l'utilisateur et la station de base.

        > [!NOTE]
        > Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Radio_Resource_Control).

    3. Afficher alors le tableau `Events Grid : Layer3/RRC messages`

        - Quel message de PAGING RRC est à l'origine du premier message de couche 3 du §2.1 ?

          Le message est le `RCC_CONNECTION_REQUEST`;

        - Comparer avec une capture 2G (sur quel canal sont transportés les messages de paging par exemple).

          Pour la 2G, le canal utilisé est le `TCH/F`

3. ## Capture de trames

    1. Ouvrir le fichier `Nemo-23-05-24.nmf` et déterminer les différentes technologies utilisées au cours de la capture.

        |            Technologie | Bande de fréquence |
        | ---------------------: | ------------------ |
        | GSM               (2G) | 900                |
        | LTE FDD   - 1800  (4G) | 3                  |
        | LTE FDD - 800     (4G) | 2                  |
        | LTE FDD - 2700    (4G) | 7                  |
        | UMTS FDD          (3G) | 900                |

    2. Comment se passe le changement de technologie 4G/3G, 3G/2G, 2G/4G, etc ?


