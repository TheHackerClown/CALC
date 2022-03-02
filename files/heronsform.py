import math
import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Herons    Formula'))
print('                    ___________________')
print('Formula ----->  --\/s*(s-a)*(s-b)*(s-c)')
print('')
print('')
a = int(input('Enter the Side A : '))
b = int(input('Enter the Side B : '))
c = int(input('Enter the Side C : '))
s = (a+b+c)/2
step1 = s-a
step2 = s-b
step3 = s-c
step4 = s*(step1)*(step2)*(step3)
print('Area After  Square-rooting : ',(step4**(1/2)))
print('Area Before Square-rooting : ',(step4))
