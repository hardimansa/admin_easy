from netmiko import ConnectHandler
from getpass import getpass
import json

# ensure routerlist.txt / commands.txt / are populated


uname = input("Username: ")
pythonpassword= getpass("Password: ")


with open(file="routerlist.txt", mode="r") as hosts:
    # list of devices in netmiko format
    devices = [
        {
            "device_type": "cisco_ios",
            "ip": ip,
            "username": uname,
            "password": pythonpassword,
          # no need for sesssion log with output section below -  "session_log": ip
        }
        for ip in hosts.read().splitlines()
    ]

with open('commands.txt') as f:
    commands = f.read().splitlines()
    

    

# JSON print of device configuration

json_formatted = json.dumps(devices, indent=4)
print(json_formatted)



#  SEND COMMANDS & CREATE OUTPUT FILES
for device in devices:
    print(f'Connecting to {device["ip"]}')  
    net_connect = ConnectHandler(**device)
    print(f'Connected to {device["ip"]}')  
    output = net_connect.send_config_set(commands)
    print(output)
    file = open(f' {device["ip"]}', "a")
    file.write(output)


