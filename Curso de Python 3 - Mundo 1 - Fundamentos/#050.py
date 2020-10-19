# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
sum = 0
count = 0

for x in range(1,7):
  n = int(input('Enter a number: '))

  if n % 2 == 0:
    sum += n
    count += 1

print(count, sum)
