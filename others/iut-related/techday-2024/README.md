---
Author: Alexis Opolka
Company: IUT Béziers
Subject: Techday
---

# Techday - L'IoT par satellite: Etat des lieux et persperctives

Captronic -> Société qui aide les autres qui manquent de connaissances électroniques
Déjà 5 ans de techday
formations en entreprise (quand une seule) ou programmées (quand plusieurs)

## Hiotee

  - Maturation UM2
  - Tracking Worldwide
  - Monitoring

  - Nano Satellites --> Lanceurs dédiés --> Réduction de prix --> Démocratisation du spatial (?)

  - orbites:
    - leo (IoT/SAT, Imagery)
    - geostationnary
    - meo (GPS)

  - 80% terre en zone blanche

  - Marchés
    - Mines, Défenses, Oil & Gas, Transport, Maritime, Agriculture

  - Avantages du satellite
    - Connexion permanente
    - Backup (Fiabilité)
    - Hors couverture
    - Sécurité

  - Applications
    - Sécurité et tracabilité (Geofencing, Tracking personnel)
    - Automatisation (Télémetrei, Maintenance à distance)
    - Monitorign Environnemental (Données météo)

  - Enjeu de souveraineté
    - Constellations
      - Kinéis - Français
        - 25 satellites prévus
        - Orbite Basse (LEO)
        - Bande UHF
      - Astrocast - Suisse
        - 80 satellites prévus
        - Orbite Basse (LEO)
        - Bande L/S
      - Projet ELO (standby)
      - Immarsat ELERA
        - 15 satellites
        - GEO
        - Bande L
        - Ca fonctionne en IP, gateway LoRaSaT (?)
      - Iridium: USA
        - 66 satellites actifs
        - Orbite Basse (LEO)
        - Bande L
        - Module Iridium 150-200€ (cher)
      - GlobalStart: USA
        - 48 satellites
        - Orbite Basse (LEO)
        - Bande L et S
      - EchoStar Mobile Satellite
        - 1 satellite
        - GEO
        - Bande S et sub GhZ
      - Swarm
        - 120 PICOSatellite
        - Orbite Basse (LEO)
        - Bande VHF

  - Amis Americains
    - SpaceX
    - Amazon

  - OneWeb, C'est français (Oneweb et Google, non ?)

HioSense
HioTrack
HioSafe

## Kinéis

  - Freins
    - Interconnexion complexe (Normes)
    - Déploiements complexes
    - Maintenance ++
    - Use-Case pas adaptées

  - Constellation: 25 satellites
    - 5 pour l'AIS --> communications marines

  - System overview
    - Kineis informations processing and distribution center
    - ground station
    - Kineis Constellation

L'utilisation de la batterie peut être un frein pour certains acteurs, un workflow lourd consomme plus (?)

  - Services
    - Device messaging --> Quelques messages par jours (?, très peu de possibilité dans ce cas)

1. ????

1. Choisir son antenne

   - External
   - Internal
   - Custom

1. Step HW Selection

## Semtech and Sierra Wireless

Standardisation
problème de la massification

NTN = "Non Terrestrial Networks", 3GPP

### CEA - Antennes miniatures pour IoT par satellite

Premier prototype d'antenne sans contexte (c'est trop bien, j'adore)
prototype d'antenne sur contexte metallique

3cmx5cm

chambre anéchoide

Gain supérieur à une antenne COTS
Augmentation de 60% des messages reçus par les satellites de la constellation Kinéis

réduction bande passant de l'antenne

grande sensibilité du réglage de son impédance

labos: LAPCI et LAIR

mesure in-situ d'impédance sur RC IC
reconfigurabilité en impédance et/ou en fréquence d'antenne miniature (LAPCI)

  Permettre d'unifier l'impédance de la ligne peu importe la fréquence (par exemple entre 2.4 et 1),
  de manière à perdre le moins possible et de s'aligner sur une impédance de 50 Ohms.

## Hortus Technologies

## Emitech Groupe

Réglementations

laboratoire tierce partie
traçabilité et métrologie
bien-fondé technique
confidentialité prestations

marquage CE

- Directive REd
  - Domaine d'application
    Radioélectriques
  - Exigences essentielles
    - Sécurité et Santé
    - Compatibilité Electromagnétique
    - utilisation du spectre

    - Chargeurs universels
    - Cybersécurité

  - Procédures d'évaluation
    - Seul
      - procédure A: Contrôle interne de la fabrication (auto-certification)
        - Essais réalisés suivant la ou les Nomes harmonisées radio
        - Au choix pour les exigences CEM et sécurité/santé
          - Analyse de risques
        - ne peut pas prétendre au module A
          - Inexistence d'une norme harmonisée adaptée
          - Intégration d'un module qualifié sans re-test global complet du produit final
          - Gamme validée en ne testant qu'un produit
    - organisme notifié
      - Procédure B&C: Examen UE de type (ON) + Contrôle prod.
        - Présentation d'un dossier à un ON -> Certificat
        - Suivi interne de la production (info vers ON si modif)
      - Procédure H: Assurance complète de la qualité
        - Suivi global du système qualité

- Directive ou Règlement Ce
  - Procédures d'évaluation
  - analyse de risque
  - Validations techniques
  - Informations utilisateur
  - Engagements fabricant

  Ca compte aussi sur l'importation

- Produit a evaluer
  - Radio propriétaire
    - Essais complets NH inadaptée ou NNH
      - organisme Notifié
        - Procédure BC&H
    - Essais complets NH adaptée
      - Procédure A Autocertif DoC sans ON

  - Intégration module
    - Essais complets NH adapaptés
      - Procédure A autocertif. DoC sans ON
    - Essais complets NH inadaptées ou NNH
      - organisme notifié
        - Procédure B&C ou H DoC avec ON
    - Essais partiels (intégration)
      - organisme notifié
        - Procédure B&C ou H DoC avec ON

---
