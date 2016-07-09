from fabric.api import run, sudo, settings, hide
from ilogue.fexpect import expect, expecting, run 
from termcolor import colored
import nmap
import netifaces
import iptools

'''
def sudosu(user, cmd):
    cmd += ' ;exit'
    prompts = []
    prompts += expect('bash', cmd)
    prompts += expect('password:', vagrant)

    with expecting(prompts):
        run('sudo su - ' + user)
'''

def kali():
    with settings(warn_only=True):
        print colored('###################################################################', 'blue') 
        print colored('############################ KALI LINUX ###########################', 'blue')
        print colored('###################################################################', 'blue') 

        print colored(' _     _                    ____                       _ _         ', 'blue')
        print colored('| |   (_)_ __  _   ___  __ / ___|  ___  ___ _   _ _ __(_) |_ _   _ ', 'blue')
        print colored('| |   | |  _ \| | | \ \/ / \___ \ / _ \/ __| | | |  __| | __| | | |', 'blue')
        print colored('| |___| | | | | |_| |>  <   ___) |  __/ (__| |_| | |  | | |_| |_| |', 'blue')
        print colored('|_____|_|_| |_|\__,_/_/\_\ |____/ \___|\___|\__,_|_|  |_|\__|\__, |', 'blue')
    
        print colored(' _        _    ____            _  __    _    _     ___ ', 'blue')
        print colored('| |      / \  | __ )          | |/ /   / \  | |   |_ _|', 'blue')
        print colored('| |     / _ \ |  _ \   _____  |   /   / _ \ | |    | | ', 'blue')
        print colored('| |___ / ___ \| |_) | |_____| | . \  / ___ \| |___ | | ', 'blue')
        print colored('|_____/_/   \_\____/          |_|\_\/_/   \_\_____|___|', 'blue')

        print colored('                                                                  ', 'blue') 
        print colored('                                                                  ', 'blue') 

        print colored('                        .,:lodxxxxdlc,.                           ', 'red')
        print colored('                    .cxKNNNNNNNNNNXXXXXXx,                        ', 'red')
        print colored('                  ,OXNNNNNNNNNNNXXXXNXXXXXKc                      ', 'red')
        print colored('                .ONNNNNNNNNNNNNNNXXXXXXXXXXXK:                    ', 'red')
        print colored('               :XNNNNNNNNNNNNNNNXXXXXXXXXXXXXXO.                  ', 'red')
        print colored('               KNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXX0                  ', 'red')
        print colored('               NNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXX.                 ', 'red')
        print colored('              ;XKcd0XXXXXXXXXXXXXXXXXXXXXXXOxo0X.                 ', 'red')
        print colored('              ,XO   .;xXXXXXXXXXXXXNXXXXx,    kK                  ', 'red')
        print colored('              .XX.       lOXXXXXXXXXXkc.     .Kd                  ', 'red')
        print colored('               cXO.        .,oXX0l;.        .kX,                  ', 'red')
        print colored('                :XX0xocccccld0:.l0dl:,,,:cdOXXk                   ', 'red')
        print colored('                ;OXXXXXXXXXXK. l ;XXXXXXXXXXXX:                   ', 'red')
        print colored('                OXXXXXkl:dXXO lX. KXXXOc;:dXXXd                   ', 'red')
        print colored('                :XKOx.   :XXXKXXKKXXXXl   .K0d.                   ', 'red')
        print colored('                  .       oXKl0XdOK.oXK                           ', 'red')
        print colored('                          0O kX xK.XX:                            ', 'red')
        print colored('                          0K.kK.kK XX                             ', 'red')
        print colored('                          0K kX.OK;XK                             ', 'red')
        print colored('                          0K.kK OO,XK                             ', 'red')
        print colored('                          0K.OK.Kd,KK                             ', 'red')
        print colored('                          ;K.O0 K:,Kk                             ', 'red')
        print colored('                             `.   ,                               ', 'red')

        print colored('###################################################################', 'blue') 
        print colored('###################################################################', 'blue') 

        sudo('apt-get -y update')
        sudo('apt-get -y install inetutils-traceroute traceroute dnstop tcpdump nmap vim python-pip python-dev libevent-dev')
        sudo('apt-get -y install mcrypt')
        sudo('apt-get -y install apache2 dsniff mcrypt mail mailutils cron')

        sudo('pip install fabric netifaces python-nmap iptools fexpect')        
        # sudo('if ! [ -L /var/www ]; then'
        #		'rm -rf /var/www'
        #		'ln -fs /vagrant/ /var/www'
        #	'fi')

        print colored('##########################', 'blue')
        print colored('### STARTING NET CONF ####', 'blue')
        print colored('##########################', 'blue')
        sudo('echo 1 >> /proc/sys/net/ipv4/ip_forward')
        # sysctl -w net.ipv4.ip_forward=1
        sudo('service ufw stop')
        sudo('service apparmor teardown')
        sudo('service networking restart')

        print colored('##########################', 'blue')
        print colored('##### STATIC ROUTING #####', 'blue')
        print colored('##########################', 'blue')
        sudo('dhclient eth1')
        #sudo('echo nameserver 192.168.43.1 >> /etc/resolv.conf')
        sudo('ip route del default via 10.0.2.2 dev eth0')

        print colored('#####################################', 'blue')
        print colored('#### AUTO-SIGNED CERT GENERATION ####', 'blue')
        print colored('#####################################', 'blue')
        sudo('sh /vagrant/conf/gen-cer.sh mybank.com')

        print colored('##########################', 'blue')
        print colored('#### APACHE2 WEB_SERV ####', 'blue')
        print colored('##########################', 'blue')
        # sudo('wget -P /var/www/ -E -H -k -K -p http://www.binbash.com.ar')
        # sudo('cp -r /var/www/www.binbash.com.ar/* /var/www/')
        sudo('cp /vagrant/www/Apache2/ports.conf /etc/apache2/ports.conf')
        sudo('cp /vagrant/www/Apache2/binbash.com.ar.conf /etc/apache2/sites-available/binbash.com.ar')
        sudo('cp /vagrant/www/Apache2/mybank.com.conf /etc/apache2/sites-available/mybank.com')
        sudo('mkdir -p /var/www/binbash.com.ar/public_html')
        sudo('mkdir -p /var/www/binbash.com.ar/logs')
        sudo('mkdir -p /var/www/mybank.com/public_html')
        sudo('mkdir -p /var/www/mybank.com/logs')
        
        sudo('wget -P /var/www/binbash.com.ar'
             ' --recursive'
             ' --no-clobber'
             ' --page-requisites'
             ' --html-extension'
             ' --convert-links'
             ' --restrict-file-names=windows'
             ' --domains website.org'
             ' --no-parent'
             ' http://www.binbash.com.ar')

        sudo('cp /var/www/binbash.com.ar/www.binbash.com.ar/index.html /var/www/binbash.com.ar/public_html/index.html')
        sudo('rm -r /var/www/binbash.com.ar/www.binbash.com.ar/')
        sudo('cp /vagrant/www/mybank.com/index.html /var/www/mybank.com/public_html/index.html')
        sudo('cp /vagrant/www/mybank.com/index.php /var/www/mybank.com/public_html/index.php')
        sudo('echo "ServerName localhost" >> /etc/apache2/apache2.conf')
        sudo('a2ensite binbash.com.ar')
        sudo('a2ensite mybank.com')
        sudo('chmod -R 755 /var/www')
        sudo('service apache2 restart')
        sudo('service apache2 restart')
        # sudo chown -R $USER:$USER /var/www/ejemplo.com/public_html
        # sudo chown -R $USER:$USER /var/www/pruebas.com/public_html

        print colored('############################', 'blue')
        print colored('#### /etc/hosts EDITION ####', 'blue')
        print colored('############################', 'blue')
        sudo('python /vagrant/conf/hosts.py')

        print colored('##############################', 'blue')
        print colored('###### ARP/DNS SPOOFED  ######', 'blue')
        print colored('##############################', 'blue')
        sudo('fab -f /vagrant/conf/fabfile.py arpdnsspoof')
        sudo('python /vagrant/conf/hosts-spoof.py')
        sudo('nohup dnsspoof -i eth1 -f /etc/hosts.spoof > /vagrant/logs/dnsspoof.txt 2>&1 &', pty=False)
        
        print colored('##########################', 'blue')
        print colored('### ENCRIPTED BACKUP   ###', 'blue')
        print colored('##########################', 'blue')
        sudo('sh /vagrant/conf/backup.sh')
        #sudo('at -f /vagrant/conf/backup.sh midnight -m exequielrafaela@gmail.com') # schedule 1 time exection.

        ##########################################################
        #minuto (0-59),                                          #
        #|  hora (0-23),                                         #
        #|  |  dia del mes (1-31),                               #
        #|  |  |  mes (1-12),                                    #
        #|  |  |  |  dia de la semana (0-6 donde 0=Domingo)      #
        #|  |  |  |  |       comandos                            #
        ##########################################################

        #run('line="0 0 * * * /vagrant/conf/backup.sh | mail -s \"VagrantSec-Backup\" exequielrafaela@gmail.com"') 
        #run('line="@daily vagrant /vagrant/conf/backup.sh | mail -s \"VagrantSec-Backup\" exequielrafaela@gmail.com"') 
        sudo('touch /etc/cron.d/daily-cron') 
        sudo('chmod a+rwx /etc/cron.d/daily-cron')
        #with settings(user='root'):
        #    run('echo "$line" > /etc/cron.d/daily-cron')
        sudo('echo "@daily vagrant /vagrant/conf/backup.sh | mail -s \"VagrantSec-Backup\" exequielrafaela@gmail.com" > /etc/cron.d/daily-cron')
        sudo('crontab -u vagrant /etc/cron.d/daily-cron') 
        #sudo('/etc/init.d/cron  start')
        sudo('service cron start')
        run('crontab -u vagrant -l')

        print colored('##########################', 'blue')
        print colored('##### START FIREWALL #####', 'blue')
        print colored('##########################', 'blue')

        # To stop Ipv4 based iptables firewall
        sudo('iptables-save > $HOME/firewall.txt')
        sudo('iptables -X')
        sudo('iptables -t nat -F')
        sudo('iptables -t nat -X')
        sudo('iptables -t mangle -F')
        sudo('iptables -t mangle -X')
        sudo('iptables -P INPUT ACCEPT')
        sudo('iptables -P FORWARD ACCEPT')
        sudo('iptables -P OUTPUT ACCEPT')

        # To stop Ipv6 based iptables firewall, enter:
        sudo('ip6tables-save > $HOME/firewall-6.txt')
        sudo('ip6tables -X')
        sudo('ip6tables -t mangle -F')
        sudo('ip6tables -t mangle -X')
        sudo('ip6tables -P INPUT ACCEPT')
        sudo('ip6tables -P FORWARD ACCEPT')
        sudo('ip6tables -P OUTPUT ACCEPT')

        # To start Ipv4 based iptables firewall, enter:
        # sudo('iptables -t nat -A PREROUTING -i eth2 -d 192.168.1.1 -p tcp --dport 80 -j DNAT --to-destination 172.16.0.1:8080')
        # sudo('iptables -t nat -A PREROUTING -i eth1 -d 192.168.3.2 -p tcp --dport 80 -j DNAT --to-destination 172.16.0.1:8080')
        # sudo('iptables -t nat -A PREROUTING -i eth1 -d 172.16.2.1 -p tcp --dport 80 -j DNAT --to-destination 172.16.0.1:8080')
        # sudo('iptables -A INPUT -p tcp -s 10.0.2.2 --dport ssh -j ACCEPT')
        # sudo('iptables -A INPUT -p tcp -s 172.16.0.1 --dport ssh -j ACCEPT')
        # sudo('iptables -A INPUT -p tcp -s 172.16.1.1 --dport ssh -j ACCEPT')
        # sudo('iptables -A INPUT -p tcp -s 172.16.2.1 --dport ssh -j ACCEPT')
        # sudo('iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport ssh -j DROP')

        print colored('######################################', 'blue')
        print colored('END FIREWALL - NAT TABLE STATUS:      ', 'blue')
        print colored('######################################', 'blue')
        with hide('output'):
            fw = sudo('iptables -t nat -L')
        print colored(fw, 'red')

        print colored('######################################', 'blue')
        print colored('END FIREWALL - FILTER TABLE STATUS:   ', 'blue')
        print colored('######################################', 'blue')
        with hide('output'):
            fw = sudo('iptables -L')
        print colored(fw, 'red')

        print colored('##########################', 'blue')
        print colored('## NETWORK CONFIGURATION #', 'blue')
        print colored('##########################', 'blue')
        with hide('output'):
            netconf = sudo('ip addr show')
        print colored(netconf, 'yellow')

        #############################################################################
        #############################################################################