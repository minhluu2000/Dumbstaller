# import networkconfigdata.txt
# ask user if he/she wants program to config automatically or manually
# if automatically
# check host name
#   if host name matches with data, config network with networkconfigdata.txt
#   if host name doesn't match any data, ask if he/she wants to continue
#       if yes, ask him/her to config manually
#           export the data to networkconfigdata.txt after finish
#       if not, leave DHCP on and exit the program
# if not, promp user to enter network config manually
#   export the data to networkconfigdata.txt after finish

#-------------------------------------------------------------------------------

#------------------------------------import-------------------------------------

import socket, os, subprocess
from platform import node
import ifaddr


#-------------------import data from networkconfigdata.txt----------------------
"""This is will be replaced with better a better database system in the future"""
# check the host name for auto config
# hostname = node().lower()

# import networkconfigdata.txt file and make it easy to access
# with open("networkconfigdata.txt", "r") as myfile:
#     network_config = myfile.read().splitlines()

# for i in network_configs:
#     network_config_elements.append(i.split(","))

#-------------------------------class and functions-----------------------------

class NetworkConfig:
    
    """This class collects and stores data from networkconfigdata.txt.
    This class is still under heavy development, so not many features are
    available yet."""

    def __init__(self, netmode, ip4, ip4_subnet, gateway, dns1, dns2):
        self.netmode = netmode
        self.ip4 = ip4
        self.ip4_subnet = ip4_subnet
        self.gateway = gateway
        self.dns1 = dns1
        self.dns2 = dns2
    
    def netmask_to_cidr(self):

        """This method converts TCP/IP to CIDR form for the subnet mask."""
        
        self.cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')])
        return self.cidr

    def network_config(self):

        """This method deploys user network configuration through system-dependent PowerShell (for now). 
        It also converts TCP/IP to CIDR notation for subnet mask."""

        self.cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')])
        subprocess.call(['powershell.exe', "New-NetIPAddress –InterfaceAlias %s –IPAddress %s -PrefixLength %s -DefaultGateway %s" % (self.netmode, self.ip4, self.cidr, self.gateway)])
        subprocess.call(['powershell.exe', "Set-DnsClientServerAddress -InterfaceAlias %s -ServerAddresses %s, %s" % (self.netmode, self.dns1, self.dns2)])

class InputCheck:
    """This class does input checking for the program. It will warn user if a particular input is invalid."""
    def __init__(self, user_input):
        self.input = user_input



adapters = ifaddr.get_adapters()
print("Please choose your target network interface below:\n ")
for i in range(len(adapters)):
        print(i + 1, adapters[i].nice_name)

adapter_choice = int(input("\nYour choice: "))



host_network_config = NetworkConfig(str(adapters[0].ips[0].nice_name), "192.168.1.233", "255.255.255.0", "192.168.1.1", "1.1.1.1", "8.8.8.8")
host_network_config.network_config()

input("Enter...")

