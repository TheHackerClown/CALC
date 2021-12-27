print('Note : This Repl Converts Into Farenheit, Celcius, Kelvin Only.')
temp1 = input('From Which Unit: ')
temp2 = input('To Which Unit: ')
if temp1 == 'F':
  if temp2 == 'C':
            feren = int(input('Enter the Temprature in Farenheit: '))
            cel = (feren - 32) * 5 / 9
            print('Temprature in Celsius: ',cel)
        elif temp2 == 'K':
            feren1 = int(input('Enter the Temprature in Farenheit: '))
            kel = (feren1 - 32) * 5/9 + 273.15
            print('Temprature in Kelvin: ',kel)
        else:
            print('Invalid Input')
elif temp1 == 'C':
        
        if temp2 == 'F':
            cel1 = int(input('Enter Temprature in Celsius: '))
            feren1 = (cel1 * 9/5) + 32
            print('Temprature in Farenheit: ',feren1)
        elif temp2 == 'K':
            cel2 = int(input('Enter Temprature in Celsius: '))
            kel1 = cel2 + 273.15
            print('Temprature in Kelvin: ',kel1)
        else:
            print('Invalid Input')
elif temp1 == 'K':
        
        if temp2 == 'F':
            kel5 = int(input('Enter Temprature in Kelvin: '))
            feren5 = (kel5 - 273.15) * 9 / 5 + 32
            print('Temprature in Farenheit: ',feren5)

        elif temp2 == 'C':
            kel6 = int(input('Enter Temprature in Kelvin: '))
            cel6 = kel6 - 273.15
            print('Your Temprature in Celsius: ',cel6)

        else:
            print('Invalid Input')
    else:
        print('We will update our database soon')
else:
  print('Sorry Our sytem is not so updated.')