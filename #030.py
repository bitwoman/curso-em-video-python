# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
number = int(input('Enter any number: '))

if number % 2 == 0: #or if 2*int(n/2) == n
  print('Even number!')
else:
  print('Odd number!')
