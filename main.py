import math
import requests
import json
import pyfiglet
import os
import time
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format("C", font = "isometric1" ))
time.sleep(1)
os.system('clear')
print(pyfiglet.figlet_format("CA", font = "isometric1" ))
time.sleep(1)
os.system('clear')
print(pyfiglet.figlet_format("CAL", font = "isometric1" ))
time.sleep(1)
os.system('clear')
print(pyfiglet.figlet_format("CALC", font = "isometric1" ))
time.sleep(1)
os.system('clear')
print(pyfiglet.figlet_format("CALC", font = "isometric1" ))
time.sleep(1)
print('I am a ...... Everything you want as Calculator [Made VERY EASILY]')
print('What do you want:')
print("1. Currency Convertor \n2. Divider Which says everything \n3. Simple Calculator \n4. Temprature Convertor\n5. Speed Convertor \n6. Factorial Finder\n7. Distance Formula Calculator\n8. Statistics Calculator\n9. Factor Finder\n10. Area Of Triangle [Heron's Formula]\n11. Quadratic Formula\n12. LCM and HCF Finder")
choice = input('Enter Your Choice [1/2/3/4/5/6/7/8/9/10/11/12]- ')
if choice == '1':
    exec(open("files/currencyCalc.py").read())
elif choice == '2':
    exec(open("files/opendivider.py").read())
elif choice == '3':
    os.system('clear')
    #os.system('cls')
    print(pyfiglet.figlet_format("CALC", font = "3-d" ))
    print('------------------------------------------')
    toeval = input('Enter the Equation : ')
    print(eval(toeval))
elif choice == '4':
    exec(open("files/tempCalc.py").read())
elif choice == '5':
    exec(open("files/speedCalc.py").read())
elif choice == '6':
  os.system('clear')
  print(pyfiglet.figlet_format('Factorial', font='slant'))
  print('')
  factorial = math.factorial(int(input('Enter the number: ')))
  print(f'Factorial : {factorial}')
elif choice == '7':
  exec(open("files/distCalc.py").read())
elif choice == '8':
  exec(open("files/statsCalc.py").read())
elif choice == '9':
  exec(open("files/factorFinder.py").read())
elif choice == '10':
  exec(open("files/heronsform.py").read())
elif choice == '11':
  exec(open("files/quadform.py").read())
elif choice == '12':
  exec(open('files/lcmnhcf.py').read())
else:
    print('Thanks for using me. \n Credits- Dhruv Pratap Singh,@TheHackerClown')