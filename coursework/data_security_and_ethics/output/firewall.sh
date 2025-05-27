::::::::::::::
firewall.sh (inventive)
::::::::::::::
Added user rules (see 'ufw status' for running firewall):
ufw route allow from 192.168.30.20 to any port 443
ufw route allow from 192.168.30.10 to any port 5000
ufw route limit to 192.168.30.10 port 5000
ufw route allow to 192.168.30.30 port 4500
ufw route allow to 192.168.30.30 port 500
ufw route limit to 192.168.30.30 port 20
ufw route allow from 192.168.30.30