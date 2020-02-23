#IMPORTS
import os, time, sys, socket, getpass
from colorama import Fore, Style, Back

#INFOS
menu = Fore.CYAN+"""
+-------------------------------------------+
|        ___           _ _                  |
|       /   \_ __ ___ (_) |_ _ __ _   _     |
|      / /\ / '_ ` _ \| | __| '__| | | |    |
|     / /_//| | | | | | | |_| |  | |_| |    |
|    /___,' |_| |_| |_|_|\__|_|   \__, |    |
|                                  |___/    |
+-------------------------------------------+
"""+Style.RESET_ALL
tool = "*"
permission = "$"
user = "Geek"


#commands
def clear():
    os.system('clear')
    print(menu)
    command = ""
def exit():
    print(Fore.RED+"You are quitting terminal..."+Style.RESET_ALL)
    time.sleep(1)
    os.system('clear')
    sys.exit()
def list(p="", permission="$"):
    if(p == ""):
        print(Fore.BLUE)
        os.system('ls')
        print(Style.RESET_ALL)
    elif(p == "ranged"):
        print(Fore.BLUE)
        os.system('ls -l')
        print(Style.RESET_ALL)
    elif(p == "all"):
        if(permission == "#"):
            print(Fore.BLUE)
            os.system('ls -a')
            print(Style.RESET_ALL)
        else:
            print(Fore.RED+"You don't have permission"+Style.RESET_ALL)
    elif(p == "*"):
        if(permission == "#"):
            print(Fore.BLUE)
            os.system('ls -al')
            print(Style.RESET_ALL)
        else:
            print(Fore.RED+"You don't have permission"+Style.RESET_ALL)
