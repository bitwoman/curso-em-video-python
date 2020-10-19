# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
count = 0
n = int(input('Enter a number: '))

for x in range(1, n + 1):
  if n % x == 0:
    print(f'\033[33m{x}\033[m', end=' ')
    count += 1
  else:
    print(f'\033[32m{x}\033[m', end=' ')
  
print(f'\n\033[0;0mThe number was divided by {count}')
if count > 2:
  print('\033[0;0mThis number isnt prime')
else:
  print('\033[0;0mThis number is prime, because it is divisible for two numbers: 1 and himself.')
