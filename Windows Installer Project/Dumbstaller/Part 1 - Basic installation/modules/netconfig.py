import subprocess # call powershell.exe
from platform import node # check host name
import ifaddr # collect network interface(s) configs
import csv # import and export network config data
from pathlib import Path


class NetworkConfig:
    """This class collects your network config data and output it 
    to a database (if being the network is configured manually)."""
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

    def net_data_output(self, output_path):
        """This method pushes manually configured network configuration
        to a database (CSV for now) for future automatic config."""
        self.output_path = str(output_path) # path to the database for data output
        temp = Path(self.output_path) # a snapshot of file to check whether the file exits or not
        if temp.is_file():
            file = open(output_path, "a")
            writer = csv.writer(file, lineterminator = "\n")
            writer.writerow([self.hostname, self.adapter, self.ip4, self.ip4_subnet, self.gateway, self.dns1, self.dns2])
        else:
            file = open(output_path, "a")
            writer = csv.writer(file, lineterminator = "\n")  
            writer.writerow(["Host name", "Adapter", "IPv4", "Subnet", "Default Gateway", "DNS 1", "DNS 2",])
            writer.writerow([self.hostname, self.adapter, self.ip4, self.ip4_subnet, self.gateway, self.dns1, self.dns2])


    def net_data_input(self):
        """This method pull data from a database for auto network config."""
        pass

    def enable_dhcp(self):
        """This method enable DHCP for your Windows PC. Careful, it also enables auto dns as well."""
        subprocess.call(["powershell.exe", "Set-NetIPInterface -InterfaceAlias %s -Dhcp Enable" % (self.adapter)]) # enable dhcp
        subprocess.call(["powershell.exe", "Remove-NetRoute -InterfaceAlias %s" % (self.adapter)]) # reset default gateway (might need some improvements)
        subprocess.call(["powershell.exe", "Set-DnsClientServerAddress -InterfaceAlias %s -ResetServerAddresses" % (self.adapter)]) # reset dns
        subprocess.call(["powershell.exe", "Restart-NetAdapter -Name %s" % (self.adapter)]) # restart adapter

    def net_config(self):
        """This method deploys user network configuration through system-dependent PowerShell. 
        It also converts TCP/IP to CIDR notation for subnet mask."""
        self.cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')]) # convert 
        subprocess.call(["powershell.exe", "New-NetIPAddress –InterfaceAlias %s –IPAddress %s -PrefixLength %s -DefaultGateway %s" % (self.adapter, self.ip4, self.cidr, self.gateway)]) # change ip config
        subprocess.call(["powershell.exe", "Set-DnsClientServerAddress -InterfaceAlias %s -ServerAddresses %s, %s" % (self.adapter, self.dns1, self.dns2)]) # change dns config
        subprocess.call(["powershell.exe", "Restart-NetAdapter -Name %s" % (self.adapter)]) # restart network interface

    def net_config_help(self):
        """This function explains briefly about the program""" # might move this (method/function?) to main.py 
        pass