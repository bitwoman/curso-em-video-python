#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
number = float(input('how much money do you have in your wallet?'))
dollar = 5.10
rate = number/dollar

print('You can to buy %.2f dollars with your money!' % rate)
