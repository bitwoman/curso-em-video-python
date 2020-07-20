# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer 
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
number = int(input('Enter a number: '))
term_1 = 0
term_2 = 1
count = 3

print(f'{term_1} -> {term_2}', end='')

while count <= number:
  term_3 = term_1 + term_2
  print(f' -> {term_3}', end='')
  term_1 = term_2
  term_2 = term_3
  count += 1

print('END')
