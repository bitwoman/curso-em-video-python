# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

number_1 = int(input('Enter a first number: '))
number_2 = int(input('Enter a second number: '))

if number_1 > number_2:
  print('The first number is bigger')
elif number_2 > number_1:
  print('The second number is bigger')
else:
  print('The both numbers are equals')
