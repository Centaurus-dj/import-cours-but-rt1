#### 4 Configurer SNMP sur les switchs CISCO

Afin de récupérer les informations sur le switch, nous exécutons la commande suivante :

```bash
snmpwalk -v 2c -c public 192.168.1.254 -m IF-MIB
```

Nous pouvons filtrer pour récupérer les informations essentielles :

```bash
snmpwalk -v 2c -c public 192.168.1.254 -m IF-MIB | egrep "ifDescr|ifType|ifMtu|ifSpeed|ifPhysAddress
```

Nous obtenons les informations suivantes :

```bash
root@57bf1abe4f10:/# snmpwalk -v 2c -c public 192.168.1.254 -m IF-MIB | egrep "ifDescr|ifType|ifMtu|ifSpeed|ifPhysAddress"
IF-MIB::ifDescr.1 = STRING: GigabitEthernet1
IF-MIB::ifDescr.2 = STRING: GigabitEthernet2
IF-MIB::ifDescr.3 = STRING: GigabitEthernet3
IF-MIB::ifDescr.4 = STRING: GigabitEthernet4
IF-MIB::ifDescr.5 = STRING: GigabitEthernet5
IF-MIB::ifDescr.6 = STRING: GigabitEthernet6
IF-MIB::ifDescr.7 = STRING: GigabitEthernet7
IF-MIB::ifDescr.8 = STRING: GigabitEthernet8
IF-MIB::ifDescr.1000 = STRING: Port-Channel1
IF-MIB::ifDescr.1001 = STRING: Port-Channel2
IF-MIB::ifDescr.1002 = STRING: Port-Channel3
IF-MIB::ifDescr.1003 = STRING: Port-Channel4
IF-MIB::ifDescr.3000 = STRING: tunnel1
IF-MIB::ifDescr.7000 = STRING: loopback1
IF-MIB::ifDescr.8000 = STRING: User Defined Port 1
IF-MIB::ifDescr.9000 = STRING: stack-port
IF-MIB::ifDescr.20000 = STRING: Logical-int 1
IF-MIB::ifDescr.100000 = STRING: 1
IF-MIB::ifType.1 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.2 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.3 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.4 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.5 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.6 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.7 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.8 = INTEGER: ethernetCsmacd(6)
IF-MIB::ifType.1000 = INTEGER: ieee8023adLag(161)
IF-MIB::ifType.1001 = INTEGER: ieee8023adLag(161)
IF-MIB::ifType.1002 = INTEGER: ieee8023adLag(161)
IF-MIB::ifType.1003 = INTEGER: ieee8023adLag(161)
IF-MIB::ifType.3000 = INTEGER: tunnel(131)
IF-MIB::ifType.7000 = INTEGER: softwareLoopback(24)
IF-MIB::ifType.8000 = INTEGER: propPointToPointSerial(22)
IF-MIB::ifType.9000 = INTEGER: propVirtual(53)
IF-MIB::ifType.20000 = INTEGER: propPointToPointSerial(22)
IF-MIB::ifType.100000 = INTEGER: propVirtual(53)
IF-MIB::ifMtu.1 = INTEGER: 1500
IF-MIB::ifMtu.2 = INTEGER: 1500
IF-MIB::ifMtu.3 = INTEGER: 1500
IF-MIB::ifMtu.4 = INTEGER: 1500
IF-MIB::ifMtu.5 = INTEGER: 1500
IF-MIB::ifMtu.6 = INTEGER: 1500
IF-MIB::ifMtu.7 = INTEGER: 1500
IF-MIB::ifMtu.8 = INTEGER: 1500
IF-MIB::ifMtu.1000 = INTEGER: 1500
IF-MIB::ifMtu.1001 = INTEGER: 1500
IF-MIB::ifMtu.1002 = INTEGER: 1500
IF-MIB::ifMtu.1003 = INTEGER: 1500
IF-MIB::ifMtu.3000 = INTEGER: 1500
IF-MIB::ifMtu.7000 = INTEGER: 1500
IF-MIB::ifMtu.8000 = INTEGER: 1500
IF-MIB::ifMtu.9000 = INTEGER: 1500
IF-MIB::ifMtu.20000 = INTEGER: 1500
IF-MIB::ifMtu.100000 = INTEGER: 1500
IF-MIB::ifSpeed.1 = Gauge32: 1000
IF-MIB::ifSpeed.2 = Gauge32: 1000
IF-MIB::ifSpeed.3 = Gauge32: 1000
IF-MIB::ifSpeed.4 = Gauge32: 1000
IF-MIB::ifSpeed.5 = Gauge32: 1000
IF-MIB::ifSpeed.6 = Gauge32: 1000
IF-MIB::ifSpeed.7 = Gauge32: 1000
IF-MIB::ifSpeed.8 = Gauge32: 1000
IF-MIB::ifSpeed.1000 = Gauge32: 0
IF-MIB::ifSpeed.1001 = Gauge32: 0
IF-MIB::ifSpeed.1002 = Gauge32: 0
IF-MIB::ifSpeed.1003 = Gauge32: 0
IF-MIB::ifSpeed.3000 = Gauge32: 0
IF-MIB::ifSpeed.7000 = Gauge32: 100000000
IF-MIB::ifSpeed.8000 = Gauge32: 0
IF-MIB::ifSpeed.9000 = Gauge32: 0
IF-MIB::ifSpeed.20000 = Gauge32: 0
IF-MIB::ifSpeed.100000 = Gauge32: 0
IF-MIB::ifPhysAddress.1 = STRING: 3c:57:31:d6:c5:e
IF-MIB::ifPhysAddress.2 = STRING: 3c:57:31:d6:c5:f
IF-MIB::ifPhysAddress.3 = STRING: 3c:57:31:d6:c5:10
IF-MIB::ifPhysAddress.4 = STRING: 3c:57:31:d6:c5:11
IF-MIB::ifPhysAddress.5 = STRING: 3c:57:31:d6:c5:12
IF-MIB::ifPhysAddress.6 = STRING: 3c:57:31:d6:c5:13
IF-MIB::ifPhysAddress.7 = STRING: 3c:57:31:d6:c5:14
IF-MIB::ifPhysAddress.8 = STRING: 3c:57:31:d6:c5:15
IF-MIB::ifPhysAddress.1000 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.1001 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.1002 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.1003 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.3000 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.7000 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.8000 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.9000 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.20000 = STRING: 3c:57:31:d6:c5:d
IF-MIB::ifPhysAddress.100000 = STRING: 3c:57:31:d6:c5:d
```