---
Author: Alexis Opolka
Company: IUT de Béziers
Subject: Ansible
Copyright: All Rights Reserved
---

# TP Ansible

1. ## 3.2 Installation de la VM

    > [!NOTE]
    > Les scripts d'automatisation de ce TP sont disponibles à l'adresse suivante: [github.com/pushou/tp3automatisation](https://github.com/pushou/tp3automatisation).

    On doit faire lors d'une première installation:

    ```sh
    ./revert2cgroupv1.sh
    ```

    Puis à chaque démarrage, pour les conteneurs:

    ```sh
    ./create-cont-debian12.sh
    ```

    nous donnant:

    ```sh
    effacement des containers existants
    ################################
    66750eb22f30
    61fb107f86ac
    2d12f313051e
    831e55a271c0
    81c8cd9b73f0
    e18d0912211b
    f64bca7dd992
    1b1cc89d97b4
    ecdf326ed46f
    b45fe4c2a669
    851a5b79dffc
    fd9723fb5fd8
    4924f55bd746
    66750eb22f30
    61fb107f86ac
    2d12f313051e
    831e55a271c0
    81c8cd9b73f0
    e18d0912211b
    f64bca7dd992
    1b1cc89d97b4
    ecdf326ed46f
    b45fe4c2a669
    851a5b79dffc
    fd9723fb5fd8
    4924f55bd746
    effacement des network dockers existants
    ################################
    1ca62e4dbc47
    2fca35d2f015
    abbeba436bd8
    1b6a5383f395
    58c66f611e7e
    e46d6e9c7120
    05c4538fbc51
    d8eacfce71ef
    bfe35a70179b
    734155aa4eac
    f16dea07d3b5
    b430f9170f07
    eb2c83907f7d
    eabe787f2bd6
    3c9448b2e43b
    831a3b94b965
    8000156aaadc
    ad6c44adfa17
    e6bfb3f4f13d
    6e29ef62dd2f
    c7d4830d5087
    ################################
    Creation des network dockers pour le TP
    ################################
    23ac425100e2c022e783b20714208a68a5e8b29d1e9613a081d9459bcfbaf789
    89cf58120d14471f2c63949e2223535253e2fbe293dd59c62395b61a99861648
    ced51af8ed98b5ddfbdb50ee451d3471abcfbd2d490fd85821501fd7cdd8c8ba
    68036ed110f6adde78184fcc242f05c96437d6b61051355a62e69d090089d4cf
    e4810db11e7278be4f50099fe15061533f089cd81be94b38e2e4195738d39645
    7518a53017d83407125c5642d6734d0f868de17cf4ab4eb02c61cc8e0e1d7dbd
    f544ef0396eaa1709e4ea411aa70c9e25d0b10797fafd5bf88160a4ba65cb2d2
    9aaad809aaaf399a2aefea3c4ac3c672841633ad7049b8e3f3bc24466fb166d5
    59195650f6d6f3164ebcaa43c6f1f89c308797f3c3d5eb8b890078fa20637f10
    0dd1f694da660c1c4ee31b85b8751832229ae16358a108e36b6ce06cddc3af6d
    36a657645e47faeaf5ec54cd3c38201847bda3243f40ed0a71bfc50d653d520c
    d2a77b66291cc2664a1630d663dfab4955ffa0c05caae83b57cb44cc16a5cf0a
    d857573dedd5475bf9bd2f7ec93234ea2e430ae57b5c267e0be2e080ad58d97b
    b5e52226f6570c942ffb1bcf49311f963925a07fcb20058329fd96cbae32c272
    118a5b1750b7ee6e22565941c802e06f83d49fe32c065374e9ccd0dc0a513ef2
    81154d49eb2d755e9892f60937d1def414e81a20a8ae9ef3bf8a8253bb410b8d
    582f2e5d33ddfc3123981dd5ca0d93790e0450945a3ede6332008c70322f3fe7
    aea2b046552cff0e56c6212e6576a5887416c64f40ec405fa0097ec13760818f
    24a71ddfc971e0fb269fdf4bbe276e66d69e642b009cc5aad489320e7d0a0665
    3b3b6b6de5db8991fd321e6f0a06e27cb1338fdd16df5073750f443facacd528
    remise à zero de  /root/.ssh/known_hosts
    ################################
    supression des adresses des containers existants dans /etc/hosts
    ################################
    Création des containers Debian et rocky
    ################################
    9766ff5c65ac62040b045d0a653c3c8a8ec1e201a83a80db7e4babd56b59cf4c
    c5866279c3825c3f47c9325b56ee96fc4117e94f3c39fb8531cb0323a74d8687
    82164891c1d017a9dbedf890a6a3475895b34f044439f2023106c7c6250972db
    8fb1a0e491c2547d832a9321a43d0b812c1d14b83108aa34ea28cfb077732fda
    a010daf191da961d45fc1f4def023d71d55f34f5ea02c3769d6db90b1b2710c7
    a19c78b4f4036b29618f23eccd9b74587757a5753bd939ad1a3a5868841dbfb0
    b8a3115729487ab37b3132d31fa3f78faa3d8223e842f8de99f7e2ecd2cd108c
    3129ab6e4485f5b36b3369ff8ea98305624b768083c392e12f8812561f9265f1
    e38b88b44fb5da2ba018e5cd29e1e2770098236efc4571c7772f0da48f139ef7
    0404a0ea51f7b0df059a8706a7596a6ac18e057ee787929491199cfea0ed7984
    creation des ip des containers dans /etc/hosts
    ################################
    installation depuis galaxy de la collection arista
    installation de l'image ceos & aliasing routeur
    Starting galaxy collection install process
    Nothing to do. All requested collections are already installed. If you want to reinstall them, consider using `--force`.
    4.29.02F: Pulling from ceosimage
    Digest: sha256:6b147e735fc2b10820af7bc54e9da5a2490469ea327d76ca112037b9494ee637
    Status: Image is up to date for registry.iutbeziers.fr/ceosimage:4.29.02F
    registry.iutbeziers.fr/ceosimage:4.29.02F
    création des containers routers Arista ceos
    +---+----------------------+--------------+-------------------------------------------+-------------+---------+------------------+--------------+
    | # |         Name         | Container ID |                   Image                   |    Kind     |  State  |   IPv4 Address   | IPv6 Address |
    +---+----------------------+--------------+-------------------------------------------+-------------+---------+------------------+--------------+
    | 1 | clab-srlceos01-ceos1 | 8f398d03f42c | registry.iutbeziers.fr/ceosimage:4.29.02F | arista_ceos | running | 172.100.100.2/24 | N/A          |
    | 2 | clab-srlceos01-ceos2 | add7843f8576 | registry.iutbeziers.fr/ceosimage:4.29.02F | arista_ceos | running | 172.100.100.3/24 | N/A          |
    | 3 | clab-srlceos01-ceos3 | 20474239a17d | registry.iutbeziers.fr/ceosimage:4.29.02F | arista_ceos | running | 172.100.100.4/24 | N/A          |
    +---+----------------------+--------------+-------------------------------------------+-------------+---------+------------------+--------------+
    voila le boulot
    CONTAINER ID   IMAGE                                       COMMAND                  CREATED          STATUS          PORTS                                                                                                        NAMES
    8f398d03f42c   registry.iutbeziers.fr/ceosimage:4.29.02F   "bash -c '/mnt/flash…"   42 seconds ago   Up 41 seconds                                                                                                                clab-srlceos01-ceos1
    add7843f8576   registry.iutbeziers.fr/ceosimage:4.29.02F   "bash -c '/mnt/flash…"   42 seconds ago   Up 41 seconds                                                                                                                clab-srlceos01-ceos2
    20474239a17d   registry.iutbeziers.fr/ceosimage:4.29.02F   "bash -c '/mnt/flash…"   42 seconds ago   Up 41 seconds                                                                                                                clab-srlceos01-ceos3
    0404a0ea51f7   registry.iutbeziers.fr/debian12:ssh         "/lib/systemd/systemd"   45 seconds ago   Up 45 seconds   161/udp, 88/tcp, 749-750/tcp, 464/udp, 2049/udp, 2049/tcp, 4444/udp, 0.0.0.0:2224->22/tcp, :::2224->22/tcp   debian-4
    e38b88b44fb5   registry.iutbeziers.fr/debian12:ssh         "/lib/systemd/systemd"   45 seconds ago   Up 45 seconds   161/udp, 88/tcp, 749-750/tcp, 464/udp, 2049/udp, 2049/tcp, 4444/udp, 0.0.0.0:2223->22/tcp, :::2223->22/tcp   debian-3
    3129ab6e4485   registry.iutbeziers.fr/debian12:ssh         "/lib/systemd/systemd"   46 seconds ago   Up 45 seconds   161/udp, 88/tcp, 749-750/tcp, 464/udp, 2049/udp, 2049/tcp, 4444/udp, 0.0.0.0:2222->22/tcp, :::2222->22/tcp   debian-2
    b8a311572948   registry.iutbeziers.fr/debian12:ssh         "/lib/systemd/systemd"   46 seconds ago   Up 46 seconds   161/udp, 88/tcp, 749-750/tcp, 464/udp, 2049/udp, 2049/tcp, 4444/udp, 0.0.0.0:2221->22/tcp, :::2221->22/tcp   debian-1
    a19c78b4f403   registry.iutbeziers.fr/debian12:ssh         "/lib/systemd/systemd"   47 seconds ago   Up 46 seconds   161/udp, 88/tcp, 749-750/tcp, 464/udp, 2049/udp, 2049/tcp, 4444/udp, 0.0.0.0:2220->22/tcp, :::2220->22/tcp   debian-0
    a010daf191da   registry.iutbeziers.fr/rocky9:ssh           "/usr/sbin/init"         47 seconds ago   Up 46 seconds   0.0.0.0:3224->22/tcp, :::3224->22/tcp                                                                        rocky-4
    8fb1a0e491c2   registry.iutbeziers.fr/rocky9:ssh           "/usr/sbin/init"         47 seconds ago   Up 47 seconds   0.0.0.0:3223->22/tcp, :::3223->22/tcp                                                                        rocky-3
    82164891c1d0   registry.iutbeziers.fr/rocky9:ssh           "/usr/sbin/init"         47 seconds ago   Up 47 seconds   0.0.0.0:3222->22/tcp, :::3222->22/tcp                                                                        rocky-2
    c5866279c382   registry.iutbeziers.fr/rocky9:ssh           "/usr/sbin/init"         48 seconds ago   Up 47 seconds   0.0.0.0:3221->22/tcp, :::3221->22/tcp                                                                        rocky-1
    9766ff5c65ac   registry.iutbeziers.fr/rocky9:ssh           "/usr/sbin/init"         48 seconds ago   Up 47 seconds   0.0.0.0:3220->22/tcp, :::3220->22/tcp                                                                        rocky-0
    ```

    > [!TIP]
    > Ce fichier est accessible [ici](https://github.com/alexis-opolka/import-cours-but-rt/blob/master/cours/modules/R405/src/tp-ansible/create-cont.sh.keep.log).

1. ## 4 - Prise en main d'Ansible

    1. ### Vérification et "debug" basique

         1. On vérifie que nos cibles sont vivantes

             - Debian

                 ```sh
                 ansible -m ping debian
                 ```

             - Centos (Rocky)

                 ```sh
                 ansible -m ping rocky
                 ```

             - Arista (EOS)

                 ```sh
                 ansible -m ping eos
                 ```

         1. Lancer la commande `ip a` sur toutes les machines

            On fait:

            ```sh
            ansible-console
            ```

            puis on entre la commande:

            ```sh
            ip a
            ```

            nous donnant:

            ```sh
            debian-1 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if58        UP             172.29.0.2/16 fe80::42:acff:fe1d:2/64
            debian-0 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if56        UP             172.28.0.2/16 fe80::42:acff:fe1c:2/64
            clab-srlceos01-ceos2 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0             UP             192.168.1.211/24 metric 100
            docker0          DOWN           172.17.0.1/16
            br-23ac425100e2  UP             172.18.0.1/16 fe80::42:42ff:fecb:a5b7/64
            br-89cf58120d14  UP             172.19.0.1/16 fe80::42:d2ff:fe20:c410/64
            br-ced51af8ed98  UP             172.20.0.1/16 fe80::42:1bff:fea3:989b/64
            br-68036ed110f6  UP             172.21.0.1/16 fe80::42:fbff:fe43:9f6e/64
            br-e4810db11e72  UP             172.22.0.1/16 fe80::42:27ff:fe1f:5527/64
            br-7518a53017d8  DOWN           172.23.0.1/16
            br-f544ef0396ea  DOWN           172.24.0.1/16
            br-9aaad809aaaf  DOWN           172.25.0.1/16
            br-59195650f6d6  DOWN           172.26.0.1/16
            br-0dd1f694da66  DOWN           172.27.0.1/16
            br-36a657645e47  UP             172.28.0.1/16 fe80::42:e2ff:fe01:ecd3/64
            br-d2a77b66291c  UP             172.29.0.1/16 fe80::42:3bff:fef1:5602/64
            br-d857573dedd5  UP             172.30.0.1/16 fe80::42:baff:fef8:cb/64
            br-b5e52226f657  UP             172.31.0.1/16 fe80::42:8ff:feb0:9965/64
            br-118a5b1750b7  UP             192.168.16.1/20 fe80::42:4dff:fefd:5041/64
            br-81154d49eb2d  DOWN           192.168.32.1/20
            br-582f2e5d33dd  DOWN           192.168.48.1/20
            br-aea2b046552c  DOWN           192.168.64.1/20
            br-24a71ddfc971  DOWN           192.168.80.1/20
            br-3b3b6b6de5db  DOWN           192.168.96.1/20
            vethdc8db0c@if45 UP             fe80::d0ff:92ff:fe61:c82a/64
            veth0370a6f@if47 UP             fe80::e83b:b1ff:fe60:b299/64
            veth639b2db@if49 UP             fe80::f4a2:85ff:fe1a:e611/64
            vethef49fb9@if51 UP             fe80::a8a7:46ff:fe16:5672/64
            vethd3e7e41@if53 UP             fe80::b4e7:5bff:fe29:edc4/64
            vethe4675f2@if55 UP             fe80::b87c:9ff:fe1f:1956/64
            veth08217d6@if57 UP             fe80::600d:e4ff:fe0e:7f5b/64
            veth7442831@if59 UP             fe80::c465:f5ff:fe20:aa79/64
            vethd5f8d31@if61 UP             fe80::54e4:2dff:fe35:a3be/64
            veth5fc5681@if63 UP             fe80::8c0:d8ff:fe13:3da9/64
            br-548907c2ffc4  UP             172.100.100.1/24 fe80::42:74ff:fe79:befa/64
            veth1a80c59@if66 UP             fe80::d4b5:9fff:fe88:d747/64
            vethc555d76@if68 UP             fe80::4893:abff:fef7:4e5/64
            veth93a3bde@if70 UP             fe80::a881:daff:fe7b:3fcf/64
            clab-srlceos01-ceos1 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0             UP             192.168.1.211/24 metric 100
            docker0          DOWN           172.17.0.1/16
            br-23ac425100e2  UP             172.18.0.1/16 fe80::42:42ff:fecb:a5b7/64
            br-89cf58120d14  UP             172.19.0.1/16 fe80::42:d2ff:fe20:c410/64
            br-ced51af8ed98  UP             172.20.0.1/16 fe80::42:1bff:fea3:989b/64
            br-68036ed110f6  UP             172.21.0.1/16 fe80::42:fbff:fe43:9f6e/64
            br-e4810db11e72  UP             172.22.0.1/16 fe80::42:27ff:fe1f:5527/64
            br-7518a53017d8  DOWN           172.23.0.1/16
            br-f544ef0396ea  DOWN           172.24.0.1/16
            br-9aaad809aaaf  DOWN           172.25.0.1/16
            br-59195650f6d6  DOWN           172.26.0.1/16
            br-0dd1f694da66  DOWN           172.27.0.1/16
            br-36a657645e47  UP             172.28.0.1/16 fe80::42:e2ff:fe01:ecd3/64
            br-d2a77b66291c  UP             172.29.0.1/16 fe80::42:3bff:fef1:5602/64
            br-d857573dedd5  UP             172.30.0.1/16 fe80::42:baff:fef8:cb/64
            br-b5e52226f657  UP             172.31.0.1/16 fe80::42:8ff:feb0:9965/64
            br-118a5b1750b7  UP             192.168.16.1/20 fe80::42:4dff:fefd:5041/64
            br-81154d49eb2d  DOWN           192.168.32.1/20
            br-582f2e5d33dd  DOWN           192.168.48.1/20
            br-aea2b046552c  DOWN           192.168.64.1/20
            br-24a71ddfc971  DOWN           192.168.80.1/20
            br-3b3b6b6de5db  DOWN           192.168.96.1/20
            vethdc8db0c@if45 UP             fe80::d0ff:92ff:fe61:c82a/64
            veth0370a6f@if47 UP             fe80::e83b:b1ff:fe60:b299/64
            veth639b2db@if49 UP             fe80::f4a2:85ff:fe1a:e611/64
            vethef49fb9@if51 UP             fe80::a8a7:46ff:fe16:5672/64
            vethd3e7e41@if53 UP             fe80::b4e7:5bff:fe29:edc4/64
            vethe4675f2@if55 UP             fe80::b87c:9ff:fe1f:1956/64
            veth08217d6@if57 UP             fe80::600d:e4ff:fe0e:7f5b/64
            veth7442831@if59 UP             fe80::c465:f5ff:fe20:aa79/64
            vethd5f8d31@if61 UP             fe80::54e4:2dff:fe35:a3be/64
            veth5fc5681@if63 UP             fe80::8c0:d8ff:fe13:3da9/64
            br-548907c2ffc4  UP             172.100.100.1/24 fe80::42:74ff:fe79:befa/64
            veth1a80c59@if66 UP             fe80::d4b5:9fff:fe88:d747/64
            vethc555d76@if68 UP             fe80::4893:abff:fef7:4e5/64
            veth93a3bde@if70 UP             fe80::a881:daff:fe7b:3fcf/64
            clab-srlceos01-ceos3 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0             UP             192.168.1.211/24 metric 100
            docker0          DOWN           172.17.0.1/16
            br-23ac425100e2  UP             172.18.0.1/16 fe80::42:42ff:fecb:a5b7/64
            br-89cf58120d14  UP             172.19.0.1/16 fe80::42:d2ff:fe20:c410/64
            br-ced51af8ed98  UP             172.20.0.1/16 fe80::42:1bff:fea3:989b/64
            br-68036ed110f6  UP             172.21.0.1/16 fe80::42:fbff:fe43:9f6e/64
            br-e4810db11e72  UP             172.22.0.1/16 fe80::42:27ff:fe1f:5527/64
            br-7518a53017d8  DOWN           172.23.0.1/16
            br-f544ef0396ea  DOWN           172.24.0.1/16
            br-9aaad809aaaf  DOWN           172.25.0.1/16
            br-59195650f6d6  DOWN           172.26.0.1/16
            br-0dd1f694da66  DOWN           172.27.0.1/16
            br-36a657645e47  UP             172.28.0.1/16 fe80::42:e2ff:fe01:ecd3/64
            br-d2a77b66291c  UP             172.29.0.1/16 fe80::42:3bff:fef1:5602/64
            br-d857573dedd5  UP             172.30.0.1/16 fe80::42:baff:fef8:cb/64
            br-b5e52226f657  UP             172.31.0.1/16 fe80::42:8ff:feb0:9965/64
            br-118a5b1750b7  UP             192.168.16.1/20 fe80::42:4dff:fefd:5041/64
            br-81154d49eb2d  DOWN           192.168.32.1/20
            br-582f2e5d33dd  DOWN           192.168.48.1/20
            br-aea2b046552c  DOWN           192.168.64.1/20
            br-24a71ddfc971  DOWN           192.168.80.1/20
            br-3b3b6b6de5db  DOWN           192.168.96.1/20
            vethdc8db0c@if45 UP             fe80::d0ff:92ff:fe61:c82a/64
            veth0370a6f@if47 UP             fe80::e83b:b1ff:fe60:b299/64
            veth639b2db@if49 UP             fe80::f4a2:85ff:fe1a:e611/64
            vethef49fb9@if51 UP             fe80::a8a7:46ff:fe16:5672/64
            vethd3e7e41@if53 UP             fe80::b4e7:5bff:fe29:edc4/64
            vethe4675f2@if55 UP             fe80::b87c:9ff:fe1f:1956/64
            veth08217d6@if57 UP             fe80::600d:e4ff:fe0e:7f5b/64
            veth7442831@if59 UP             fe80::c465:f5ff:fe20:aa79/64
            vethd5f8d31@if61 UP             fe80::54e4:2dff:fe35:a3be/64
            veth5fc5681@if63 UP             fe80::8c0:d8ff:fe13:3da9/64
            br-548907c2ffc4  UP             172.100.100.1/24 fe80::42:74ff:fe79:befa/64
            veth1a80c59@if66 UP             fe80::d4b5:9fff:fe88:d747/64
            vethc555d76@if68 UP             fe80::4893:abff:fef7:4e5/64
            veth93a3bde@if70 UP             fe80::a881:daff:fe7b:3fcf/64
            debian-2 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if60        UP             172.30.0.2/16 fe80::42:acff:fe1e:2/64
            debian-3 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if62        UP             172.31.0.2/16 fe80::42:acff:fe1f:2/64
            debian-4 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if64        UP             192.168.16.2/20 fe80::42:c0ff:fea8:1002/64
            rocky-0 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if46        UP             172.18.0.2/16 fe80::42:acff:fe12:2/64
            rocky-1 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if48        UP             172.19.0.2/16 fe80::42:acff:fe13:2/64
            rocky-2 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if50        UP             172.20.0.2/16 fe80::42:acff:fe14:2/64
            rocky-3 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if52        UP             172.21.0.2/16 fe80::42:acff:fe15:2/64
            rocky-4 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if54        UP             172.22.0.2/16 fe80::42:acff:fe16:2/64
            ```

            > [!TIP]
            > Ce fichier est accessible [ici](https://github.com/alexis-opolka/import-cours-but-rt/blob/master/cours/modules/R405/src/tp-ansible/ansible-all-ip-a.keep.log).

            Dans le cas où les cartes ont leur statut marqué comme UP, les
            conteneurs ont un accès au réseau.

            > [!NOTE]
            > On peut aussi utiliser la commande de la forme:
            >
            > ```sh
            > ansible <group> -m <module-id> -a <arguments>
            > ```
            >
            > tel que:
            >
            > ```sh
            > ansible all -m command -a "ip -br a"
            > ```

         1. Quel est le protocole réseau utilisé par Ansible ?

            Ansible utilise le protocole SSH.

         1. Analyser le fonctionnement de la commande Ansible avec l'option `-vvv`. Que pouvez-vous en déduire du fonctionnement d'Ansible ?  
                Expliquer comment Ansible peut être "agentless" ?

            Vu que Ansible utilise le SSH comme protocole de communication, il n'a pas besoin d'avoir une dépendence client ou agent sur
            la machine en question, il n'a besoin que du daemon du serveur SSH afin de pouvoir s'y connecter à distance.

            Exemple avec la commande précédente en mode triple verbeux (ou en mode verbosité debogage):

            ```sh
            ansible [core 2.16.5]
            config file = /home/ansible/ansible.cfg
            configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
            ansible python module location = /usr/local/lib/python3.11/dist-packages/ansible
            ansible collection location = /root/.ansible/collections:/usr/share/ansible/collections
            executable location = /usr/local/bin/ansible
            python version = 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] (/usr/bin/python3)
            jinja version = 3.1.2
            libyaml = True
            Using /home/ansible/ansible.cfg as config file
            host_list declined parsing /etc/ansible/hosts as it did not pass its verify_file() method
            script declined parsing /etc/ansible/hosts as it did not pass its verify_file() method
            auto declined parsing /etc/ansible/hosts as it did not pass its verify_file() method
            Parsed /etc/ansible/hosts inventory source with ini plugin
            Skipping callback 'default', as we already have a stdout callback.
            Skipping callback 'minimal', as we already have a stdout callback.
            Skipping callback 'oneline', as we already have a stdout callback.
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'/root\n', b'')
            redirecting (type: become) ansible.builtin.enable to ansible.netcommon.enable
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245 `" && echo ansible-tmp-1715128258.9719698-18095-245966705795245="` echo /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245 `" ) && sleep 0'"'"''
            redirecting (type: become) ansible.builtin.enable to ansible.netcommon.enable
            redirecting (type: become) ansible.builtin.enable to ansible.netcommon.enable
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226 `" && echo ansible-tmp-1715128258.9810672-18094-235469732102226="` echo /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128258.9719698-18095-245966705795245=/root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245\n', b'')
            <127.0.0.1> (0, b'ansible-tmp-1715128258.9810672-18094-235469732102226=/root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226\n', b'')
            <debian-1> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <debian-0> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.11\n/usr/bin/python3\nENDFOUND\n', b'')
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.11\n/usr/bin/python3\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.11 && sleep 0'"'"''
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.11 && sleep 0'"'"''
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "PRETTY_NAME=\\"Debian GNU/Linux 12 (bookworm)\\"\\nNAME=\\"Debian GNU/Linux\\"\\nVERSION_ID=\\"12\\"\\nVERSION=\\"12 (bookworm)\\"\\nVERSION_CODENAME=bookworm\\nID=debian\\nHOME_URL=\\"<https://www.debian.org/\\"\\nSUPPORT_URL=\\"https://www.debian.org/support\\"\\nBUG_REPORT_URL=\\"https://bugs.debian.org/\\"\\n"}\n>', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpzmqggafj TO /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' '[127.0.0.1]'
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "PRETTY_NAME=\\"Debian GNU/Linux 12 (bookworm)\\"\\nNAME=\\"Debian GNU/Linux\\"\\nVERSION_ID=\\"12\\"\\nVERSION=\\"12 (bookworm)\\"\\nVERSION_CODENAME=bookworm\\nID=debian\\nHOME_URL=\\"<https://www.debian.org/\\"\\nSUPPORT_URL=\\"https://www.debian.org/support\\"\\nBUG_REPORT_URL=\\"https://bugs.debian.org/\\"\\n"}\n>', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpdorazz8m TO /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' '[127.0.0.1]'
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpzmqggafj /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245/ /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpdorazz8m /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226/ /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if56        UP             172.28.0.2/16 fe80::42:acff:fe1c:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 02:30:59.342645", "end": "2024-05-08 02:30:59.348612", "delta": "0:00:00.005967", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/712b1e5e5d"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128258.9810672-18094-235469732102226/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if58        UP             172.29.0.2/16 fe80::42:acff:fe1d:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 02:30:59.349936", "end": "2024-05-08 02:30:59.355898", "delta": "0:00:00.005962", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/8455cc56eb"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128258.9719698-18095-245966705795245/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            debian-0 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if56        UP             172.28.0.2/16 fe80::42:acff:fe1c:2/64
            <127.0.0.1> (0, b'', b'')
            debian-1 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if58        UP             172.29.0.2/16 fe80::42:acff:fe1d:2/64
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767 `" && echo ansible-tmp-1715128259.4732916-18184-223658367848767="` echo /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887 `" && echo ansible-tmp-1715128259.4894423-18186-12654882004887="` echo /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128259.4732916-18184-223658367848767=/root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767\n', b'')
            <debian-2> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128259.4894423-18186-12654882004887=/root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887\n', b'')
            <debian-3> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.11\n/usr/bin/python3\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.11 && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.11\n/usr/bin/python3\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.11 && sleep 0'"'"''
            <172.100.100.3> ESTABLISH LOCAL CONNECTION FOR USER: root
            <172.100.100.3> EXEC /bin/sh -c '( umask 77 && mkdir -p "` echo /root/.ansible/tmp/ansible-local-180872a73cz3c `"&& mkdir "` echo /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098 `" && echo ansible-tmp-1715128259.5514915-18092-136270934518098="` echo /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098 `" ) && sleep 0'
            <172.100.100.2> ESTABLISH LOCAL CONNECTION FOR USER: root
            <172.100.100.2> EXEC /bin/sh -c '( umask 77 && mkdir -p "` echo /root/.ansible/tmp/ansible-local-180872a73cz3c `"&& mkdir "` echo /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279 `" && echo ansible-tmp-1715128259.5529292-18091-147883278960279="` echo /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279 `" ) && sleep 0'
            <172.100.100.4> ESTABLISH LOCAL CONNECTION FOR USER: root
            <172.100.100.4> EXEC /bin/sh -c '( umask 77 && mkdir -p "` echo /root/.ansible/tmp/ansible-local-180872a73cz3c `"&& mkdir "` echo /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554 `" && echo ansible-tmp-1715128259.558992-18093-178321007887554="` echo /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554 `" ) && sleep 0'
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <172.100.100.3> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmp6fcuc3tn TO /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098/AnsiballZ_command.py
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "PRETTY_NAME=\\"Debian GNU/Linux 12 (bookworm)\\"\\nNAME=\\"Debian GNU/Linux\\"\\nVERSION_ID=\\"12\\"\\nVERSION=\\"12 (bookworm)\\"\\nVERSION_CODENAME=bookworm\\nID=debian\\nHOME_URL=\\"<https://www.debian.org/\\"\\nSUPPORT_URL=\\"https://www.debian.org/support\\"\\nBUG_REPORT_URL=\\"https://bugs.debian.org/\\"\\n"}\n>', b'')
            <172.100.100.3> EXEC /bin/sh -c 'chmod u+x /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098/ /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098/AnsiballZ_command.py && sleep 0'
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <172.100.100.2> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmplxkhmoxt TO /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279/AnsiballZ_command.py
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <172.100.100.2> EXEC /bin/sh -c 'chmod u+x /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279/ /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279/AnsiballZ_command.py && sleep 0'
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpnlg8j17u TO /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' '[127.0.0.1]'
            <172.100.100.3> EXEC /bin/sh -c '/usr/bin/python3 /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098/AnsiballZ_command.py && sleep 0'
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <172.100.100.4> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmp4rrm95km TO /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554/AnsiballZ_command.py
            <172.100.100.2> EXEC /bin/sh -c '/usr/bin/python3 /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279/AnsiballZ_command.py && sleep 0'
            <172.100.100.4> EXEC /bin/sh -c 'chmod u+x /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554/ /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554/AnsiballZ_command.py && sleep 0'
            <172.100.100.4> EXEC /bin/sh -c '/usr/bin/python3 /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554/AnsiballZ_command.py && sleep 0'
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "PRETTY_NAME=\\"Debian GNU/Linux 12 (bookworm)\\"\\nNAME=\\"Debian GNU/Linux\\"\\nVERSION_ID=\\"12\\"\\nVERSION=\\"12 (bookworm)\\"\\nVERSION_CODENAME=bookworm\\nID=debian\\nHOME_URL=\\"<https://www.debian.org/\\"\\nSUPPORT_URL=\\"https://www.debian.org/support\\"\\nBUG_REPORT_URL=\\"https://bugs.debian.org/\\"\\n"}\n>', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmplhcts8tu TO /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' '[127.0.0.1]'
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpnlg8j17u /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767/ /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmplhcts8tu /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887/ /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887/AnsiballZ_command.py && sleep 0'"'"''
            <172.100.100.2> EXEC /bin/sh -c 'rm -f -r /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5529292-18091-147883278960279/ > /dev/null 2>&1 && sleep 0'
            clab-srlceos01-ceos1 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0             UP             192.168.1.211/24 metric 100
            docker0          DOWN           172.17.0.1/16
            br-23ac425100e2  UP             172.18.0.1/16 fe80::42:42ff:fecb:a5b7/64
            br-89cf58120d14  UP             172.19.0.1/16 fe80::42:d2ff:fe20:c410/64
            br-ced51af8ed98  UP             172.20.0.1/16 fe80::42:1bff:fea3:989b/64
            br-68036ed110f6  UP             172.21.0.1/16 fe80::42:fbff:fe43:9f6e/64
            br-e4810db11e72  UP             172.22.0.1/16 fe80::42:27ff:fe1f:5527/64
            br-7518a53017d8  DOWN           172.23.0.1/16
            br-f544ef0396ea  DOWN           172.24.0.1/16
            br-9aaad809aaaf  DOWN           172.25.0.1/16
            br-59195650f6d6  DOWN           172.26.0.1/16
            br-0dd1f694da66  DOWN           172.27.0.1/16
            br-36a657645e47  UP             172.28.0.1/16 fe80::42:e2ff:fe01:ecd3/64
            br-d2a77b66291c  UP             172.29.0.1/16 fe80::42:3bff:fef1:5602/64
            br-d857573dedd5  UP             172.30.0.1/16 fe80::42:baff:fef8:cb/64
            br-b5e52226f657  UP             172.31.0.1/16 fe80::42:8ff:feb0:9965/64
            br-118a5b1750b7  UP             192.168.16.1/20 fe80::42:4dff:fefd:5041/64
            br-81154d49eb2d  DOWN           192.168.32.1/20
            br-582f2e5d33dd  DOWN           192.168.48.1/20
            br-aea2b046552c  DOWN           192.168.64.1/20
            br-24a71ddfc971  DOWN           192.168.80.1/20
            br-3b3b6b6de5db  DOWN           192.168.96.1/20
            vethdc8db0c@if45 UP             fe80::d0ff:92ff:fe61:c82a/64
            veth0370a6f@if47 UP             fe80::e83b:b1ff:fe60:b299/64
            veth639b2db@if49 UP             fe80::f4a2:85ff:fe1a:e611/64
            vethef49fb9@if51 UP             fe80::a8a7:46ff:fe16:5672/64
            vethd3e7e41@if53 UP             fe80::b4e7:5bff:fe29:edc4/64
            vethe4675f2@if55 UP             fe80::b87c:9ff:fe1f:1956/64
            veth08217d6@if57 UP             fe80::600d:e4ff:fe0e:7f5b/64
            veth7442831@if59 UP             fe80::c465:f5ff:fe20:aa79/64
            vethd5f8d31@if61 UP             fe80::54e4:2dff:fe35:a3be/64
            veth5fc5681@if63 UP             fe80::8c0:d8ff:fe13:3da9/64
            br-548907c2ffc4  UP             172.100.100.1/24 fe80::42:74ff:fe79:befa/64
            veth1a80c59@if66 UP             fe80::d4b5:9fff:fe88:d747/64
            vethc555d76@if68 UP             fe80::4893:abff:fef7:4e5/64
            veth93a3bde@if70 UP             fe80::a881:daff:fe7b:3fcf/64
            <172.100.100.3> EXEC /bin/sh -c 'rm -f -r /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.5514915-18092-136270934518098/ > /dev/null 2>&1 && sleep 0'
            clab-srlceos01-ceos2 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0             UP             192.168.1.211/24 metric 100
            docker0          DOWN           172.17.0.1/16
            br-23ac425100e2  UP             172.18.0.1/16 fe80::42:42ff:fecb:a5b7/64
            br-89cf58120d14  UP             172.19.0.1/16 fe80::42:d2ff:fe20:c410/64
            br-ced51af8ed98  UP             172.20.0.1/16 fe80::42:1bff:fea3:989b/64
            br-68036ed110f6  UP             172.21.0.1/16 fe80::42:fbff:fe43:9f6e/64
            br-e4810db11e72  UP             172.22.0.1/16 fe80::42:27ff:fe1f:5527/64
            br-7518a53017d8  DOWN           172.23.0.1/16
            br-f544ef0396ea  DOWN           172.24.0.1/16
            br-9aaad809aaaf  DOWN           172.25.0.1/16
            br-59195650f6d6  DOWN           172.26.0.1/16
            br-0dd1f694da66  DOWN           172.27.0.1/16
            br-36a657645e47  UP             172.28.0.1/16 fe80::42:e2ff:fe01:ecd3/64
            br-d2a77b66291c  UP             172.29.0.1/16 fe80::42:3bff:fef1:5602/64
            br-d857573dedd5  UP             172.30.0.1/16 fe80::42:baff:fef8:cb/64
            br-b5e52226f657  UP             172.31.0.1/16 fe80::42:8ff:feb0:9965/64
            br-118a5b1750b7  UP             192.168.16.1/20 fe80::42:4dff:fefd:5041/64
            br-81154d49eb2d  DOWN           192.168.32.1/20
            br-582f2e5d33dd  DOWN           192.168.48.1/20
            br-aea2b046552c  DOWN           192.168.64.1/20
            br-24a71ddfc971  DOWN           192.168.80.1/20
            br-3b3b6b6de5db  DOWN           192.168.96.1/20
            vethdc8db0c@if45 UP             fe80::d0ff:92ff:fe61:c82a/64
            veth0370a6f@if47 UP             fe80::e83b:b1ff:fe60:b299/64
            veth639b2db@if49 UP             fe80::f4a2:85ff:fe1a:e611/64
            vethef49fb9@if51 UP             fe80::a8a7:46ff:fe16:5672/64
            vethd3e7e41@if53 UP             fe80::b4e7:5bff:fe29:edc4/64
            vethe4675f2@if55 UP             fe80::b87c:9ff:fe1f:1956/64
            veth08217d6@if57 UP             fe80::600d:e4ff:fe0e:7f5b/64
            veth7442831@if59 UP             fe80::c465:f5ff:fe20:aa79/64
            vethd5f8d31@if61 UP             fe80::54e4:2dff:fe35:a3be/64
            veth5fc5681@if63 UP             fe80::8c0:d8ff:fe13:3da9/64
            br-548907c2ffc4  UP             172.100.100.1/24 fe80::42:74ff:fe79:befa/64
            veth1a80c59@if66 UP             fe80::d4b5:9fff:fe88:d747/64
            vethc555d76@if68 UP             fe80::4893:abff:fef7:4e5/64
            veth93a3bde@if70 UP             fe80::a881:daff:fe7b:3fcf/64
            <172.100.100.4> EXEC /bin/sh -c 'rm -f -r /root/.ansible/tmp/ansible-local-180872a73cz3c/ansible-tmp-1715128259.558992-18093-178321007887554/ > /dev/null 2>&1 && sleep 0'
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if60        UP             172.30.0.2/16 fe80::42:acff:fe1e:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 02:30:59.761879", "end": "2024-05-08 02:30:59.766721", "delta": "0:00:00.004842", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/591e71187a"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.4732916-18184-223658367848767/ > /dev/null 2>&1 && sleep 0'"'"''
            clab-srlceos01-ceos3 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0             UP             192.168.1.211/24 metric 100
            docker0          DOWN           172.17.0.1/16
            br-23ac425100e2  UP             172.18.0.1/16 fe80::42:42ff:fecb:a5b7/64
            br-89cf58120d14  UP             172.19.0.1/16 fe80::42:d2ff:fe20:c410/64
            br-ced51af8ed98  UP             172.20.0.1/16 fe80::42:1bff:fea3:989b/64
            br-68036ed110f6  UP             172.21.0.1/16 fe80::42:fbff:fe43:9f6e/64
            br-e4810db11e72  UP             172.22.0.1/16 fe80::42:27ff:fe1f:5527/64
            br-7518a53017d8  DOWN           172.23.0.1/16
            br-f544ef0396ea  DOWN           172.24.0.1/16
            br-9aaad809aaaf  DOWN           172.25.0.1/16
            br-59195650f6d6  DOWN           172.26.0.1/16
            br-0dd1f694da66  DOWN           172.27.0.1/16
            br-36a657645e47  UP             172.28.0.1/16 fe80::42:e2ff:fe01:ecd3/64
            br-d2a77b66291c  UP             172.29.0.1/16 fe80::42:3bff:fef1:5602/64
            br-d857573dedd5  UP             172.30.0.1/16 fe80::42:baff:fef8:cb/64
            br-b5e52226f657  UP             172.31.0.1/16 fe80::42:8ff:feb0:9965/64
            br-118a5b1750b7  UP             192.168.16.1/20 fe80::42:4dff:fefd:5041/64
            br-81154d49eb2d  DOWN           192.168.32.1/20
            br-582f2e5d33dd  DOWN           192.168.48.1/20
            br-aea2b046552c  DOWN           192.168.64.1/20
            br-24a71ddfc971  DOWN           192.168.80.1/20
            br-3b3b6b6de5db  DOWN           192.168.96.1/20
            vethdc8db0c@if45 UP             fe80::d0ff:92ff:fe61:c82a/64
            veth0370a6f@if47 UP             fe80::e83b:b1ff:fe60:b299/64
            veth639b2db@if49 UP             fe80::f4a2:85ff:fe1a:e611/64
            vethef49fb9@if51 UP             fe80::a8a7:46ff:fe16:5672/64
            vethd3e7e41@if53 UP             fe80::b4e7:5bff:fe29:edc4/64
            vethe4675f2@if55 UP             fe80::b87c:9ff:fe1f:1956/64
            veth08217d6@if57 UP             fe80::600d:e4ff:fe0e:7f5b/64
            veth7442831@if59 UP             fe80::c465:f5ff:fe20:aa79/64
            vethd5f8d31@if61 UP             fe80::54e4:2dff:fe35:a3be/64
            veth5fc5681@if63 UP             fe80::8c0:d8ff:fe13:3da9/64
            br-548907c2ffc4  UP             172.100.100.1/24 fe80::42:74ff:fe79:befa/64
            veth1a80c59@if66 UP             fe80::d4b5:9fff:fe88:d747/64
            vethc555d76@if68 UP             fe80::4893:abff:fef7:4e5/64
            veth93a3bde@if70 UP             fe80::a881:daff:fe7b:3fcf/64
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            debian-2 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if60        UP             172.30.0.2/16 fe80::42:acff:fe1e:2/64
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601 `" && echo ansible-tmp-1715128259.8238103-18303-83767468022601="` echo /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if62        UP             172.31.0.2/16 fe80::42:acff:fe1f:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 02:30:59.789993", "end": "2024-05-08 02:30:59.795004", "delta": "0:00:00.005011", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c3cd0d8d90"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.4894423-18186-12654882004887/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> (0, b'ansible-tmp-1715128259.8238103-18303-83767468022601=/root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601\n', b'')
            <debian-4> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            debian-3 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if62        UP             172.31.0.2/16 fe80::42:acff:fe1f:2/64
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.11\n/usr/bin/python3\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.11 && sleep 0'"'"''
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613 `" && echo ansible-tmp-1715128259.8804858-18310-240969304274613="` echo /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613 `" ) && sleep 0'"'"''
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147 `" && echo ansible-tmp-1715128259.9027028-18319-229441786144147="` echo /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147 `" ) && sleep 0'"'"''
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "PRETTY_NAME=\\"Debian GNU/Linux 12 (bookworm)\\"\\nNAME=\\"Debian GNU/Linux\\"\\nVERSION_ID=\\"12\\"\\nVERSION=\\"12 (bookworm)\\"\\nVERSION_CODENAME=bookworm\\nID=debian\\nHOME_URL=\\"<https://www.debian.org/\\"\\nSUPPORT_URL=\\"https://www.debian.org/support\\"\\nBUG_REPORT_URL=\\"https://bugs.debian.org/\\"\\n"}\n>', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmp5lvf4tn6 TO /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' '[127.0.0.1]'
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165 `" && echo ansible-tmp-1715128259.9227135-18328-2823223559165="` echo /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128259.8804858-18310-240969304274613=/root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613\n', b'')
            <rocky-0> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmp5lvf4tn6 /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601/ /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905 `" && echo ansible-tmp-1715128259.9430583-18346-40438730809905="` echo /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128259.9027028-18319-229441786144147=/root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147\n', b'')
            <rocky-1> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128259.9227135-18328-2823223559165=/root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165\n', b'')
            <rocky-2> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.9\n/usr/bin/python3\n/usr/libexec/platform-python\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.9 && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128259.9430583-18346-40438730809905=/root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905\n', b'')
            <rocky-3> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.9\n/usr/bin/python3\n/usr/libexec/platform-python\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.9 && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.9\n/usr/bin/python3\n/usr/libexec/platform-python\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.9 && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.9\n/usr/bin/python3\n/usr/libexec/platform-python\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.9 && sleep 0'"'"''
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "NAME=\\"Rocky Linux\\"\\nVERSION=\\"9.3 (Blue Onyx)\\"\\nID=\\"rocky\\"\\nID_LIKE=\\"rhel centos fedora\\"\\nVERSION_ID=\\"9.3\\"\\nPLATFORM_ID=\\"platform:el9\\"\\nPRETTY_NAME=\\"Rocky Linux 9.3 (Blue Onyx)\\"\\nANSI_COLOR=\\"0;32\\"\\nLOGO=\\"fedora-logo-icon\\"\\nCPE_NAME=\\"cpe:/o:rocky:rocky:9::baseos\\"\\nHOME_URL=\\"<https://rockylinux.org/\\"\\nBUG_REPORT_URL=\\"https://bugs.rockylinux.org/\\"\\nSUPPORT_END=\\"2032-05-31\\"\\nROCKY_SUPPORT_PRODUCT=\\"Rocky-Linux-9\\"\\nROCKY_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\nREDHAT_SUPPORT_PRODUCT=\\"Rocky> Linux\\"\\nREDHAT_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\n"}\n', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmph4mlbx2c TO /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' '[127.0.0.1]'
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "NAME=\\"Rocky Linux\\"\\nVERSION=\\"9.3 (Blue Onyx)\\"\\nID=\\"rocky\\"\\nID_LIKE=\\"rhel centos fedora\\"\\nVERSION_ID=\\"9.3\\"\\nPLATFORM_ID=\\"platform:el9\\"\\nPRETTY_NAME=\\"Rocky Linux 9.3 (Blue Onyx)\\"\\nANSI_COLOR=\\"0;32\\"\\nLOGO=\\"fedora-logo-icon\\"\\nCPE_NAME=\\"cpe:/o:rocky:rocky:9::baseos\\"\\nHOME_URL=\\"<https://rockylinux.org/\\"\\nBUG_REPORT_URL=\\"https://bugs.rockylinux.org/\\"\\nSUPPORT_END=\\"2032-05-31\\"\\nROCKY_SUPPORT_PRODUCT=\\"Rocky-Linux-9\\"\\nROCKY_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\nREDHAT_SUPPORT_PRODUCT=\\"Rocky> Linux\\"\\nREDHAT_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\n"}\n', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpfnvohvxb TO /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' '[127.0.0.1]'
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "NAME=\\"Rocky Linux\\"\\nVERSION=\\"9.3 (Blue Onyx)\\"\\nID=\\"rocky\\"\\nID_LIKE=\\"rhel centos fedora\\"\\nVERSION_ID=\\"9.3\\"\\nPLATFORM_ID=\\"platform:el9\\"\\nPRETTY_NAME=\\"Rocky Linux 9.3 (Blue Onyx)\\"\\nANSI_COLOR=\\"0;32\\"\\nLOGO=\\"fedora-logo-icon\\"\\nCPE_NAME=\\"cpe:/o:rocky:rocky:9::baseos\\"\\nHOME_URL=\\"<https://rockylinux.org/\\"\\nBUG_REPORT_URL=\\"https://bugs.rockylinux.org/\\"\\nSUPPORT_END=\\"2032-05-31\\"\\nROCKY_SUPPORT_PRODUCT=\\"Rocky-Linux-9\\"\\nROCKY_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\nREDHAT_SUPPORT_PRODUCT=\\"Rocky> Linux\\"\\nREDHAT_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\n"}\n', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpu64xwvw2 TO /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' '[127.0.0.1]'
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmph4mlbx2c /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613/ /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "NAME=\\"Rocky Linux\\"\\nVERSION=\\"9.3 (Blue Onyx)\\"\\nID=\\"rocky\\"\\nID_LIKE=\\"rhel centos fedora\\"\\nVERSION_ID=\\"9.3\\"\\nPLATFORM_ID=\\"platform:el9\\"\\nPRETTY_NAME=\\"Rocky Linux 9.3 (Blue Onyx)\\"\\nANSI_COLOR=\\"0;32\\"\\nLOGO=\\"fedora-logo-icon\\"\\nCPE_NAME=\\"cpe:/o:rocky:rocky:9::baseos\\"\\nHOME_URL=\\"<https://rockylinux.org/\\"\\nBUG_REPORT_URL=\\"https://bugs.rockylinux.org/\\"\\nSUPPORT_END=\\"2032-05-31\\"\\nROCKY_SUPPORT_PRODUCT=\\"Rocky-Linux-9\\"\\nROCKY_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\nREDHAT_SUPPORT_PRODUCT=\\"Rocky> Linux\\"\\nREDHAT_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\n"}\n', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpoolgr_1o TO /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' '[127.0.0.1]'
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpfnvohvxb /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147/ /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpu64xwvw2 /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165/ /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if64        UP             192.168.16.2/20 fe80::42:c0ff:fea8:1002/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 02:31:00.137842", "end": "2024-05-08 02:31:00.143658", "delta": "0:00:00.005816", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=2224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/5fd358a2fb"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.8238103-18303-83767468022601/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpoolgr_1o /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905/ /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147/AnsiballZ_command.py && sleep 0'"'"''
            debian-4 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if64        UP             192.168.16.2/20 fe80::42:c0ff:fea8:1002/64
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' 127.0.0.1 '/bin/sh -c '"'"'echo ~ && sleep 0'"'"''
            <127.0.0.1> (0, b'/root\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' 127.0.0.1 '/bin/sh -c '"'"'( umask 77 && mkdir -p "` echo /root/.ansible/tmp `"&& mkdir "` echo /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834 `" && echo ansible-tmp-1715128260.3180676-18768-101582889372834="` echo /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834 `" ) && sleep 0'"'"''
            <127.0.0.1> (0, b'ansible-tmp-1715128260.3180676-18768-101582889372834=/root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834\n', b'')
            <rocky-4> Attempting python interpreter discovery
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' 127.0.0.1 '/bin/sh -c '"'"'echo PLATFORM; uname; echo FOUND; command -v '"'"'"'"'"'"'"'"'python3.12'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.11'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.10'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.9'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.8'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python3.6'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python3'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/libexec/platform-python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python2.7'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'/usr/bin/python'"'"'"'"'"'"'"'"'; command -v '"'"'"'"'"'"'"'"'python'"'"'"'"'"'"'"'"'; echo ENDFOUND && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if46        UP             172.18.0.2/16 fe80::42:acff:fe12:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 00:31:00.391064", "end": "2024-05-08 00:31:00.397233", "delta": "0:00:00.006169", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3220 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/a50dd80583"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.8804858-18310-240969304274613/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'PLATFORM\nLinux\nFOUND\n/usr/bin/python3.9\n/usr/bin/python3\n/usr/libexec/platform-python\nENDFOUND\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3.9 && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if48        UP             172.19.0.2/16 fe80::42:acff:fe13:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 00:31:00.421918", "end": "2024-05-08 00:31:00.428968", "delta": "0:00:00.007050", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3221 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c9d6d0572c"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.9027028-18319-229441786144147/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            rocky-0 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if46        UP             172.18.0.2/16 fe80::42:acff:fe12:2/64
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if50        UP             172.20.0.2/16 fe80::42:acff:fe14:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 00:31:00.453439", "end": "2024-05-08 00:31:00.459130", "delta": "0:00:00.005691", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3222 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/326c3db515"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.9227135-18328-2823223559165/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if52        UP             172.21.0.2/16 fe80::42:acff:fe15:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 00:31:00.456065", "end": "2024-05-08 00:31:00.461676", "delta": "0:00:00.005611", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3223 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/c0dec22752"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128259.9430583-18346-40438730809905/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> (0, b'{"platform_dist_result": [], "osrelease_content": "NAME=\\"Rocky Linux\\"\\nVERSION=\\"9.3 (Blue Onyx)\\"\\nID=\\"rocky\\"\\nID_LIKE=\\"rhel centos fedora\\"\\nVERSION_ID=\\"9.3\\"\\nPLATFORM_ID=\\"platform:el9\\"\\nPRETTY_NAME=\\"Rocky Linux 9.3 (Blue Onyx)\\"\\nANSI_COLOR=\\"0;32\\"\\nLOGO=\\"fedora-logo-icon\\"\\nCPE_NAME=\\"cpe:/o:rocky:rocky:9::baseos\\"\\nHOME_URL=\\"<https://rockylinux.org/\\"\\nBUG_REPORT_URL=\\"https://bugs.rockylinux.org/\\"\\nSUPPORT_END=\\"2032-05-31\\"\\nROCKY_SUPPORT_PRODUCT=\\"Rocky-Linux-9\\"\\nROCKY_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\nREDHAT_SUPPORT_PRODUCT=\\"Rocky> Linux\\"\\nREDHAT_SUPPORT_PRODUCT_VERSION=\\"9.3\\"\\n"}\n', b'')
            Using module file /usr/local/lib/python3.11/dist-packages/ansible/modules/command.py
            <127.0.0.1> PUT /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpq016ait8 TO /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834/AnsiballZ_command.py
            <127.0.0.1> SSH: EXEC sftp -b - -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' '[127.0.0.1]'
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> (0, b'', b'')
            rocky-1 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if48        UP             172.19.0.2/16 fe80::42:acff:fe13:2/64
            rocky-2 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if50        UP             172.20.0.2/16 fe80::42:acff:fe14:2/64
            rocky-3 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if52        UP             172.21.0.2/16 fe80::42:acff:fe15:2/64
            <127.0.0.1> (0, b'sftp> put /root/.ansible/tmp/ansible-local-180872a73cz3c/tmpq016ait8 /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834/AnsiballZ_command.py\n', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' 127.0.0.1 '/bin/sh -c '"'"'chmod u+x /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834/ /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' -tt 127.0.0.1 '/bin/sh -c '"'"'/usr/bin/python3 /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834/AnsiballZ_command.py && sleep 0'"'"''
            <127.0.0.1> (0, b'\r\n{"changed": true, "stdout": "lo               UNKNOWN        127.0.0.1/8 ::1/128 \\neth0@if54        UP             172.22.0.2/16 fe80::42:acff:fe16:2/64 ", "stderr": "", "rc": 0, "cmd": ["ip", "-br", "a"], "start": "2024-05-08 00:31:00.786341", "end": "2024-05-08 00:31:00.790456", "delta": "0:00:00.004115", "msg": "", "invocation": {"module_args": {"_raw_params": "ip -br a", "_uses_shell": false, "expand_argument_vars": true, "stdin_add_newline": true, "strip_empty_ends": true, "argv": null, "chdir": null, "executable": null, "creates": null, "removes": null, "stdin": null}}}\r\n', b'Shared connection to 127.0.0.1 closed.\r\n')
            <127.0.0.1> ESTABLISH SSH CONNECTION FOR USER: None
            <127.0.0.1> SSH: EXEC ssh -C -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o Port=3224 -o 'IdentityFile="/root/.ssh/id_ed25519"' -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o 'ControlPath="/root/.ansible/cp/e9a5a67de2"' 127.0.0.1 '/bin/sh -c '"'"'rm -f -r /root/.ansible/tmp/ansible-tmp-1715128260.3180676-18768-101582889372834/ > /dev/null 2>&1 && sleep 0'"'"''
            <127.0.0.1> (0, b'', b'')
            rocky-4 | CHANGED | rc=0 >>
            lo               UNKNOWN        127.0.0.1/8 ::1/128
            eth0@if54        UP             172.22.0.2/16 fe80::42:acff:fe16:2/64
            ```

            > [!TIP]
            > Ce fichier est accessible [ici](https://github.com/alexis-opolka/import-cours-but-rt/blob/master/cours/modules/R405/src/tp-ansible/ansible-all-ip-a-verbose.keep.log).

         1. Créez un groupe container qui regroupe tous les containers et vérifiez via les commandes:

            Pour créer un groupe `container`, nous pouvons faire ajouter dans notre fichier `hosts` la configuration suivante:

            ```toml
            [container:children]
            eos
            debian
            rocky
            ```

            ```sh
            ansible-inventory --list all
            ansible-navigator
            ```

    1. ### Installation d’Apache via les modules dnf et apt d’Ansible core

        1. Sur deux des containers créés installez un serveur web Apache sous Debian et Centos à
            l’aide de la commande ansible et des modules Ansible de gestion des paquets apt et dnf. Le
            package s’appelle apache2 pour Debian et httpd pour Rocky Linux

            On crée un playbook ansible comme ceci:

            ```yaml
            ---
            - hosts: debian-0
                tasks:
                    - name: Apache Installation
                        ansible.builtin.apt:
                            name=apache2
                            state=present

                    - name: Enabling and starting Apache daemon
                        ansible.builtin.service:
                            name=apache2
                            state=started
                            enabled=true

            - hosts: rocky-0
                tasks:
                    - name: Apache (httpd) Installation
                        ansible.builtin.dnf:
                            name=httpd
                            state=present

                    - name: Enabling and starting Apache daemon
                        ansible.builtin.service:
                            name=httpd
                            state=started
                            enabled=true
            ```

            > [!TIP]
            > Ce fichier est accessible [ici](https://github.com/alexis-opolka/import-cours-but-rt/blob/master/cours/modules/R405/src/tp-ansible/install-apache.yml).

            nous donnant:

            ```sh
            PLAY [debian-0] *****************************************************************************************************************************************************************************

            TASK [Gathering Facts] **********************************************************************************************************************************************************************
            ok: [debian-0]

            TASK [Apache Installation] ******************************************************************************************************************************************************************
            changed: [debian-0]

            TASK [Enabling and starting Apache daemon] **************************************************************************************************************************************************
            changed: [debian-0]

            PLAY [rocky-0] ******************************************************************************************************************************************************************************

            TASK [Gathering Facts] **********************************************************************************************************************************************************************
            ok: [rocky-0]

            TASK [Apache (httpd) Installation] **********************************************************************************************************************************************************
            changed: [rocky-0]

            TASK [Enabling and starting Apache daemon] **************************************************************************************************************************************************
            changed: [rocky-0]

            PLAY RECAP **********************************************************************************************************************************************************************************
            debian-0                   : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
            rocky-0                    : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
            ```

        1. Le playbook suivant installera Apache et PHP, un fichier info.php et qui démarrera le serveur web
            Apache sur vos containers Debian

            ```yml
            ---
            - hosts: debian
                tasks:
                    - name: Installer Apache
                        ansible.builtin.apt:
                            name: apache2
                            state: present
                            update_cache: true
                    - name: Installer Php7
                        ansible.builtin.apt:
                            name: libapache2-mod-php7.4
                            state: present
                    - name: Démarrer le service Apache
                        ansible.builtin.service:
                            name: apache2
                            state: started
                            enabled: true
                    - name: Copier le fichier phpinfo
                        ansible.builtin.copy:
                            src: info.php
                            dest: /var/www/html/index.php
                            owner: www-data
                            group: www-data
                            mode: 0664
            ```

        1. Avant de le lancer avec la commande ansible-playbook, vérifiez le bon enchainement des taches avec
            les options `--check` et `--diff` (pas d’éxécution réelle), `--list-hosts`, `--list-tasks` de la commande `ansible-playbook`.  
            Testez aussi la conformité de votre playbook avec le "linteur" `ansible-lint`.

            - `--check` et `--diff`:

                On fait:

                ```sh
                ansible-playbook scripts/apache-prof.yml --check --diff
                ```

                nous donnant:

                ```sh
                PLAY [debian] ******************************************************************

                TASK [Gathering Facts] *********************************************************
                ok: [debian-0]
                ok: [debian-3]
                ok: [debian-2]
                ok: [debian-4]
                ok: [debian-1]

                TASK [Installer Apache] ********************************************************
                fatal: [debian-3]: FAILED! => {"changed": false, "msg": "python3-apt must be installed to use check mode. If run normally this module can auto-install it."}
                fatal: [debian-2]: FAILED! => {"changed": false, "msg": "python3-apt must be installed to use check mode. If run normally this module can auto-install it."}
                fatal: [debian-4]: FAILED! => {"changed": false, "msg": "python3-apt must be installed to use check mode. If run normally this module can auto-install it."}
                fatal: [debian-1]: FAILED! => {"changed": false, "msg": "python3-apt must be installed to use check mode. If run normally this module can auto-install it."}
                ok: [debian-0]

                TASK [Installer Php7] **********************************************************
                fatal: [debian-0]: FAILED! => {"changed": false, "msg": "No package matching 'libapache2-mod-php7.4' is available"}

                PLAY RECAP *********************************************************************
                debian-0                   : ok=2    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
                debian-1                   : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
                debian-2                   : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
                debian-3                   : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
                debian-4                   : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
                ```

            - `--list-hosts`:

                On fait:

                ```sh
                ansible-playbook scripts/apache-prof.yml --list-hosts
                ```

                nous donnant:

                ```sh
                playbook: apache-prof.yml

                play #1 (debian): debian TAGS: []
                    pattern: ['debian']
                    hosts (5):
                    debian-3
                    debian-4
                    debian-1
                    debian-0
                    debian-2
                ```

            - `--list-tasks`:

                On fait:

                ```sh
                ansible-playbook scripts/apache-prof.yml --list-tasks
                ```

                nous donnant:

                ```sh
                playbook: apache-prof.yml

                play #1 (debian): debian TAGS: []
                    tasks:
                    Installer Apache TAGS: []
                    Installer Php7 TAGS: []
                    Démarrer le service Apache TAGS: []
                    Copier le fichier phpinfo TAGS: []
                ```

            - `ansible-lint`:

                On fait:

                ```sh
                ansible-lint scripts/apache-prof.yml
                ```

                nous donnant:

                ```sh
                ]8;id=165535;<https://ansible.readthedocs.io/projects/lint/rules/name/\[1;91mname[play][0m]8;;\[2m:[0m> [91mAll plays should be named.[0m
                [34mapache-prof.yml[0m:2

                ]8;id=342551;<https://ansible.readthedocs.io/projects/lint/rules/yaml/\[1;91myaml[indentation][0m]8;;\[2m:[0m> [91mWrong indentation: expected 0 but found 2[0m
                [34mapache-prof.yml[0m:2

                ]8;id=88727;<https://ansible.readthedocs.io/projects/lint/rules/yaml/\[1;91myaml[octal-values][0m]8;;\[2m:[0m> [91mForbidden implicit octal value "0664"[0m
                [34mapache-prof.yml[0m:24
                ```

                ou

                ```sh
                WARNING  Listing 3 violation(s) that are fatal
                name[play]: All plays should be named.
                apache-prof.yml:2

                yaml[indentation]: Wrong indentation: expected 0 but found 2
                apache-prof.yml:2

                yaml[octal-values]: Forbidden implicit octal value "0664"
                apache-prof.yml:24

                Read documentation for instructions on how to ignore specific rule violations.

                                Rule Violation Summary
                count tag                profile rule associated tags
                    1 name[play]         basic   idiom
                    1 yaml[indentation]  basic   formatting, yaml
                    1 yaml[octal-values] basic   formatting, yaml

                Failed: 3 failure(s), 0 warning(s) on 1 files. Last profile that met the validation criteria was 'min'.
                A new release of ansible-lint is available: 24.2.2 → 24.2.3
                ```

                Le linter ansible nous montre qu'il existe plusieurs erreurs dans notre playbook actuel.  
                Ces erreurs sont au niveau "fatal", cela veut dire que l'exécution de notre playbook va être
                compromise par ces erreurs.

        1. Créer une tache nommée "reload" 9 qui "reload" le server web 10. Tagué cette tache "relance" puis
            utilisez le tag pour n’exécuter que cette tache dans le playbook

            On ajoute la tâche suivante en bas de notre playbook Ansible actuel (`apache-prof.yml`):

            ```yaml
            - name: Reload Apache
                ansible.builtin.service:
                    name: apache2
                    state: reloaded
                    tags: relance
            ```

            On fera ensuite:

            ```sh
            ansible-playbook scripts/apache-prof.yml --tags relance
            ```

        1. A quoi servent les tags "never" et "always" (testez) ?

        1. Lister les facts à l’aide du module setup. A quoi servent ces facts ?

        1. Récupérez les facts contenant les adresses IP de tous les containers via un filtre.

        1. Utilisez les facts et les templates jinja2 afin de modifier la directive fichier ports.conf sous Debian pour
            que lors de l’installation du module apache2 de Debian n’écoute que sur l’IP interne du container.
            Vous utiliserez les mots clefs notify et handler pour relancer le service apache dans le playbook
