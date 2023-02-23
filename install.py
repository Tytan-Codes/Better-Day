import os


def ready():
    with open('eula.txt', 'a') as f:
        f.write('yes')
    
    os.system('git clone git clone https://github.com/tytan-codes/better_day.git ')
    os.system('cd better-day')
    os.system('wsl --install')
    os.system('winget install GNU.nano')
    os.system('py -m pip install -r requirments.txt')
    os.system('cls')
    

os.system('cls')
print("""
██████╗░███████╗████████╗████████╗███████╗██████╗░  ██████╗░░█████╗░██╗░░░██╗
██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚██╗░██╔╝
██████╦╝█████╗░░░░░██║░░░░░░██║░░░█████╗░░██████╔╝  ██║░░██║███████║░╚████╔╝░
██╔══██╗██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗  ██║░░██║██╔══██║░░╚██╔╝░░
██████╦╝███████╗░░░██║░░░░░░██║░░░███████╗██║░░██║  ██████╔╝██║░░██║░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░""")
print('Author        :   ', 'Tytan-Codes')
print( 'Code Type     :   ', 'Python 3')
print('Description   :   ', 'Install requirments for my script')
print('By pressing enter to continue, you will also argee to my EULA.')
print('')


enter = input('Press enter to install requirments...')

if enter == "":
    ready()

else:
    print('You can\'t do that')
