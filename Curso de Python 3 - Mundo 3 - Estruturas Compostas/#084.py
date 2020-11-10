# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
people = [] 
mainPeople = []
bigger = smaller = 0

while True:
  people.append(str(input('Enter a name: ')))
  people.append(float(input('Enter a weight: ')))

  if len(mainPeople) == 0:
    bigger = smaller = people[1]
  else:
    if people[1] > bigger:
      bigger = people[1]
    if people[1] < smaller:
      smaller = people[1]

  mainPeople.append(people[:])
  people.clear()

  exit = str(input('Do you want to continue? [Y/N] ')).upper().strip()
  if exit == 'N':
    break
  
print('\n')
print(f'Registered people: {len(mainPeople)}')
print(f'Smaller weight: {smaller}')
print(f'Bigger weight: {bigger}')
