import sys

## ex option, reads function from ex_connect.py

ex = input("Do you want to modify the ex?  ")
if ex == ('yes'):
       from ex_connect import ex_connect
       print("Connecting to hosts in routerlist.txt, exiting when complete")
       ex_connect()
       sys.exit()

elif ex ==(''):
       pass


## ex2 option, reads function from ex2_connect.py

ex2 = input("Do you want to modify a ex2 SW?  ")
if boc == ('yes'):
      from ex2_connect import ex2_connect
      print("Connecting to the selected ex2, exiting when complete")
      ex2_connect()
      sys.exit()

elif ex2 ==(''):
      pass


## ex2-FW (ex2 and ex3) option, reads function from ex3_connect.py - assumes 0.1 ip for management interface 

fw = input("Do you want to modify a FW?  ")
if fw == ('yes'):
      from ex3_connect import ex3_connect
      print("Connecting to the ex3 firewall, exiting when complete")
      ex3_connect()
      sys.exit()

else:
      print('No selection made, exiting')
      sys.exit()








