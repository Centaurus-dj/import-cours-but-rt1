# R509-TP2 - Kerberos

On installe un Box `fedora` avec vagrant:

> [!NOTE]
> On utilise le `Vagrantfile` disponible, [ici](./src/Vagrantfile).

```
vagrant up
```

## Installation de serveur Kerberos

- ### Installation

    On installe ensuite Kerberos sur notre système:

    ```sh
    yum install krb5-server krb5-libs krb5-auth-dialog
    ```

- ### Configuration

    On modifie la configuration de Kerberos:

    - `/etc/krb5.conf`: Voir le fichier de configuration, disponible [ici](./src/krb5.conf)
    - `/var/kerberos/krb5kdc/kdc.conf`: Voir le fichier de configuration, disponible [ici](./src/kdc.conf)

- ### Création de la BDD

    Pour créer la BDD Kerberos, on fait:

    ```sh
    /usr/sbin/kdb5_util create -s
    ```

    ce qui nous donne:

    ```txt
    Loading random data
    Initializing database '/var/kerberos/krb5kdc/principal' for realm 'AO.LOCAL',
    master key name 'K/M@AO.LOCAL'
    You will be prompted for the database Master Password.
    It is important that you NOT FORGET this password.
    Enter KDC database master key: 
    Re-enter KDC database master key to verify: 
    ```

    Dans le cas de ce TP, les credentials sont:

    | ID  | PWD  |
    |-----|------|
    | N/A | root |

- ### Modification des utilisateurs administrateurs

    On modifie le fichier suivant:

    - `/var/kerberos/krb5kdc/kadm5.acl`: Voir le fichier de configuration, disponible [ici](./src/kadm5.acl)

- ### Démarrage des services Kerberos 5

  ```sh
  systemctl enable --now krb5kdc
  systemctl enable --now kadmin
  ```

- ### Ajout d'un Principal dans Kerberos

    Maintenant que `kadmin` a démarré, on peut ajouter un utilisateur en tant que `principal`:

    ```sh
    sudo kadmin.local
    addprinc vagrant
    ```

- ### Configuration des enregistrements DNS MaraDNS

    Voir le fichier de configuration de la zone MaraDNS, disponible [ici](./src/db.ao.local).
    Voir le fichier de configuration MaraRC, disponible [ici](./src/mararc).

## Installation de clients Kerberos

- ### Installation

    On installe les dépendances pour un client Kerberos:

    ```sh
    yum install krb5-workstation krb5-libs krb5-auth-dialog
    ```

- ### Configuration

    On configure le client Kerberos avec le même fichier `krb5.conf` que le KDC.



## Debian

## Server

```
sudo apt install -y nano git dnsutils gcc make
git clone https://gitlab.com/maradns/maradns.git maradns && cd maradns
./configure
CC=gcc
export CC
make
sudo make install
sudo apt install -y krb5-kdc krb5-admin-server
/usr/sbin/kdb5_util create -s
sudo systemctl start krb5-admin-server.service
sudo systemctl status krb5-kdc.service
sudo kadmin.local -q "addprinc vagrant/admin"
kinit vagrant/admin
klist
```

> [!NOTE]
> Il faut penser à modifier la configuration de resolv.conf afin de pointer sur MaraDNS.

## Client