---
Author:
  - Alexis Opolka
  - Lucas Simpol
Company: IUT Béziers
Subject: Sécurisation des conteneurs
Copyright: All Rights Reserved
---

# R410 - Développement de microservices

1. ## 1 - Installation de Docker et obtenir de l’aide

   1. Rappel: Installation de Docker sous Linux.

      - Vérifier  la version installée de Docker:

        ```bash
        docker --version
        ```

      - Obtenir des informations sur Docker installé

        ```bash
        docker info
        ```

      - Obtenir de l'aide sur Docker:

        ```bash
        docker help
        ```

      - Lancer un conteneur:

        ```bash
        docker run <docker-name>
        ```

      - Lister les docker en cours d'exécution:

        ```bash
        docker ps
        ```

      - Lister tous les docker lancés peu importe leur état d'exécution

        ```bash
        docker ps -a
        ```

      - Lister les images en local:

        ```bash
        docker images
        ```

      - Supprimer le docker en local:

        ```bash
        docker rm <container-id>
        ```

      - Supprimer l'image docker en local:

        ```bash
        docker rmi <image-id>
        ```

1. ## 2 - Peurs sur les containers

   1. Etat des lieux rapide de la sécurité des containers

      Les containers sont souvent vu comme étant d’un niveau de sécurité moindre que celui d’une machine virtuelle.  
      C’est le cas mais il ne fait pas perdre de vue que ce modèle est plus sécurisé que l’hébergement simple de plusieurs services
      sur un même hôte bien que systemd puisse apporter lui aussi des éléments de sécurité identiques à ceux utilisés dans les containers.

      **Un container reste donc plus sécurisé qu’un processus ou un groupe de processus lancé sur un hôte sans les contingentements fournis par les namespaces , les cgroups et les capabilities.**

      Néanmoins le mix de ces éléments impacte le niveau de privilèges du containers et il faut donc être conscient de ce que vous faites
      en donnant accès à tel ou tel privilège.  
      Un container super-privilégié (ils sont parfois nécessaires) peut être très dangereux pour la sécurité de votre hôte.  
      En fonction des besoins de sécurité remontés par l’analyse de risques il est néanmoins concevable de mettre un container par machine virtuelle.  
      Ces machines virtuelles sont minimalistes afin de fournir des performances acceptables dans le cadre d’un instanciation suffisamment rapide pour ne pas être considérée comme pénalisante.  

      C’est la tendance à ce jour.

   2. Les menaces

      Plusieurs menaces pèsent sur les containers :

      - L’installation de packages vulnérables: des packages vulnérables peuvent être utilisés pour le build de l’image.

        Il est donc important d’utiliser un scanner de vulnérabilités donnant la liste et l’impact des "Common Vulnerabilities and Exposures" de l’image.  
        Il est tout aussi important de disposer d’une chaîne d’intégration et de déploiement continu afin de mettre à jour les images en continu afin d’éviter
        une probabilité d’occurrence forte d’un incident de sécurité et/ou un impact important.  

      - Vulnérabilités au build de l’image proprement dit:

        Construire une image avec des droits root ou du groupe Docker peut poser des problèmes si l’attaquant s’introduit dans la chaîne de build.  
        L’utilisateur "root" est utilisé pour le daemon Docker ce qui est intrinsèquement dangereux.

      - L’intégrité des images de containers est un point important:

        Si l’attaquant modifie une image sur un registry à votre insu vous pouvez lui permettre d’accéder à votre environnement containérisé.  
        Ce n’est pas un problème spécifique de Docker mais le succès des containers amplifie la probabilité de trouver des images corrompues...

      - Un container ne doit pas être plus privilégié que nécessaire:

        En fonction des besoins il peut être judicieux de durcir le container en limitant les "capabilities" de celui-ci.

      - La question de l’appartenance des processus dans un container à un utilisateur est essentielle:

        Un processus appartenant au root de l’hôte dans un container induit une vulnérabilité en profondeur sur l’hôte
        et les autres containers dans le cas ou le container est compromis.

      - Attaques par dépassement des capacités:

        Un container qui n’est pas contingenté au niveau de ses ressources peut être soumis à un déni de services
        et peut perturber l’exploitation de l’application qu’il porte mais aussi les resources des autres containers voire de l’hôte lui-même.

      - l’encodage en dur des mots de passes ou de token peut poser des problèmes triviaux mais courant comme en témoigne les chasseurs de secrets sur GitHub.

      - Vulnérabilités de l’hôte: un hôte vulnérable ou exposant une large surface aux attaques donnera l’accès à tous les containers.

      - Vulnérabilités liées au réseau: un container compromis peut permettre d’attaquer d’autres containers via le réseau si ceux ci sont accessibles.

      - L’infrastructure liée à Docker doit être aussi prise en compte lors de l’analyse de risques: une socket d’un daemon Docker en accès distant ouvert est une porte d’entrée très appétissante pour un attaquant.

      - Le Daemon Docker est lancé sous root afin de lui permettre de gérer les containers.

        Il est possible d’être "rootless" afin de limiter la surface d’attaque.  
        Dans le cadre d’un hébergement "multi-tenants" 1 on peut légitimement se poser la question de la sécurité de vos clients lors de l’utilisation de containers.  
        Heureusement pour nous il existe des outils pour mitiger le risque ou l’accepter en toute connaissance de cause.

1. ## 3. Utilisation des namespaces par Docker

    Les namespaces permettent de dresser un décor pour les processus de nos containers.  
    Le container ne verra que le contexte qu’on l’autorise à voir au travers des namespaces et on ne peut pas attaquer ce qu’on ne peut pas atteindre.  
    Un container est donc contraint par les namespaces qui sont appliqués par le Kernel à ses processus.

   1. Accéder au namespace de l’hôte depuis un container Docker c’est mal

      Créez un container et vérifiez que les options suivantes de docker run `-–pid=host` et `--net=host` permettent d’accéder aux processus et au réseau de l’hôte.

      On peut faire:

      ```bash
      docker run -it --rm --pid=host --net=host --name host_access ubuntu:latest /bin/bash
      ```

      - On vérifie que l'on voie les processus de l'hôte:

        ```bash
        ps -ef
        ```

        nous donnant:

        ```sh
        root       57116       2  0 07:20 ?        00:00:00 [kworker/4:0-events]
        root       57215       2  0 07:20 ?        00:00:00 [kworker/u33:2-hci0]
        root       57399       2  0 07:21 ?        00:00:00 [kworker/14:0-events]
        root       57413       2  0 07:21 ?        00:00:00 [kworker/1:2]
        ubuntu     58004   16780  0 07:22 ?        00:00:00 docker run -it --rm --pid=host --net=host --name host_access ubuntu
        root       58125       2  0 07:22 ?        00:00:00 [kworker/u32:1-btrfs-endio-write]
        root       58126       2  0 07:22 ?        00:00:00 [kworker/u32:2-btrfs-delalloc]
        root       58134       1  0 07:22 ?        00:00:00 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 5fb2d4a0a0af16
        root       58154   58134  0 07:22 pts/0    00:00:00 /bin/bash
        root       58199       2  0 07:23 ?        00:00:00 [kworker/5:0-events]
        root       58212       2  0 07:23 ?        00:00:00 [kworker/2:2]
        root       58240   58154 99 07:23 pts/0    00:00:00 ps -ef
        ```

      - On vérifie que l'on voie les interfaces réseaux de l'hôte:

        ```bash
        hostname -i
        ```

        nous donnant:

        ```sh
        192.168.227.199 10.0.3.1 172.17.0.1 172.18.0.1 192.168.124.1 192.168.100.1 192.168.200.1 fe80::78a3:379c:97c1:c19c fe80::fc54:ff:fe9f:2d7
        ```

      On peut finir par quitter le container.

   2. Utilisation des usernamespaces par Docker afin de limiter les droits d’un attaquant

      Docker présente une fonctionnalité depuis la version 1.10 très intéressante et très attendue en terme de sécurité:
      la possibilité d’utiliser des `user namespaces`.  

      Si l’attaquant prend le contrôle du container Docker et que le microservice du container est porté par root,
      l’attaquant a accès au root de l’hôte et donc aux autres containers.  
      Les `user namespaces` permettent d’avoir un compte qui a les droits de root dans le container
      et qui a les droits d’un utilisateur non privilégié sur l’hôte.

      1. Activez l’option `–userns-remap` avec le daemon docker afin d’activer les usernamespaces pour l’ensemble de containers.  
        Pour cela ajoutez dans le fichier `/etc/docker/daemon.json` :

          ```json
          {
            "userns-remap": "default"
          }
          ```

          suivi de :

          ```sh
          systemctl restart docker
          ```

          On va pouvoir ainsi mapper les `uid`/`gid` des users dans les containers à partir des fichiers `/etc/subuid` et `/etc/subgid`. Modifiez ce fichier.

          Nous avons par défaut ces valeurs:

          - `/etc/subuid`:

            ```sh
            test:100000:65536
            dockremap:165536:65536
            ```

          - `/etc/subgid`:

            ```sh
            test:100000:65536
            dockremap:165536:65536
            ```

          Lorsque l'on modifie `/etc/docker/daemon.json` comme ceci:

          ```json
          {
            "userns-remap": "pushou"
          }
          ```

          nous obtenons:

          - `/etc/subuid`:

            ```sh
            test:100000:65536
            dockremap:165536:65536
            pushou:589824:65536
            ```

          - `/etc/subgid`:

            ```sh
            test:100000:65536
            dockremap:165536:65536
            pushou:589824:65536
            ```

          > [!NOTE]
          > Il est important d'utiliser un utilisateur existant sur l'hôte à la place de la valeur de `default`.  
          > Pour en créer un, faire:
          >
          > ```sh
          > useradd -u <user-id> <username>
          > ```

      2. Lancez un container avec un processus bash et vérifiez que dans le container ce processus est vu comme appartenant à root et comme appartenant à un utilisateur mappé dans l’hôte.  

          > [!NOTE]
          > Pour la suite du TP, désactiver les usernamespaces ils sont parfois contraignants quand il faut accéder aux partages sur l’hôte.  

          On lance notre conteneur:

            ```sh
            docker run -it --rm --name userns --userns=host ubuntu:latest /bin/bash
            ```

          On fait:

          ```sh
          ps -ef
          ```

          nous donnant

          ```sh
          UID          PID    PPID  C STIME TTY          TIME CMD
          root           1       0  0 06:41 pts/0    00:00:00 /bin/bash
          root          10       1  0 06:41 pts/0    00:00:00 ps -ef
          ```

   3. Contrôle des ressources allouées aux processus d’un container

      1. Contrôle des ressources des containers au travers des cgroups

          Un attaquant peut saturer un container en lançant un déni de services.  
          Si on ne limite pas les ressources consommées par un container, c’est l’hôte qui sera en manque de ressource à son tour.  
          Il est donc important de limiter les ressources prises par un container via les CGROUPS.

         1. A partir de ce Dockerfile.

             ```dockerfile
             FROM debian:latest
             RUN apt-get update && \
                 apt-get install -y stress
             ENTRYPOINT ["stress"]
             CMD ["--timeout 10 --cpu 10"]
             ```

             Générez une image d’un container "stresseur":

             ```sh
             cd ../buildstress
             docker rmi stress
             docker build -t stress .
             ```

         2. Lancez le container "stresseur" et ouvrez une fenêtre htop pour voir la consommation de ressources sur l’hôte:

             ```sh
             docker run -it --rm stress
             ```

             ![docker-stress-btop](./src/img/docker-stress-btop.png)
             ![docker-stress-btop-alexis](./src//img/docker-stress-btop-alexis.png)

         3. Récréez le container et limitez-le à l’utilisation d’un seul CPU.

            On fait:

            ```sh
            docker run -d --name stress --cpus 1 -m 100m stress
            ```

      2. Lutte contre l’épuisement des ressources du container et de l’hôte par déni de service local ( "fork bomb" par exemple ).

          Une forkbomb crée des processus qui vont eux mêmes générer (appel système FORK ) d’autres processus fils identiques au père.

          La commande suivante permet de lister les ressources du container à l’aide de la commande docker stats:

          ```bash
          docker stats --no-stream=True
          CONTAINER CPU % MEM USAGE / LIMIT MEM % NET I/O BLOCKI/O PIDS
          ```

          1. Dans votre machine virtuelle Ubuntu lancez une "forkbomb" bash dans un container.

              Si tout se passe bien votre container et votre machine virtuelle ne répondront plus, vous voilà prévenu...

              La commande suivante permet de lancer un container contenant une fork bomb:  

              ```bash
                docker exec -it deb1 /bin/bash -c ":(){ :|:& };:"
              ```

          2. Trouvez le moyen lors de sa création ( docker run ) de limiter le nombre de processus dans le container

              ```bash
                docker run --pids-limit 100 -d registry.iutbeziers.fr/debianiut
              ```

1. ## 4 - Sécurisation des capacités données à un container Docker

    Il existe des possibilités de rendre le container super-privilégié. C’est parfois nécessaire en dernier recours
    mais il faut en payer le prix en termes de sécurité

    1. Création d'un container privilégié

        Utilisez l’option `-–privileged` lors de la création d’un container.  
        Dans le container et l’aide de la commande `capsh` et de la commande `pscap2`
        obtenez les capabilities de votre container et de votre processus bash.

        Comparez avec un container non privilegié

        On crée une image Docker nous permettant d'utiliser `capsh` et `pscap`:

        ```dockerfile
        FROM debian:latest
        RUN apt-get update && \
          apt-get install -y libcap2-bin libcap-ng-utils
        ENTRYPOINT [ "/bin/bash" ]
        ```

        - Conteneur non privilégié:

          > [!NOTE]
          >
          > ```sh
          > docker run --rm -it caps
          > ```

          > [!TIP]
          > `caps` est le nom donné lors du build de l'image Docker pour cette question.

          - `capsh`

            On fait:

            ```sh
            capsh --print
            ```

            nous donnant

            ```sh
            Current: cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap=ep
            Bounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap
            Ambient set =
            Current IAB: !cap_dac_read_search,!cap_linux_immutable,!cap_net_broadcast,!cap_net_admin,!cap_ipc_lock,!cap_ipc_owner,!cap_sys_module,!cap_sys_rawio,!cap_sys_ptrace,!cap_sys_pacct,!cap_sys_admin,!cap_sys_boot,!cap_sys_nice,!cap_sys_resource,!cap_sys_time,!cap_sys_tty_config,!cap_lease,!cap_audit_control,!cap_mac_override,!cap_mac_admin,!cap_syslog,!cap_wake_alarm,!cap_block_suspend,!cap_audit_read,!cap_perfmon,!cap_bpf,!cap_checkpoint_restore
            Securebits: 00/0x0/1'b0 (no-new-privs=0)
            secure-noroot: no (unlocked)
            secure-no-suid-fixup: no (unlocked)
            secure-keep-caps: no (unlocked)
            secure-no-ambient-raise: no (unlocked)
            uid=0(root) euid=0(root)
            gid=0(root)
            groups=0(root)
            Guessed mode: HYBRID (4)
            ```

          - `pscap`

            On fait:

            ```sh
            pscap -a
            ```

            nous donnant:

            ```sh
            ppid  pid   name        command             capabilities
            0     1     root        bash                chown, dac_override, fowner, fsetid, kill, setgid, setuid, setpcap, net_bind_service, net_raw, sys_chroot, mknod, audit_write, setfcap +
            ```

        - Conteneur privilégié:

          > [!NOTE]
          >
          > ```sh
          > docker run --privileged --rm -it caps
          > ```

          - `capsh`

            On fait:

            ```sh
            capsh --print
            ```

            nous donnant

            ```sh
            Current: =ep
            Bounding set =cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read,cap_perfmon,cap_bpf,cap_checkpoint_restore
            Ambient set =
            Current IAB:
            Securebits: 00/0x0/1'b0 (no-new-privs=0)
            secure-noroot: no (unlocked)
            secure-no-suid-fixup: no (unlocked)
            secure-keep-caps: no (unlocked)
            secure-no-ambient-raise: no (unlocked)
            uid=0(root) euid=0(root)
            gid=0(root)
            groups=0(root)
            Guessed mode: HYBRID (4)
            ```

          - `pscap`

            On fait:

            ```sh
            pscap -a
            ```

            nous donnant:

            ```sh
            ppid  pid   name        command             capabilities
            0     1     root        bash                full +
            ```

        > [!NOTE]
        > Si le tuple IAB de capabilities vous intéresse, voir le man-page linux accessible [ici](https://www.man7.org/linux/man-pages/man3/cap_iab_dup.3.html).

        A quelles capabilities l’option –privileged donne-t-elle accès ?

        L'option `--privileged` permet de configurer le tuple IAB des capabilities afin de que les conteneurs docker héritent des capabilities du deamon.

    1. Prise de contrôle du container avec capabilities permettant une escalade de privilèges

        Nous allons utiliser les mécanismes existants de Docker afin de renforcer la sécurité d’un container.
        Utilisez votre container ssh afin de voir si peut limiter les capabilities du processus sshd.

        Testez-le à chaque fois à l'aide de la commande:

        > [!NOTE]
        > Aidez-vous de: [docs.docker.com/engin/../run](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)

        On utilise les capabilities suivantes lors d'une connexion ssh:

        ```sh
        cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid, \
        cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast, \
        cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio, \
        cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice, \
        cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write, \
        cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm, \
        cap_block_suspend,cap_audit_read,cap_perfmon,cap_bpf,cap_checkpoint_restore
        ```

        On fera donc:

        ```sh
        docker run --rm --cap-drop=ALL --cap-add SYS_ADMIN --cap-add NET_ADMIN --cap-add SYS_RAWIO \
        --cap-add SETPCAP --cap-add SETGID --cap-add SETUID --cap-add SETFCAP --cap-add CHOWN  \
        --cap-add FOWNER --cap-add DAC_OVERRIDE --rm -it debian
        ```

1. ## 5 - Attaque sur le daemon Docker par un utilisateur local à l’hôte

    1. Sous le compte d’un utilisateur appartenant au groupe Docker,
      trouvez le moyen d’accéder à `/etc/password` et `/usr/sbin/` de la machine en utilisant les volumes Docker.

        ```sh
        docker run -v /etc/passwd:/etc/passwd -v /usr/sbin:/usr/sbin -it \
        registry.iutbeziers.fr/debianiut /bin/bash
        ```

        ```sh
        cat /etc/passwd
        ```

        ```sh
        Debian-gdm:x:112:121:Gnome Display Manager:/var/lib/gdm3:/bin/false
        test:x:1000:1000:test,,,:/home/test:/bin/bash
        sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
        dockremap:x:114:122::/nonexistent:/bin/false
        ```

    2. Qu’en deduisez-vous de la sécurité d’un PC de développeur avec Docker ?

        Cela réduit grandement la sécurité sur un PC car si le docker se trouve être infecté
        il est possible de pouvoir récupérer tous les utilisateurs de la machine hôte.

1. ## 6 - Utilisation de AppArmor aﬁn de contrôler un container vulnérable à ShellShock

    Shellshock est une faille du shell permettant à un attaquant de prendre la main sur une machine. voir:

    - [https://www.symantec.com/connect/blogs/shellshock-all-you-need-know-about-bash-bug-vulnerabilit](https://www.symantec.com/connect/blogs/shellshock-all-you-need-know-about-bash-bug-vulnerabilit)
    - [http://www.cert.ssi.gouv.fr/site/CERTFR-2014-ALE-006/index.html](http://www.cert.ssi.gouv.fr/site/CERTFR-2014-ALE-006/index.html)

    1. Créez le fichier simple-cgi-bin.sh

        ```bash
        #!/bin/bash
        echo "Content-type: text/plain"
        echo
        echo
        echo "shellshockme if youcan"
        ```

    2. Générez l’image Docker suivante vulnérable à ShellShock au travers de ce Dockerfile:

        Créez un container shell-shock à partir de l’image registry.iutbeziers.fr/debian-lenny-shellshock.

        ```bash
        docker run -d -p 80:80 --name=hitme --hostname=hitme registry.iutbeziers.fr/debian-lenny-shellshock
        ```

    3. Vériﬁez qu’il est bien vulnérable à ShellShock en lancant un shell dans le container.

        ```bash
        hitme:/# env x='() { :;}; echo vulnerable'
        HOSTNAME=hitme
        TERM=xterm
        PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        PWD=/
        PS1=\h:\w\$ 
        SHLVL=1
        HOME=/root
        _=/usr/bin/env
        x=() { :;}; echo vulnerable
        hitme:/# 
        ```

    4. Vériﬁez à l’aide d’un wget que vous pouvez récupérer "à distance" le fichier /etc/password du container.

        ```bash
        curl -H 'User-Agent: () { :; }; echo ; echo ; /bin/cat /etc/passwd' bash -s :'' http://172.17.0.2/cgi-bin/simple-cgi-bin.sh

        root:x:0:0:root:/root:/bin/bash
        daemon:x:1:1:daemon:/usr/sbin:/bin/sh
        bin:x:2:2:bin:/bin:/bin/sh
        sys:x:3:3:sys:/dev:/bin/sh
        sync:x:4:65534:sync:/bin:/bin/sync
        games:x:5:60:games:/usr/games:/bin/sh
        man:x:6:12:man:/var/cache/man:/bin/sh
        lp:x:7:7:lp:/var/spool/lpd:/bin/sh
        mail:x:8:8:mail:/var/mail:/bin/sh
        news:x:9:9:news:/var/spool/news:/bin/sh
        uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
        proxy:x:13:13:proxy:/bin:/bin/sh
        www-data:x:33:33:www-data:/var/www:/bin/sh
        backup:x:34:34:backup:/var/backups:/bin/sh
        list:x:38:38:Mailing List Manager:/var/list:/bin/sh
        irc:x:39:39:ircd:/var/run/ircd:/bin/sh
        gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
        nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
        libuuid:x:100:101::/var/lib/libuuid:/bin/sh
        ```

1. ## 7 - Utilisation de SecComp pour limiter l’utilisation de certains appels systèmes

    Seccomp permet de filtrer des appels systèmes en KernelLand. Vous devez vérifier que votre kernel supporte cette fonctionnalité:

    ```bash
    cat /boot/config-6.1.0-13-amd64 | grep CONFIG_SECCOMP
      CONFIG_SECCOMP=y
      CONFIG_SECCOMP_FILTER=y
    ```

    et que votre version de SecComp est supérieure à >= 2.2.1. La fonctionnalité a uniquement été testée avec succès sur Ubuntu 16.

    1. Téléchargez le fichier default-no-chmod.json qui va interdire le lancement de la commande chmod dans le container.

        [https://nextcloud.iutbeziers.fr/s/F9RkFKGZMas9fnc](https://nextcloud.iutbeziers.fr/s/F9RkFKGZMas9fnc)

    2. Utilisez ce fichier pour limiter les appels systèmes du container lors du “docker run“.

        ```bash
        docker run --rm -it --security-opt seccomp=default-no-chmod.json  ubuntu bash
        ```

    3. Expliquez en le fonctionnement.

        Seccomp est une fonctionnalité du noyau Linux qui permet de filtrer les appels système effectués par un processus. Dans le contexte de Docker, vous pouvez utiliser Seccomp pour limiter les appels système qu'un conteneur est autorisé à effectuer

    4. Créez un container et lancez un chmod 777 sur le fichier /etc/password.

        ```bash
        chmod 777 /etc/passwd
        chmod: changing permissions of '/etc/passwd': Operation not permitted
        ```

        comme on peut le voir, on ne peut pas exécuté la commande sur le docker proteger mais sur un docker non proteger on peut.

1. ## 8 - Containers en lecture seule

    Créez un container Web et mettez-le en lecture seule. C’est trivial et idéal pour des containers mettant à disposition des contenus statiques. Refaites-le mais avec /tmp en lecture-écriture.

    1. Créez un container Web et mettez-le en lecture seule.

        ```bash
        docker run -d -p 80:80 --read-only --name=web registry.iutbeziers.fr/debianiut
        ```

    2. Refaites-le mais avec /tmp en lecture-écriture.

        ```bash
        docker run -d -p 80:80 --read-only --tmpfs /tmp --name=web registry.iutbeziers.fr/debianiut
        ```

1. ## 9 - Contrôle de l’élévation de privilèges dans un container via

    L’option `--security-opt=no-new-privileges`, buildez l’image en suivant le README du repo git suivant: [github.com/pushou/docker-secu-priv](https://github.com/pushou/docker-secu-priv).
    Testez et expliquez l’effet de cette option.

    Le `--security-opt=no-new-privileges` permet de bloquer l'élévation de privilèges dans un container.  
    Cela signifie que si un processus dans un container tente de lancer un processus avec des privilèges plus élevés, l'opération échouera.

1. ## 10 - Rootless containers

    Le mode rootless s’obtient le durcissement du daemon responsable de la gestion des containers qui n’a plus besoin d’être root afin de manager des containers.
    Docker n’est pas le seul "manager" de processus containairisé: Podman de RedHat est rootless par construction. Docker est néanmoins capable de fonctionner en userspace.

    1. En suivant la documentation officielle installez "Docker rootless" avec le user student.

        ```bash
        sudo apt install slirp4netns uidmap
        export FORCE_ROOTLESS_INSTALL=1
        curl -sSL https://get.docker.com/rootless | sh
        sudo setcap cap_net_bind_service=ep $HOME/bin/rootlesskit
        /home/student/bin/dockerd-rootless.sh --experimental --storage-driver vfs
        export XDG_RUNTIME_DIR=/home/student/.docker/run
        export PATH=/home/student/bin:$PATH
        export DOCKER_HOST=unix:///home/student/.docker/run/docker.sock
        ```

    1. Lancez un container et donnez un port d’écoute inférieur à 1024.

        ```bash
        docker run -d -p 80:80 --name=web registry.iutbeziers.fr/debianiut
        ```

        retour de la commande :  

        ```bash
        docker: Cannot connect to the Docker daemon at unix:///home/student/.docker/run/docker.sock. Is the docker daemon running?.
        See 'docker run --help'.
        ```

    1. Expliquez rapidement comment fonctionne Docker en mode Rootless.

        Docker en mode rootless permet une plus grande securité au detriment de la performance.  
        Il permet de faire fonctionner le démon Docker en tant qu'utilisateur non privilégié, c'est-à-dire sans nécessiter les privilèges de root.  
        Cela améliore la sécurité en réduisant le risque d'exploits du démon Docker qui pourraient donner un accès root à un attaquant.

1. ## 11 - Kata containers

    Il s’agit de faire tourner un container dans une machine virtuelle. La solution des "kata containers" permet de faire exécuter un container dans une machine virtuele KVM ou FireCracker (VMS d’AWS). On va tester ici la solution avec KVM:

    ```bash
    sudo snap install kata-containers --classic
    ```

    Modifiez le fichier `/etc/docker/daemon.json` et redémarrer Docker

    ```bash
    {
      "insecure-registries" : ["registry.infres.local"],
      "default-runtime": "runc",
      "runtimes": {
        "kata-runtime": {
          "path": "/snap/bin/kata-containers.runtime"
        }
      }
    }
    ```

    Maintenant que cela est fait et que l'on a redémarré le daemon Docker (`systemctl restart docker`),
    nous pouvons voir que l'on peut tout autant lancer des conteneurs.

    ```sh
    docker run --rm -it debian:latest
    ```

1. ## 12 - Annexe : Débugguer un container

    Les containers sont optimisés pour être les plus légers possibles et n’embarquent pas en général pas d’outils facilitant l’analyse. Voilà une façon de les débugguer (sur une idée de J. Petazzoni) 5:

    1. Générer une instance Apache. Cette instance ne contient pas d’éditeur ni de d’outils réseaux (iproute2/ifconfig)

        ```bash
        docker run -d --rm httpd
        ```

    2. Télécharger un binaire statique busybox

        ```bash
        wget https://www.busybox.net/downloads/binaries/1.31.0-defconfig-multiarch-musl/busybox-x86_64 \ -O busybox && chmod +x busybox
        ```

    3. Récupérez l’Id du container afin de copier le binaire busybox.

        ```bash
        docker cp ./busybox-x86_64 b6356349ccae:/busybox
        ```

    4. Vous pouvez maintenant utiliser les commandes de busybox pour analyser votre container.

        ```bash
        docker exec -it b6356349ccae /busybox ip a
          1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
              link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
              inet 127.0.0.1/8 scope host lo
                valid_lft forever preferred_lft forever
              inet6 ::1/128 scope host 
                valid_lft forever preferred_lft forever
          22: eth0@if23: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
              link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
              inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
                valid_lft forever preferred_lft forever
        ```

    5. Installez nsenter.

    6. Trouvez le pid d’un process dans le container :

        ```bash
        docker inspect b6356349ccae|grep -i pid
            "Pid": 5552,
            "PidMode": "",
            "PidsLimit": null,
        ```

    7. Utilisez nsenter pour retrouver les NameSpaces du container et lancez les commandes de votre hôte dans le container.

        ```bash
        export LANG=C
        nsenter --target 5552 -p -u -n -i
        ```

1. ## 13 - flintlock

    c'est un outil qui permet de mettre en place des docker sous forme de VM.

    1. mise en place de flintlock

        - installation des dependances:

            ```bash
            sudo apt install qemu qemu-kvm libvirt-clients libvirt-daemon-system virtinst bridge-utils

            sudo systemctl enable libvirtd
            sudo systemctl start libvirtd
            ```

        - création d'un réseaux virtuel:

            ```bash
            nano flintlock-net.xml
            ```

            ```xml
            <network>
              <name>flintlock</name>
              <forward mode='nat'>
                <nat>
                  <port start='1024' end='65535'/>
                </nat>
              </forward>
              <bridge name="$BRIDGE" stp='on' delay='0'/>
              <ip address='192.168.100.1' netmask='255.255.255.0'>
                <dhcp>
                  <range start='192.168.100.10' end='192.168.100.254'/>
                </dhcp>
              </ip>
            </network>
            EOF
            ```

            ```bash
            sudo virsh net-define flintlock.xml
            sudo virsh net-start flintlock
            ```

        - auto démarrage du réseau:

            ```bash
            sudo virsh net-autostart flintlock
            ```

        - connection au tap device

            ```bash
            TAPNAME=tap0

            sudo ip tuntap add ${TAPNAME} mode tap
            sudo ip link set ${TAPNAME} master ${BRIDGE} up

            sudo virsh net-dhcp-leases default
            ```

        - installation de containerd

            ```bash
            sudo apt update
            sudo apt install -y dmsetup bc

            sudo ./hack/scripts/provision.sh devpool
            ```

        - configuration de containerd

            ```bash
            sudo nano /etc/containerd/config-dev.toml
            ```

            ```toml
            cat << EOF >/etc/containerd/config-dev.toml
            version = 2

            root = "/var/lib/containerd-dev"
            state = "/run/containerd-dev"

            [grpc]
              address = "/run/containerd-dev/containerd.sock"

            [metrics]
              address = "127.0.0.1:1338"

            [plugins]
              [plugins."io.containerd.snapshotter.v1.devmapper"]
                pool_name = "flintlock-dev-thinpool"
                root_path = "/var/lib/containerd-dev/snapshotter/devmapper"
                base_image_size = "10GB"
                discard_blocks = true

            [debug]
              level = "trace"
            ```

            ```bash
            sudo mkdir -p /var/lib/containerd-dev/snapshotter/devmapper
            sudo mkdir -p /run/containerd-dev/
            ```

        - demarage de containerd

            ```bash
            sudo apt install -y containerd
            sudo containerd --config /etc/containerd/config-dev.toml
            ```
