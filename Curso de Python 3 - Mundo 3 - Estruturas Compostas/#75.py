# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
randomList = []
timesNine = 0
evenNumbers = []
positionThree = 0

for x in range(0, 4):
    number = int(input('Enter a number: '))
    randomList.append(number)

randomTuple = tuple(randomList)

for x in range(len(randomTuple)):
    if (randomTuple[x] == 9):
        timesNine += 1

    if (randomTuple[x] == 3):
        positionThree = x + 1

    if (randomTuple[x] % 2 == 0 and randomTuple[x] != 0):
        evenNumbers.append(randomTuple[x])

print('\n')
print(f'The entered numbers are: {randomList}')
print(f'The number 9 showed {timesNine} times')
print(f'The first position of Three is {positionThree}')
print(f'The even number (s) is (are) {evenNumbers}')