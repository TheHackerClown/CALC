import requests
import pyfiglet
import os
os.system('clear')
#os.system('cls')
print(pyfiglet.figlet_format('Currency'))
print('')
print('')
input("Do You Know the Codes Name Of A Country's Currency [i.e. USD, INR, AUD, VND] : \nEnter (Y/n) : ")
print('hmm, you can go but be careful a wrong code and the software...... ')
class Currency_convertor:
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()
		self.rates = data["rates"]
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

#RUNNN
if __name__ == "__main__":
	url = str.__add__('http://data.fixer.io/api/latest?access_key=', '2488fcce4c79a39bbd7b90dd955315bb')
	c = Currency_convertor(url)
	from_country = input("From Country [Enter country code to convert from] : ")
	to_country = input("To Country [Enter country code to convert to]     : ")
	amount = int(input("Amount                                            : "))
  
c.convert(from_country, to_country, amount)
