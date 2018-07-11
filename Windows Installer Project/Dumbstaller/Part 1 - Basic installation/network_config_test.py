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
import socket, os
from platform import node


# check the host name for auto config
hostname = node().lower()


# import networkconfigdata.txt file and make it easy to access
with open("networkconfigdata.txt", "r") as myfile: # put raw data into a raw list
    network_configs = myfile.read().splitlines()

network_config_elements = []  # list of network elements within a list of
                              # network configs ("2D" list)

for i in network_configs:
    network_config_elements.append(i.split(","))


# automatic network config function
def auto_network_config():
    # create objects as entries for powershell
    # compare the hostname with any entry in networkconfigdata.txt
    for i in network_config_elements:
        if hostname == i[0]:






# manual network config function
def manual_network_config():
    print()

# manual syntax check: make sure the data is written with correct syntax
def syntax_check():
    print()



# config export function: export the file
def config_export():
    print()


# main function
def main():
    print()













