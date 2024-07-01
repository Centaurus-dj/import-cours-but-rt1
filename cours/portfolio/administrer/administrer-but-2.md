---
Author: Alexis Opolka

---

# Administrer BUT2

## Introduction

### Glossaire des termes et du formattage syntaxique

#### Termes

<!-- | Terme    | Définition                                                                                                                                                  |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IDE      | Integrated Development Environment / Envrionnement de Développement Intégré                                                                                 |
| Endpoint | Chemin, notamment d'une API, où l'on a accès à différentes actions en fonction du cheminn et de l'API                                                       |
| CRUD     | Create, Read, Update, Delete / Créer, Lire, Editer, Supprimer - Un terme utilisé principalement pour catégoriser les applications avec des bases de données |
| Wrappers | Programme qui appelle un programme en spécifiant certaines options et facilitent les appels à ce dit programme                                              | -->

#### Formattage syntaxique

| Syntaxe                  | Signification                                                      |
| ------------------------ | ------------------------------------------------------------------ |
| `un mot en surbrillance` | Un mot ou une suite de mots ayant de l'importance dans le contexte |

### Situations professionnelles

| Situations professionnelles                                                                            |
| ------------------------------------------------------------------------------------------------------ |
| Conception et administration de l'infrastructure du réseau informatique d'une entreprise               |
| Installation et administration des services réseau informatique d'une entreprise                       |
| Déploiement et administration des solutions fixes pour les clients d'un opérateur de télécommunication |
| Gestion des postes clients                                                                             |
| Utilisation des technologies de la virtualisation                                                      |

### Composantes Essentielles

| Composantes Essentielles                                                   |
| -------------------------------------------------------------------------- |
| Choisir les solutions et technologies réseaux adaptées                     |
| Respecter les principes fondamentaux de la sécurité informatique           |
| Utiliser une approche rigoureuse pour la résolution des dysfonctionnements |
| Respecter les règles métiers                                               |
| Assurer une veille technologique                                           |
| Communiquer avec les clients et les différents acteurs impliqués           |
| Utiliser une approche rigoureuse et méthodique (démarche scientifique)     |

### Apprentissages Critiques

| Apprentissages Critiques                                                                                |
| ------------------------------------------------------------------------------------------------------- |
| Configurer et dépanner le routage dynamique dans un réseau (protocoles IGP)                             |
| Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau |
| Déployer des postes clients et des solutions virtualisées adaptées à une situation donnée               |
| Déployer des services réseaux avancés                                                                   |
| Identifier les réseaux opérateurs et l'architecture d'Internet                                          |
| Travailler en équipe pour développer ses compétences professionnelles                                   |
| Déployer et gérer des postes clients                                                                    |
| Déployer des solutions virtualisées en particulier pour le poste client                                 |
| Utiliser des services conteneurisés                                                                     |
| Déployer et utiliser un système de supervision                                                          |
| Déployer des technologies d'opérateurs (BGP et commutation de paquets MPLS)                             |

## Sommaire

- [Administrer BUT2](#administrer-but2)
  - [Introduction](#introduction)
    - [Glossaire des termes et du formattage syntaxique](#glossaire-des-termes-et-du-formattage-syntaxique)
      - [Termes](#termes)
      - [Formattage syntaxique](#formattage-syntaxique)
    - [Situations professionnelles](#situations-professionnelles)
    - [Composantes Essentielles](#composantes-essentielles)
    - [Apprentissages Critiques](#apprentissages-critiques)
  - [Sommaire](#sommaire)
  - [Composantes Essentielles](#composantes-essentielles-1)
    - [Choisir les solutions et technologies réseaux adaptées](#choisir-les-solutions-et-technologies-réseaux-adaptées)
    - [Respecter les principes fondamentaux de la sécurité informatique](#respecter-les-principes-fondamentaux-de-la-sécurité-informatique)
    - [Utiliser une approche rigoureuse pour la résolution des dysfonctionnements](#utiliser-une-approche-rigoureuse-pour-la-résolution-des-dysfonctionnements)
    - [Respecter les règles métiers](#respecter-les-règles-métiers)
    - [Assurer une veille technologique](#assurer-une-veille-technologique)
    - [Communiquer avec les clients et les différents acteurs impliqués](#communiquer-avec-les-clients-et-les-différents-acteurs-impliqués)
    - [Utiliser une approche rigoureuse et méthodique (démarche scientifique)](#utiliser-une-approche-rigoureuse-et-méthodique-démarche-scientifique)
  - [Apprentissages Critiques](#apprentissages-critiques-1)
    - [Configurer et dépanner le routage dynamique dans un réseau (protocoles IGP)](#configurer-et-dépanner-le-routage-dynamique-dans-un-réseau-protocoles-igp)
    - [Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau](#configurer-et-expliquer-une-politique-simple-de-qos-et-les-fonctions-de-base-de-la-sécurité-dun-réseau)
    - [Déployer des postes clients et des solutions virtualisées adaptées à une situation donnée](#déployer-des-postes-clients-et-des-solutions-virtualisées-adaptées-à-une-situation-donnée)
    - [Déployer des services réseaux avancés](#déployer-des-services-réseaux-avancés)
    - [Identifier les réseaux opérateurs et l'architecture d'Internet](#identifier-les-réseaux-opérateurs-et-larchitecture-dinternet)
    - [Travailler en équipe pour développer ses compétences professionnelles](#travailler-en-équipe-pour-développer-ses-compétences-professionnelles)
    - [Déployer et gérer des postes clients](#déployer-et-gérer-des-postes-clients)
    - [Déployer des solutions virtualisées en particulier pour le poste client](#déployer-des-solutions-virtualisées-en-particulier-pour-le-poste-client)
    - [Utiliser des services conteneurisés](#utiliser-des-services-conteneurisés)
    - [Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau](#configurer-et-expliquer-une-politique-simple-de-qos-et-les-fonctions-de-base-de-la-sécurité-dun-réseau-1)
    - [Déployer des technologies d'opérateurs (BGP et commutation de paquets MPLS)](#déployer-des-technologies-dopérateurs-bgp-et-commutation-de-paquets-mpls)
  - [Situations professionnelles](#situations-professionnelles-1)
    - [Conception et administration de l'infrastructure du réseau informatique d'une entreprise](#conception-et-administration-de-linfrastructure-du-réseau-informatique-dune-entreprise)
    - [Installation et administration des services réseaux informatique d'une entreprise](#installation-et-administration-des-services-réseaux-informatique-dune-entreprise)
    - [Déploiement et administration des solutions fixes pour les clients d'un opérateur de télécommunication](#déploiement-et-administration-des-solutions-fixes-pour-les-clients-dun-opérateur-de-télécommunication)
    - [Gestion des postes clients](#gestion-des-postes-clients)
    - [Utilisation des technologies de la virtualisation](#utilisation-des-technologies-de-la-virtualisation)

## Composantes Essentielles

### Choisir les solutions et technologies réseaux adaptées

Choisir les solutions et technologies réseaux adaptées c'est savoir prendre la décision de ne pas prendre un switch 10 Gbits alors
que notre réseau ne sort qu'au maximum 100 mbits/s, ou bien d'utiliser de l'OSPF pour le routage dynamique lorsque nous avons un
réseau trop grand pour que des routes manuelles soient le choix le plus judicieux.

Dans le cadre étudiant, j'ai du mettre en place des réseaux, j'ai ainsi dû faire des choix sur les solutions réseaux
et les technologies à utiliser.
Comme par exemple, le choix de mettre de l'OSPF dans du BGP avec des loopbacks afin de garder les routes BGP valides même si les
interfaces tombent.

Ou choisir d'utiliser `dnsmasq`, un serveur DNS et DHCP, principalement utilisé par Fedora, mais pas que, lorsque mon environnement ne contient que des clients
sous Fedora.

Dans le cadre personnel, j'ai du mettre en place un système de vidéosurveillance et en profiter pour mettre à niveau l'infrastructure réseau,
j'ai préféré choisir du matériel "user-friendly" même s'il présentait plus de limitations technique car il permet un panneau d'accès facile
et visuel, simplifiant la formation des personnes ayant des droits administrateurs dessus.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de choisir les solutions et technologies réseaux adaptées.

### Respecter les principes fondamentaux de la sécurité informatique

Dans le cadre étudiant et personnel, j'ai déjà eu à respecter les principes fondamentaux de la
sécurité informatique. J'ai eu, que ce soit dans une SAE ou lors de la mise en place du nouveau matériel
réseau Ubiquiti chez moi, à créer des VLANs, des ACLs, créer un wifi invité afin de pouvoir limiter l'accès au réseau
aux personnes ne faisant pas parties des membres du foyer.

Tout comme la mise en place d'un réseau de vidéosurveillance nécessite certaines règles de sécurité, au niveau de l'accès réseau,
au niveau de la rétention des données ainsi que de leur emplacement.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de respecter les principes fondamentaux de la sécurité informatique.

### Utiliser une approche rigoureuse pour la résolution des dysfonctionnements

Utiliser une approche rigoureuse pour la résolution des dysfonctionnements nous permet de ne pas rebooter le routeur du réseau
alors que nous n'avions pas notre câble ethernet de branché.

j'ai eu à de plusieurs reprises, le besoin d'utiliser une approche rigoureuse afin de résoudre des dysfonctionnements,
princiapelement en réseau, mais cela peut s'appliquer tout autant à la programmation ou à n'importe quel sujet ayant
des dysfonctionnements à proprement parler et qui relève d'un domaine scientifique.

Dans le cadre personnel, j'ai eu à comprendre pourquoi le proxy que j'avais mis en place ne fonctionnait pas.

Il a fallu donc tester la configuration du proxy pour s'assurer qu'elle ne soit pas défectueuse, puis l'accès à l'adresse de
destination avec le client sans passer par le proxy afin de s'assurer qu'elle est accessible de notre réseau, puis enfin, dans
le cas où les deux étapes fonctionneraient, regarder les réponses HTTP de la requête afin de se rendre compte que l'on recevait
une réponse avec code d'erreur, faisant "crasher" le proxy et l'empêchant de fonctionner comme attendu.

Je pense donc, qu'à date d'écriture, je suis compétent et capable d'utiliser une approche rigoureuse pour la résolution des dysfonctionnements.

### Respecter les règles métiers

J'ai eu dans le cadre personnel, professionnel et étudiant, l'occasion de m'appuyer sur les règles métiers que je connais de part mon expérience
mais aussi celles qui découlent de la formation que je suis actuellement afin de construire des réseaux et des infrastructures sur des bases saines.

Il est à toutefois noter que les règles métiers, vues de manière objective, ne se trouvent être que des bonnes recommendations et ne peuvent pas
tout le temps être suivies en fonction de nos circonstances. Il est néanmoins préférable de les suivre, si la situation nous le permet.

Dans le cadre personnel, j'ai eu à concevoir une infrastructure réseau contenant de la vidéosurveillance, avoir connaissance et respecter les
règles métiers m'a permis de savoir qu'il était préférable de faire un VLAN dédié à la vidéosurveillance, tout comme il était préférable de
faire un VLAN dédié pour les visiteurs et les utilisateurs courant du foyer.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de respecter les règles métiers.

### Assurer une veille technologique

J'assure quotidiennement une veille technologique, qui me permet d'être à jour sur les technologies que j'utilise mais aussi sur les
nouvelles technologies qui sortent, que ce soit en programmation en matériel physique (i.e. Hardware). \
Pour cela, j'écoute des podcasts, je regarde, quand mon emploi du temps me le permet, des vidéos de chaines youtube "techniques" tel que Linus Tech Tips
sur différents sujets de la technologie, je préfère tout de même venir m'abonner au flux RSS ou au flux Linkedin de Pro, Créateurs, Entrepreneurs ou Organisationnels
afin d'être rapidement tenu au courant de possibles nouveautés.

Je pense donc, qu'à date d'écriture, je suis compétent et capable d'assurer une veille technologique

### Communiquer avec les clients et les différents acteurs impliqués

Comme dis l'année dernière, communiquer avec les clients et les différents acteurs impliqués d'un projet, c'est d'être capable de se faire
comprendre par tous les acteurs impliqués peut importe leur niveau de technicité.

Par exemple, lorsque j'ai continué à travailler sur mon site web, qui est toujours en construction, j'ai pu ouvrir et discuter dans une issue GitHub sur
l'ajout du support du type `StaticImageData` lors de l'utilisation de la libraire `primer/react` développée et maintenue par GitHub, même si la langue
utilisée n'est pas ma langue natale.

![github-primer-issue](./src/github-primer-issue.png)

Je pense donc, qu'à date d'écriture, je suis compétent et capable de communiquer avec les clients et les différents acteurs impliqués.

### Utiliser une approche rigoureuse et méthodique (démarche scientifique)

## Apprentissages Critiques

### Configurer et dépanner le routage dynamique dans un réseau (protocoles IGP)

Dans le réseau, après avoir configuré du routage dynamique dans un réseau, il est possible d'avoir besoin de le dépanner,
notamment par manque d'expérience avec la technologie ou à cause de cas imprévus.

Dans le cas d'IGP tel que OSPF utilisés en concordance avec BGP, j'ai pu dans le cadre personnel et étudiant,
me confronter à la configuration et au dépannage de routage dynamique.

J'ai dû, par exemple comprendre pourquoi les routes OSPF n'étaient pas retransmises dans du BGP alors qu'inversement cela fonctionnait,
cela a été finalement une simple erreur de configuration de ma part où j'avais oublié de préciser de aussi prendre en compte les routes statiques.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de dépanner le routage dynamique dans un réseau.

### Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau

Une QoS ou Quality Of Service est un outil que l'on peut configurer afin d'assurer un certain niveau de service, c'est
à dire d'assurer ou non que tous les paquets émis vont être reçus, ou autre.

Lors du Festival du Fantastique, j'ai pu mettre en place une politique de QoS afin d'assurer la bonne transmissions de données critiques.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau.

### Déployer des postes clients et des solutions virtualisées adaptées à une situation donnée

La virtualisation est un outil comme un autre, elle ne peut être utilisée qu'à son plein potentiel que lorsque elle est
adaptée aux besoins d'une situation donnée.

Je n'ai malheureusement pas pu déployer de postes clients mais j'ai pu déployer des solutions virtualisées adaptées, que ce soit pour la SAE-401 où j'ai pu déployer
des services au sein d'une VM et accessible du réseau afin de permettre sa réplication.

Je pense donc, qu'à date d'écriture, je suis compétent, ou en tout cas le serais au besoin, de déployer des postes clients et des solutions virtualisées adaptées à une situation donnée.

### Déployer des services réseaux avancés

Dans le cadre personnel et étudiant, j'ai pu déployer des services avancés tel qu'un LDAP, un SAMBA, un serveur NFS, un serveur proxy, un serveur proxy inverse.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de déployer des services réseaux avancés.

### Identifier les réseaux opérateurs et l'architecture d'Internet

### Travailler en équipe pour développer ses compétences professionnelles

Lors de la SAE 401 et de la SAE 301, j'ai pu travailler en équipe afin de développer des compétences professionnelles,
j'ai pu développer mes compétences professionnelles en gestion de projet et en gestion d'équipe.

![gh-project-sae-41](../programmer/src/github-project-sae-41.png)

Je pense donc, qu'à date d'écriture, je suis compétent et capable de travailler en équipe pour développer ses compétences professionnelles

### Déployer et gérer des postes clients

Je n'ai pas pu, lors de cette année, déployer et gérer en pratique des postes clients, je pense néanmoins en être capable
où seulement la solution utilisée pourrait me nécessiter de lire un peu de documentation afin de comprendre et apprendre
les actions spécifiques à cette solution à effectuer.

### Déployer des solutions virtualisées en particulier pour le poste client

Depuis que j'ai accès à l'infrastructure de Enzo Cadière ou que j'ai connaissance de la capacité à mon ordinateur de virtualiser à un certain degré,
j'ai pu déployer plusieurs solutions virtualisées en particulier pour le poste client.

Dans le cadre personnel, j'ai pu déployer un LDAP, un GitLab, un Scodoc, un WScodoc sous forme de machines virtuelles.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de déployer des solutions virtualisées en particulier pour le poste client

### Utiliser des services conteneurisés

Depuis que la conteneurisation est possible et facile d'utilisation, il est simple d'utiliser des services conteneurisés.

Dans le cadre de la SAE-401, j'ai du installer et configurer des services conteneurisés afin d'ils soient déployés avec un outil tel que Ansible.
J'ai pu par exemple configurer un CMS Javascript du nom de Ghost:

![ghost](./src/ghost.png)

Comme la plupart des services non monoléthiques, il a été plutôt facile de transformer le Dockerfile de ce service en docker-compose afin qu'il puisse
être déployable sur notre infrastructure de SAE.

Je pense donc, qu'à date d'écriture, je suis compétent et capable d'utiliser des services conteneurisés.

### Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau

Une QoS ou Quality Of Service est un outil que l'on peut configurer afin d'assurer un certain niveau de service, c'est
à dire d'assurer ou non que tous les paquets émis vont être reçus, ou autre.

Lors du Festival du Fantastique, j'ai pu mettre en place une politique de QoS afin d'assurer la bonne transmissions de données critiques.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau.

> [!NOTE]
> Est-ce une duplicata des Composantes Essentielles, je ne comprends pas ce qu'il est nécessaire d'écrire dans la version de l'aprentissage critique qui soit fondamentalement
> différent de la composante essentielle.

### Déployer des technologies d'opérateurs (BGP et commutation de paquets MPLS)

Lorsque nous gérons le routage à grande échelle, nous préferrons utiliser des algorithmes tels que BGP ou MPLS,
qui nous permettent de router dynamiquement tout en répondant aux besoins de routage nécessaire dans de telles infrastructures.

Dans le cadre étudiant, j'ai eu à faire du BGP, et comme toute bonne pratique, j'ai mis en place des routes BGP allant d'une loop^back à une autre loopback
permettant de garder en vie les routes même lorsque l'interface tombe.

Je pense donc, qu'à date d'écriture, je suis compétent et capable de déployer des technologies d'opérateurs (BGP et commutation de paquets MPLS).

## Situations professionnelles

### Conception et administration de l'infrastructure du réseau informatique d'une entreprise

Dans le cadre étudiant et personnel, j'ai été amené à faire la conception et l'administration de l'infrastructure du réseau informatique d'une entreprise,
ou tout du moins ce qui peut s'y apparenter.

Comme dis plus en haut, j'ai du installer un système de vidéosurveillance, combiné à une mise à niveau nécessaire du réseau, m'a forcé à faire à nouveau la
conception de l'infrastructure d'un réseau en prenant en compte la sécurité, les accès des utilisateurs, etc.

Il m'a été nécessaire de m'appuyer sur les ressources R401, R301, R302, R303, R306 et R307, des apprentissages critiques `Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau`,
`Configurer et expliquer une politique simple de QoS et les fonctions de base de la sécurité d'un réseau`, `Déployer des services réseaux avancés` ainsi que les apprentissages critiques

### Installation et administration des services réseaux informatique d'une entreprise

Dans le cadre étudiant et personnel, j'ai été amené à faire l'installation de services réseaux et leur administration.
Comme précédemment dis, j'ai du installer de la vidéosurveillance, mais qui dis vidéosurveillance dis stockage réseau, mais j'ai aussi
pu mettre en place un serveur mail, ainsi qu'un serveur Gitea, un serveur Apache et un serveur NodeJS.

Il m'a été nécessaire de m'appuyer sur les ressources R401, R303, R304, R307, des apprentissages critiques `Déployer des solutions virtualisées en particulier pour le poste client`,
`Déployer des services réseaux avancés`, ``

### Déploiement et administration des solutions fixes pour les clients d'un opérateur de télécommunication

### Gestion des postes clients

Cette année, je n'ai pas eu à faire de la gestion des postes clients, je pense néamoins être capable de mettre en place
une gestion des postes clients.

Il me faudrait tout du moins m'appuyer sur les ressources R3D16, R3D17, R304, R303, des apprentissages critiques `Déployer des solutions virtualisées en particulier pour le poste client`.

### Utilisation des technologies de la virtualisation

Dans le cadre étudiant et personnel, j'ai pu utiliser des technologies de virtualisation tel que KVM, QEMU et leurs wrappers comme virt-install, virsh, boxes (sous Fedora). \
J'ai aussi pu utiliser des logiciels permettant de faire de la virtualisation tel que Proxmox, GNS3, OpenNebula, etc.

Il m'a été nécessaire de m'appuyer sur les ressources R410, R3D17, R3D16, des apprentissages critiques `Déployer des solutions virtualisées en particulier pour le poste client` et
`Déployer des postes clients et des solutions virtualisées adaptées à une situation donnée`.
