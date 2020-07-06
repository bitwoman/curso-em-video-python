# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
print('{:=^40}'.format(' 10 TERMS OF A.P '))
first_term = int(input('Enter a first term: '))
reason = int(input('Enter a reason: '))
last_term = first_term + (10 - 1) * reason

for x in range(first_term, last_term + reason, reason):
  print(f'{x}', end=' -> ')

print("It's over.")
