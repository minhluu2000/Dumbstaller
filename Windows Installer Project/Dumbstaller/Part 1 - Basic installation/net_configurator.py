from modules.netconfig import NetworkConfig
from modules.netconfig import NetworkDataHandler
from modules.uinputcheck import ipfcheck
import ifaddr # network info, p
from platform import node

adapters = ifaddr.get_adapters()
host = node()

print("Please choose your target network interface below:\n ")
for i in range(len(adapters)):
    print(i + 1, adapters[i].nice_name)

adapter_choice = int(input("\nYour choice: ")) - 1

adapters = ifaddr.get_adapters()
hostnetconfig = NetworkConfig(host, str(adapters[adapter_choice].ips[0].nice_name), "192.168.1.233", "255.255.255.0", "192.168.1.1", "1.1.1.1", "8.8.8.8")
data = hostnetconfig.data_send()

netdatahandler = NetworkDataHandler(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
try:
    netdatahandler.net_data_output("C:\\Users\\Minh Luu\\Desktop\\test.csv")
except PermissionError:
    print("Error!")

netdatahandler.net_data_input("C:\\Users\\Minh Luu\\Desktop\\test.csv")

# print(netdatahandler.data_return())

print(netdatahandler.search_data("minhpc"))

