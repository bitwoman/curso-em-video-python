# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados; A soma dos valores da terceira coluna.; O maior valor da segunda linha.
matrix = [[0,0,0], [0,0,0], [0,0,0]]
sumEven = sumThirdColumn = biggest = smallest = 0

for i in range(0,3):
  for j in range(0,3):
    matrix[i][j] = int(input(f'Enter a number in the position [{i}][{j}]: '))

    if(matrix[i][j] % 2 == 0):
      sumEven += matrix[i][j]

    if(j == 2):
      sumThirdColumn +=  matrix[i][j]

    if(j == 1):
      if matrix[i][j] == 1:
        biggest = matrix[i][j]
        smallest = matrix[i][j]
      else:
        if matrix[i][j] > biggest:
          biggest = matrix[i][j]
        if matrix[i][j] < smallest:
          smallest = matrix[i][j]

print('\n')

for i in range(0,3):
  for j in range(0,3):
       print(f'[{matrix[i][j]:^5}]', end='')
  print()

print('\n')

print(f'The sum of all even numbers: {sumEven}')
print(f'The sum off all numbers of third column: {sumThirdColumn}')
print(f'The bigest number in the second column: {biggest}')
