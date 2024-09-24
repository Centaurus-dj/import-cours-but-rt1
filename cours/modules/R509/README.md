# R509 - DevOps

## Kerberos

> A secure, SSO, Trusted third party mutual authentification service.

Kerberos: L'utilisateur et sa machine

- Secure
- SSO
- Trusted Third Party

KDC: `Key Distribution Center`

TGT: `Ticket Granted Ticket`

## IPS et IDS

Détection par:

- Scénarios (IDS[^1] vs IPS[^2])
- Comportement
  - EDR (Antivirus par comportement)

[^1]: Intrusion Detection System
[^2]: Intrusion Prevention System

Threat Hunting:

- Sniffers: Wireshark, tcpdump
- Collecteur & aggrégateurs NetFlow: nfsen, nfpcap

WAF: Web Application Firewall

Applications:

- SNORT
- SURICATA
- ZEEK
- ZUI


SIEM = SIM[^3] + SEM[^4]

[^3]: Security Information Management
[^4]: Security Event Management

Wazuh: un HIPS et un [SOAR](https://www.google.com/search?q=soar+it+meaning&client=firefox-b-e&sca_esv=eeaa99d7703dda14&sca_upv=1&ei=amTyZpbZHrmokdUP-ZeB4AM&ved=0ahUKEwiWtujlgduIAxU5VKQEHflLADwQ4dUDCA8&uact=5&oq=soar+it+meaning&gs_lp=Egxnd3Mtd2l6LXNlcnAiD3NvYXIgaXQgbWVhbmluZzIKEAAYExgHGB4YDzIHEAAYgAQYEzIIEAAYExgIGB4yCBAAGBMYCBgeMggQABgTGAgYHjIIEAAYExgIGB4yCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESNoLUNcHWJYKcAF4AZABAJgBVqAB9AGqAQEzuAEDyAEA-AEBmAIEoAKwAsICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIQEC4YgAQYsAMYQxjUAhiKBcICBxAAGIAEGA3CAgYQABgHGB7CAggQABgHGB4YD8ICCBAAGBMYBxgewgIKEAAYExgHGAgYHsICDBAAGBMYBxgIGB4YD5gDAIgGAZAGCpIHATSgB4IV&sclient=gws-wiz-serp)

Framework MITRE on security