# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
numbers = []

for x in range(1,6):
  weight = float(input('Enter a weight: '))
  numbers.append(weight)

bigger = max(numbers)
smaller = min(numbers)

print(f'Bigger: {bigger}\nSmaller: {smaller}') 


# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#2ª FORMA:
bigger = 0
smaller = 0

for x in range(1,6):
  weight = float(input('Enter a weight: '))

  if x == 1:
    bigger = weight
    smaller = weight
  else:
    if weight > bigger:
      bigger = weight
    if weight < smaller:
      smaller = weight

print(f'Bigger: {bigger}\nSmaller: {smaller}') 
