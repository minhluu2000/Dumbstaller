import subprocess # call powershell.exe
import csv # import and export network config data
from pathlib import Path # analyze WindowsPath


class NetworkDataHandler:
    """This class handles import and export network data to a database (csv)."""
    def __init__(self, host, adapter, mac_addr, ip4, ip4_subnet, gateway, dns1, dns2):
        """This method receives data passed from NetworkConfig class."""
        self.hostname = host
        self.adapter = adapter
        self.mac_addr = mac_addr
        self.ip4 = ip4
        self.ip4_subnet = ip4_subnet
        self.gateway = gateway
        self.dns1 = dns1
        self.dns2 = dns2

    def net_data_output(self, output_path):
        """This method pushes manually configured network configuration to a database (CSV for now) for future automatic config."""
        self.output_path = str(output_path) # path to the database for data output
        temp = Path(self.output_path) # a snapshot of file to check whether the file exits or not
        if temp.is_file():
            with open(output_path, "a") as f:
                writer = csv.writer(f, lineterminator = "\n")
                writer.writerow([self.hostname, self.adapter, self.mac_addr, self.ip4, self.ip4_subnet, self.gateway, self.dns1, self.dns2])
        else:
            with open(output_path, "a") as f:
                writer = csv.writer(f, lineterminator = "\n")  
                writer.writerow(["Host name", "Adapter", "MAC", "IPv4", "Subnet", "Default Gateway", "DNS 1", "DNS 2"])
                writer.writerow([self.hostname, self.adapter, self.mac_addr, self.ip4, self.ip4_subnet, self.gateway, self.dns1, self.dns2])

    def net_data_input(self, input_path):
        """This method pulls data from a database"""
        self.input_path = str(input_path) 
        with open(self.input_path, "r") as f:
            reader = csv.reader(f, lineterminator = "\n")
            next(reader) # skip the header
            self.data = [] # data holder
            for row in reader: # put the csv data to data list
                # return = [Host name, Adapter, MAC, IPv4, Subnet, Default Gateway, DNS 1, DNS 2]
                self.data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
    
    def get_data(self):
        """This method returns the entire data from net_data_input method as a list."""
        return self.data

    def search_hostname(self, search_hostname):
        """This method returns the data that matches the desired host name."""
        result = [] # search result holder
        for i in range(len(self.data)):
            if self.data[i][0] == search_hostname:
                result.append(self.data[i])
        return result

    def search_macaddr(self, search_mac_addr):
        """This method returns the data that matches the desired mac address."""
        result = [] # search result holder
        for i in range(len(self.data)):
            if self.data[i][0] == search_mac_addr:
                result.append(self.data[i])
        return result



class NetworkConfig:
    """This class collects your network config data and output it to a database (if being the network is configured manually)."""
    def __init__(self, host, adapter, mac_addr, ip4, ip4_subnet, gateway, dns1, dns2):
        self.hostname = host
        self.adapter = adapter
        self.mac_addr = mac_addr
        self.ip4 = ip4
        self.ip4_subnet = ip4_subnet
        self.gateway = gateway
        self.dns1 = dns1
        self.dns2 = dns2
    
    def netmask_to_cidr(self):
        """This method converts TCP/IP to CIDR form for the subnet mask."""
        cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')])
        return cidr

    def enable_dhcp(self):
        """This method enable DHCP for your Windows PC. Careful, it also enables auto dns as well."""
        subprocess.call(["powershell.exe", "Set-NetIPInterface -InterfaceAlias %s -Dhcp Enable" % (self.adapter)]) # enable dhcp
        subprocess.call(["powershell.exe", "Remove-NetRoute -InterfaceAlias %s" % (self.adapter)]) # reset default gateway (might need some improvements)
        subprocess.call(["powershell.exe", "Set-DnsClientServerAddress -InterfaceAlias %s -ResetServerAddresses" % (self.adapter)]) # reset dns
        subprocess.call(["powershell.exe", "Restart-NetAdapter -Name %s" % (self.adapter)]) # restart adapter

    def net_config(self):
        """This method deploys user network configuration through system-dependent PowerShell. It also converts TCP/IP to CIDR notation for subnet mask."""
        self.cidr = sum([bin(int(x)).count('1') for x in self.ip4_subnet.split('.')]) # convert 
        subprocess.call(["powershell.exe", "New-NetIPAddress –InterfaceAlias %s –IPAddress %s -PrefixLength %s -DefaultGateway %s" % (self.adapter, self.ip4, self.cidr, self.gateway)]) # change ip config
        subprocess.call(["powershell.exe", "Set-DnsClientServerAddress -InterfaceAlias %s -ServerAddresses %s, %s" % (self.adapter, self.dns1, self.dns2)]) # change dns config
        subprocess.call(["powershell.exe", "Restart-NetAdapter -Name %s" % (self.adapter)]) # restart network interface
    
    def get_data(self):
        """This method returns all the data of an instance of NetworkConfig. It's mainly used to pass data to NetworkDataHandler for data output"""
        data = [self.hostname, self.adapter, self.mac_addr, self.ip4, self.ip4_subnet, self.gateway, self.dns1, self.dns2]
        return data

    def net_config_help(self):
        """This function explains briefly about the program.""" # might move this (method/function?) to main.py 
        return help(NetworkConfig)

