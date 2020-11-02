# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
randomNumbers = []
bigger = smaller = 0

for n in range(0,5):
  number = int(input('Enter a number: '))
  randomNumbers.append(number)

for n in range(0, len(randomNumbers)):
  if randomNumbers[n] > 0:
    if randomNumbers[n] == 1:
      bigger = randomNumbers[n]
      smaller = randomNumbers[n]
    else:
      if randomNumbers[n] > bigger:
          bigger = randomNumbers[n]
      if randomNumbers[n] < smaller:
        smaller = randomNumbers[n]

indexBigger = randomNumbers.index(bigger, 0, len(randomNumbers))
indexSmaller = randomNumbers.index(smaller, 0, len(randomNumbers))

print(f'\nBigger number: {bigger} and his position: {indexBigger}')
print(f'Smaller number: {smaller} and his position: {indexSmaller}')
