import math
import pyfiglet
from termcolor import colored
import os
import time
from files import modules
modules.tryclear()
#os.system('cls')
print(colored(pyfiglet.figlet_format("C", font = "isometric1" ), 'red'))
time.sleep(1)
modules.tryclear()
print(colored(pyfiglet.figlet_format("CA", font = "isometric1" ), 'red'))
time.sleep(1)
modules.tryclear()
print(colored(pyfiglet.figlet_format("CAL", font = "isometric1" ), 'red'))
time.sleep(1)
modules.tryclear()
print(colored(pyfiglet.figlet_format("CALC", font = "isometric1" ), 'red'))
time.sleep(1)
modules.tryclear()
print(colored(pyfiglet.figlet_format("CALC", font = "isometric1" ), 'cyan'))

print(colored('I am a can do everything that listed below :\n','red'))
print(colored("\n[1. Currency Convertor ,2. Simple Calculator ,3. Temprature Convertor ,4. Speed Convertor ,5. Factorial Finder ,6. Distance Formula Calculator ,7. Statistics Calculator ,8. Factor Finder ,9. Area Of Triangle [Heron's Formula,Normal Formula] ,10. Quadratic Formula ,11. LCM and HCF Finder]\n\n",'red'))
choice = input(colored('\nTest My Skills [1/2/3/4/5/6/7/8/9/10/11]- ','green'))
if choice == '1':
    exec(open("files/currencyCalc.py").read())
elif choice == '2':
    modules.tryclear()
    #os.system('cls')
    print(pyfiglet.figlet_format("CALC", font = "3-d" ))
    print('------------------------------------------')
    toeval = input('Enter the Equation : ')
    print(eval(toeval))
elif choice == '3':
    exec(open("files/tempCalc.py").read())
elif choice == '4':
    exec(open("files/speedCalc.py").read())
elif choice == '5':
  modules.tryclear()
  print(pyfiglet.figlet_format('Factorial', font='slant'))
  print('')
  factorial = math.factorial(int(input('Enter the number: ')))
  print(f'Factorial : {factorial}')
elif choice == '6':
  exec(open("files/distCalc.py").read())
elif choice == '7':
  exec(open("files/statsCalc.py").read())
elif choice == '8':
  exec(open("files/factorFinder.py").read())
elif choice == '9':
  exec(open("files/heronsform.py").read())
elif choice == '10':
  exec(open("files/quadform.py").read())
elif choice == '11':
  exec(open('files/lcmnhcf.py').read())
else:
    print('Thanks for taking a whole knowledge-full bucket of calculation for my little big brain calculator.')