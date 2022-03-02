import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Speed'))
print('')
print('')
speedunit = input('From Which  Unit: ')
speedunit2 = input('To which Unit: ')
kmph = ['kmph', 'KMPH', 'kilometre per hour', 'kilometre ph', 'km per h', 'km/h']
mps = ['mps', 'MPS', 'metre per second', 'metre ps', 'm per s', 'm/s']
if speedunit in kmph:
  if speedunit2 in mps:
    speed2 = int(input(f'Enter the Speed in {speedunit}: '))
    speed3 = speed2 * 5/18
    print(f'Speed in {speedunit2}: ',speed3)
  else:
    print('We will update our server')
elif speedunit in mps:
  if speedunit2 in kmph:
    speed67 = int(input(f'Enter the Speed in {speedunit}: '))
    speed57 = speed67 * 18 / 5
    print(f'Speed in {speedunit2}: ',speed57)
  else:
    print('We will update our server')
else:
  print('We will update our server')