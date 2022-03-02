import time
import pyfiglet
import os
os.system('clear')
print(pyfiglet.figlet_format('LCM', font = '3-d'))
time.sleep(1)
os.system('clear')
print(pyfiglet.figlet_format('LCM    n', font = '3-d'))
time.sleep(1)
os.system('clear')
print(pyfiglet.figlet_format('LCM    n    HCF', font = '3-d'))
time.sleep(1)
print('')
choice = input('What you Want I will Give: \n1. LCM\n2. HCF\nEnter [1/2]: ')
num1 = int(input('Enter First Number  : '))
num2 = int(input('Enter Second Number : '))
if choice == '1':
  def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
  print("The L.C.M. is", compute_lcm(num1, num2))
if choice == '2':
  def compute_gcd(x, y):
    if x > y:
      lower = y
    else:
      lower = x
    while True:
      if((x % lower == 0) and (y%lower== 0)):
          hcf = lower
          break
      else:
        lower -= 1
    return hcf
  print("The H.C.F. is", compute_gcd(num1, num2))