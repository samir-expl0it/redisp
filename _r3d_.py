import sys
import os
import socket
import subprocess
import datetime
from datetime import datetime
import colorama
from colorama import Fore, Style, init 
colorama.init()

""" 
  - Documentation
  - just for linux user's ()
  




  
""" 

 

def _display():
  r3d_ = """
  
 |***********************************************************|
 |                                                           |
 |  ➥ dev by @S4M!R                ██████╗ ██████╗ ██████╗   |
 |  ➥ version v0.1                 ██╔══██╗╚════██╗██╔══██╗  |
 |                                 ██████╔╝ █████╔╝██║  ██║  |
 |                                 ██╔══██╗ ╚═══██╗██║  ██║  |
 |                                 ██║  ██║██████╔╝██████╔╝  |
 |                                 ╚═╝  ╚═╝╚═════╝ ╚═════╝   |
 |                                                           |
 *************************************************************

 """

  print(Fore.RED + r3d_)
_display()


remoteServer = input(""" ➥ """)

remoteServerIP = socket.gethostbyname(remoteServer)
print("-" * 60)
print(" WAIT, SCANING IS GOING ON... ", remoteServerIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(" Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print(" You passed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting  ")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
t2 = datetime.now()
total = t2 - t1 
print(" finish scaning in : ", total)















































