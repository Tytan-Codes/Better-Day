import os
import colorama
import openai
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
import time
openai.api_key = "YOUR_API_KEY_HERE"



#kjhgasdasdasd
    
    

try:
    
    def Linux():
        os.system('clear')
        print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' System')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' chatGPT')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' Other')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' Start my Day')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Exit')
        
        pick = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))
        
        if pick == 1:
            lixSearch()
        if pick == 2:
            system()
        if pick == 3:
            chatGPT()
        if pick == 4:
            other()
        if pick == 5:
            startDay()
        if pick == 0:
            os.system('clear')
            exit()
        
        else: 
            os.system('clear')
            print(f'{Fore.RED}Invalid Option')


    def lixSearch():
        os.system('clear')
        print(f"""{Fore.WHITE + Style.BRIGHT}  _      _                         _____                     _     
 | |    (_)                       / ____|                   | |    
 | |     _ _ __  _   ___  __     | (___   ___  __ _ _ __ ___| |__  
 | |    | | '_ \| | | \ \/ /      \___ \ / _ \/ _` | '__/ __| '_ \ 
 | |____| | | | | |_| |>  <   _   ____) |  __/ (_| | | | (__| | | |
 |______|_|_| |_|\__,_/_/\_\ (_) |_____/ \___|\__,_|_|  \___|_| |_|
                                                                   
                                                                   """)
        print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search Amazom.com')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search DuckDuckGo')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search Youtube')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search NewEgg')        
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search Google')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'6' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Open VSCODE Web Builder')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Back')
        llixSearch = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))

        if llixSearch == 1:
            var1 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('firefox https://www.amazon.ca/s?k='+var1+'')
            os.system('python3 main.py')
        if llixSearch == 2:
            var2 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('firefox https://duckduckgo.com/?q='+var2+' ')
            os.system('python3 main.py')
        if llixSearch == 3:
            var3 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('firefox https://www.youtube.com/results?search_query='+var3+'')
            os.system('python3 main.py')
        if llixSearch == 4:
            var4 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('firefox https://www.newegg.ca/p/pl?d='+var4+'')
            os.system('python3 main.py')
        if llixSearch == 5:
            var5 = str(input('What would you like to search for. Spaces must be +: '))
            os.system('firefox https://www.google.com/search?q='+var5+'')
            os.system('python3 main.py')
        if llixSearch == 6:
            os.system('firefox vscode.dev')
            os.system('python3 main.py')
        if llixSearch == 0:
            Linux()
        else: 
            os.system('clear')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')
            
            
    def sssystem():
        print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Run train')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' HTOP')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' List directory')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Clone something off of github')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Make a file')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'6' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Run a system command')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Back')
        
        Ssystem = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))          

        
    
        if Ssystem == 1:
            os.system('sl')
            os.system('python3 main.py')
        if Ssystem == 2:
            os.system('htop')
            os.system('python3 main.py')
        if Ssystem == 3:
            var7 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What directory would you like to search? ')))
            os.system('ls '+var7+'')
            os.system('python3 main.py')
        if Ssystem == 4:
            var8 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What would you like to clone? ')))
            os.system('git clone '+var8+'')
            os.system('python3 main.py')
        if Ssystem == 5:
            var9 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'WHat file would you like to make? ')))
            os.system('touch '+var9+'')
            os.system('python3 main.py')
        if Ssystem == 6:
            os.system('clear')
            var10 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What command would you like to run? ')))
            os.system(''+var10+'')
            os.system('python3 main.py')
        if Ssystem == 0:
            Linux()
        else: 
            os.system('clear')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('python3 main.py') 

            
        
        
        
        
#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    def thing():
            os.system('clear')
            print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
            print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search')
            print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' System')
            print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' chatGPT')
            print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' Other')
            print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' Start my Day')
            print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Exit')
            
            pick = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))
            
            if pick == 1:
                search()
            if pick == 2:
                system()
            if pick == 3:
                chatGPT()
            if pick == 4:
                other()
            if pick == 5:
                startDay()
            if pick == 0:
                os.system('clear')
                exit()
            
            else: 
                os.system('clear')
                print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
                time.sleep(3)
                os.system('py main.py')

    def main():
        
        os.system('clear')
        os.system('clear')
        print(Style.BRIGHT + """  ____       _   _                  _____              
 |  _ \     | | | |                |  __ \             
 | |_) | ___| |_| |_ ___ _ __      | |  | | __ _ _   _ 
 |  _ < / _ \ __| __/ _ \ '__|     | |  | |/ _` | | | |
 | |_) |  __/ |_| ||  __/ |     _  | |__| | (_| | |_| |
 |____/ \___|\__|\__\___|_|    (_) |_____/ \__,_|\__, |
                                                  __/ |
                                                 |___/ """)
        print(Style.BRIGHT + 'Author        :   ', Fore.RED + Style.BRIGHT + 'Tytan-Codes')
        print(Style.BRIGHT + 'Code Type     :   ', Fore.RED + Style.BRIGHT + 'Python 3')
        print(Style.BRIGHT + 'Description   :   ', Fore.RED + Style.BRIGHT + 'Cool python things')
        print(Style.BRIGHT + 'Goal          :   ', Fore.RED + Style.BRIGHT + 'Make something COOL')
        print(Style.BRIGHT + 'Github        : ', Fore.RED + Style.BRIGHT +'  github.com/Tytan-Codes')
        print(Style.BRIGHT + 'Version       : ', Fore.RED + Style.BRIGHT + '  1.1 -- Better Day Project')
        print(Style.BRIGHT + '(c) 2022-2033, Tytan-Codes All rights reserved')
        print(Style.BRIGHT + Fore.YELLOW + '* ' + Style.BRIGHT + 'Trust Me It\'s good' + Style.BRIGHT + Fore.RED + ' -- ' + Style.BRIGHT + 'I\'m a CODER' + Style.BRIGHT + Fore.YELLOW + ' *')
        print('')
        enter = input(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '~' + Style.BRIGHT + Fore.YELLOW + '] ' + Style.BRIGHT + Fore.RED + 'Press Enter to Continue...' )

        if enter == "":
            chooseOS()

        else:
            print(Style.BRIGHT + Fore.RED +"THATS NOT ENTER, THAT\'s ", enter)
        

    def search():
        os.system('clear')
        print(f"""{Fore.WHITE + Style.BRIGHT} __          ___              _____                     _     
 \ \        / (_)            / ____|                   | |    
  \ \  /\  / / _ _ __       | (___   ___  __ _ _ __ ___| |__  
   \ \/  \/ / | | '_ \       \___ \ / _ \/ _` | '__/ __| '_ \ 
    \  /\  /  | | | | |  _   ____) |  __/ (_| | | | (__| | | |
     \/  \/   |_|_| |_| (_) |_____/ \___|\__,_|_|  \___|_| |_|
                                                              
                                                              """)
        print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search Amazom.com')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search DuckDuckGo')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search Youtube')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search NewEgg')        
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Search Google')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'6' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Open VSCODE Web Builder')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Back')
        search = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))
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
            thing()
        else: 
            os.system('clear')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')






    def system():
        os.system('clear')
        print(f"""{Fore.WHITE+ Style.BRIGHT} __          ___              _____           _                 
 \ \        / (_)            / ____|         | |                
  \ \  /\  / / _ _ __       | (___  _   _ ___| |_ ___ _ __ ___  
   \ \/  \/ / | | '_ \       \___ \| | | / __| __/ _ \ '_ ` _ \ 
    \  /\  /  | | | | |  _   ____) | |_| \__ \ ||  __/ | | | | |
     \/  \/   |_|_| |_| (_) |_____/ \__, |___/\__\___|_| |_| |_|
                                     __/ |                      
                                    |___/                       """)
        print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Run train')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' HTOP')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'3' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' List directory')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'4' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Clone something off of github')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'5' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Make a file')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'6' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Run a system command')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Back')
        
        System = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))
        if System == 1:
            os.system('sl')
            os.system('py main.py')
        if System == 2:
            os.system('htop')
            os.system('py main.py')
        if System == 3:
            var7 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What directory would you like to search? ')))
            os.system('ls '+var7+'')
            os.system('py main.py')
        if System == 4:
            var8 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What would you like to clone? ')))
            os.system('git clone '+var8+'')
            os.system('py main.py')
        if System == 5:
            var9 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'WHat file would you like to make? ')))
            os.system('type nul > '+var9+'')
            os.system('py main.py')
        if System == 6:
            os.system('clear')
            var10 = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'What command would you like to run? ')))
            os.system(''+var10+'')
            os.system('py main.py')
        if System == 0:
            thing()
        else: 
            os.system('clear')
            print(f'{Fore.RED + Style.BRIGHT}Please choose a valid input.')
            time.sleep(3)
            os.system('py main.py')
    
    
    def chatGPT():
        os.system('clear')
        print(f'{Fore.RED + Style.BRIGHT}Go to line 8 of the script and put your openAI API key.')
        # Main loop
        while True:
            try:
                # Get user input
                prompt = input(
                    f"{Style.BRIGHT}{Fore.RED}Better Day {Style.BRIGHT}{Fore.YELLOW}> {Style.BRIGHT}{Fore.RED}What would you like to generate? "
                )

                # Call OpenAI API
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.9,
                    max_tokens=2048,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6,
                    stop=[" Human:", " AI:"],
                )

                # Print response
                text = response["choices"][0]["text"]
                print(f"{Fore.GREEN}Reply: {Fore.WHITE}{text}")
            except ApiException as e:
                print(f"{Fore.RED}Error: {Fore.WHITE}{e}")
            except KeyboardInterrupt:
                # Exit gracefully on Ctrl+C
                print(f"{Fore.YELLOW}Exiting...")
                break
    def other():
        os.system('clear')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE + ' Watch a funny video.')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'0' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Back')

        
        oter = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))
        
        if oter == 1:
            os.system('start firefox https://youtube.com/ozzymanreviews')
        if oter == 0:
            thing()
            
        else:
            input('eeeeeeeeeeeeeeeeeeeeeeeeeeee')
    
    def startDay():
        os.system('start firefox https://stackoverflow.com')


    
    
    
    def chooseOS():
        os.system('clear')
        print(Style.BRIGHT + Fore.YELLOW + '[' + Style.BRIGHT + Fore.RED + '#' + Style.BRIGHT + Fore.YELLOW + '] Options:')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'1' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Windows')
        print(Style.BRIGHT + Fore.RED + '   {' + Style.BRIGHT + Fore.WHITE +'2' + Style.BRIGHT + Fore.RED + '}' + Style.BRIGHT + Fore.YELLOW + ' ~> ' +  Style.BRIGHT + Fore.WHITE +' Linux')
    
    
        chooooooose = (int(input(Style.BRIGHT + Fore.RED + 'Better Day ' + Style.BRIGHT + Fore.YELLOW + '> ' + Style.BRIGHT + Fore.RED + 'Choose ')))
        if chooooooose == 1:
            thing()
        if chooooooose == 2:
            Linux()
    
    
    
           

except KeyboardInterrupt:
    os.system('clear')
    print(f'{Fore.RED + Style.BRIGHT}If you are trying to end the script please type zero when you get the popup.')
    time.sleep(3)
    os.system('py main.py')
    
except Exception:
    os.system('clear')
    print(f'{Fore.RED + Style.BRIGHT }Sorry for this error. Please report it to https://github.com/tytan-codes/better-day/issues')
    time.sleep(3)
    os.system('start firefox https://github.com/tytan-codes/better-day/issues')




#args
parser = argparse.ArgumentParser(description='It makes you day easier as a developer. As this script is not finished please make sure to look at the github for the latest updates.')
parser.add_argument('--Windows', action='store_true', help='Go stratight into Windows mode')
parser.add_argument('--Linux', action='store_true', help='Go straight into Linux mode')
args = parser.parse_args()

if args.Windows:
    thing()
if args.Linux:
    Linux()



main()
