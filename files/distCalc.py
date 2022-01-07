print('OUR MOTIVE IS TO FIND USING THIS:')
print("  ____________________________")
print("\/ (x2 - x1)**2 + (y2 - y1)**2")
x1 = int(input('Enter the Value of X of co-ordinate 1 : '))
y1 = int(input('Enter the Value of Y of co-ordinate 1 : '))
x2 = int(input('Enter the Value of X of co-ordinate 2 : '))
y2 = int(input('Enter the Value of Y of co-ordinate 2 : '))
firstpart = (x2 - x1)**2
secondpart = (y2 - y1)**2
printpart = firstpart + secondpart
print('  ____________________')
print('\/ ',firstpart," + ",secondpart,"  ")
print('                _______')
print('Your Answer : \/ ',printpart,'    ')