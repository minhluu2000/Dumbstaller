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


#---------------------functions except for main functions-----------------------


# netmask to cidr function
# this is used for convert netmask (255.255.255.0) to cidr notation (24)
def netmask_to_cidr(netmask):
    return sum([bin(int(x)).count('1') for x in netmask.split('.')])


# automatic network config function
def network_config(net_mode, ip, submask, def_gate, dns_1, dns_2):

    subprocess.call(['powershell.exe', r'New-NetIPAddress –InterfaceAlias "' + net_mode + r'"  –IPAddress "' + ip + r'" -PrefixLength ' + str(netmask_to_cidr(submask)) + r' -DefaultGateway ' + def_gate])
    subprocess.call(['powershell.exe', r'Set-DnsClientServerAddress -InterfaceAlias "' + net_mode + r'" -ServerAddresses ' + dns_1 + r', ' + dns_2])


# manual syntax check: make sure the data is written with correct syntax
def syntax_check():
    pass


# config export function: export new data entry to the networkconfigdata.txt
def config_export(hn, ip, submask, def_gate, dns_1, dns_2):
    with open("networkconfigdata_test.txt", "a") as f:
        f.write("\n" + hn + "," + ip + "," + submask + "," + def_gate + "," + dns_1 + "," + dns_2)
    f.close()


#-------------------------------------------------------------------------------


# main function (test for now)
def main():

    # welcome text
    print("\nWelcome line...\n")
    print("Welcome line...\n")


    # temporary way to detect the right adapter for the network config function
    net_mode_input = str(input("Are you using Wi-Fi or Ethernet Cable?(w/e): ")).lower()
    net_mode = ""

    while net_mode_input != "w" and net_mode_input != "e": # input check
        print("Invalid input!")
        net_mode_input = str(input("Are you using Wi-Fi or Ethernet Cable?(w/e): ")).lower()

    if net_mode_input == "w":
        net_mode = "Wi-Fi"


    if net_mode_input == "e":
        net_mode = "Ethernet"

    # ask for auto or manual mode
    mode = str(input("\nAuto or manual?(a/m): ").lower())

    while mode != "a" and mode != "m":
        print("Invalid input!\n")
        mode = str(input("Auto or manual?(a/m): ").lower())

    if mode == "a":
        print("\nConfiguring the network automatically...")
        # only works when the host name matches with data from networkconfigdata.txt
        for i in network_config_elements:
            if hostname == i[0]: # if there is an entry, move the elements to discrete objects
                ip_address = str(i[1])
                subnet_mask = str(i[2])
                default_gateway = str(i[3])
                dns_1 = str(i[4])
                dns_2 = str(i[5])
                network_config(net_mode, ip_address, subnet_mask, default_gateway, dns_1, dns_2)
                print("\nNetwork is configured successfully!\n")
                print("Here is the info: \n")
                print("IP Address: " + ip_address + "\nSubnet Mask: " + subnet_mask + "\nDefault Gateway: " + default_gateway + "\nPrimary DNS: " + dns_1 + "\nSecondary DNS: " + dns_2)

                input("Press enter to continue...\n")
                print("The program will exit.\nIf you already finished Windows update, please go to part 2.\nIf you haven't done Windows update, please run it now.\n")
                print("If you want to re-configure the network again, please run network_reset BEFORE re-running this program.")
                print("If you run this program before network_reset, the program will give you an error.\n")
                input("Press enter to exit...")
                exit()

            else: # if there is no matched data, ask the user to enter manually or exit the program
                print("\nThere is no data entry that matches your host name!")
                print("You can enter the network configuration manually.")
                print("The data you enter will be saved.")
                print("If you exit, the machine will be in DHCP mode.\n")

                # ask user to enter manually or exit
                mode = str(input("Do you want to enter manually or exit?(m/e): ")).lower()

                while mode != "m" and mode != "e": # input check
                    print("Invalid input!\n")
                    mode = str(input("Do you want to enter manually or exit?(m/e): ")).lower()

                if mode == "m": # enter manually
                    ip_address = str(input("IP Address: "))
                    subnet_mask = input("Subnet Mask:  ")
                    default_gateway = str(input("Default Gateway: "))
                    dns_1 = str(input("Primary DNS: "))
                    dns_2 = str(input("Secondary DNS: "))
                    network_config(net_mode ,ip_address, subnet_mask, default_gateway, dns_1, dns_2)
                    config_export(hostname, ip_address, subnet_mask, default_gateway, dns_1, dns_2)
                else:
                    exit()
    elif mode == "m":
        pass

main()

#------------------------------Terminated---------------------------------------








