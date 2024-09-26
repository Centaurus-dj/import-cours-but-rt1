# R502-TP2 - Supervision SNMP, CHECK-MK et LibreNMS

La supervision s'appuie sur des agents (entre autres de type SNMP)

- Les "pure players" SNMP qui ne s'appuient que sur ce protocole pour monitorer les équipements réseaux.
- les logiciels généralistes pour la plupart issus du logiciel NAGIOS et qui s'appuient aux aussi sur des agents.

L'évaluation se fera au travers d'une grille validant les différentes capacités acquises par l'étudiant lors du TP. Le compte rendu est comme d'habitude obligatoire.

1. Le cahier des charges

    Vous utiliserez une machine virtuelle sous Debian et vous travaillerez par groupe de deux.  
    Votre mission est de monitorer les réseaux et les systèmes de l'IUT réels ou bâtis par vos soins.  

    La liste des équipements interrogeables par SNMP sur l'IUT est la suivante:

    - Le serveur registry.iutbeziers.fr
    - La pile de switch 10g de l'IUT
    - Installez pour le monitorer un serveur SNMP sur vos machines Linux sous forme de container (voir [cs.iutbeziers.fr/jmp/dockersnmp](http://cs.iutbeziers.fr/jmp/dockersnmp)) pour le faire.

    Vous superviserez aussi avec check_MK:

    - Le serveur registry.iutbeziers.fr (communauté snmp publicbeziers en ro et agent check_mk).
    - Votre machine Linux sur laquelle vous installerez l'agent check-mk (téléchargeable sur store.iutbeziers.fr).
    - Le services web de <www.iutbeziers.fr> (Vérifiez la durée du certificat pour les services SSL).
    - L'annuaire de l'IUT.(compte à utiliser sur Moodle)
    - Le service ldap de l'IUT..
    - Les services de messagerie de l'université.
    - Le temps de réponse http de <www.iutbeziers.fr>.
    - La validité du certificat ssl de <www.iutbeziers.fr>.
    - le temps de réponse ICMP de google.fr.
    - le temps de réponse de chaque routeur sur le réseau pour la destination <www.umontpellier.fr>. (il s'agit de mettre en place le plugin mtr de Check-MK).

    Le liens suivant peut vous aider: [https://checkmk.com/cms.html](https://checkmk.com/cms.html)

2. Installation de Check_MK comme logiciel de supervision

    Check_MK est un logiciel qui permet une installation très rapide d'un environnement de supervision.
    En suivant [https://docs.checkmk.com/latest/en/](https://docs.checkmk.com/latest/en/).
    
    Vous paramétrerez une instance de supervision appelée IUTBEZIERS.  
    Vous utiliserez Wato(menu setup) afin de créer vos hôtes.

    On installe CheckMK en container, avec docker, en faisant:

    ```sh
    docker container run -dit -p 8080:5000 -p 8000:8000 --tmpfs /opt/omd/sites/cmk/tmp:uid=1000,gid=1000 -v monitoring:/omd/sites --name monitoring -v /etc/localtime:/etc/localtime:ro --restart always checkmk/check-mk-raw:2.3.0-latest
    ```

    On peut voir que l'on peut y accéder à l'addresse suivante: [](http://localhost:8080)

    ![Page de connection CheckMK](./src/img/login_page_checkmk.png)

    - Après, nous pouvons retrouver notre MDP avec:

        ```sh
        docker container logs monitoring
        ```

        ce qui nous donne les credentials suivants:

        | Username | Password     |
        | -------- | ------------ |
        | cmkadmin | tlgLn4ZIgJB2 |

    - On peut accéder à la page principale:

        ![dashboard_connect](./src/img/dashboard_connect.png)

    - ### Services et Hôtes

        | Service                                                                                    | Statut             | Screenshot (Preuve)                                                                                                                      |
        | ------------------------------------------------------------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
        | Registry IUT                                                                               | :white_check_mark: | [![monitoring_registry_iutbeziers](./src/img/monitoring_registry_iutbeziers.png)](#registry-iut)                                         |
        | Machine Linux                                                                              | :white_check_mark: | [![monitoring_debian](./src/img/monitoring_debian.png)](#monitoring_debian)                                                              |
        | Service Web IUT (No-SSL / HTTP)                                                            | :white_check_mark: | [![web-iut-http](./src/img/web-iut-http.png)](#service-web-iut-http)                                                                     |
        | Service Web IUT (SSL / HTTPS)                                                              | :white_check_mark: | [![web-iut-https](./src/img/web-iut-https.png)](#service-web-iut-https)                                                                  |
        | Annuaire LDAP IUT                                                                          | :white_check_mark: | [![ldap-access](./src/img/ldap-access.png)](#ldap-iut)                                                                                   |
        | Annuaire IUT                                                                               | :x:                |                                                                                                                                          |
        | Services Mail Université                                                                   | :white_check_mark: | [![telephone_mail](./src/img/telephone_mail.png)](#Controle-présence-serveur-mail-umontpellier)                                                                       |
        | Temps de réponse HTTP Site Web IUT                                                         | :white_check_mark: | [![monitoring-www-iutbeziers-fr](./src/img/monitoring-www-iutbeziers-fr.png)](#temps-réponse-site-web-iut)                               |
        | Validité Certificat SSL Site Web IUT                                                       | :white_check_mark: | [![monitoring-www-iutbeziers-fr-ssl-certs](./src/img/monitoring-www-iutbeziers-fr-ssl-certs.png)](#validité-certificat-ssl-site-web-iut) |
        | Temps de réponse ICMP de google.fr                                                         | :white_check_mark: | [![ping_google.fr](./src/img/ping_google.png)](#ping_google)                                                                             |
        | Temps de réponse de chaque routeur pour [www.umontpellier.fr](https://www.umontpellier.fr) | :x:                |                                                                                                                                          |


        Ce qui nous donne à la fin:


        - Le Dashboard:

            ![checkmk-dashboard](./src/img/dashboard_final.png)  

        - Les hôtes

            ![checkmk-hosts](./src/img/hosts_final.png)

        #### Annexes Images Par Hôtes / Services

        - ##### Registry IUT

            - ![monitoring_registry_iutbeziers](./src/img/monitoring_registry_iutbeziers.png)

        - ##### Service Web IUT (HTTP)

            - ![web-iut-http](./src/img/web-iut-http.png)

        - ##### Service Web IUT (HTTPS)

            - ![web-iut-https](./src/img/web-iut-https.png)

        - ##### LDAP IUT

            - ![ldap-iut](./src/img/ldap-access.png)

        - ##### Temps Réponse Site Web IUT

            [![monitoring-www-iutbeziers-fr](./src/img/monitoring-www-iutbeziers-fr.png)]

        - ##### Validité Certificat SSL Site Web IUT

            - ![monitoring-www-iutbeziers-fr-ssl-certs](./src/img/monitoring-www-iutbeziers-fr-ssl-certs.png)
            - ![monitored-cert-web-iut](./src/img/monitored-cert-web-iut.png)

        - ##### Controle présence serveur mail umontpellier

            - ![telephone_mail](./src/img/telephone_mail.png)


3. Installation de LibreNMS comme logiciel de supervision (pure SNMP player)

    1. Installez libreNMS en clonant le repo git suivant: [github.com/librenms/docker](https://github.com/librenms/docker)

        ```bash
        git clone https://github.com/librenms/docker librenms-docker
        cd librenms-docker/examples/compose

        docker-compose up -d
        ```

        Utilisez LibreNMS afin de monitorer quelques équipements SNMP comme précédemment. \
        Vous pouvez vous aider de l'article sur LibreNMS posé dans l'ENT.

        On configure LibreNMS:

        ```sh
        lnms user:add --role=admin
        ```

        On ajoute:

        - `registry.iutbeziers.fr`:

            ```sh
            ./lnms device:add --v2c -c publicbeziers registry.iutbeziers.fr
            ```

            ![librenms-registry-snmp](./src/img/librenms-registry-snmp.png)

        - le switch de la salle (`10.202.255.252`):

            ```sh
            ./lnms device:add --v2c -c publicbeziers 10.202.255.252
            ```

            ![librenms-switch-snmp](./src/img/librenms-switch-snmp.png)

    2. Créez une alerte sur le CPU de registry.iutbeziers.fr.

        On crée l'alerte:

        ![librenms-registry-alert](./src/img/librenms-registry-alert.png)

    3. Créez un token et interrogez LibreNMS en ligne de commande à l'aide de curl. Listez les "devices" monitorés.

        On crée un token:

        ![librenms-api-token](./src/img/librenms-api-token.png)

        On peut ensuite faire:

        ```sh
        curl -H 'X-Auth-Token: 27e17053b770bc54c9a53b9c63982c5e' http://localhost:9000/api/v0/devices/registry.iutbeziers.fr
        ```

        Ce qui nous donne:

        ```json
        {
            "status": "ok",
            "devices": [
                {
                    "device_id": 1,
                    "inserted": "2024-09-26T15:20:15.000000Z",
                    "hostname": "registry.iutbeziers.fr",
                    "sysName": "registry",
                    "display": null,
                    "ip": "10.255.255.135",
                    "overwrite_ip": null,
                    "community": "publicbeziers",
                    "authlevel": null,
                    "authname": null,
                    "authpass": null,
                    "authalgo": null,
                    "cryptopass": null,
                    "cryptoalgo": null,
                    "snmpver": "v2c",
                    "port": 161,
                    "transport": "udp",
                    "timeout": null,
                    "retries": null,
                    "snmp_disable": 0,
                    "bgpLocalAs": null,
                    "sysObjectID": ".1.3.6.1.4.1.8072.3.2.10",
                    "sysDescr": "Linux registry 6.1.0-25-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.106-3 (2024-08-26) x86_64",
                    "sysContact": "Moa  <jean-marc.pouchoulon@iutbeziers.fr>",
                    "version": "6.1.0-25-amd64",
                    "hardware": "Generic x86 64-bit",
                    "features": null,
                    "location_id": 1,
                    "os": "linux",
                    "status": true,
                    "status_reason": "",
                    "ignore": 0,
                    "disabled": 0,
                    "uptime": 800542,
                    "agent_uptime": 0,
                    "last_polled": "2024-09-26T15:50:18.000000Z",
                    "last_poll_attempted": null,
                    "last_polled_timetaken": 1.6447660923004,
                    "last_discovered_timetaken": 3.127,
                    "last_discovered": "2024-09-26T15:20:21.000000Z",
                    "last_ping": "2024-09-26T15:50:17.000000Z",
                    "last_ping_timetaken": 0.269,
                    "purpose": null,
                    "type": "server",
                    "serial": null,
                    "icon": "images\/os\/linux.svg",
                    "poller_group": 0,
                    "override_sysLocation": 0,
                    "notes": null,
                    "port_association_mode": 1,
                    "max_depth": 0,
                    "disable_notify": 0,
                    "ignore_status": 0,
                    "location": "iutbeziers",
                    "lat": null,
                    "lng": null
                }
            ],
            "count": 1
        }
        ```