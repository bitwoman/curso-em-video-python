# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
term = int(input('Enter a first term: '))
reason = int(input('Enter a reason: '))
count = 0

while count < 10:
  print(f'{term}', end=' -> ')
  count += 1
  term += reason  

print('END')
