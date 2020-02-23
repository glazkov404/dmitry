from settings import *

os.system('clear')

print(menu)


while(True):
    terminal = "["+Fore.BLUE+tool+Style.RESET_ALL+"]"+Fore.CYAN+"@"+user+Style.RESET_ALL+"~"+Fore.RED+permission+Style.RESET_ALL+" "
    command = raw_input(terminal).split()
    n = len(command)
    if(n > 0):
        if(command[0] == "su"):
            if(n == 2):
                if(command[1] == "root"):
                    password = getpass.getpass("Password for [root] ->")
                    if(password == "dmitri404"):
                        user = "Dmitri"
                        permission = "#"
                        print(Fore.BLUE+"Welcome back Dmitri"+Style.RESET_ALL)
                        time.sleep(1)
                        clear()
                    else:
                        print(Fore.RED+"Wrong password"+Style.RESET_ALL)
                        time.sleep(1)
                elif(command[1] == "geek"):
                    permission = "$"
                    user = "Geek"
                    clear()
                else:
                    print(Fore.RED+"Incorrect user"+Style.RESET_ALL)
            else:
                print(Fore.RED+"Need argument"+Style.RESET_ALL)
        elif(command[0] == "clear"):
            clear()
        elif(command[0] == "exit"):
            exit()
        elif(command[0] == "list"):
            if(n == 1):
                list()
            elif(n == 2):
                list(command[1], permission)
            else:
                print(Fore.RED+"Too much argument"+Style.RES)
        elif(command[0] == "connect"):
            if(n == 2):
                try:
                    os.system('ping -ac 5 '+command[1])
                except:
                    print("No connection")
            elif(n >= 2):
                print(Fore.RED+"Too much argument")
            else:
                print("Please input DNS")
        elif(command[0] == "getip"):
            if(n == 2):
                try:
                    ip = socket.gethostbyname(command[1])
                    print("["+Fore.CYAN+command[1]+Style.RESET_ALL+"] : "+Fore.RED+ip+Style.RESET_ALL)
                except:
                    print(Fore.RED+"Invalid domain"+Style.RESET_ALL)
            else:
                print(Fore.RED+"Need argument"+Style.RESET_ALL)
        else:
            print("Unknow command")
    else:
        pass
