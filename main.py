import math
print('Hello Mister')
print('I am a ...... Everything you want as Calculator [Version 1.5 with little updates]')
print('What do you want:')
print('1. Currency Convertor \n2. Divider Which says everything \n3. Arithematic Calculator \n4. Temprature Convertor\n5. Speed Convertor \n6. Factorial Finder\n7. Distance Formula Calculator\n8. Statistics Calculator\n9. Factor Finder')
choice = input('User@Calc~#~ ')
if choice == '1':
    exec(open("usdtoinr.py").read())
elif choice == '2':
    exec(open("opendivider.py").read())
elif choice == '3':
    exec(open("mathsCalc.py").read())
elif choice == '4':
    exec(open("tempCalc.py").read())
elif choice == '5':
    exec(open("speedCalc.py").read())
elif choice == '6':
	num2345 = int(input('Enter the number: '))
	print('Factorial: ',math.factorial(num2345))
elif choice == '7':
  exec(open("distCalc.py").read())
elif choice == '8':
  exec(open("statsCalc.py").read())
else:
    print('Thanks for using me. \n Credits- Dhruv Pratap Singh,@TheHackerClown,ME-@dhruvpratap(both are my accounts)')
