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
import csv
# import logging

#-------------------------------------logger------------------------------------
# create and configure logger
# logging is under testing
# LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# logging.basicConfig(filename = "network_config.log", level = logging.CRITICAL, format = LOG_FORMAT) # set to critical for testing
# logger = logging.getLogger()

#-------------------import data from network_config.csv-------------------------
"""A csv database system is under development to replace the 
old networkconfigdata.txt system"""

# import networkconfigdata.txt file and make it easy to access
# with open("networkconfigdata.txt", "r") as myfile:
#     network_config = myfile.read().splitlines()

# for i in network_configs:
#     network_config_elements.append(i.split(","))

#------------------------------classes and functions----------------------------

class NetworkConfig:
    """This class collects your network config data and output it 
    to a database (if being configured manually). It is still under 
    heavy development, so not many features are available yet."""
    def __init__(self, adapter, ip4, ip4_subnet, gateway, dns1, dns2):
        self.hostname = node().lower() # retrive host name for auto network config detection, may move this to the main file
        self.adapter = adapter
        self.ip4 = ip4
        self.ip4_subnet = ip4_subnet
        self.gateway = gateway
        self.dns1 = dns1
        self.dns2 = dns2
    
    def netmask_to_cidr(self):
        """This method converts TCP/IP to CIDR form for the subnet mask."""
        cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')])
        return cidr

    def net_data_output(self):
        """This method pushes manually configured network configuration
        to a database for future automatic config."""
        pass

    def enable_dhcp(self):
        """This method enable DHCP for your Windows PC. Careful, it also enables auto dns as well."""
        subprocess.call(["powershell.exe", "Set-NetIPInterface -InterfaceAlias %s -Dhcp Enable" % (self.adapter)]) # enable dhcp
        subprocess.call(["powershell.exe", "Remove-NetRoute -InterfaceAlias %s" % (self.adapter)]) # reset default gateway (might need some improvements)
        subprocess.call(["powershell.exe", "Set-DnsClientServerAddress -InterfaceAlias %s -ResetServerAddresses" % (self.adapter)]) # reset dns
        subprocess.call(["powershell.exe", "Restart-NetAdapter -Name %s" % (self.adapter)]) # restart adapter

    def net_config(self):
        """This method deploys user network configuration through system-dependent PowerShell (for now). 
        It also converts TCP/IP to CIDR notation for subnet mask."""
        self.cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')]) # convert 
        subprocess.call(["powershell.exe", "New-NetIPAddress –InterfaceAlias %s –IPAddress %s -PrefixLength %s -DefaultGateway %s" % (self.adapter, self.ip4, self.cidr, self.gateway)]) # change ip config
        subprocess.call(["powershell.exe", "Set-DnsClientServerAddress -InterfaceAlias %s -ServerAddresses %s, %s" % (self.adapter, self.dns1, self.dns2)]) # change dns config
        subprocess.call(["powershell.exe", "Restart-NetAdapter -Name %s" % (self.adapter)]) # restart network interface

    def net_config_help(self):
        """This function explains briefly about the program""" # might move this (method/function?) to main.py 
        pass

class InputCheck:
    """This class does input checking for the program. It will warn user if a particular input is invalid."""
    def __init__(self, user_input):
        self.input = user_input

    def ipfcheck(self):
        """This method checks IP format."""
        pass

    def gchoice(self):
        """This method checks user general choices (char and num)""" 
        pass


#--------------------------------------main-------------------------------------


# def main():
#     print("Network Configuration Menu: \n1. Auto network config (check the database before using this or make sure you know what you're doing) \n2. Manual network config (with data saving) \n3. Manual network config (without data saving) \n4. Enable DHCP \n5. View known network configs (aka database) \n6. Help!!! IDK What I'm doing!")




adapters = ifaddr.get_adapters()
#     # print("Please choose your target network interface below:\n ")
#     # for i in range(len(adapters)):
#     #         print(i + 1, adapters[i].nice_name)

adapter_choice = int(input("\nYour choice: ")) - 1
#     # print(adapters[adapter_choice].ips[0].nice_name)

hostnetconfig = NetworkConfig(str(adapters[adapter_choice].ips[0].nice_name), "192.168.1.233", "255.255.255.0", "192.168.1.1", "1.1.1.1", "8.8.8.8")
hostnetconfig.enable_dhcp()
# hostnetconfig.network_config()
print(hostnetconfig.hostname)
#     # host_network_config.network_config()

#     # help(NetworkConfig)

#     # input("Enter...")



# main()