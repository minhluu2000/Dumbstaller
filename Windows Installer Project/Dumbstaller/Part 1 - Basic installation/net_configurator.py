#----------------------------pseudo--------------------------------
# functionalities of net_configurator.py
# assign net config manually
# assign net config automatically based on the mac address or hostname
# collect network manually entered config data
# collect network interface data
# collect 








#-----------------------------import-------------------------------

from modules.netconfig import NetworkConfig
from modules.netconfig import NetworkDataHandler
from modules.uinputcheck import ipfcheck
import ifaddr # collect network interface info
from platform import node # collect host name
from uuid import getnode as get_mac # collect 
import uuid, sys, os
from pathlib import Path
from modules import admin



#---------------------------functions------------------------------

def uuid_to_mac(address):
    """This function convert uuid node (48-bit) to hex MAC address."""
    h = hex(address)[2:].zfill(12)
    mac = ":".join(i + j for i, j in zip(h[::2], h[1::2]))
    return mac

def auto_net_config():
    pass

def test():
    if not admin.isUserAdmin(): # if user is not admin then run as admin
        admin.runAsAdmin()
    input("Press enter to exit...")



#------------------------------main--------------------------------
if __name__ == "__main__":
    sys.exit(test())






# adapters = ifaddr.get_adapters()
# host = node()

# print("Please choose your target network interface below:\n ")
# for i in range(len(adapters)):
#     print(i + 1, adapters[i].nice_name)

# adapter_choice = int(input("\nYour choice: ")) - 1

# adapters = ifaddr.get_adapters()
# hostnetconfig = NetworkConfig(host, str(adapters[adapter_choice].ips[0].nice_name), get_mac(), "192.168.1.233", "255.255.255.0", "192.168.1.1", "1.1.1.1", "8.8.8.8")
# data = hostnetconfig.get_data()


# netdatahandler = NetworkDataHandler(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
# try:
#     netdatahandler.net_data_output("C:\\Users\\Minh Luu\\Desktop\\test.csv")
# except PermissionError:
#     print("Error!")

# netdatahandler.net_data_input("C:\\Users\\Minh Luu\\Desktop\\test.csv")

# # print(netdatahandler.data_return())

# print(netdatahandler.search_macaddr("minhpc"))

