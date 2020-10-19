#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float(input('Enter product price: '))
discount = price * 0.05
new_price = price - discount

print('New product price is: %.2f' %new_price)
