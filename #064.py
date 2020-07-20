# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
count = sum = number = 0

while number != 999:
  number = int(input('Enter a number: '))
  
  if number != 999:
    sum += number
    count += 1
  else:
    continue

print(f'Total of numbers: {count}')
print(f'Sum of all numbers: {sum}')
