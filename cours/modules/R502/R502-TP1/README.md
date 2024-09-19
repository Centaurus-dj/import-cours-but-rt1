# R502-TP1 - SNMP

## 1 - Installation du client SNMP et test sur un serveur containérisé Linux

  ```sh
  docker run -it registry.iutbeziers.fr/debianiut:latest bash
  apt-get update
  apt-get install snmp snmpd snmp-mibs-downloader
  ```

  > [!NOTE]
  > La container debian n'a pas par défaut les paquets `non-free` alors que le paquet
  > `snmp-mibs-downloader` est un paquet résidant dans le dépôt `non-free`, il faut alors activer
  > ce dépôt dans les sources APT.
  >
  > Voir le fichier de sources [ici](./src/debian.sources).

  - Voir le fichier de configuration SNMP (/etc/snmp/snmp.conf), [ici](./src/snmp.conf).

  > [!CAUTION]
  > Les services SNMPD ont du mal à être kill par eux-même, toujours vérifier les process actifs
  > lorsque l'on a une erreur du type: `Error opening specified endpoint`.
  >
  > ```sh
  > ps aux | grep snmp
  > ```

## 2 - Interrogation d’un serveur Linux via SNMP

- Lancement d'un container SNMP via la commande suivante:

  ```sh
  docker run --rm -p 161:161/udp -p 162:162/udp -d \
    --hostname snmpserver -it registry.iutbeziers.fr/snmpiut:latest
  ```

- On fait:

  ```sh
  snmpwalk -v2c -c publicbeziers 172.17.0.3 system
  ```

  ce qui nous donne:

  ```txt
  SNMPv2-MIB::sysDescr.0 = STRING: Linux snmpserver 6.1.0-25-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.106-3 (2024-08-26) x86_64
  SNMPv2-MIB::sysObjectID.0 = OID: NET-SNMP-TC::linux
  DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (263234) 0:43:52.34
  SNMPv2-MIB::sysContact.0 = STRING: pouchou <pouchou@iutbeziers.fr>
  SNMPv2-MIB::sysName.0 = STRING: snmpserver
  SNMPv2-MIB::sysLocation.0 = STRING: quelpart dans un container
  SNMPv2-MIB::sysServices.0 = INTEGER: 72
  SNMPv2-MIB::sysORLastChange.0 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORID.1 = OID: SNMP-MPD-MIB::snmpMPDCompliance
  SNMPv2-MIB::sysORID.2 = OID: SNMP-USER-BASED-SM-MIB::usmMIBCompliance
  SNMPv2-MIB::sysORID.3 = OID: SNMP-FRAMEWORK-MIB::snmpFrameworkMIBCompliance
  SNMPv2-MIB::sysORID.4 = OID: SNMPv2-MIB::snmpMIB
  SNMPv2-MIB::sysORID.5 = OID: SNMP-VIEW-BASED-ACM-MIB::vacmBasicGroup
  SNMPv2-MIB::sysORID.6 = OID: TCP-MIB::tcpMIB
  SNMPv2-MIB::sysORID.7 = OID: IP-MIB::ip
  SNMPv2-MIB::sysORID.8 = OID: UDP-MIB::udpMIB
  SNMPv2-MIB::sysORID.9 = OID: SNMP-NOTIFICATION-MIB::snmpNotifyFullCompliance
  SNMPv2-MIB::sysORID.10 = OID: NOTIFICATION-LOG-MIB::notificationLogMIB
  SNMPv2-MIB::sysORDescr.1 = STRING: The MIB for Message Processing and Dispatching.
  SNMPv2-MIB::sysORDescr.2 = STRING: The management information definitions for the SNMP User-based Security Model.
  SNMPv2-MIB::sysORDescr.3 = STRING: The SNMP Management Architecture MIB.
  SNMPv2-MIB::sysORDescr.4 = STRING: The MIB module for SNMPv2 entities
  SNMPv2-MIB::sysORDescr.5 = STRING: View-based Access Control Model for SNMP.
  SNMPv2-MIB::sysORDescr.6 = STRING: The MIB module for managing TCP implementations
  SNMPv2-MIB::sysORDescr.7 = STRING: The MIB module for managing IP and ICMP implementations
  SNMPv2-MIB::sysORDescr.8 = STRING: The MIB module for managing UDP implementations
  SNMPv2-MIB::sysORDescr.9 = STRING: The MIB modules for managing SNMP Notification, plus filtering.
  SNMPv2-MIB::sysORDescr.10 = STRING: The MIB module for logging SNMP Notifications.
  SNMPv2-MIB::sysORUpTime.1 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.2 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.3 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.4 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.5 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.6 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.7 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.8 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.9 = Timeticks: (0) 0:00:00.00
  SNMPv2-MIB::sysORUpTime.10 = Timeticks: (0) 0:00:00.00
  ```

  - La mémoire totale de la machine.

    ```sh
    snmpwalk -v2c -c publicbeziers 172.17.0.3 memory
    ```

    nous donne:

    ```sh
    UCD-SNMP-MIB::memIndex.0 = INTEGER: 0
    UCD-SNMP-MIB::memErrorName.0 = STRING: swap
    UCD-SNMP-MIB::memTotalSwap.0 = INTEGER: 999420 kB
    UCD-SNMP-MIB::memAvailSwap.0 = INTEGER: 999420 kB
    UCD-SNMP-MIB::memTotalReal.0 = INTEGER: 32596892 kB
    UCD-SNMP-MIB::memAvailReal.0 = INTEGER: 20998096 kB
    UCD-SNMP-MIB::memTotalFree.0 = INTEGER: 21997516 kB
    UCD-SNMP-MIB::memMinimumSwap.0 = INTEGER: 16000 kB
    UCD-SNMP-MIB::memShared.0 = INTEGER: 931620 kB
    UCD-SNMP-MIB::memBuffer.0 = INTEGER: 153428 kB
    UCD-SNMP-MIB::memCached.0 = INTEGER: 5232256 kB
    UCD-SNMP-MIB::memSwapError.0 = INTEGER: noError(0)
    UCD-SNMP-MIB::memSwapErrorMsg.0 = STRING: 
    ```

    La valeur de

    ```txt
    UCD-SNMP-MIB::memTotalReal.0 = INTEGER: 32596892 kB
    ```

    nous donne la valeur totale de la mémoire disponible.

  - L’uptime de la machine

    ```sh
    snmpwalk -v2c -c publicbeziers 172.17.0.3 sysuptime
    ```

    nous donne:

    ```sh
    DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (298622) 0:49:46.22
    ```

  - Le nombre de process de la machine

    ```sh
    snmpwalk -v2c -c publicbeziers 172.17.0.3 hrSystemProcesses
    ```

    nous donne:

    ```sh
    HOST-RESOURCES-MIB::hrSystemProcesses.0 = Gauge32: 3
    ```

  - L’espace de stockage utilisée sur la machine

    ```sh
    snmpwalk -v2c -c publicbeziers 172.17.0.3 hrStorageUsed
    ```

    nous donne:

    ```sh
    HOST-RESOURCES-MIB::hrStorageUsed.1 = INTEGER: 11702368
    HOST-RESOURCES-MIB::hrStorageUsed.3 = INTEGER: 11702368
    HOST-RESOURCES-MIB::hrStorageUsed.6 = INTEGER: 155168
    HOST-RESOURCES-MIB::hrStorageUsed.7 = INTEGER: 5249284
    HOST-RESOURCES-MIB::hrStorageUsed.8 = INTEGER: 946184
    HOST-RESOURCES-MIB::hrStorageUsed.10 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.34 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.39 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.40 = INTEGER: 5604898
    HOST-RESOURCES-MIB::hrStorageUsed.41 = INTEGER: 5604898
    HOST-RESOURCES-MIB::hrStorageUsed.42 = INTEGER: 5604898
    HOST-RESOURCES-MIB::hrStorageUsed.49 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.50 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.51 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.52 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.53 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.54 = INTEGER: 0
    HOST-RESOURCES-MIB::hrStorageUsed.55 = INTEGER: 0
    ```

  - La taille d’une unité d’allocation de stockage

    ```sh
    snmpwalk -v2c -c publicbeziers 172.17.0.3 hrStorageAllocationUnits
    ```

    nous donne:

    ```sh
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.1 = INTEGER: 1024 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.3 = INTEGER: 1024 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.6 = INTEGER: 1024 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.7 = INTEGER: 1024 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.8 = INTEGER: 1024 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.10 = INTEGER: 1024 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.34 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.39 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.40 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.41 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.42 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.49 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.50 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.51 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.52 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.53 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.54 = INTEGER: 4096 Bytes
    HOST-RESOURCES-MIB::hrStorageAllocationUnits.55 = INTEGER: 4096 Bytes
    ```

  > [!NOTE]
  > Les MIBS sont disponibles à ces addresses suivantes:
  >
  > - [cric.grenoble.cnrs.fr](https://cric.grenoble.cnrs.fr/Administrateurs/Outils/MIBS/?module=UCD-SNMP-MIB&fournisseur=netsnmp)
  > - [cric.grenoble.cnrs.fr](https://cric.grenoble.cnrs.fr/Administrateurs/Outils/MIBS/?module=HOST-RESOURCES-MIB&fournisseur=CISCO)

- On fait

  ```sh
  snmptable -v 2c -c publicbeziers -Os 172.17.0.3 <tableID>
  ```

  - la table des interfaces réseaux

    On fait

    ```sh
    snmptable -v 2c -c publicbeziers -Os 172.17.0.3 -Ci -Cb ifTable
    ```

    ce qui nous donne:

    ```
    SNMP table: ifTable

    index Index Descr             Type   Mtu      Speed    PhysAddress AdminStatus OperStatus   LastChange InOctets InUcastPkts InNUcastPkts InDiscards InErrors InUnknownProtos OutOctets OutUcastPkts OutNUcastPkts OutDiscards OutErrors OutQLen    Specific
        1     1    lo softwareLoopback 65536   10000000                         up         up 0:0:00:00.00     1712           8            0          0        0               0      1712            8             0           0         0       0 zeroDotZero
        7     7  eth0   ethernetCsmacd  1500 4294967295 2:42:ac:11:0:3          up         up 0:0:00:00.00    43712         471            0          0        0               0     46390          432             0           0         0       0 zeroDotZero
    ```

    > [!NOTE]
    > La MIB est disponible à l'adresse suivante: [cric.grenoble.cnrs.fr](https://cric.grenoble.cnrs.fr/Administrateurs/Outils/MIBS/?module=IF-MIB&fournisseur=ietf)


  - la table des partitions

    On fait

    ```sh
    snmptable -v 2c -c publicbeziers -Os 172.17.0.3 -Ci -Cb diskIOTable
    ```

    ce qui nous donne:

    ```
    SNMP table: diskIOTable

    index Index    Device      NRead   NWritten Reads Writes LA1 LA5 LA15     NReadX  NWrittenX BusyTime
        1     1   nvme0n1 2229510144 4105589760 39694  63787   0   0    0 2229510144 4105589760        ?
        2     2 nvme0n1p1    8436736       1024   266      2   0   0    0    8436736       1024        ?
        3     3 nvme0n1p2 2182534144 4105588736 37885  63773   0   0    0 2182534144 4105588736        ?
        4     4 nvme0n1p3    3538944          0    97      0   0   0    0    3538944          0        ?
        5     5 nvme0n1p4    1028096          0    70      0   0   0    0    1028096          0        ?
        6     6 nvme0n1p5    3338240          0    88      0   0   0    0    3338240          0        ?
        7     7 nvme0n1p6    3338240          0    88      0   0   0    0    3338240          0        ?
        8     8     loop0          0          0     0      0   0   0    0          0          0        ?
        9     9     loop1          0          0     0      0   0   0    0          0          0        ?
        10    10     loop2          0          0     0      0   0   0    0          0          0        ?
        11    11     loop3          0          0     0      0   0   0    0          0          0        ?
        12    12     loop4          0          0     0      0   0   0    0          0          0        ?
        13    13     loop5          0          0     0      0   0   0    0          0          0        ?
        14    14     loop6          0          0     0      0   0   0    0          0          0        ?
        15    15     loop7          0          0     0      0   0   0    0          0          0        ?
    ```

    > [!NOTE]
    > La MIB est disponible à l'adresse suivante: [cric.grenoble.cnrs.fr](https://cric.grenoble.cnrs.fr/Administrateurs/Outils/MIBS/?module=UCD-DISKIO-MIB)

  - la table des loadaverage

    On fait

    ```sh
    snmptable -v 2c -c publicbeziers -Os 172.17.0.3 -Ci -Cb laTable
    ```

    ce qui nous donne:

    ```
    SNMP table: laTable

    index Index   Names Load Config LoadInt LoadFloat ErrorFlag ErrMessage
        1     1  Load-1 0.54  12.00      54  0.540000   noError           
        2     2  Load-5 0.40  10.00      40  0.400000   noError           
        3     3 Load-15 0.38   5.00      38  0.380000   noError           
    ```

    > [!NOTE]
    > La MIB est disponible à l'adresse suivante: [docs.redhat.com](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/sect-system_monitoring_tools-net-snmp-retrieving#sect-System_Monitoring_Tools-Net-SNMP-Retrieving-CPU)

  - la table des IO

    On fait

    ```sh
    snmptable -v 2c -c publicbeziers -Os 172.17.0.3 -Ci -Cb diskIOTable
    ```

    ce qui nous donne:

    ```
    SNMP table: diskIOTable

    index Index    Device      NRead   NWritten Reads Writes LA1 LA5 LA15     NReadX  NWrittenX BusyTime
        1     1   nvme0n1 2229510144 4105589760 39694  63787   0   0    0 2229510144 4105589760        ?
        2     2 nvme0n1p1    8436736       1024   266      2   0   0    0    8436736       1024        ?
        3     3 nvme0n1p2 2182534144 4105588736 37885  63773   0   0    0 2182534144 4105588736        ?
        4     4 nvme0n1p3    3538944          0    97      0   0   0    0    3538944          0        ?
        5     5 nvme0n1p4    1028096          0    70      0   0   0    0    1028096          0        ?
        6     6 nvme0n1p5    3338240          0    88      0   0   0    0    3338240          0        ?
        7     7 nvme0n1p6    3338240          0    88      0   0   0    0    3338240          0        ?
        8     8     loop0          0          0     0      0   0   0    0          0          0        ?
        9     9     loop1          0          0     0      0   0   0    0          0          0        ?
        10    10     loop2          0          0     0      0   0   0    0          0          0        ?
        11    11     loop3          0          0     0      0   0   0    0          0          0        ?
        12    12     loop4          0          0     0      0   0   0    0          0          0        ?
        13    13     loop5          0          0     0      0   0   0    0          0          0        ?
        14    14     loop6          0          0     0      0   0   0    0          0          0        ?
        15    15     loop7          0          0     0      0   0   0    0          0          0        ?
    ```

    > [!NOTE]
    > On peut aussi utiliser l'OID SNMP `hrPartitionTable` mais dans ce cas, aucune entrée n'était présente.

    > [!NOTE]
    > La MIB est disponible à l'adresse suivante: [cric.grenoble.cnrs.fr](https://cric.grenoble.cnrs.fr/Administrateurs/Outils/MIBS/?module=UCD-DISKIO-MIB)

## 3 - Installation d’un serveur SNMP sous Linux

On installe un serveur apache sous linux.


après avoir lancé la commande suivante:

```sh
ab -c 100 -n 100000 http://localhost/
```

qui nous donne:

```sh
This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        Apache/2.4.62
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        10701 bytes

Concurrency Level:      100
Time taken for tests:   3.205 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      1097500000 bytes
HTML transferred:       1070100000 bytes
Requests per second:    31203.57 [#/sec] (mean)
Time per request:       3.205 [ms] (mean)
Time per request:       0.032 [ms] (mean, across all concurrent requests)
Transfer rate:          334432.74 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.2      1       2
Processing:     1    2   1.7      2      56
Waiting:        0    1   1.7      1      55
Total:          2    3   1.7      3      57

Percentage of the requests served within a certain time (ms)
  50%      3
  66%      3
  75%      3
  80%      3
  90%      3
  95%      4
  98%      4
  99%      4
 100%     57 (longest request)
```

on fait la commande suivante:

```sh
snmpwalk localhost -v2c -c publicbeziers UCD-SNMP-MIB::prTable
```

ce qui nous donne:

```sh
UCD-SNMP-MIB::prIndex.1 = INTEGER: 1
UCD-SNMP-MIB::prNames.1 = STRING: apache2
UCD-SNMP-MIB::prMin.1 = INTEGER: 1
UCD-SNMP-MIB::prMax.1 = INTEGER: 0
UCD-SNMP-MIB::prCount.1 = INTEGER: 3
UCD-SNMP-MIB::prErrorFlag.1 = INTEGER: noError(0)
UCD-SNMP-MIB::prErrMessage.1 = STRING: 
UCD-SNMP-MIB::prErrFix.1 = INTEGER: noError(0)
UCD-SNMP-MIB::prErrFixCmd.1 = STRING: 
```

## 4 - Configurer SNMP sur les switchs CISCO

