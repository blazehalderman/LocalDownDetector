from colorama import Fore, Back, Style
import socket
import os

VALID = 0

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)
def local_down_detector (VALID):
    while (True):
        runtime_variable = os.system('cmd /c "ping -c 1 '+ ip_address+'" | find "Reply" > nul')
        if (runtime_variable == 0 and VALID != 1):
            print(" Network is: \033[92m Active!")
            print(Style.RESET_ALL)
            VALID = 1

        elif (runtime_variable != 0):
            print("Network is " + Fore.RED + "Inactive!")
            print(Style.RESET_ALL)
            VALID = 0
        else:
            continue

local_down_detector(VALID)