# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
randomNumber = []
size = 0
exists = False

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

for i in range(0, len(randomNumber)-1):
  if randomNumber[i] != ' ':
    size += 1
    
    if 5 in randomNumber:
      exists = True


randomNumber.sort(reverse=True)
print('\n')
print(f'{size} numbers was entered.')
print(randomNumber)
print(f'5 in the list is: {exists}')
