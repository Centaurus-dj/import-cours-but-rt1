sudo apt install -y dnsutils nano git make gcc

cd /usr/src/
sudo git clone https://gitlab.com/maradns/maradns.git maradns && cd maradns
./configure
CC=gcc
export CC
sudo make
sudo make install
cd ../

sudo apt install -y krb5-admin-server krb5-kdc

sudo systemctl enable --now maradns
sudo systemctl status maradns

sudo krb5_newrealm

sudo systemctl enable --now krb5-admin-server
sudo systemctl enable --now krb5-kdc

sudo kadmin.local