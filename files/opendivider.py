import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Divider'))
print('I dont know what i am doing')
print('')
print('')
x = int(input('Enter The Divisor: '))
y = int(input('Enter The Dividend: '))
quotient = y // x
remainder = y % x
print('Divisor   : ',x)
print('Dividend  : ',y)
print('Remainder : ',remainder)
print('Quotient  : ',quotient)