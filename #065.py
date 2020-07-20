# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
sum = average = bigger = smaller = count = 0
exit = ''

while exit != 'S':
  number = int(input('Enter a number: '))
  sum += number
  count +=1

  if count == 1:
    bigger = smaller = number
  else:
    if number > bigger:
      bigger = number
    if number < smaller:
      smaller = number
  
  exit = str(input('Do you want to go out? [S/N] ')).strip().upper()[0]

average = sum/count
print(f'\nYou entered {count} numbers.')
print(f'The average of all numbers is {average}.')
print(f'The bigger number is {bigger}. And the smaller number is {smaller}.')
