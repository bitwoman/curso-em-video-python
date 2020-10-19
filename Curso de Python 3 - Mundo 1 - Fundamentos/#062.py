# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer 
# mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
term = int(input('Enter a first term: '))
reason = int(input('Enter a reason: '))
count =  total = 0
more = 10

while more !=0:
  total += more
  while count < total:
    print(f'{term} -> ', end='')
    count += 1
    term += reason 

  print('PAUSE')
  more = int(input('How many terms do you want to show? '))

print('END')
print(f'Total of terms: {count}')
