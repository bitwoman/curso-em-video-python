# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
randomNumber = []

while True:
  number = int(input('Enter the numbers '))

  if number in randomNumber:
      print('This number already exists in the list! Enter another one!')
  elif number not in randomNumber:
    randomNumber.append(number)
    
  string = str(input('Would you like to continue? [Y/N]: ')).upper().strip()
  if string == 'Y':
    continue
  elif string == 'N':
    break

randomNumber.sort()
print(f'\nSorted list: {randomNumber}')
