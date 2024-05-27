---
Author: Alexis Opolka
Subject: Nushell
Company: IUT de Béziers
Copyright: All Rights Reserved
---

# R405 - TP Nushell

Nous avons d'abord fait:

```sh
jq -s "." eve2.json | save -f eve-formatted.json
```

Puis nous pouvons faire:

```sh
open eve-formatted.json |flatten --all |default "N/A" src_ip |default "N/A" src_port \
|default "N/A" dest_ip |default "N/A" dest_port |default "N/A" proto |default "N/A" state \
|default "N/A" alerted |default "N/A" reason |default "N/A" event_type |default "N/A" signature \
|select src_ip src_port dest_ip dest_port proto state alerted reason event_type signature \
|where event_type =~ alert | to json | save -f eve-alerts.json
```

Nous pouvons ensuite travailler dessus:

- Avoir toutes les signature avec le terme `MALWARE`:

    ```sh
    open eve-alerts.json |uniq -c | where value.signature =~ "MALWARE"  
    ```

    Ce qui nous donne:

    ```txt
    ╭───┬─────────────────────────────────────────────────────────────────────────────┬───────╮
    │ # │                                    value                                    │ count │
    ├───┼─────────────────────────────────────────────────────────────────────────────┼───────┤
    │ 0 │ ╭────────────┬────────────────────────────────────────────────────────────╮ │     8 │
    │   │ │ src_ip     │ 200.51.43.5                                                │ │       │
    │   │ │ src_port   │ 53                                                         │ │       │
    │   │ │ dest_ip    │ 192.168.1.247                                              │ │       │
    │   │ │ dest_port  │ 3440                                                       │ │       │
    │   │ │ proto      │ UDP                                                        │ │       │
    │   │ │ state      │ N/A                                                        │ │       │
    │   │ │ alerted    │ N/A                                                        │ │       │
    │   │ │ reason     │ N/A                                                        │ │       │
    │   │ │ event_type │ alert                                                      │ │       │
    │   │ │ signature  │ ET MALWARE DNS Reply Sinkhole - Microsoft - 199.2.137.0/24 │ │       │
    │   │ ╰────────────┴────────────────────────────────────────────────────────────╯ │       │
    │ 1 │ ╭────────────┬────────────────────────────────────────────────────────────╮ │     3 │
    │   │ │ src_ip     │ 200.51.43.5                                                │ │       │
    │   │ │ src_port   │ 53                                                         │ │       │
    │   │ │ dest_ip    │ 192.168.1.247                                              │ │       │
    │   │ │ dest_port  │ 2898                                                       │ │       │
    │   │ │ proto      │ UDP                                                        │ │       │
    │   │ │ state      │ N/A                                                        │ │       │
    │   │ │ alerted    │ N/A                                                        │ │       │
    │   │ │ reason     │ N/A                                                        │ │       │
    │   │ │ event_type │ alert                                                      │ │       │
    │   │ │ signature  │ ET MALWARE DNS Reply Sinkhole - Microsoft - 199.2.137.0/24 │ │       │
    │   │ ╰────────────┴────────────────────────────────────────────────────────────╯ │       │
    │ 2 │ ╭────────────┬────────────────────────────────────────────────────────────╮ │     4 │
    │   │ │ src_ip     │ 200.51.43.5                                                │ │       │
    │   │ │ src_port   │ 53                                                         │ │       │
    │   │ │ dest_ip    │ 192.168.1.247                                              │ │       │
    │   │ │ dest_port  │ 2901                                                       │ │       │
    │   │ │ proto      │ UDP                                                        │ │       │
    │   │ │ state      │ N/A                                                        │ │       │
    │   │ │ alerted    │ N/A                                                        │ │       │
    │   │ │ reason     │ N/A                                                        │ │       │
    │   │ │ event_type │ alert                                                      │ │       │
    │   │ │ signature  │ ET MALWARE DNS Reply Sinkhole - Microsoft - 199.2.137.0/24 │ │       │
    │   │ ╰────────────┴────────────────────────────────────────────────────────────╯ │       │
    │ 3 │ ╭────────────┬────────────────────────────────────────────────────────────╮ │     5 │
    │   │ │ src_ip     │ 200.51.43.5                                                │ │       │
    │   │ │ src_port   │ 53                                                         │ │       │
    │   │ │ dest_ip    │ 192.168.1.247                                              │ │       │
    │   │ │ dest_port  │ 1107                                                       │ │       │
    │   │ │ proto      │ UDP                                                        │ │       │
    │   │ │ state      │ N/A                                                        │ │       │
    │   │ │ alerted    │ N/A                                                        │ │       │
    │   │ │ reason     │ N/A                                                        │ │       │
    │   │ │ event_type │ alert                                                      │ │       │
    │   │ │ signature  │ ET MALWARE DNS Reply Sinkhole - Microsoft - 199.2.137.0/24 │ │       │
    │   │ ╰────────────┴────────────────────────────────────────────────────────────╯ │       │
    │ 4 │ ╭────────────┬────────────────────────────────────────────────────────────╮ │     6 │
    │   │ │ src_ip     │ 200.51.43.5                                                │ │       │
    │   │ │ src_port   │ 53                                                         │ │       │
    │   │ │ dest_ip    │ 192.168.1.247                                              │ │       │
    │   │ │ dest_port  │ 2900                                                       │ │       │
    │   │ │ proto      │ UDP                                                        │ │       │
    │   │ │ state      │ N/A                                                        │ │       │
    │   │ │ alerted    │ N/A                                                        │ │       │
    │   │ │ reason     │ N/A                                                        │ │       │
    │   │ │ event_type │ alert                                                      │ │       │
    │   │ │ signature  │ ET MALWARE DNS Reply Sinkhole - Microsoft - 199.2.137.0/24 │ │       │
    │   │ ╰────────────┴────────────────────────────────────────────────────────────╯ │       │
    ╰───┴─────────────────────────────────────────────────────────────────────────────┴───────╯

    ```

- On peut déterminer le nombre de fois que les IP concernées ont été flag:

  ```sh
  open eve-alerts.json |uniq -c | where value.signature =~ "MALWARE" | get value.src_ip | uniq -c
  ```

  ce qui nous donne:

  ```txt
  ╭───┬──────────────┬───────╮
  │ # │    value     │ count │
  ├───┼──────────────┼───────┤
  │ 0 │ 200.51.43.5  │   100 │
  │ 1 │ 192.168.1.52 │     1 │
  ╰───┴──────────────┴───────╯
  ```
