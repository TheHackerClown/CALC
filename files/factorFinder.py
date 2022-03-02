import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Factor'))
print('')
print('')
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input('Enter the Number to Find Factor of : '))

print_factors(num)