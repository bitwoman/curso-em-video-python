# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Enter a number to calculate the factorial: '))
factorial = 1

while n > 0:
  print(f'{n}', end='')
  print(' x ' if n > 1 else ' = ', end='')
  factorial = factorial * n
  n -= 1

print(factorial)
