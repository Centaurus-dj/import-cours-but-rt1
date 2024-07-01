---
Author: Alexis Opolka
Subject: Infrastructure de sécurité
---

# R401 - Infrastructure de sécurité

## À propos

Ce compte rendu comprend tous les TP de R401 en un seul fichier.

## Sommaire

- [R401 - Infrastructure de sécurité](#r401---infrastructure-de-sécurité)
  - [À propos](#à-propos)
  - [Sommaire](#sommaire)
  - [TP 1 - Cryptographie](#tp-1---cryptographie)
    - [Fonctions de Hachage](#fonctions-de-hachage)
  - [TP 2 - VPN](#tp-2---vpn)
  - [TP 3 - Proxy](#tp-3---proxy)
    - [1 - Questions Préliminaires](#1---questions-préliminaires)
    - [2 - Proxy direct](#2---proxy-direct)
    - [3 - Proxy reverse](#3---proxy-reverse)
      - [Annexes TP 3](#annexes-tp-3)
        - [Configuration Squid](#configuration-squid)
        - [Configuration Nginx Proxy Inverse](#configuration-nginx-proxy-inverse)
          - [nginx.conf](#nginxconf)
          - [proxy\_params](#proxy_params)
  - [TP 4 - NAT et filtrage](#tp-4---nat-et-filtrage)

## TP 1 - Cryptographie

> [!NOTE]
> Vu que ce TP a été fait en ratrapage avec l'accord de M. Comby, je suis seul à faire la manipulation.

### Fonctions de Hachage

1. #### Calcul d'un condensé à l'aide de MD5

    1. Quel hash obtenez vous ?

        On fait:

        ```sh
        md5sum md5-checksum.txt
        ```

        Ce qui nous donne:

        ```sh
        e59ff97941044f85df5297e1c302d260  md5-checksum.txt
        ```

        où `e59ff97941044f85df5297e1c302d260` est le hash de notre fichier.

    1. Combien de condensés différents sont possibles ?
    1. La dernière propriété mathématique énoncée dans Wikipédia est-elle possible en pratique.

1. #### Vérification des propriétés de condensé

    1. Reprenez le fichier précédent et renommez-le. \
        Calculez son hash. Que remarquez-vous ?

        On renomme notre fichier `md5-checksum-modified.txt` puis on calcule notre hash:

        ```sh
        md5sum md5-checksum-modified.txt
        ```

        Ce qui nous donne:

        ```sh
        e59ff97941044f85df5297e1c302d260  md5-checksum-modified.txt
        ```

        On peut voir que le hash n'a pas changé.

    2. Modifiez maintenant le contenu du fichier. Recalculez le hash. Que remarquez-vous ?

        Après avoir changé le contenu du fichier, on obtient:

        ```sh
        b0b894e9da826be633b074417da4fd79  md5-checksum-modified.txt
        ```

        On peut voir que le hash a bien changé.

    3. Peut-on calculer le hash d'un fichier binaire (un executable par exemple) ? \
        Vérifiez votre réponse.

        On peut en effet calculer le hash d'un fichier binaire, par exemple le hash du binaire Bash:

        ```sh
        6c9105164270542e8b8b79ef790beee1  /bin/bash
        ```

1. #### Clefs de chiffrement

    1. Génération des clefs

        On fait:

        ```sh
        gpg --gen-key
        ```

        ou

        ```sh
        gpg --full-generate-key
        ```

        Ce qui nous donne:

        ```sh
        gpg: directory '~/.gnupg/openpgp-revocs.d' created
        gpg: revocation certificate stored as '~/.gnupg/openpgp-revocs.d/E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18.rev'
        public and secret key created and signed.

        pub   ed25519 2024-06-17 [SC] [expires: 2027-06-17]
            E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
        uid                      Alexis Opolka <contact@alexis-opolka.dev>
        sub   cv25519 2024-06-17 [E] [expires: 2027-06-17]
        ```

        1. Vérifiez que votre trousseau numérique contient bien votre clef publique avec la commande suivante:

            ```sh
            gpg --list-keys
            ```

            Quels sont les différents champs ?

            ---

            On peut voir notre clé dans notre trousseau:

            ```sh
            [keyboxd]
            ---------
            pub   ed25519 2024-06-17 [SC] [expires: 2027-06-17]
                E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
            uid           [ultimate] Alexis Opolka <contact@alexis-opolka.dev>
            sub   cv25519 2024-06-17 [E] [expires: 2027-06-17]
            ```

            Les différents champs sont:

            - `pub`
            - `uid`
            - `sub`

        1. Quelle commande permet de lister les clefs privées présentes sur votre machine ? \
            Comment peut-on savoir comment relier la clef publique et la clef privée ?

            La commande qui permet de lister les clefs privées est:

            ```sh
            gpg --list-secret-keys
            ```

            Nous avons, une empreinte similaire pour la clé privée et sa clé publique, dans notre cas nous avons:

            - empreinte clé privée: `E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18`
            - empreinte clé publique: `E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18`

            Vu qu'elles sont similaires, nous savons que la clé privée et la clé publique sont correspondantes.

    1. Diffusion de la clef publique

        On exporte notre clé:

        ```sh
        gpg --export --armor > gpg-pub-key.key
        ```

        1. Quel est le contenu de votre fichier ?

            Le contenu du fichier est:

            ```sh
            -----BEGIN PGP PUBLIC KEY BLOCK-----

            mDMEZnBSkxYJKwYBBAHaRw8BAQdA7t57Tjn0Vck11chnRKOtHn8Q489FHtTJcF3q
            0NyDOa+0KUFsZXhpcyBPcG9sa2EgPGNvbnRhY3RAYWxleGlzLW9wb2xrYS5kZXY+
            iJkEExYKAEEWIQTmEZtbcnz8ilyX5f0fWTbJZ/+6GAUCZnBSkwIbAwUJBaOagAUL
            CQgHAgIiAgYVCgkICwIEFgIDAQIeBwIXgAAKCRAfWTbJZ/+6GHOmAP42W/toxiJz
            adfMtVupXlaftvNmBV4XIfxqTMAumewKcwEAkKBowiNYmCk9LCsZWWIzjkD/7nTp
            KAL+fCe+AsIpvAe4OARmcFKTEgorBgEEAZdVAQUBAQdA0dKLR6lmZ2DSW430roUk
            dQku6u5Gqas718rsYPSYHSIDAQgHiH4EGBYKACYWIQTmEZtbcnz8ilyX5f0fWTbJ
            Z/+6GAUCZnBSkwIbDAUJBaOagAAKCRAfWTbJZ/+6GA2pAPwOUWp//mwPKiOtKKs/
            kLwVwjdmwqMVn+ZsCf7UkMjP2QEAkszkWxP3XQJk4BGj4OawB2NzZ/ydKvNl9Hg3
            WBEACgg=
            =J9Ep
            -----END PGP PUBLIC KEY BLOCK-----
            ```

            Comme nous pouvons le voir, nous avons exporté notre clé publique.

        1. Il est également possible d'exporter sa clef privée pour la mettre sur son ordinateur (si on ne l'a pas créée sur son ordinateur). \
            Pour cela, on utilise la commande suivante:

            ```sh
            gpg --export-secret-keys --armor > gpg-private-key.key
            ```

1. #### Chiffrement d'un fichier

   1. Pour envoyer un message chiffré à votre binôme, quelle clef faut-il utiliser pour chiffrer le message ?
      Pour cela, soit on la récupère sur un site de dépôt de lcef soit on l'importe à partir d'un fichier reçu.

      ```sh
      gpg --import gpg-pub-key.key
      ```

   1. Vérifier que la clef est importée sur votre trousseau numérique.

      On fait à nouveau:

      ```sh
      gpg --list-keys
      ```

      ce qui nous donne:

      ```sh
      [keyboxd]
      ---------
      pub   ed25519 2024-06-17 [SC] [expires: 2027-06-17]
          E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
      uid           [ultimate] Alexis Opolka <contact@alexis-opolka.dev>
      sub   cv25519 2024-06-17 [E] [expires: 2027-06-17]
      ```

      On peut voir que nous avons bien importé la clé publique.

   1. Générer un fichier texte `toto.txt` et chiffrez le avec la commande suivante:

      ```sh
      gpg --armor --recipient alexis.opolka@etu.umontpellier.fr --encrypt toto.txt
      ```

      Quel est le fichier généré qui correspond à la version chiffrée de `toto.txt` ?

      Le déchiffrage du fichier se fera avec la clé privée du destinaire. \
      La commande utilisée pour faire cela est:

      ```sh
      gpg --decrypt toto.txt.asc > toto.txt
      ```

      ---

      Le fichier qui correspond à la version chiffrée de `toto.txt` est `toto.txt.asc` avec le contenu suivant:

      ```sh
      -----BEGIN PGP MESSAGE-----

      hF4DtUDPdHXa7z4SAQdAM2ry0pUJ5DEQdGzqRU4Q12dg8RMlwVAd27IGU2OA4CUw
      L53oZ5qFgeGVgo/GHMgjQOptm+3x7pTy33np3s0+dlT6PnVyuRySYAhqmWxh+FVJ
      1HoBCQIQDPXb8QhUJTisHp4LjNg4KIia+UNikQVsuubKBvQxQ0ugVGRLoAGjapx8
      flNaC/D52Xsk66n87b76/G0qk30tvCWvcKiHq/rnnuAtUqrcADqCo//J0k3q3gjy
      a05KDYksA3tbZg6yvDnfCOc3r9tY/srYcr3Grg==
      =jItP
      -----END PGP MESSAGE-----
      ```

      On déchiffre le contenu du fichier, ce qui nous donne:

      ```sh
      This file has been encrypted with my GPG key
      ```

   1. Vérifier que le fichier déchiffré est équivalent au fichier initial.

      Le contenu du fichier initial est:

      ```txt
      This file has been encrypted with my GPG key
      ```

      et le contenu du fichier déchiffré est:

      ```txt
      This file has been encrypted with my GPG key
      ```

      Le fichier déchiffré est donc bien équivalent au fichier initial.

1. #### Signature numérique

   1. Signature d'un fichier

      1. Tester les commandes ci-dessus et vérifier leurs résultat.

          Pour vérifier la signature on peut utiliser la commande suivante:

          ```sh
          gpg --verify <fichier.gpg>
          ```

          ---

          - Signature avec Compression

              On fait:

              ```sh
              gpg --sign toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.gpg`.

              Où:

              ```sh
              gpg --verify toto.txt.gpg
              ```

              donne:

              ```sh
              gpg: Signature made Mon 17 Jun 2024 06:15:45 PM CEST
              gpg:                using EDDSA key E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
              gpg: Good signature from "Alexis Opolka <contact@alexis-opolka.dev>" [ultimate]
              ```

          - Signature sans Compression

              On fait:

              ```sh
              gpg --clearsign toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.asc`.

          - Export de la signature

              On fait:

              ```sh
              gpg --detach-sign toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.sig`.

              Où:

              ```sh
              gpg --verify toto.txt.sig
              ```

              donne:

              ```sh
              gpg: assuming signed data in 'toto.txt'
              gpg: Signature made Mon 17 Jun 2024 06:18:34 PM CEST
              gpg:                using EDDSA key E6119B5B727CFC8A5C97E5FD1F5936C967FFBA18
              gpg: Good signature from "Alexis Opolka <contact@alexis-opolka.dev>" [ultimate]
              ```

          - Signature et Chiffrement

              On fait:

              ```sh
              gpg -r contact@alexis-opolka.dev --armor --sign --encrypt toto.txt
              ```

              Ce qui nous donne un fichier `toto.txt.asc` avec le contenu suivant:

              ```sh
              -----BEGIN PGP MESSAGE-----

              hF4DtUDPdHXa7z4SAQdApAJZP75gr7EFGuQX3l4bn7lc+XngCUwm9IVqTGCKcCEw
              bti4GK7FeEfQi68YxF2eogQXCUop3mCrG8OXTvdrQHbfb8grMmEtcXEIItPCFA6o
              1MA3AQkCELfrQpFxSyCETvwSW03vnHaHgRnRlivrNyOoiycEFR97RiSTMdm9wx1z
              yoyji4Qggf6uZtebKLaSNSlXgQ22KFhwiK7MreYtfB0uCkpKQ4BLY4MPhmFEtEkb
              mh4IKp4I9H/SJq4jmJW7fWVCWbZmZ7t3j/zZTNJzqCO6Mb2dEOtQy7XbnHPXDMm4
              n0Hc5GhbKjDRhHcPBufk8Oq1BVm/lRxabnNaG18x1OpUpEhbDkTwHySurxae6/a5
              JwIMRIex4zXIxQqyCzDN7LlnQM8NvXNbtzIcXOK3Feh213hCbceCEEnITTBYbK8t
              jO6t6fMGYc34Ng==
              =VQo/
              -----END PGP MESSAGE-----
              ```

   1. Signature d'une clef publique

      1. Signer la clef de votre binôme avec la commande suivante:

          ```sh
          gpg --sign-key <id-clef>
          ```

          > [!NOTE]
          > Dans mon cas, je ne peux signer une autre clef que la mienne, je signe donc la clé GPG de [Fedora Project](https://fedoraproject.org) pour
          > la version 40 de la distribution linux Fedora.

          ---

          On fait:

          ```sh
          gpg --sign-key 115DF9AEF857853EE8445D0A0727707EA15B79CC
          ```

          > [!NOTE]
          > La clé GPG publique de Fedora pour la version 40 de la distribution a ces informations:
          >
          > ```sh
          > pub   rsa4096 2023-01-24 [SCE]
          >     115DF9AEF857853EE8445D0A0727707EA15B79CC
          > uid           [ unknown] Fedora (40) <fedora-40-primary@fedoraproject.org>
          > ```

          Ce qui nous donne:

          ```sh
          pub  rsa4096/0727707EA15B79CC
              created: 2023-01-24  expires: never       usage: SCE
              trust: unknown       validity: unknown
          [ unknown] (1). Fedora (40) <fedora-40-primary@fedoraproject.org>

          pub  rsa4096/0727707EA15B79CC
              created: 2023-01-24  expires: never       usage: SCE
              trust: unknown       validity: unknown
          Primary key fingerprint: 115D F9AE F857 853E E844  5D0A 0727 707E A15B 79CC

              Fedora (40) <fedora-40-primary@fedoraproject.org>

          Are you sure that you want to sign this key with your
          key "Alexis Opolka <contact@alexis-opolka.dev>" (1F5936C967FFBA18)
          ```

          Maintenant, lorsque l'on regarde la clé dans notre trousseau:

          ```sh
          pub   rsa4096 2023-01-24 [SCE]
              115DF9AEF857853EE8445D0A0727707EA15B79CC
          uid           [  full  ] Fedora (40) <fedora-40-primary@fedoraproject.org>
          ```

          On peut voir que nous avons une confiance totale à la clef puisque nous venons de la signer.

1. #### Utilisation d'un certificat

   - Nous installons OpenSSL:

      ```sh
      dnf install openssl
      ```

   - On génère sa clef:

      ```sh
      openssl genrsa -aes256 -out my-key.key 4096
      ```

   - On génère un certificat "débloqué":

      ```sh
      mv my-key.key my-key.key.lock
      openssl rsa -in my-key.key.lock -out my-key.key
      ```

   - On génère le fichier de demande de signature de notre clef et renseigner tous les champs demandés:

      ```sh
      openssl req -new -key my-key.key.lock -out certificat.csr
      ```

   - On auto-signe son certificat X509:

      ```sh
      openssl x509 -req -days 365 -in certificat.csr -signkey my-key.key.lock -out certificat.crt
      ```

   - On active Apache2

      ```sh
      systemctl start httpd
      ```

   - On active le module SSL sur le serveur Apache

      ```sh
      dnf install mod_ssl -y
      ```

   1. Effectuer la configuration sur le serveur. Faut-il prévoir quelque chose sur le client ? \
      Vérifier si le trafic est chiffré lors de l'envoi de la page web.

      Vu que l'on utilise Fedora au lieu d'une distribution Ubuntu/Debian, nous devons faire plusieurs actions en plus d'une simple
      configuration.

      - Configuration serveur

        - Création des répertoires `/etc/httpd/sites-available` et `/etc/ssl/www`

            On fait:

            ```sh
            mdkir /etc/httpd/sites-available /etc/ssl/www
            ```

        - Copie des certificats dans le répertoire

            On fait:

            ```sh
            cp certificat.crt /etc/ssl/www/
            cp my-key.key /etc/ssl/www/
            ```

        - Création du fichier de configuration `/etc/httpd/sites-available/centaurustasie.fr.conf`

            On fait:

            ```sh
            touch /etc/httpd/sites-available/centaurustasie.fr.conf
            ```

            Avec le contenu suivant:

            ```apacheconf
            <VirtualHost *:80>
                    ServerName      centaurustasie.fr
                    # On redirige le port HTTP vers le port HTTPS
                    Redirect / <https://centaurustasie.fr>
            </VirtualHost>
            <VirtualHost>
                    ServerName      centaurustasie.fr
                    DocumentRoot    /var/www/test

                    SSLEngine on
                    SSLCertificateFile      /etc/ssl/www/certificat.crt
                    SSLCertificateKeyFile   /etc/ssl/www/my-key.key
                    SSLProtocol all -SSLv2 -SSLv3
                    SSLHonorCipherOrder on
            </VirtualHost>
            ```

        - On inclue ensuite le fichier dans la configuration

            On ajoute à la fin du fichier `/etc/httpd/conf/httpd.conf`

            ```ini
            include sites-available/
            ```

      - Configuration Client

          On ajoute notre FQDN dans le fichier `/etc/hosts`:

          ```ini
          127.0.0.1 centaurustasie.fr
          ```

      On peut maintenant cURL le FQDN en HTTPS:

      ```sh
      curl -k https://centaurustasie.fr
      ```

      ce qui nous donne:

      ```html
      <!DOCTYPE html>
      <html lang="en">
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>SAE 401 - Test Page</title>
          </head>
          <body>
              Hello World, I'm not dead (yet)!
          </body>
      </html>
      ```

      On constate que l'on arrive bien à accéder à la page en HTTPS.

      Si l'on rend cURL un peu plus verbeux lors de la requête HTTPS, cela nous donne:

      ```sh
      - Host centaurustasie.fr:443 was resolved.
      - IPv6: (none)
      - IPv4: 127.0.0.1
      - Trying 127.0.0.1:443...
      - Connected to centaurustasie.fr (127.0.0.1) port 443
      - ALPN: curl offers h2,http/1.1
      - TLSv1.3 (OUT), TLS handshake, Client hello (1):
      - TLSv1.3 (IN), TLS handshake, Server hello (2):
      - TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
      - TLSv1.3 (IN), TLS handshake, Certificate (11):
      - TLSv1.3 (IN), TLS handshake, CERT verify (15):
      - TLSv1.3 (IN), TLS handshake, Finished (20):
      - TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
      - TLSv1.3 (OUT), TLS handshake, Finished (20):
      - SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / x25519 / RSASSA-PSS
      - ALPN: server accepted http/1.1
      - Server certificate:
      - subject: C=FR; ST=Occitanie; L=Béziers; O=IUT Béziers; OU=R&T; CN=centaurustasie.fr; emailAddress=<contact@centaurustasie.fr>
      - start date: Jun 17 17:32:42 2024 GMT
      - expire date: Jun 17 17:32:42 2025 GMT
      - issuer: C=FR; ST=Occitanie; L=Béziers; O=IUT Béziers; OU=R&T; CN=centaurustasie.fr; emailAddress=<contact@centaurustasie.fr>
      - SSL certificate verify result: self-signed certificate (18), continuing anyway.
      - Certificate level 0: Public key type RSA (4096/152 Bits/secBits), signed using sha256WithRSAEncryption
      - using HTTP/1.x

      > GET / HTTP/1.1
      > Host: centaurustasie.fr
      > User-Agent: curl/8.6.0
      > Accept: */*
      >
      - TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
      - TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
      - old SSL session ID is stale, removing
      < HTTP/1.1 200 OK
      < Date: Mon, 17 Jun 2024 19:51:57 GMT
      < Server: Apache/2.4.59 (Fedora Linux) OpenSSL/3.2.1
      < Last-Modified: Mon, 17 Jun 2024 19:44:25 GMT
      < ETag: "f0-61b1b31519b73"
      < Accept-Ranges: bytes
      < Content-Length: 240
      < Content-Type: text/html; charset=UTF-8
      <

      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SAE 401 - Test Page</title>
      </head>
      <body>
        Hello World, I'm not dead (yet)!
      </body>
      * Connection #0 to host centaurustasie.fr left intact
      ```

      On peut voir que l'on a bien une interaction SSL qui s'effectue lors de la requête HTTPS GET.

      Aussi visible sur cette prise sous Wireshark:

      ![ssl-centaurustasie.fr](./src/img/ssl-centaurustasie.fr.png)

   1. Quels sont d'après vous les risques pour un administrateur réseau d'avoir des utilisateurs qui utilisent principalement des sites en HTTPS ?

      Un risque qu'il pourrait y avoir, c'est d'être incapable de connaître les informations reçues et envoyées, ou bien les actions menées
      par les utilisateurs puisque le traffic est chiffré.

1. #### Client mail

    1. Installer et configurer sur votre machine le client Email Thunderbird. \
        Envoyez à votre binôme un courrier à la fois chiffré et signé.

        Nous n'avons qu'à importer notre clé GPG dans Thunderbird:

        ![thunderbird-key-import](./src/img/thunderbird-key-import.png)

        > [!NOTE]
        > Nous importons une autre clé que celle de la boîte mail en question car j'avais déjà
        > une clé présente, au lieu de générer à nouveau une clé PGP, j'ai préféré importer la clé
        > utilisée lors des manipulations plus en haut.

        Nous voyons que l'email que l'on a envoyé a été signé et crypté.

        ![thunderbird-encrypted-signed-email](./src/img/thunderbird-encrypted-signed-email.png)

## TP 2 - VPN

1. ### 1 - Questions Préliminaires

    1. Configurer la passerelle de sorte que le client interne ait accès à la partie internet.
        Il s'agira de mettre du NAT en place.

    1. Donner la configuration (`adresses`, `masques`, `routes`, `iptables`) de chacun des équipements.

    1. Installer OpenVPN et la librairie `Izo` sur la passerelle et sur le client.

1. ### 2 - Premiers tests

    1. Vérifier dans un premier temps la liste des interfaces réseau sur votre machine. \
        Ensuite, on cherchje à vérifier si OpenVPN peut être lancé à la main. \
        Sur la passerelle, exécuter la commande suivante:

        ```sh
        openvpn --dev tun0 --ifconfig 192.168.10.1 192.168.10.2
        ```

        Et sur le client OpenVPN celle indiquée ci-dessous:

        ```sh
        openvpn --remote <ip-gateway> --dev tun0 --ifconfig 192.168.10.2
        ```

    1. Vérifier que la connexion est correctement effectuée en réalisant un ping judicieux.

    1. Lister les interfaces présentes sur vos machines. Que constatez-vous ?

    1. Pendant que le ping fonctionne, capturez une trame à l'aide de wireshark sur chacune des deux \
        interfaces du client openvpn. Que constatez-vous ? \
        Expliquez et détaillez l'encapsulation du paquet capturé sur l'interface réseau ethernet de votre machine.

    1. Démarrer un service non chiffré quelconque sur la passerelle ( `telnet`, `ftp`, etc.) \
        Capturer les paquets échangés sur l'interface ethernet. Sont-ils chiffrés ?

## TP 3 - Proxy

### 1 - Questions Préliminaires

1. Rappelez quel est le rôle d'un proxy direct

    Le rôle d'un proxy direct est d'authentifier le traffic
    de clients du réseau comme étant originel de son adresse IP.

    Cela permet de masquer l'adresse des machines utilisateurs sur
    le traffic internet.

2. Quelle différence faites-vous avec le proxy inverse ?

    Le proxy inverse est principalement utilisé pour sécuriser des connexions
    serveurs. Il est utilisé comme machine hôte du traffic serveur-client
    afin d'empêcher d'exposer sur internet le serveur en question.

3. Citez quelques exemples de solutions permettant de réaliser ces fonctions.

    Nginx, Apache et tout serveur web permettant de gérer du traffic entrant et sortant.

### 2 - Proxy direct

On met en place l'infrastructure nécessaire au TP:

1. Installer le paquet `apache2` sur le serveur web. On gardera la configuration de base du serveur.

    > [!NOTE]
    > Vu que l'on utilise une VM `fedora`, nous allons devoir utiliser
    > le paquet `httpd` qui se trouve être le serveur Apache mais pour les distributions `RPM`.

    On fait:

    ```sh
    dnf install httpd
    ```

1. Installer squid sur le serveur proxy.
    Le fichier de configuration est dans `/etc/squid/squid.conf`.
    Faire une copie de sauvegarde de ce fichier (`/etc/squid/squid.conf.bak`) avant de le modifier.

    On fait:

    ```sh
    dnf install squid
    cp /etc/squid/squid.conf{, .bak}
    ```

1. Déterminer le plan d’adressage pour que le montage soit fonctionnel.

    Configurer les routes et les règles `nftables` pour que le poste client puisse joindre le serveur web et vice-versa.
    On s’arrangera pour que le serveur WEB soit sur le plan d’adressage de la salle de TP.
    Le serveur Proxy et le client Web pourront être des machines virtuelles.
    Attention, il faut que le client web ait une interface graphique pour pouvoir utiliser un navigateur Web.

    On décide d'utiliser des machines virtuelles afin de "nous simplifier" les manipulations.
    Ayant plus l'habitude de manipuler des machines sous Fedora, j'utiliserais donc des images [Fedora Cloud](https://fedoraproject.org/cloud/).

    | Machine                       | IP                 |
    | ----------------------------- | ------------------ |
    | Serveur WEB                   | 10.10.10.1/24      |
    | Routeur - Pate Réseau Externe | 10.10.10.254/24    |
    | Routeur - Pate Réseau Interne | 172.168.100.254/24 |
    | Routeur - Pate Réseau NAT     | 192.168.124.254/24 |
    | Serveur Proxy                 | 172.168.100.100/24 |
    | Client                        | 172.168.100.1/24   |

    Ce qui nous donne ce schéma réseau suivant:

    ![tp-proxy-reseau-1](./src/img/tp-proxy-reseau-1.png)

    - #### Configuration du routeur

        On configure notre routeur qui va nous permettre d'accéder à internet ainsi que d'accéder à nos deux réseaux:

        ```ini
        conf t

        ### Configuration du routage
        ip routing
        ip route 0.0.0.0 0.0.0.0 192.168.124.1 # Routeur de la machine hôte

        ### Configuration des interfaces
        int F0/0 # Interface Interne
        ip address 172.168.100.254 255.255.255.0
        no shut
        ip nat inside
        exit
        int F1/0 # Interface NAT
        ip address 192.168.124.254 255.255.255.0
        no shut
        ip nat outside
        exit
        int F0/1 # Interface Externe
        ip address 10.10.10.254 255.255.255.0
        ip nat inside
        no shut
        exit

        ### Configuration du NAT
        access-list 1 permit 172.168.100.0 0.0.0.255
        access-list 1 permit 10.10.10.0 0.0.0.255
        ip nat inside source list 1 interface F1/0 overload # NAT pour internet

        ### Enregistrement de la configuration
        do wr mem
        ```

1. Modifier le fichier de configuration de squid pour que le trafic de votre réseau local seulement soit capté par le serveur proxy.
    Squid permet également de mettre en cache les pages web visitées.
    On pourra modifier la valeur par défaut

    On modifie le fichier de configuration de squid avec les instructions suivantes:

    ```squidconf
    acl localnet src 172.168.100.0/24
    http_access allow localnet
    cache_dir ufs /var/spool/squid 100 16 256
    ```

1. Configurez le navigateur du client web pour qu'il utilise le serveur proxy que vous avez configuré (adresse IP et port d'écoute).

    On configure le navigateur afin qu'il utilise le proxy:

    ![firefox-proxy-configuration](./src/img/firefox-proxy-configuration.png)

    On peut voir que la requête `HTTP GET` est envoyée au proxy et traitée:

    ![proxy-access-1](./src/img/proxy-access-1.png)
    ![proxy-access-2](./src/img/proxy-access-2.png)

1. une fois la configuration opérationnelle, on bloquera tout autre trafic.
    Prévoir la règle nftable ou la politique par défaut qui permet de réaliser cela.

    Sur notre routeur Cisco, nous créons à nouveau l'ACL 1 qui nous permet de contrôler le trafic sortant:

    ```ini
    access-list 1 permit 172.168.100.100 0.0.0.0
    access-list 1 permit 10.10.10.0 0.0.0.255
    ip nat inside source list 1 interface F1/0 overload
    ```

1. Vérifier le fonctionnement de la mise en cache en proposant des captures de trames judicieuses.

    Nous capturons le traffic TCP et HTTP entre le client et le proxy et entre le routeur et le serveur web afin de voir si lorsque
    l'on requête le serveur web, nous retrouvons une requête HTTP liée:

    > [!NOTE]
    > Nous allons utiliser `watch` afin de ne pas avoir à s'encombrer de relancer une requête via firefox.

    On fait:

    ```sh
    watch -n 5 curl -x http://172.168.100.100:3128 http://10.10.10.1/index.html
    ```

    > [!WARNING]
    > Squid ne cache pas les requêtes avec des codes de statut 3XX, 4XX, 5XX. \
    > Si la requête se résout sous un de ces statuts, Squid indiquera un CACHE_MISS.
    > Si la requête est effectuée en HTTPS, Squid ne cache pas non plus la requête.

    On peut voir que nous avons une réponse directement sans passer par le serveur web:

    ![proxy-cache](./src/img/proxy-cache.png)

    On peut aussi voir avec les logs d'accès de Squid:

    ```sh
    tail -f /var/log/squid/access.log
    ```

    ce qui nous donne:

    ```sh
    1718783702.696      0 172.168.100.1 TCP_MEM_HIT/200 360 HEAD http://10.10.10.1/index.html - HIER_NONE/- text/html
    ```

    On tombe bien sur une page web qui a été cachée et est donc retournée du disque du serveur proxy et non du serveur web.

1. Prévoir une procédure de test pour illustrer que le trafic est bien capturé par le serveur proxy. \
    Vous analyserez également les logs qui sont situés dans `/var/log/squid/`. \
    Une description des logs possibles se trouve [ici](https://wiki.squid-cache.org/SquidFaq/SquidLogs).

    De la même manière que l'on a fait, nous capturons le trafic entre le client et le proxy et le proxy et le serveur web,
    si à chaque requête HTTP, nous avons du trafic HTTP et TCP entre le proxy et le serveur web, tout est bon.

    Si à chaque requête HTTP, nous avons du trafic HTTP et TCP entre le client et le serveur web, alors le proxy ne capture pas tout le trafic.

    On peut aussi voir les logs d'accès situés dans le fichier `/var/log/squid/access.log`, si l'on retrouve une entrée correspondante à la requête
    du client alors le proxy capture le trafic de celui-ci.

1. Quel peut-être, à votre avis, une des difficultés rencontrée avec squid pour la navigation sur le WEB ?

    Une des difficultés rencontrée avec squid peut être une atteinte à la vie privée des personnes étant sur le réseau capturé
    par le proxy.

    On peut aussi avoir le problème du "Single Point of Failure", si nous arrivons à surcharger le proxy, nous ne pouvons plus
    accéder à Internet puisque c'est une étape obligatoire d'accès.

1. Afin que la sécurité soit assurée (utilisation du proxy obligatoire pour sortir) que faudrait-il prévoir au niveau de la configuration des postes client ?

    il faudrait configurer les postes clients de manière à s'assurer que toutes leurs requêtes passent par le proxy.

### 3 - Proxy reverse

1. Dans un premier temps, on va monter l’infrastructure réseau simplifiée pour tester notre proxy inverse. Réaliser le montage de la figure 2.

    On crée le réseau suivant:

    ![tp-proxy-reseau-2](./src/img/tp-proxy-reseau-2.png)

    où:

    | Machine                                          | IP                 |
    | ------------------------------------------------ | ------------------ |
    | Serveur WEB Apache                               | 192.168.1.120/24   |
    | Serveur WEB Nginx                                | 192.168.1.130/24   |
    | Routeur - Pate Réseau Interne                    | 172.168.100.254/24 |
    | Routeur - Pate Réseau NAT                        | 192.168.124.254/24 |
    | Serveur Proxy Inverse - Pate Réseau client       | 172.168.100.100/24 |
    | Serveur Proxy Inverse - Pate Réseau Serveurs Web | 192.168.1.254/24   |
    | Client                                           | 172.168.100.1/24   |

1. Installer Nginx sur le serveur proxy inverse et tester son fonctionnement. Attention si vous avez un apache2 qui tourne sur la même machine, il risque d’y avoir des conflits

    Quand on fait un cURL, nous voyons que nous accédons bien au serveur Nginx:

    ```sh
    curl -I 127.0.0.1
    ```

    nous donne:

    ```sh
    HTTP/1.1 200 OK
    Server: nginx/1.26.1
    Date: Wed, 19 Jun 2024 12:15:17 GMT
    Content-Type: text/html
    Content-Length: 59
    Last-Modified: Wed, 19 Jun 2024 12:06:08 GMT
    Connection: keep-alive
    ETag: "6672c9b0-3b"
    Accept-Ranges: bytes
    ```

1. Installer un serveur web sur les 2 machines qui font office de serveur web (apache ou Nginx) on différenciera les 2 page web pour bien arriver à faire la différence au moment de l’accès à ces pages web.

    On installe un serveur apache et un serveur Nginx.

    Vu que sous Fedora les deux serveurs ont la même page d'accueil, nous créons ces pages-ci:

    - Nginx:

        ```html
        <html>
            <body>
                This is the Nginx server
            </body>
        </html>
        ```

    - Apache:

        ```html
        <html>
            <body>
                This is the Apache server
            </body>
        </html>
        ```

1. On se servira d’une machine avec une interface graphique pour faire le client.
    Configurer le plan d’adressage du schéma pour que cela fonctionne.
    Configurer le fichier /etc/hosts sur le client web pour que le nom de domaine que vous choisirez soit associé à votre
    serveur proxy inverse (cela remplacera le fonctionnement du DNS).

    On ajoute dans `/etc/hosts`:

    ```inimynetwork
    172.168.100.100 centaurustasie.fr
    ```

1. Configurer le serveur proxy inverse pour que tout le trafic provenant du client web
    à destination du nom de site que vous avez renseigné dans le `/etc/hosts` soit redirigé alternativement vers l’un ou l’autre des serveurs web.

    On crée un fichier de configuration `centaurustasie.fr.conf` dans le dossier `/etc/nginx/sites-available` que nous venons de créer.

    ```nginxconf
    upstream backend {
        server 192.168.1.120:80 weight=1 max_fails=3 fail_timeout=30s;
        server 192.168.1.130:80 weight=1 max_fails=3 fail_timeout=30s;
    }

    server {
        listen 80;
        listen [::]:80;

        server_name centaurustasie.fr www.centaurustasie.fr;

        location / {
            proxy_pass http://backend;
            include proxy_params;
        }
    }
    ```

    Nous l'ajoutons ensuite dans le fichier de configurations `nginx.conf`

    > [!NOTE]
    > Si nous tombons sur une erreur `502: Bad Gateway`, une solution peut être
    > de paramétrer SELinux:
    >
    > ```sh
    > setsebool -P httpd_can_network_connect 1
    > ```

    En effectuant un cURL plusieurs fois, nous pouvons voir que notre Reverse Proxy et notre Load Balancing fonctionnent:

    - Requête 1:

        ```html
        <html>
            <body>
                This is the Apache server
            </body>
        </html>
        ```

    - Requête 2:

        ```html
        <html>
            <body>
                This is the Nginx server
            </body>
        </html>
        ```

#### Annexes TP 3

##### Configuration Squid

```squidconf
#
# Recommended minimum configuration:
#

acl localnet src 172.168.100.0/24

acl SSL_ports port 443
acl Safe_ports port 80  # http
acl Safe_ports port 21  # ftp
acl Safe_ports port 443  # https
acl Safe_ports port 70  # gopher
acl Safe_ports port 210  # wais
acl Safe_ports port 1025-65535 # unregistered ports
acl Safe_ports port 280  # http-mgmt
acl Safe_ports port 488  # gss-http
acl Safe_ports port 591  # filemaker
acl Safe_ports port 777  # multiling http

#
# Recommended minimum Access Permission configuration:
#
# Deny requests to certain unsafe ports
http_access deny !Safe_ports

# Deny CONNECT to other than secure SSL ports
http_access deny CONNECT !SSL_ports

# Only allow cachemgr access from localhost
http_access allow localhost manager
http_access deny manager

# This default configuration only allows localhost requests because a more
# permissive Squid installation could introduce new attack vectors into the
# network by proxying external TCP connections to unprotected services.
http_access allow localhost

# The two deny rules below are unnecessary in this default configuration
# because they are followed by a "deny all" rule. However, they may become
# critically important when you start allowing external requests below them.

# Protect web applications running on the same server as Squid. They often
# assume that only local usersmynetwork can access them at "localhost" ports.
http_access deny to_localhost

# Protect cloud servers that provide local users with sensitive info about
# their server via certain well-known link-local (a.k.a. APIPA) addresses.
http_access deny to_linklocal

# For example, to allow access from your local networks, you may uncomment the
# following rule (and/or add rules that match your definition of "local"):
http_access allow localnet

# And finally deny all other access to this proxy
http_access deny all

# Squid normally listens to port 3128
http_port 3128
mynetwork
# Uncomment and adjust the following to add a disk cache directory.
cache_dir ufs /var/spool/squid 100 16 256

# Leave coredumps in the first cache dir
coredump_dir /var/spool/squid

#
# Add any of your own refresh_pattern entries above these.
#
refresh_pattern ^ftp:  1440 20% 10080
refresh_pattern -i (/cgi-bin/|\?) 0 0% 0
refresh_pattern .  0 20% 4320
```

##### Configuration Nginx Proxy Inverse

###### nginx.conf

```nginxconf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log notice;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '

                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    include sites-enabled/*.conf;

}
```

###### proxy_params

```nginxconf
proxy_set_header Host $http_host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

## TP 4 - NAT et filtrage
