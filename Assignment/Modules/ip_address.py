import ipaddress

ip = ipaddress.ip_address("192.168.1.10")

print(ip)


#----------------To check Ip address valid or not--------------
ip = "192.168.1.10"

try:
    address = ipaddress.ip_address(ip)
    print("Valid IP address")
except ValueError:
    print("Invalid IP address")


#------------------------Check Version-------------------------------
    
ip = ipaddress.ip_address("192.168.1.10")

print(ip.version)

ip = ipaddress.ip_address("2001:db8::1")

print(ip.version)

#-------------------------Check Private or not-----------------------
print("Private", ip.is_private)
print("Global:", ip.is_global)


#-----------------------------Lookback Address-------------------------
ip = ipaddress.ip_address("127.0.0.1")

print(ip.is_loopback)

#----------------------------- ALL---------------------------------------

ip_text = input("Enter IP address: ")

try:
    ip = ipaddress.ip_address(ip_text)

    print("Valid IP")
    print("Version:", ip.version)
    print("Private:", ip.is_private)
    print("Global:", ip.is_global)
    print("Loopback:", ip.is_loopback)

except ValueError:
    print("Invalid IP address")
    
    
#------------------------------Get Network Information---------------
import ipaddress

network = ipaddress.ip_network("192.168.1.0/24")

print("Network:", network.network_address)
print("Broadcast:", network.broadcast_address)
print("Netmask:", network.netmask)

#---------------------------Check Whether an IP Belongs to a Network-------
import ipaddress

network = ipaddress.ip_network("192.168.1.0/24")

ip = ipaddress.ip_address("192.168.1.50")

print(ip in network)

