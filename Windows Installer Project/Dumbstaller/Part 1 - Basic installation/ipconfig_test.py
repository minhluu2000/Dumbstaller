#------------------------------------NOTE---------------------------------------
# This program is just a format test.
# Please DO NOT use it unless you know what you're doing.
#-------------------------------------------------------------------------------



import subprocess
from sys import exit

ip_address = str(input("IP Address: "))
subnet_mask = input("Subnet Mask:  ")
default_gateway = str(input("Default Gateway: "))
dns_1 = str(input("Primary DNS: "))
dns_2 = str(input("Secondary DNS: "))


def netmask_to_cidr(netmask):
    '''
    :param netmask: netmask ip addr (eg: 255.255.255.0)
    :return: equivalent cidr number to given netmask ip (eg: 24)
    '''
    return sum([bin(int(x)).count('1') for x in netmask.split('.')])

num = str(netmask_to_cidr(subnet_mask))


subprocess.call(['powershell.exe', r'New-NetIPAddress –InterfaceAlias “Ethernet”  –IPAddress "' + ip_address + r'" -PrefixLength ' + num + r' -DefaultGateway ' + default_gateway])
subprocess.call(['powershell.exe', r'Set-DnsClientServerAddress -InterfaceAlias “Ethernet” -ServerAddresses' + dns_1 + r', ' + dns_2])

input("Press enter to exit...")
exit()