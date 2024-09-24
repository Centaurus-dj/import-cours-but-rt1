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

### 3.1 - Installation de l'agent Elastic sur un p oste Windows

On installe ensuite un agent Windows:

```pwsh
$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.15.1-windows-x86_64.zip -OutFile elastic-agent-8.15.1-windows-x86_64.zip
Expand-Archive .\elastic-agent-8.15.1-windows-x86_64.zip -DestinationPath .
cd elastic-agent-8.15.1-windows-x86_64
.\elastic-agent.exe install --url=https://10.202.0.229:8220 --enrollment-token=S3pqLUk1SUJlNXFVWXptRWxkeW86NUtsekplTk9Uc0dFNXNYekVZTUI2dw==
```

> [!NOTE]
> On a besoin de mettre `--insecure` afin que le certificat ne soit pas vérifié avec
> une autorité de certificats.

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

### 3.4 Retrouvez des informations sur votre p oste Windows

1. Retrouvez les métriques systèmes de votre poste Windows dans Kibana (voir menu "hosts")

    ![]()

2. Retrouvez les métriques sur les services de votre machine Windows
3. Retrouvez les pourcentages des différents type d'évènements windows
    ("security" , "sysmon" ...) de votre machine dans Kibana.
4. Retrouvez les alertes liées à Suricata

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

