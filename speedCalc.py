speedunit = input('From Which  Unit: ')
speedunit2 = input('To which Unit: ')
if speedunit == 'Kmph':
  if speedunit2 == 'mps':
    speed2 = int(input('Enter the Speed in KMPH: '))
    speed3 = speed2 * 5/18
    print('Speed in M/S: ',speed3)
  else:
    print('We will update our server')
elif speedunit == 'mps':
  if speedunit2 == 'kmph':
    speed67 = int('Enter the Speed M/s: ')
    speed57 = speed67 * 18 / 5
    print('Speed in Km/h: ',speed57)
  else:
    print('Invalid Input')
else:
  print('Sorry our database is not so updated')