from netmiko import ConnectHandler
from getpass import getpass
import json

# ensure routerlist.txt / commands.txt are populated with desired host ip's and commands


uname = input("Username: ")
pythonpassword= getpass("Password: ")
type = 'cisco_ios'


with open(file="routerlist.txt", mode="r") as hosts:
    # A list comprehension
    devices = [
        {
            "device_type": "cisco_ios",
            "ip": ip,
            "username": uname,
            "password": pythonpassword,
        }
        for ip in hosts.read().splitlines()
    ]

with open('commands.txt') as f:
    lines = f.read().splitlines()
    print(lines)




json_formatted = json.dumps(devices, indent=4)
print(json_formatted)



# 
for device in devices:
    print(f'Connecting to {device["ip"]}')  
    net_connect = ConnectHandler(**device)
    print(f'Connected to {device["ip"]}')  
    prompt = net_connect.find_prompt()
    output = net_connect.send_config_set(lines)
    print(output)


