import os
import sys
import sys
import colorama
import openai
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
import time
import traceback
from tqdm import tqdm



   
    
    
    
#args
parser = argparse.ArgumentParser(description='This is a script that will make your day faster.')
args = parser.parse_args()

try:
    def main():
        os.system('cls')
        print(f'{Fore.RED + Style.BRIGHT}Checking Directories...')
        for i in tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]):
            time.sleep(0.05)
        print(f'{Fore.RED + Style.BRIGHT}Checking Dependencies...')
        for i in tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]):
            time.sleep(0.05)
        os.system('cls')
        os.system('cls')
        print("""
██████╗░███████╗████████╗████████╗███████╗██████╗░  ██████╗░░█████╗░██╗░░░██╗
██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚██╗░██╔╝
██████╦╝█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝  ██║░░██║███████║░╚████╔╝░
██╔══██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗  ██║░░██║██╔══██║░░╚██╔╝░░
██████╦╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║  ██████╔╝██║░░██║░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░""")
        print(Style.BRIGHT + 'Author        :   ', Fore.RED + Style.BRIGHT + 'Tytan-Codes')
        print(Style.BRIGHT + 'Code Type     :   ', Fore.RED + Style.BRIGHT + 'Python 3')
        print(Style.BRIGHT + 'Description   :   ', Fore.RED + Style.BRIGHT + 'Make something COOL')
        print(Style.BRIGHT + Fore.YELLOW + '* ' + Style.BRIGHT + 'Trust Me It\'s good' + Style.BRIGHT + Fore.RED + ' -- ' + Style.BRIGHT + 'I\'m a CODER' + Style.BRIGHT + Fore.YELLOW + ' *')
        print('')
        enter = input(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '~' + Style.BRIGHT + Fore.YELLOW + '] ' + Style.BRIGHT + Fore.RED + 'Press Enter to Continue...' )

        if enter == "":
            pass

        else:
            print(Style.BRIGHT + Fore.RED +"THATS NOT ENTER, THAT\'s ", enter)
            
        os.system('cls')
        print(f'{Fore.RED}(1) Search')
        print(f'{Fore.RED}(2) System')
        print(f'{Fore.RED}(3) ChatGPT')
        print('(0) Exit')
        
        pick = (int(input(f'{Fore.GREEN}What would you like to do? ')))
        
        if pick == 1:
            search()
        if pick == 2:
            system()
        if pick == 3:
            chatGPT()
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
        print(f'{Fore.RED}(1) Search Amazon.com')
        print(f'{Fore.RED}(2) Search DuckDuckGo')
        print(f'{Fore.RED}(3) Search YouTube')        
        print(f'{Fore.RED}(4) Search NewEgg')
        print(f'{Fore.RED}(5) Search Google')
        print(f'{Fore.RED}(6) VSCODE Web Builder')
        print('(0) Quit')
        search = int(input(f'{Fore.GREEN}What do you want to do: '))
        if search == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.amazon.ca/s?k='+var1+'')
            os.system('py main.py')
        if search == 2:
            var2 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://duckduckgo.com/?q='+var2+' ')
            os.system('py main.py')
        if search == 3:
            var3 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.youtube.com/results?search_query='+var3+'')
            os.system('py main.py')
        if search == 4:
            var4 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.newegg.ca/p/pl?d='+var4+'')
            os.system('py main.py')
        if search == 5:
            var5 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('start firefox https://www.google.com/search?q='+var5+'')
            os.system('py main.py')
        if search == 6:
            os.system('start firefox vscode.dev')
            os.system('py main.py')
        if search == 0:
            os.system('cls')
            sys.exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')






    def system():
        os.system('cls')
        print(f"""{Fore.WHITE}
░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝""")
        print(f'{Fore.RED}(1) Run train')
        print(f'{Fore.RED}(2) HTOP')
        print(f'{Fore.RED}(3) List directory')
        print(f'{Fore.RED}(4) Clone somthing off of Github.')
        print(f'{Fore.RED}(5) Make a File')
        print(f'{Fore.RED}(6) Run system command')
        print(f'{Fore.WHITE}(0) Quit')
        System = (int(input(f'{Fore.GREEN}What would you like to do: ')))
        if System == 1:
            os.system('sl')
            os.system('py main.py')
        if System == 2:
            os.system('htop')
            os.system('py main.py')
        if System == 3:
            var7 = str(input(f'{Fore.GREEN}What directory would you like to search: '))
            os.system('ls '+var7+'')
            os.system('py main.py')
        if System == 4:
            var8 = str(input(f'{Fore.GREEN}What would you like to clone: '))
            os.system('git clone '+var8+'')
            os.system('py main.py')
        if System == 5:
            var9 = str(input(f'{Fore.GREEN}What file would you like to make. EX text.txt: '))
            os.system('type nul > '+var9+'')
            os.system('py main.py')
        if System == 6:
            os.system('cls')
            var10 = str(input(f'{Fore.GREEN}What command would you like to run: '))
            os.system(''+var10+'')
            os.system('py main.py')
        if System == 0:
            os.system('cls')
            exit()
        else: 
            os.system('cls')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')
    
    
    def chatGPT():
        os.system('cls')
        print(f'{Fore.RED + Style.BRIGHT}Go to line 179 of the script and put your openAI API key.')
        while True:
            openai.api_key = 'YOUR openAI API KEY HERE'
            ask = str(input(f'{Fore.WHITE}What would you like to generate? '))
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=ask,
                temperature=0.9,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
                )

            text = response['choices'][0]['text']
            print ('Reply: '+text)
                

    



    
    
    

    
    
    
           

except KeyboardInterrupt:
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT}If you are trying to end the script please type zero when you get the popup.')
    time.sleep(3)
    os.system('py main.py')
    
except Exception:
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT }Sorry for this error. Please report it to https://github.com/tysudo/better_day-0.0.1/issues')
    time.sleep(3)
    os.system('start firefox https://github.com/tysudo/better_day-0.0.1/issues')




main()
