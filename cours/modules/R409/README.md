---
Author: Alexis Opolka
Company: IUT de Béziers - Parcours DevCloud
Subject: Conteneurisation
Copyright: All Rights Reserved
---

# R4D09 - Les fondamentaux de la conteneurisation

1. ## 1 - Compétences à acquérir lors du TP

1. ## 2 - Pré-requis, recommendations et notation du TP

1. ## 3 - Docker sous Linux

    > [!NOTE]
    > Nous avons effectué une installation dite `rootless` de Docker
    > nous permettant de converser avec le daemon Docker sans avoir
    > de privilèges.
    >
    > Cela n'est pas une configuration par défaut, pour plus d'informations
    > veuillez vous diriger sur la page de documentation accessible [ici](https://docs.docker.com/engine/security/rootless/).

    1. Quelle est la version de Docker installée ?

        On fait:

        ```sh
        docker --version
        ```

        nous donnant:

        ```sh
        Docker version 26.1.0, build 9714adc
        ```

    1. Vérifiez que votre installation foncionne bien avec la commande:

        ```sh
        docker run hello-world
        ```

        1. Que vous explique le retour de cette commande ?

            Cette commande explique le processus "habituel" du fonctionnement d'un docker.  
            Si une de ces étapes échoue, cela veut dire que notre installation est défectueuse.

            1. Docker a réussi à contacter le "Daemon" installé sur le client
            2. Ce "Daemon" a réussi à vérifier, et mettre à jour si nécessaire, l'image `hello-world` via le dépôt d'images Docker.
            3. Un conteneur a bien été créé de l'image précédemment récupérée
            4. La sortie (output) du conteneur a bien été réécrite sur notre terminal.

        2. Retrouvez sur [hub.docker.com](https://hub.docker.com) l'image hello-world.

            L'image hello-world est accessible à l'adresse suivante: `https://hub.docker.com/_/hello-world`.

            > [!NOTE]
            > Elle est aussi accessible directement, [ici](https://hub.docker.com/_/hello-world).

        3. Expliquez les mécanismes en jeux pour la création du container `helloworld`.  
            Quel est le fichier sur DockerHub qui permet de créer le container ?

            La création du container `helloworld` se fait de `scratch` (à partir de zéro),
            on retrouve les instructions en C dans le fichier `hello.c`, accessible [ici](https://github.com/docker-library/hello-world/blob/master/hello.c).

    1. Recherchez les images officielles Debian à l'aide de docker search.  
        Récupérez-les ainsi que les images officielles busybox (une distribution légère).

        On récupère les images officielles `Debian` à l'adresse suivante: `https://hub.docker.com/_/debian`, accessible [ici](https://hub.docker.com/_/debian).

        On fait de même pour busybox, se trouvant à l'adresse suivante: `https://hub.docker.com/_/busybox` accessible [ici](https://hub.docker.com/_/busybox).

        > [!NOTE]  
        > Il faut noter que la dénomination officielle pour ces images qualifie que ces images sont crées par
        > l'équipe de Docker et non l'équipe de développement derrière le système d'exploitation Debian.
        >
        > On peut noter le `_` dans l'URL, signifiant que l'image provient de Docker (Namespace réservé) et non
        > d'une organisation tierce. Pour plus d'informations, voir à cette addresse: `docs.docker.com/trusted-content/official-images`, accessible [ici](https://docs.docker.com/trusted-content/official-images/using/)

    1. Créez votre premier container à partir de l'image Debian officielle et en utilisant la commande `docker run -d debian` sans argument.

        On fait:

        ```sh
        docker run -d debian:latest
        ```

    1. En utilisant la commande `docker ps` vérifiez que le container est "vivant" ?  Expliquez ?

        En faisant:

        ```sh
        docker ps
        ```

        On ne voit pas le container, on peut donc considérer qu'il n'est pas "vivant", car il n'a pas
        de processus actifs.

    1. Relancez le `docker run` en lui donnant comme argument bash `-c "while :; do echo "coucou"; sleep 1; done"`.

        On fait:

        ```sh
        docker run -it debian -c "while :; do echo "coucou"; sleep 1; done"
        ```

    1. Stoppez et redémarrez le container.

        On fait:

        ```sh
        docker stop 4a3560eda125
        ```

        puis

        ```sh
        docker restart 4a3560eda125
        ```

    1. Supprimez le container

        On fait:

        ```sh
        docker rm --force 4a3560eda125
        ```

    1. Utilisez les options `-it` afin d'être dans le container après son lancement.

        On fait:

        ```sh
        docker run -it debian
        ```

    1. Même opération mais nommant le container et son hostname DebianOne.

        On fait:

        ```sh
        docker run --name="DebianOne" -h "DebianOne" -it debian
        ```

    1. Détachez-vous du container DebianOne puis rattachez-vous à lui de nouveau

        Après un <kbd>Ctrl+C</kbd>, on fait:

        ```sh
        docker start DebianOne
        ```

        puis

        ```sh
        docker attach DebianOne
        ```

    1. Lancez un processus bash supplémentaire dans le container DebianOne. Pour celà utilisez la commande `docker exec`.

        On fait:

        ```sh
        docker exec DebianOne bash
        ```

    1. Listez le container restant. Ne listez ensuite que le dernier ContainerId.

        On fait:

        ```sh
        docker ps -a -l
        ```

        Pour lister le dernier `ContainerId`, on peut faire:

        ```sh
        docker ps -a -f id=<ContainerId>
        ```

    1. Utilisez un volume pour donner à votre container l'accès à un répertoire de l'hôte. Quels sont les
        avantages de l'utilsation d'un volume ? un inconvénient ? A l'aide de la commande docker volume
        affichez les volumes présents sur votre hôte.

        On fait:

        ```sh
        docker volume create hello
        ```

        Pour afficher les volumes présents sur l'hôte, on fait:

        ```sh
        docker volume list
        ```

    1. Supprimez le container et son image

        On fait:

        ```sh
        docker rmi -f debian && docker rm -f DebianOne
        ```

    1. Supprimez tous les containers avec un oneliner sous bash. Idem pour les images

        - Pour supprimer tous les containers avec un onliner en bash, on fait:

            ```sh
            docker rm -f $(docker ps -a -q)
            ```

        - Pour supprimer toutes les images avec un oneliner en bash, on fait:

            ```sh
            docker rmi -f $(docker image list -q)
            ```

    1. Supprimez les images et les containers non utilisés avec la commande `docker system prune`.

        On fait:

        ```sh
        docker system prune
        ```

1. ## 4 - Création d'images Docker

    > [!NOTE]
    > Nous devons récupérer des fichiers de cours dans le git suivant:
    >
    > ```sh
    > git@github.com:pushou/tpdocker.git
    > ```

    1. ### 4.1 - Build d'une image Docker Debian

        1. Construisez l'image `debian:vosinitiales` à partir du Dockerfile du repository et de la commande `docker build`.

            Pour build l'image `debian:ao`, on peut faire:

            ```sh
            docker build -t debian:ao .
            ```

            > [!NOTE]
            > Nous devons être dans le répertoire du dépôt `tpdocker` avec un `Dockerfile`, sinon
            > cette commande renverra une erreur.

        1. Expliquez ce que font les différentes commandes `RUN, ENV, FROM` de ce DockerFile.

            - `RUN`

                1. Il met à jour les en-têtes pour APT, mets à jours les paquets puis installe des paquets dépendances
                2. Il met à jour la locale et la timezone dans les fichiers de configurations de la Debian
                3. Il crée le répertoire `/home/git/.ssh`

            - `ENV`

                1. Rend le docker non interactif et précise les variables d'environnement de locale / langue en Frnaçais. (et UTF-8)
                2. Définie à nouveau la locale ainsi que la langue actuelle

                > [!NOTE]
                > Nous traitons les blocs de commande ENV par numérotation.

            - `FROM`

                Informe le moteur Docker qu'il faut baser notre image Docker à partir de la version nommée `bullseye` de `Debian`.

        1. Que est l'intérêt de faire tous les `apt-get` en une seule fois pour la taille de l'image Docker (indice: voir AUFS et Docker).

            L'intérêt de faire toutes les opérations apt-get en une commande nous permet d'éviter de trop "committer" sur notre image
            et ainsi donc la rendre moins lourde qu'au contraire.

        1. A partir de l'image `debian:vosinitiales`, générez une image `pingfour` qui permettra de lancer un container de type ping se limitant à 4 envois ICMP vers `www.iutbeziers.fr` par défaut.
            Vous utiliserez les commandes `ENTRYPOINT` et `CMD` dans le Dockerfile.

            On fait:

            ```sh
            docker build -t pingfour -f Dockerfile.ping4 .
            ```

        1. Lancez un container issu de cette image au travers de la commande `docker run -rm -it ...`
            A quoi sert le `-rm` ?

            On fait:

            ```sh
            docker run --rm -it pingfour
            ```

            L'option `--rm` nous permet de détruire automatiquement le container dès que l'on sortira
            de celui-ci.

        1. Peux-t-on changer la destination du ping ? Le nombre de ping ?

            On peut changer la destination du ping ainsi que son nombre.

        1. utilisez l'option `entrypoint` de `docker run` pour changer la commande `ping` par `traceroute`.

            On peut utiliser `entrypoint` de `docker run` pour changer la commande `ping` par `traceroute`,
            nous allons par contre devoir s'assurer que le container a traceroute d'installé, pour cela, nous allons
            modifier notre Dockerfile afin de lui ajouter `traceroute` dans les paquets dépendences à installer.

            Puis, nous pourrons faire:

            ```sh
            docker run --entrypoint="traceroute" -it debian www.iutbeziers.fr
            ```

        1. Transformez votre container en image en le "commitant" via la commande `docker commit ...`

            On peut faire:

            ```sh
            docker commit <docker-name>
            ```

        1. Créez un projet dont le nom sera de la forme `prenom.nom` sur registry.iutbeziers.fr

            > [!WARNING]
            > A date du TP, le registry accessible à l'adresse suivante: [registry.iutbeziers.fr](https://registry.iutbeziers.fr)
            > ne nous permet pas de nous connecter car le login `LDAP` ne fonctionne pas.

        1. Utilisez la commande `docker tag` pour générer une image `registry.iutbeziers.fr/votre-prenom.votre-nom/adet-ping` à partir de l'image committée précédemment.
            Poussez cette image sur votre namespace généré précédemment vers le registry de l'IUT de Béziers.

            > [!WARNING]
            > A date du TP, le registry accessible à l'adresse suivante: [registry.iutbeziers.fr](https://registry.iutbeziers.fr)
            > ne nous permet pas de nous connecter car le login `LDAP` ne fonctionne pas.

        1. Récupérez l'image de votre voisin via un docker pull sur le registry mis en place par votre enseignant.
            Instanciez-la afin de vérifier qu'elle fonctionne.

            > [!WARNING]
            > A date du TP, le registry accessible à l'adresse suivante: [registry.iutbeziers.fr](https://registry.iutbeziers.fr)
            > ne nous permet pas de nous connecter car le login `LDAP` ne fonctionne pas.

    1. ### 4.2 - Installation d'un "insecure registry" sur votre poste de travail

        En suivant [docs.docker.com/registry/insecure](https://docs.docker.com/registry/insecure) installez un registry sur votre VM et testez le.  
        L'installation d'un certificate n'est pas demandée.

        On fait:

        - Installation du registry:

            ```sh
            docker run -d -p 5000:5000 --restart=always --name registry registry:2
            ```

        - Ajout d'un container `fedora` du registry Docker à notre registry:

            ```sh
            docker pull fedora:40
            docker tag fedora:40 localhost:5000/fedorao
            docker push localhost:5000/fedorao
            ```

        - On peut maintenant voir que le registry local a bien l'image `fedorao` car le `docker pull` a bien été effectué:

            ```sh
            docker image remove fedora:40
            docker image remove localhost:5000/fedorao
            docker pull localhost:5000/fedorao
            ```

    1. ### 4.3 - Création d'un Dockerfile afin de générer une image debian ssh

        Créez un Docker afin de générer un container fournissant un serveur SSH.  
        Vous utiliserez l'image `registry.iutbeziers.fr/debianiut` comme image de base.

        Vous instancierez cette image sous forme d'un container accessible en ssh sur le port 2222.  
        Le container permettrea l'authentification sur le compte root.

        > [!NOTE]
        > Utilisez `chpasswd` pour saisir le mot de passe root du container lors de son build.

    1. ### 4.4 - Dockérisation d'une application Python

        1. Sans le container, lancez l'application suivante fonctionnant avec Python 3:

            ```py
            from flask import Flask

            app = Flask(__name__)

            @app.route("/")
            def hello_world():
                return "Le python c'est bon, mangez en"

            if __name__ == "__main__":
                app.run(debug=True, host="0.0.0.0")
            ```

            Lancez l'appli via:

            ```sh
            pip3 install flask
            export ENV_FLASK_APP=app.py
            export ENV_FLASK_ENV=development
            export FLASK_APP=app.py flask run
            ```

        1. "Dockérisez" cette application

            Dockérisez cette application en créant un Dockerfile et en utilisant une image Python 3 (base Debian).  
            L'application doit être accessible sur le port 9999 de l'hôte.

            Notre configuration Dockerfile:

            ```dockerfile
            from python:3.12

            maintainer Alexis Opolka <support@alexis-opolka.dev>

            COPY flask-uncontainerized.py /

            RUN pip install --no-cache-dir --upgrade pip && \
            pip install --no-cache-dir flask

            EXPOSE 5000/tcp
            EXPOSE 5000/udp

            CMD ["python3", "/flask-uncontainerized.py"]
            ```

            On fait:

            ```sh
            docker run -p 9999:5000 -it flaskapp
            ```

            On peut maintenant accéder au conteneur en accédant à l'IP suivante:

            ```url
            http://127.0.0.1:9999/
            ```

        1. Création d'un docker-compose pour une application en "micro-services"

            Il est possible de démarrer plusieurs containers afin de former un ensemble applicatif cohérent.

            Pour cela, il faut utiliser un fichier `docker-compose.yml` qui sera utilisé par la commande `docker-compose` afin de démarrer cet ensemble cohérent de containers.

            1. Modifiez l'application flask précédente de façon à afficher le TP du container sur l'uri `/whoami`.  
               Recréez une image.

                ```py
                from flask import Flask, jsonify, request
                import os

                app = Flask(__name__)

                @app.route("/")
                def hello_world():
                    return "Le Python c'est bon, mangez en.\n"

                @app.route("/whoami")
                def get_task():
                    ipv4 = os.popen("ip add show eth0").read().strip().split("inet")[1].split("/")[0].strip()
                    return jsonify({"ip_hote": ipv4}), 200

                if __name__ == "__main__":
                    app.run(debug=True, host="0.0.0.0", port=5000)
                ```

            1. Créez un fichier `docker-compose.yml` qui générera un ensemble contenant un container `traefik`
               (version 2+) et un container issus de notre application. Aidez-vous de [docs.traefik.io](https://docs.traefik.io/).  
               Vous pouvez utiliser le domaine `nip.io` qui renvoie une ip privée lorsqu'on fait une requête (mon ip privée est ici `192.168.1.95`):

                ```sh
                host 192.168.1.95.nip.io
                ```

                Vous pouvez générer un certificat auto-signé avec `mkcert`:

                ```sh
                mkcert 192.168.1.95.nip.io "whoami.192.168.1.95.nip.io" "*.192.168.1.95.nip.io"
                ```

                L'application `whoami` sera testée avec la commande suivante:

                ```sh
                curl -H Host:whoami.192.168.1.95.nip.io http://whoami.192.168.1.95.nip.io
                ```

                Il vous reste les certificats à générer et le fichier `docker-compose.yml` à créer.

                ---

                On crée nos configurations comme ceci:

                - Le fichier `docker-compose.yml`:

                    ```yaml
                    services:
                        reverse-proxy:
                            # The official v3 Traefik docker image
                            image: traefik:v3.0
                            ports:
                                # The HTTP port
                                - "80:80"
                                - "443:443"
                                # The Web UI (enabled by --api.insecure=true)
                                - "3000:8080"
                            volumes:
                                - /var/run/docker.sock:/var/run/docker.sock:ro
                                - ./192.168.1.236.nip.io+2-key.pem:/certs/192.168.1.236.nip.io+2-key.pem
                                - ./192.168.1.236.nip.io+2.pem:/certs/192.168.1.236.nip.io+2.pem
                                - ./traefik_v3.toml:/etc/traefik/traefik.toml
                                - ./traefik_dynamic.toml:/etc/traefik/dynamic/traefik_dynamic.toml
                                - ./traefik.logs.d/:/var/log/
                            labels:
                                - "traefik.http.services.traefik.loadbalancer.server.port=8080"

                        flaskapp:
                            # Our current flask application
                            image: flaskapp:latest
                            build:
                            dockerfile: ./Dockerfile

                            expose:
                                # The Web UI port
                                - "5000:5000"
                                - "80:80"

                            labels:
                                - "traefik.enable=true"
                                - "traefik.http.routers.api.rule=Host(`flaskapp.192.168.1.236.nip.io`)"
                                - "traefik.http.services.flaskapp.loadbalancer.server.port=5000"

                        whoami:
                            # A container that exposes an API to show its IP address
                            image: traefik/whoami

                            expose:
                                - "80:80"

                            labels:
                                - "traefik.enable=true"
                                - "traefik.http.routers.api.rule=Host(`whoami.192.168.1.236.nip.io`)"
                                - "traefik.http.services.whoami.loadbalancer.server.port=80"
                    ```

                - Le fichier `traefik.toml`:

                    ```toml
                    [global]
                        checkNewVersion = true
                        sendAnonymousUsage = true

                    [entryPoints]
                        [entryPoints.web]
                            address = ":3000"

                        [entryPoints.websecure]
                            address = ":443"

                    [log]
                        level = "DEBUG"
                        filePath = "/var/log/traefik.log"
                        format = "common"

                    [accessLog]
                        filePath = "/var/log/access.log"
                        format = "common"

                    [api]
                        insecure = true
                        dashboard = true

                    [ping]
                       entryPoint = "traefik"

                    [providers]
                        [providers.docker]
                            defaultRule = "Host(`{{ normalize .Name}}.192.168.1.236.nip.io`)"
                            exposedByDefault = true
                        [providers.file]
                            directory = "/etc/traefik/dynamic/"
                            watch = true
                    ```

                - Le fichier `traefik_dynamic.toml`:

                    ```toml
                    [http.middlewares.simpleAuth.basicAuth]
                    users = [
                        "admin:$apr1$..QI.Lsl$MWLpkfS026zCDTU6NOB9x0"
                    ]

                    [http.routers]
                    [http.routers.api]
                        rule = "Host(`192.168.1.236.nip.io`) && PathPrefix(`/dashboard/`)"
                        entrypoints = ["websecure", "web"]
                        middlewares = ["simpleAuth"]
                        service = "api@internal"

                        [http.routers.api.tls]


                    [http.routers.to-whoami]
                        rule = "Host(`whoami.192.168.1.236.nip.io`)"
                        service = "whoami@docker"
                        entrypoints = ["websecure", "web"]
                        # middlewares = ["simpleAuth"]

                        [http.routers.to-whoami.tls]

                    [http.routers.to-flaskapp]
                        rule = "Host(`flaskapp.192.168.1.236.nip.io`)"
                        service = "flaskapp@docker"
                        entrypoints = ["websecure", "web"]
                        # middlewares = ["simpleAuth"]

                        [http.routers.to-flaskapp.tls]

                    [[tls.certificates]]
                    certFile = "/certs/192.168.1.236.nip.io+2.pem"
                    keyFile = "/certs/192.168.1.236.nip.io+2-key.pem"
                    ```

                Test:

                ```sh
                curl -H Host:whoami.192.168.1.236.nip.io https://whoami.192.168.1.236.nip.io
                ```

                nous donnant:

                ```sh
                Hostname: c69d5cdc8873
                IP: 127.0.0.1
                IP: ::1
                IP: 192.168.16.4
                RemoteAddr: 192.168.16.2:59602
                GET / HTTP/1.1
                Host: whoami.192.168.1.236.nip.io
                User-Agent: curl/8.2.1
                Accept: */*
                Accept-Encoding: gzip
                X-Forwarded-For: 192.168.1.236
                X-Forwarded-Host: whoami.192.168.1.236.nip.io
                X-Forwarded-Port: 443
                X-Forwarded-Proto: https
                X-Forwarded-Server: b35ee8d46d1c
                X-Real-Ip: 192.168.1.236
                ```

            1. Utilisez l'option scale de `docker-compose` pour générer plusieurs containers afinn d'équilibrer la charge.  

                > [!NOTE]
                > On peut utiliser:
                >
                > ```sh
                > docker compose up -d --scale <mon-app>=<mon-nombre>
                > ```

                On fait:

                ```sh
                docker compose up -d --scale whoami=2
                ```

                On peut voir avec `traefik` que nous avons bien plusieurs containers générés
                et que l'équilibrage de charge les a pris en compte.

                ![traefik-equilibrage-charge](./src/img/traefik-ha-whoami.png)

1. ## 5 - Réseaux Docker

---

Pastebin

````md
```sh
```
````
