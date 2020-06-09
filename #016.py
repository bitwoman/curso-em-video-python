#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
number = float(input('Enter a float number: '))
print(f'{round(number)} is yours int number')

'''or:
from math import trunc
number = float(input('Enter a float number: '))
print('{}'.format(number, trunc(number)))
print('{}'.format(number, int(number)))
'''
