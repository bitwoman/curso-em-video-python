# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.
#Inicializando com 0's.
matrix = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(0,3):
  for j in range(0,3):
    matrix[i][j] = int(input(f'Enter a number in the position: '))
  
for i in range(0,3):
    for j in range(0,3):
      print(f'[{matrix[i][j]:^5}]', end='')
    print()
