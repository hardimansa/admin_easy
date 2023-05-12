from netmiko import ConnectHandler
from getpass import getpass
import json

# ensure routerlist.txt / commands.txt are populated with desired host ip's


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

    
# enter commands to execute on all hosts in routerlist.txt
    
with open('commands.txt') as f:
    lines = f.read().splitlines()
    print(lines)


# json formated view of netmiko router list, optional 

json_formatted = json.dumps(devices, indent=4)
print(json_formatted)



#  connect to each system, execute commands 

for device in devices:
    print(f'Connecting to {device["ip"]}')  
    net_connect = ConnectHandler(**device)
    print(f'Connected to {device["ip"]}')  
    prompt = net_connect.find_prompt()
    output = net_connect.send_config_set(lines)
    print(output)
    # dump output to a file for parsing 
    file = open("commandoutput.txt", "a")
    file.write(output)
    file.close


