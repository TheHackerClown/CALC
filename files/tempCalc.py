import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Temprature'))
print('')
print('')
print('Note : This Repl Converts Into Farenheit, Celcius, Kelvin Only.')
temp1 = input('From Which Unit [C/F/K] : ')
temp2 = input('To   Which Unit [C/F/K] : ')
val = int(input('Enter The Temprature To Convert : '))
def conv_temp(val, temp1, temp2):
  if temp1 == 'C':
    if temp2 == 'F':
      val = (val * (1.8)) + 32
    elif temp2 == 'K':
      val = val + 273.15
  elif temp1 == 'F':
    if temp2 == 'C':
      val = (val-32)*(5/9)
    elif temp2 == 'K':
      val = ((val-32)*(5/9))+273.15
  elif temp1 == 'K':
    if temp2 == 'C':
      val = val - 273.15
    elif temp2 == 'F':
      val = (val - 273.15) * 9/5 + 32
  return val
  
print(f'Temprature in {temp2} : ',conv_temp(val, temp1, temp2))