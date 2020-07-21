# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada 
# valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
table = 0

while True:
  number = int(input('Enter a number: '))
  print('-' * 17)

  if number < 0:
    print('PROGRAM CLOSED!')
    break
  else:
    for x in range(1,11):
      table = number * x
      print(f'{number} x {x} = {table}')
    print('-' * 17)
