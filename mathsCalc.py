print('What DO you want to do \n1. Add \n2. Subtract \n3. Divide \n4. Multiply')
epoxy = input('Enter Your Choice [1/2/3/4]: ')
num1 = int(input('Enter the First Number: '))
num2 = int(input('Enter the Second Number: '))
if epoxy == '1':
  sum1 = num1 + num2
  print('Your Sum :',sum1)
elif epoxy == '2':
  sub1 = num1 - num2
  print('Your Subtract: ',sub1)
elif epoxy == '3':
  div1 = num1 / num2
  print('Your Divide: ',div1)
elif epoxy == '4':
  multi1 = num1 * num2
  print('Your Multiply: ',multi1)
else:
  print('Invalid Input')