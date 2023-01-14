import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
import time
import traceback
#args
parser = argparse.ArgumentParser(description='This is a script that will make your day faster.')
args = parser.parse_args()

try:
    def main():
        os.system('cls')
        print("""
    ██████╗░███████╗████████╗████████╗███████╗██████╗░  ██████╗░░█████╗░██╗░░░██╗
    ██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚██╗░██╔╝
    ██████╦╝█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝  ██║░░██║███████║░╚████╔╝░
    ██╔══██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗  ██║░░██║██╔══██║░░╚██╔╝░░
    ██████╦╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║  ██████╔╝██║░░██║░░░██║░░░
    ╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

    ░█████╗░░░░░█████╗░░░░░░███╗░░
    ██╔══██╗░░░██╔══██╗░░░░████║░░
    ██║░░██║░░░██║░░██║░░░██╔██║░░
    ██║░░██║░░░██║░░██║░░░╚═╝██║░░
    ╚█████╔╝██╗╚█████╔╝██╗███████╗
    ░╚════╝░╚═╝░╚════╝░╚═╝╚══════╝""")
        print(f'{Fore.RED}(1) Search')
        print('(0) Exit')
        
        pick = (int(input(f'{Fore.GREEN}What would you like to do? ')))
        
        if pick == 1:
            search()
        if pick == 0:
            os.system('cls')
            exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')


    def search():
        os.system('cls')
        print(f"""{Fore.WHITE}
    ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
    ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
    ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
    ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
    ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""")
        print(f'{Fore.RED}(1)Search Amazon.com')
        print(f'{Fore.RED}(2)Search DuckDuckGo')
        print(f'{Fore.RED}(3)Search YouTube')        
        print(f'{Fore.RED}(4)Search NewEgg')
        print(f'{Fore.RED}(5)Search Google')
        print(f'{Fore.RED}(6)VSCODE Web Builder')
        print('(0)Quit')
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
        if search == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start chrome https://www.amazon.ca/s?k='+var1+'')
            os.system('py main.py')
        if search == 2:
            var2 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start chrome https://duckduckgo.com/?q='+var2+' ')
            os.system('py main.py')
        if search == 3:
            var3 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start chrome https://www.youtube.com/results?search_query='+var3+'')
            os.system('py main.py')
        if search == 4:
            var4 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start chrome https://www.newegg.ca/p/pl?d='+var4+'')
            os.system('py main.py')
        if search == 5:
            var5 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start chrome https://www.google.com/search?q='+var5+'')
            os.system('py main.py')
        if search == 6:
            os.system('start chrome vscode.dev')
            os.system('py main.py')
        if search == 0:
            os.system('cls')
            sys.exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')

        
    main()

except KeyboardInterrupt:
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT}If you are trying to end the script please type zero when you get the popup.')
    time.sleep(3)
    os.system('py main.py')
    
except Exception:
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT }Sorry for this error. Please report it to https://github.com/tysudo/better_day-0.0.1/issues')
    os.system('start chrome https://github.com/tysudo/better_day-0.0.1/issues')
