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

# import
import socket, os, subprocess
from platform import node

#-------------------import data from networkconfigdata.txt----------------------


# check the host name for auto config
hostname = node().lower()


# import networkconfigdata.txt file and make it easy to access
with open("networkconfigdata.txt", "r") as myfile: # put raw data into a raw list
    network_configs = myfile.read().splitlines()

network_config_elements = []  # list of network elements within a list of
                              # network configs ("2D" list)

for i in network_configs:
    network_config_elements.append(i.split(","))

##global ip_address
##global subnet_mask
##global default_gateway
##global dns_1
##global dns_2

#-------------------------------------------------------------------------------

# netmask to cidr function
# this is used for convert netmask (255.255.255.0) to cidr notation (24)
def netmask_to_cidr(netmask):
    return sum([bin(int(x)).count('1') for x in netmask.split('.')])


# automatic network config function
def network_config(ip_address, subnet_mask, default_gateway, dns_1, dns_2):

    subprocess.call(['powershell.exe', r'New-NetIPAddress –InterfaceAlias “Ethernet”  –IPAddress "' + ip_address + r'" -PrefixLength ' + str(netmask_to_cidr(subnet_mask)) + r' -DefaultGateway ' + default_gateway])
    subprocess.call(['powershell.exe', r'Set-DnsClientServerAddress -InterfaceAlias “Ethernet” -ServerAddresses ' + dns_1 + r', ' + dns_2])


# manual syntax check: make sure the data is written with correct syntax
def syntax_check():
    pass


# config export function: export the file
def config_export():
    pass

#-------------------------------------------------------------------------------

# main function (test for now)
def main():

    # welcome text
    print("Welcome line...\n")
    print("Welcome line...\n")
    mode = str(input("Auto or manual?(a/m): ").lower())

    while mode != "a" and mode != "m":
        print("Invalid input!")
        mode = str(input("Auto or manual?(a/m): ").lower())

    if mode == a:
        # only works when the host name matches with data from networkconfigdata.txt
        for i in network_config_elements:
            if hostname == i[0]: # if there is an entry, move the elements to discrete objects
                ip_address = str(i[1])
                subnet_mask = str(i[2])
                default_gateway = str(i[3])
                dns_1 = str(i[4])
                dns_2 = str(i[5])
                network_config(ip_address, subnet_mask, default_gateway, dns_1, dns_2)
            else:
                print("There is no data entry that matches your host name!\n")
                print("There ")
                mode = str(input("Do you want to enter manually or exit?(m/e): ")).lower()

                while mode != "m" and mode != "e":
                    print("Invalid input!")
                    mode = str(input("Do you want to enter manually or exit?(m/e): ")).lower()

                if mode == "m":
                    ip_address = str(i[1])
                    subnet_mask = str(i[2])
                    default_gateway = str(i[3])
                    dns_1 = str(i[4])
                    dns_2 = str(i[5])
                    network_config(ip_address, subnet_mask, default_gateway, dns_1, dns_2)




main()










