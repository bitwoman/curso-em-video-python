# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

total = count_k = count = min = 0

while True:
  product = str(input('Enter a product: ')).strip() 
  price = float(input('Enter a price of product: '))
  count += 1
  total += price

  if price > 1000:
    count_k += 1
  if count == 1:
    min = price
  else:
    if price < min:
      min = price

  option = ' '
  while option not in ('YN'):
    option = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]

  if option == 'N':
    break
  else:
    continue

print(f'Total: {total}')
print(f'How many products that cost more than R$ 1000: {count_k}')
print(f'Product more cheap: {min}')
