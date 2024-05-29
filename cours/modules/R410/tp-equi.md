---
Author:
  - Alexis Opolka
  - Thibault Garcia
Subject: R411 - Équilibrage de charge
Company: IUT de Béziers
Copyright: All Rights Reserved
---

# R411 - Équilibrage de charge

## Glossaire des termes

| Terme | Définition           |
| ----- | -------------------- |
| VIP   | Virtual IP Address   |
| RIP   | Real IP Address      |
| LVS   | Linux Virtual Server |

1. ## LVS en mode NAT

     ![LVS NAT](./src/tp-equi/img/schema_LVS.drawio.svg)

     1. ### Configuration du LVS

        1. #### Configuration de ipvsadm

            ```sh
            echo "
            ipvsadm -C
            ipvsadm -A -t <ip>:<port> -s rr
            ipvsadm -a -t <ip>:<port> -r <ip>:<port> -m
            ipvsadm -a -t <ip>:<port> -r <ip>:<port> -m
            " | ipvsadm -R
            ```

            Ce qui nous donnerait:

            ```sh
            echo "
            ipvsadm -C
            ipvsadm -A -t 10.202.100.200:80 -s rr
            ipvsadm -a -t 10.202.100.200:80 -r 192.168.200.1:80 -m
            ipvsadm -a -t 10.202.100.200:80 -r 192.168.200.2:80 -m
            " | ipvsadm -R
            ```

            où:

            - `-C`: Pour nettoyer des règles, si déjà présentes
            - `-A`: Pour ajouter une nouvelle VIP
            - `-s`: Pour définir le type de scheduling
            - `-a`: Pour append au VIP déjà créé
            - `-r`: Pour ajouter un RIP au VIP
            - `-m`: Pour faire du NAT (i.e. `masquerading`)
            - `-R`: Pour passer d'une chaine sous forme de liste et traiter chaque ligne comme étant une commande `ipvsadm`.

            > [!NOTE]
            > Pour plus d'informations, voir le manpage [ipvsadm](https://manpages.org/ipvsadm/0).

            Il nous faudra ensuite ajouter l'IP sur notre interface publique:

            ```sh
            ip a add 10.202.100.200/16 dev eth0
            ```

            Nos résultats avec:

            - `httpie`:

              > [!NOTE]
              > La commande:
              >
              > ```sh
              > http -h 10.202.100.200
              > ```

              ```sh
              HTTP/1.1 200 OK
              Connection: keep-alive
              Content-Encoding: gzip
              Content-Type: text/html
              Date: Tue, 28 May 2024 08:45:28 GMT
              ETag: W/"665588d5-267"
              Last-Modified: Tue, 28 May 2024 07:33:41 GMT
              Server: nginx/1.26.0
              Transfer-Encoding: chunked
              ```

              ```sh
              HTTP/1.1 200 OK
              Accept-Ranges: bytes
              Connection: Keep-Alive
              Content-Encoding: gzip
              Content-Length: 3121
              Content-Type: text/html
              Date: Tue, 28 May 2024 08:45:41 GMT
              ETag: "29af-6197e9eaed8d7-gzip"
              Keep-Alive: timeout=5, max=100
              Last-Modified: Tue, 28 May 2024 07:31:19 GMT
              Server: Apache/2.4.52 (Ubuntu)
              Vary: Accept-Encoding
              ```

            - `Apache Benchmark`

              > [!NOTE]
              > La commande:
              >
              > ```sh
              > ab -c -n 150 http://10.202.100.200:80/
              > ```

              ```sh
              This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
              Copyright 1996 Adam Twiss, Zeus Technology Ltd, <http://www.zeustech.net/>
              Licensed to The Apache Software Foundation, <http://www.apache.org/>

              Benchmarking 10.202.100.200 (be patient).....done

              Server Software:        Apache/2.4.52
              Server Hostname:        10.202.100.200
              Server Port:            80

              Document Path:          /
              Document Length:        10671 bytes

              Concurrency Level:      2
              Time taken for tests:   0.277 seconds
              Complete requests:      150
              Failed requests:        75
                (Connect: 0, Receive: 0, Length: 75, Exceptions: 0)
              Total transferred:      884475 bytes
              HTML transferred:       846450 bytes
              Requests per second:    542.41 [#/sec] (mean)
              Time per request:       3.687 [ms] (mean)
              Time per request:       1.844 [ms] (mean, across all concurrent requests)
              Transfer rate:          3123.34 [Kbytes/sec] received

              Connection Times (ms)
                            min  mean[+/-sd] median   max
              Connect:        1    1   0.4      1       4
              Processing:     1    2   0.7      2       4
              Waiting:        1    2   0.4      2       3
              Total:          2    4   1.0      4       7

              Percentage of the requests served within a certain time (ms)
                50%      4
                66%      4
                75%      4
                80%      4
                90%      5
                95%      5
                98%      6
                99%      7
              100%      7 (longest request)
              ```

              ```sh
              This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
              Copyright 1996 Adam Twiss, Zeus Technology Ltd, <http://www.zeustech.net/>
              Licensed to The Apache Software Foundation, <http://www.apache.org/>

              Benchmarking 10.202.100.200 (be patient).....done

              Server Software:        nginx/1.26.0
              Server Hostname:        10.202.100.200
              Server Port:            80

              Document Path:          /
              Document Length:        615 bytes

              Concurrency Level:      2
              Time taken for tests:   0.261 seconds
              Complete requests:      150
              Failed requests:        75
                (Connect: 0, Receive: 0, Length: 75, Exceptions: 0)
              Total transferred:      884475 bytes
              HTML transferred:       846450 bytes
              Requests per second:    575.77 [#/sec] (mean)
              Time per request:       3.474 [ms] (mean)
              Time per request:       1.737 [ms] (mean, across all concurrent requests)
              Transfer rate:          3315.44 [Kbytes/sec] received

              Connection Times (ms)
                            min  mean[+/-sd] median   max
              Connect:        0    1   0.4      1       3
              Processing:     1    2   0.7      2       5
              Waiting:        1    2   0.5      2       5
              Total:          2    3   0.9      3       6

              Percentage of the requests served within a certain time (ms)
                50%      3
                66%      3
                75%      4
                80%      4
                90%      5
                95%      5
                98%      6
                99%      6
              100%      6 (longest request)
              ```

1. ## LVS en mode Direct-Routing

    1. ### Configuration du LVS

        > [!NOTE]
        > On nettoie d'abord les règles LVS avec:
        >
        > ```sh
        > ipvsadm -C
        > ```

        ```sh
        ipvsadm -A -t 10.10.200.200:80 -s rr
        ipvsadm -a -t 10.10.200.200:80 -r 10.10.100.16:80
        ipvsadm -a -t 10.10.200.200:80 -r 10.10.100.18:80
        ```

    1. ### Configuration des RIP

        ```sh
        echo "0" >/proc/sys/net/ipv4/ip_forward
        echo "1" >/proc/sys/net/ipv4/conf/all/arp_ignore
        echo "2" >/proc/sys/net/ipv4/conf/all/arp_announce
        echo "1" >/proc/sys/net/ipv4/conf/default/arp_ignore
        echo "2" >/proc/sys/net/ipv4/conf/default/arp_announce
        echo "1" >/proc/sys/net/ipv4/conf/lo/arp_ignore
        echo "2" >/proc/sys/net/ipv4/conf/lo/arp_announce
        echo "1" >/proc/sys/net/ipv4/conf/eth0/arp_ignore
        echo "2" >/proc/sys/net/ipv4/conf/eth0/arp_announce
        ```

        Dans `/etc/sysctl.conf`:

        ```sh
        net.ipv4.conf.lo.arp_ignore = 1
        net.ipv4.conf.lo.arp_announce = 2
        ```

  <!-- sudo virt-install --name apache-fedora --memory 4096 --cpu host --vcpus 4 --graphics none --os-variant fedora40 --import --disk /home/centaurus/Documents/iso/Fedora-Cloud-Base-39-1.5.x86_64.qcow2,format=qcow2,bus=virtio --cloud-init -->
