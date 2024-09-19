# R503-TP1 - Modulation et démodulation OOK et ASK

## 1 - Introduction

## 2 - Modulation OOK

1. Rappeler le principe de la modulation OOK.
    Expliquer les différentes fonctions à réaliser pour mettre en oeuvre un
    système de communication utilisant cette technique.

    La modulation OOK[^1] est un principe de modulation où l'on utilise l'amplitude
    afin de moduler un signal.

    On module de la manière suivante:

    - On émet (= 1)
    - On émet pas

    [^1]: On-Off Keying

2. Créer  un  nouveau  diagramme  de  flux  sous  GNURadio  et  choisir  une  fréquence
  d’échantillonnage globale de 2 MHz.

    ![2-2-sample-rate](./src/img/2-2-sample-rate.png)

3. Dans le but de définir le message à transmettre, nous utiliserons le bloc « Vector Source ». \
  Expliquer le fonctionnement de ce bloc.

    Selon le wiki, [accessible ici](https://wiki.gnuradio.org/index.php/Vector_Source),
    le block `Vector Source` prend en argument, en Python, une liste ou un tuple, considéré
    un vecteur d'entrée et produit un flux d'échantillon qui s'arrête soit selon son comportement
    par défaut soit par une condition définie par l'utilisateur.

4. Nous  prendrons  comme  exemple  la  séquence  de  données  à  transmettre  suivante :
  `0111010100000000` que nous souhaitons transmettre à un rythme
  de `1` symbole toutes les 1ms.
  Donner le débit d’une telle transmission.

    Le débit d'une telle transmission serait de 1 kbits/s car 1ms = 1*10^(-3) s.

5. Utiliser un bloc « Repeat » pour obtenir la bonne durée d’un symbole.

    Après le calcul si-dessous, afin d'obtenir le temps nécessaire à ajouter pour avoir une
    transmission avec 1 symbole toutes les 1ms.

    ![2-4-calc-T](./src/img/2-4-calc-T.png)

    Cela nous donne donc `2000` répétitions à avoir
    afin d'obtenir 1 symbole toutes les 1ms.

6. Compléter le diagramme avec un bloc oscilloscope « QT GUI Time Sink » afin de vérifier que le
  signal produit est conforme à vos attentes.

    ![2-6-diagram](./src/img/2-6-gnu-diagram.png)

7. Mesurer la durée d'un symbole.

    ![2-7-](./src/img/2-7-time-symbol.png)

    Sur l'image ci-dessus, on voit bien que la durée d'un symbole est d'1 ms.

8. Dans le but de transmettre ce signal, nous souhaitons utiliser une porteuse de fréquence 100
  KHz. Utiliser pour cela un bloc « Signal Source » afin de générer un signal cosinus réel (en effet,
  en modulation d’amplitude, seule la voie I d’un modulateur IQ est utilisée). Compléter le
  montage pour obtenir une modulation OOK. Vérifier le signal modulé obtenu. Est-il conforme
  à vos attentes ?

    ![2-8-diagram](./src/img/2-8-diagram.png)
    ![2-8-signal](./src/img/2-8-signal.png)

    D'après l'image ci-dessus, le signal est bien conforme à nos attentes.

9. <br />

10. Expliquer le rôle de ce bloc et la signification de toutes les configurations.

    > [!NOTE]
    > Dans le cas du `Taps` utilisé pour le filtre pass bas,
    > d'après la documentation de la fonction en C,
    > [disponible ici](https://www.gnuradio.org/doc/doxygen/classgr_1_1filter_1_1firdes.html#abe4f96dd8c792ca3ddda655cd60f494b),
    > les quatres arguments utilisés avec leur valeur sont:
    >
    > - `gain`: 1
    > - `sampling_freq`: `samp_rate` (2 MHz)
    > - `cutoff_freq`: 20 000 Hz
    > - `transition_width`: 500

    Paramètres:

    - `Decimation`: Le ratio entre la fréquence d'échantillonage initiale et celle qui sera la fréquence d'échantillonage après ce bloc.
    - `Taps`: Le filtre appliquer à ce bloc, il utilise notamment la librairie firdes disponible en C et en Python.
    - `Center frequency`: La fréquence utilisée pour centrer le signal.
    - `Sample Rate`: Fréquence d'échantillonage

11. Compléter le diagramme et vérifier que vous obtenez bien le résultat attendu. Commentez.

    ![2-9-diagram](./src/img/2-9-diagram.png)
    ![2-9-diagram](./src/img/2-9-signal.png)

    D'après l'image ci-dessous, le signal récupéré semble bien être
    le signal d'origine.

12. <br />

    ![2-12-diagram](./src/img/2-12-diagram.png)

    - Signal avec peu de bruit:

      ![2-12-low-noise](./src/img/2-12-signal-low-noise.png)

    - Signal avec beaucoup de bruit:

      ![2-12-high-noise](./src/img/2-12-signal-high-noise.png)

    En ayant du bruit gaussien sur la ligne de transmission, le signal
    observé ressemble plus à un signal que l'on aurait reçu sur un médium
    physique.

    On voit aussi que le bruit déforme effectivement le signal à un niveau où l'on
    ne peut pas forcément le reconnaître visuellement.

13. A partir de quelle amplitude de bruit estimez-vous que la réception du signal n’est plus fiable ?

    ![2-13-noise-good](./src/img/2-13-noise-but-good.png)
    ![2-13-noise-bad](./src/img/2-13-noise-whats-that.png)

    Comme l'on peut le voir sur les images ci-dessus, à partir de 0.7 d'amplitude
    notre signal commence à devenir trop bruité pour que l'on soit capable de distinguer un
    0 d'un 1.

14. Régler l’amplitude du bruit gaussien à 0,5.
  Nous allons traiter le signal obtenu afin d’obtenir un signal « débruité » plus facile à décoder.

  s
