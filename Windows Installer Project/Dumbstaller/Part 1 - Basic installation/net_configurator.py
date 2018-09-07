from modules.netconfig import NetworkConfig
from modules.uinputcheck import ipfcheck
import ifaddr # network info

adapters = ifaddr.get_adapters()

print("Please choose your target network interface below:\n ")
for i in range(len(adapters)):
    print(i + 1, adapters[i].nice_name)

adapter_choice = int(input("\nYour choice: ")) - 1

adapters = ifaddr.get_adapters()
hostnetconfig = NetworkConfig(str(adapters[adapter_choice].ips[0].nice_name), "192.168.1.233", "255.255.255.0", "192.168.1.1", "1.1.1.1", "8.8.8.8")
hostnetconfig.net_data_output("C:\\Users\\Minh Luu\\Desktop\\test.csv")