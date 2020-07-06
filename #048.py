# Exercício Python 048: Faça um programa que calcule a soma entre todos os números 
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.
sum = 0
count = 0

for x in range(1, 501):
    if x % 2 != 0:
      if x % 3 == 0:
        sum += x
        count += 1

print(f'{count} {sum}', end=' ')
