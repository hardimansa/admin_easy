from netmiko import ConnectHandler
from getpass import getpass




uname = input("Username: ")
pythonpassword= getpass("Password: ")






with open('commands.txt') as f:
        commands = f.read().splitlines()

 
with open(file="routerlist.txt", mode="r") as hosts:
               devices = [
                    {
                        "device_type": "cisco_xe",
                        "ip": ip,
                        "username": uname,
                        "password": pythonpassword,
                    # no need for sesssion log with output section below -  "session_log": ip
                    }
                    for ip in hosts.read().splitlines()
                ]


def ex_connect():
    for device in devices: 
        print(f'Connecting to {device["ip"]}')  
        net_connect = ConnectHandler(**device)
        print(f'Connected to {device["ip"]}')  
        output = net_connect.send_config_set(commands)
        print(output)
        file = open(f'commands_{device["ip"]}', "a")
        file.write(output)
