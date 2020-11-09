# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
sortedNumber = []

for i in range(0, 5):
  number = int(input('Enter a number: '))

  if number not in sortedNumber:
    if i == 0 or number > sortedNumber[-1]:
      sortedNumber.append(number)
    else:
      j = 0
      while j < len(sortedNumber):
        if number <= sortedNumber[j]:
            sortedNumber.insert(j, number)
            break
        j += 1

print('\n')
print(sortedNumber)
