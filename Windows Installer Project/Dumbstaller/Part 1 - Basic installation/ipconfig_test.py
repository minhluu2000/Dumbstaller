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
    return sum([bin(int(x)).count('1') for x in netmask.split('.')])


subprocess.call(['powershell.exe', r'New-NetIPAddress –InterfaceAlias “Ethernet”  –IPAddress "' + ip_address + r'" -PrefixLength ' + str(netmask_to_cidr(subnet_mask)) + r' -DefaultGateway ' + default_gateway])
subprocess.call(['powershell.exe', r'Set-DnsClientServerAddress -InterfaceAlias “Ethernet” -ServerAddresses ' + dns_1 + r', ' + dns_2])

input("Press enter to exit...")
exit()