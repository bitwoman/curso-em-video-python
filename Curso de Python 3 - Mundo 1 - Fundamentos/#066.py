# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar 
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
# digitados e qual foi a soma entre elas (desconsiderando o flag).
count = sum = number = 0

while True:
  number = int(input('Enter a number: '))
  
  if number == 999:
    break
  else:
    sum += number
    count += 1

print(f'Total of numbers: {count}')
print(f'Sum of all numbers: {sum}')
