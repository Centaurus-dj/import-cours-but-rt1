# R509-TP3 - Elastic Search

## 1 - Mise en place d'un environnement Elastic Security

On fait:

```sh
git clone https://github.com/pushou/siem.git
```

On modifie `sysctl.conf`, disponible [ici](./src/sysctl.conf)

On lance make:

```sh
make es
make siem
make fleet
```

> [!NOTE]
> Pour voir le mot de passe, on fait:
>
> ```sh
> make pass
> ```

Les services sont donc:

- Kibana Web Interface: [`10.202.0.209:5601`](https://127.0.0.1:5601)
- Elastic Search RESTful API: [`10.202.0.209:9200`](https://10.202.0.209:9200)
- Evebox Web Interface: [`localhost:5636`](http://localhost:5636)
- Fleet: [`10.202.0.209:8220`](https://10.202.0.209:8220)

On se connecte sur l'interface web à l'adresse locale:

![](./src/img/elastic-web-interface.png)

> [!NOTE]
> La connexion en HTTPS est nécessaire, il n'écoute que sur le port 443.

Il faut ajouter le certificat sur notre système afin de pouvoir installer des agents:

- `/etc/ca-certificates.conf`: On ajoute l'entrée de notre certificat
- `/usr/share/ca-certificates`: On crée un dossier et on ajoute notre certificat

    > [!NOTE]
    > Récupéré depuis la commande
    >
    > ```sh
    > make prca
    > ```

- On fait la commande suivante:

    ```sh
    sudo update-ca-certificates
    ```

## 2 - Configuration de fleet

Fleet

On peut voir qu'un agent sur notre Fleet est bien installé:

![elastic-fleet-configuration](./src/img/elastic-fleet-configuration.png)

On peut donc le renseigner de manière absolure afin de pouvoir plus tard installer des agents:

![fleet-configured](./src/img/fleet-configured.png)

## 3 - Agent Elastic sur un poste Windows

### 3.1 - Installation de l'agent Elastic sur un poste Windows

On installe ensuite un agent Windows:

```pwsh
$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.15.1-windows-x86_64.zip -OutFile elastic-agent-8.15.1-windows-x86_64.zip
Expand-Archive .\elastic-agent-8.15.1-windows-x86_64.zip -DestinationPath .
cd elastic-agent-8.15.1-windows-x86_64
.\elastic-agent.exe install --url=https://10.202.0.229:8220 --enrollment-token=bkNvS0xaSUJSVDR5Z0xTWDR6NWo6YU1QTWViTjBSRFNUM3dKdXhrMS1WQQ==
```

Avant tout, on ajoute notre certificat en suivant les instructions Microsoft: ![learn.microsoft.com](https://learn.microsoft.com/en-us/biztalk/adapters-and-accelerators/accelerator-swift/adding-certificates-to-the-certificates-store-on-the-client)

![win-agent-add-certificate](./src/img/win-agent-add-certificate.png)

On peut voir qu'il a bien été connecté à notre Fleet:

![win-fleet-agent](./src/img/win-fleet-agent-configured.png)

On peut aussi voir que la `Agent Policy` a bien été créée:

![agent-policy-windows](./src/img/agent-policy-windows.png)

### 3.2 - Déploiement des intégrations pour Windows

Comme l'on peut le voir, nous avons bien ajouté les intégrations:

![policy-integrations](./src/img/policy-integrations.png)

### 3.3 - Configuration de l'`intégration` de `Elastic Defend`

Comme l'on peut le voir, notre intégration est en mode Detect:

![](./src/img/elastic-defend-detect.png)

Et notre vérification est désactivée:

![](./src/img/elastic-defend-verif-host.png)

### 3.4 Retrouvez des informations sur votre poste Windows

![hosts-metrics](./src/img/hosts-metrics.png)

1. Retrouvez les métriques systèmes de votre poste Windows dans Kibana (voir menu "hosts")

    ![win-host-metrics](./src/img/win-host-metrics.png)

2. Retrouvez les métriques sur les services de votre machine Windows

    ![win-services-metrics](./src/img/win-services-metrics.png)

3. Retrouvez les pourcentages des différents type d'évènements windows
    ("security" , "sysmon" ...) de votre machine dans Kibana.

    ![win-services-percent-metrics](./src/img/win-services-percent-metrics.png)

4. Retrouvez les alertes liées à Suricata

    ![](./src/img/)

### 3.5 - Lancez et détectez une simulation d'attaques

1. Chargez et faites "enable" de toutes les règles de détection fournies en standard par Elastic.
    Seules celles nécessitant un abonnement ne seront pas activées.

2. Clonez le "repository" suivant dans votre machine windows : [github.com/NextronSystems/APTSimulator](https://github.com/NextronSystems/APTSimulator)

    On installe d'abord Git et Sysmon:

    ```pwsh
    winget install git.git
    winget install Microsoft.Sysinternals.Sysmon
    ```

    On configure Sysmon:

    ```pwsh
    .\Sysmon64.exe -m
    .\Sysmon64.exe -i
    ```

    On peut ensuite clone le dépot:

    ```pwsh
    git clone https://github.com/NextronSystems/APTSimulator
    ```

3. Lancez le script "APTSimulator.bat" en mode administrateur et lancez toutes les simulations d'attaques pour faire réagir l'agent

    On lance le script:

    ```pwsh
    .\APTSimulator.bat
    ```

4. Vérifiez que vous avez bien des alertes dans la partie "Security" de Kibana

    On peut voir que nos alertes sont bien remontées:

    ![apt-simulator-attacks-alert](./src/img/apt-simulator-attacks-alert.png)

5. Créez une timeline sur l'alerte "process creation".
    Analyser cet évènement avec Kibana pour obtenir un joli graphique.

    ![]()

## 4 - Agent Elastic sur un poste Linux

1. Installez l'agent Elastic sur un poste Linux (VM ou physique du CloudLab) et connectez-le à votre 
    "fleet server" comme vous l'avez fait pour l'agent Windows.

    On fait:

    ```sh
    curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.15.1-linux-x86_64.tar.gz
    tar xzvf elastic-agent-8.15.1-linux-x86_64.tar.gz
    cd elastic-agent-8.15.1-linux-x86_64
    sudo ./elastic-agent install --url=https://10.202.0.229:8220 --enrollment-token=cFRrNkpKSUJlNXFVWXptRTdHUzI6TVNLaUJBeEZSOWkybGVjejNXR3JGdw==
    ```

    Notre Agent Linux a bien été installé:

    ![linux-agent](./src/img/linux-agent.png)

2. Installez et visualiser les tableaux de bord produits par l'intégration "audit manager". (auditd ne
    doit pas être activé sur votre poste Linux.


    ![linux-auditd-overview](./src/img/linux-auditd-overview.png)

3. Installez "Sysmon for Linux". voir [github.com/Sysinternals/SysmonForLinux/blob/main/INSTALL.md](https://github.com/Sysinternals/SysmonForLinux/blob/main/INSTALL.md)

    On installe Sysmon:

    ```sh
    wget -q https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    sudo dpkg -i packages-microsoft-prod.deb
    sudo apt-get update
    sudo apt-get install apt-transport-https
    sudo apt-get update
    sudo apt-get install sysmonforlinux
    ```

    > [!NOTE]
    > On doit lancer `sysmon`, de la manière suivante:
    >
    > ```sh
    > sudo sysmon -i
    > ```

4. Installez et visualiser le tableau de b ord de l'intégration "Sysmon for Linux".
    Ajouter `/var/log/syslog` dans les logs à collecter dans l'intégration

    ![linux-sysmon-overview](./src/img/linux-sysmon-overview.png)
    ![linux-sysmon-overview](./src/img/linux-sysmon-overview-2.png)
    ![linux-sysmon-overview](./src/img/linux-sysmon-overview-3.png)
