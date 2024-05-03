# TP Ansible

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

1. ## 3.2 Installation de la VM

    > [!NOTE]
    > Les scripts d'automatisation de ce TP sont disponibles à l'adresse suivante: [github.com/pushou/tp3automatisation](https://github.com/pushou/tp3automatisation).
