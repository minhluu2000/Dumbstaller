from modules.netconfig import NetworkConfig
from modules.uinputcheck import ipfcheck
import ifaddr # network info, p
from modules.looper import looper

adapters = ifaddr.get_adapters()

# print("Please choose your target network interface below:\n ")
# for i in range(len(adapters)):
#     print(i + 1, adapters[i].nice_name)

# adapter_choice = int(input("\nYour choice: ")) - 1

adapters = ifaddr.get_adapters()
hostnetconfig = NetworkConfig()
# hostnetconfig.net_data_output("C:\\Users\\Minh Luu\\Desktop\\test.csv")

data = hostnetconfig.net_data_input("C:\\Users\\Minh Luu\\Desktop\\test.csv")
print(data)