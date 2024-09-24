sudo dnf install -y nano bind-utils git

cd /usr/src/
sudo git clone https://gitlab.com/maradns/maradns.git maradns && cd maradns
./configure
CC=gcc
export CC
make
sudo make install
cd ../

sudo dnf install -y krb5-server krb5-libs krb5-auth-dialog krb5-workstation krb5-server-ldap krb5-pkinit krb5-devel
sudo systemctl enable --now maradns

mkdir /home/vagrant/{maradns,var,etc}
mkdir -p ~/var/kerberos/krb5kdc
