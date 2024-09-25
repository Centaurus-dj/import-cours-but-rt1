# R503-TP2 - Mise en oeuvre des techniques de SDR

## 1 - Introduction

## 2 - Modulation BPSK

1. Rappeler le principe de la modulation BPSK (Binary Phase Shift Keying)

    La modulation `BPSK` est une modulation binaire où l'on modifie la
    phase du signal avec deux symboles.

2. Donner le diagramme de constellation correspondant à cette modulation

    ![bpsk-constellation](./src/img/bpsk-constellation.png)

3. Expliquer comment les données binaires sont transmises à l'aide de cette de modulation.

    | Valeur Binaire | Angle de Phase |
    | -------------- | -------------- |
    | 0              | 0°             |
    | 1              | 180°           |

4. Dans GNURadio, construire un diagramme de flux permettant de produire le signal BPSK en
    bande de base. Pour cela, vous devez générer une séquence binaire à l’aide du bloc « Vector
    Source ». Utiliser une fréquence d’échantillonnage globale de 2 MHz. Choisir une durée d’un
    symbole de 1 ms. Utiliser également les blocks « Chunks to Symbols » et « QT Gui Constellation
    Sink ». Expliquer ce que font ces deux blocs.

    ![bpsk-diagram](./src/img/bpsk-diagram.png)

    - `Chunks to Symbols`: Permet d'afficher un flux en une représentation à D dimension
    - `QT GUI Constellation Sink`: Permet d'afficher la constellation d'un signal

5. Exécuter votre diagramme et faire apparaitre à l’écran la constellation obtenue.

    ![bpsk-constellation](./src/img/bpsk-constellation.png)

## 3 - Modulation QPSK

1. Refaire la même étude que précédemment pour cette modulation

    - Constellation QPSK:

      ![alt text](./src/img/qpsk-constellation.png)
      ![qpsk-diagram](./src/img/qpsk-diagram.png)

2. En pratique, la transmission de données est toujours entachée de bruit. Ajouter une source de
  bruit « Noise Source » et étudier son effet sur la constellation produite.

    ![alt text](./src/img/qpsk-noise-diagram.png)

3. Déterminer le niveau de bruit à partir duquel, la discrimination des différents symboles devient 
  problématique.

    ![](./src/img/qpsk-noise.png)

    - 0.5

      ![](./src/img/qpsk-noise-const-05.png)

    - 0.7

        ![alt text](./src/img/qpsk-noise-const-07.png)

    On peut voir qu'à partir de 0.7 nous ne pouvons plus vraiment discerner
    les différents symboles.

## 4 - Modulation 8-PSK

1. Modifier le diagramme précédent afin de réaliser une modulation 8-PSK.

    où x est notre position sur le cercle trigo:

    `cos(x) + i sin(x)`

    nous permet d'obtenir les valeurs nécessaires à la 8-PSK.

    ![alt text](./src/img/8psk-constellation.png)

    ![alt text](./src/img/8psk-diagram.png)

2. Comparer le résultat obtenu avec la technique 4-PSK du point de vue du bruit.

    - 0.11

      ![alt text](./src/img/8psk-noise-011.png)

    - 0.12

      ![alt text](./src/img/8psk-noise-012.png)

3. Commentez

    La modulation 8-PSK est beaucoup plus sensible au bruit comparé au QPSK.

## 5 - Modulation 4-QAM

1. Reprendre l'étude précédente en considérant une modulation 4-QAM

    `[-1-1j, -1+1j, 1+1j, 1-1j]`

    ![alt text](./src/img/qam-constellation.png)

2. Commentez les résultats obtenus

    s

3. Quelle est la différence entre la modulation 4-QAM et 4-PSK

    s
