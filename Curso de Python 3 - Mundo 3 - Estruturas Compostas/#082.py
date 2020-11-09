# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
randomNumber = []
evenNumbers = []
oddNumbers = []

while True:
  randomNumber.append(int(input('Enter a number: ')))
  exit = str(input('Do you want to continue? [Y/N]: ')).upper().strip()

  if exit in 'N':
    break
  
for i in range(0, len(randomNumber)):
  aux = randomNumber[i] 
  if aux != 0 and % 2 == 0:
    evenNumbers.append(aux)
  elif aux % 2 != 0:
    oddNumbers.append(aux)

print(f'\nOriginal list: {randomNumber}\n Even numbers list: {evenNumbers}\n Odd numbers list: {oddNumbers}.')
