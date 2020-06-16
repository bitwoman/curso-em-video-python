# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

price_house = float(input('Enter a price of the house: '))
salary = float(input('Enter a salary: '))
paid_years = int(input('Enter how many years you will pay: '))
thirdy_percent = (salary * (30/100))
monthly_payment = (price_house/paid_years)/12 #or price_house/(paid_years*12)

if monthly_payment > thirdy_percent:
  print('Price: %.2f' %monthly_payment)
  print('Loan denied')
else:
  print('Price: %.2f' %monthly_payment)
  sleep(2)
  print('Congratulations! Loan accept!')
