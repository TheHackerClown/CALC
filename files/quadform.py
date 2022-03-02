import re
import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Quadratic    Formula'))
todo = input('What you want to do with the equation:\n1. Finding the Roots\n2. Find The Discriminant\nEnter [1/2] : ')
e = str(input('Enter The Equation [ax2 + bx + c = 0]: '))
eq = e
eqn = eq.split()
repa = eqn[0]
a = repa.replace('x2', '')
a = int(a)
repb = eqn[2]
b = repb.replace('x', '')
b = int(b)
if eqn[1] == '-':
  b = (-1*b)
elif eqn[1] == '+':
  b = (1*b)
repc = eqn[4]
c = int(repc)
if eqn[3] == '-':
  c = (-1*c)
elif eqn[3] == '+':
  c = (1*c)
D = (b**2) - (4*a*c)
if todo == '1':
	if D > 0:
		xone = -(b) + (D**1/2)
		xtwo = -(b) - (D**1/2)
		positiveX = xone / 2*a
		negitiveX = xtwo / 2*a
		print('The solutions are : ',round(positiveX, 2),',',round(negitiveX, 2))
	elif D < 0:
		print('No Real Roots Exist')
	elif D == 0:
		x = -(b)/2*a
		print('The Roots are : ',x,',',x)
	else:
		print('Invalid Input')
elif todo == '2':
  if D > 0:
    print('Real And Distinctive Roots Exist')
  elif D == 0:
    print('Equal Roots Exist')
  elif D < 0:
    print('No Real Roots Exist')
else:
  print('ERROR 404')