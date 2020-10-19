# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Enter a number to see the multiplication table: '))

for x in range(1,11):
  mult = n * x 
  print(f'{n} X {x} = {mult}')
