currency1 = input('From Which Currency- ')
currency2 = input('TO Which Currency- ')
if currency1 == 'USD':
  if currency2 == 'INR':
    usd = 73.36
    usd = float(usd)
    currency3 = int(input('Enter The Amount In Dollar: '))
    currency4 = usd * currency3
    print('Your Currency Value in INR is : ',currency4)
  else:
    print('We Will Update The Database SO you can convert Currency.')
elif currency1 == 'INR':
  if currency2 == 'USD':
    inr = 0.014
    inr = float(inr)
    currency3 = int(input('Enter The Amount In Ruppees: '))
    currency4 = inr * currency3
    print('Your Currency Value in USD is : ',currency4)