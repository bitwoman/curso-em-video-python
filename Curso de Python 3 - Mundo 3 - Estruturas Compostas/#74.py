# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
randomList = []
bigger = 0
smaller = 0

for x in range(0, 5):
  randomNumber = random.randrange(0,100)
  randomList.append(randomNumber)

randomTuple = tuple(randomList)
print(f'The tuple is: {randomTuple}')

for x in range(0, len(randomTuple)):
  if(randomTuple[x] > 0):
      if(randomTuple[x] > bigger):
          bigger = randomTuple[x]

      if(randomTuple[x] < smaller):
          smaller = randomTuple[x]

print(f'The bigger number is: {bigger}')
print(f'The smaller number is: {smaller}')