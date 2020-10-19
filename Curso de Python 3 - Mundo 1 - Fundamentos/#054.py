# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
current_date = date.today()

count_older = 0
count_minors = 0

for x in range(1,8):
  year = int(input("Enter someone's birth year: "))
  age = current_date.year - year

  if age >= 18:
    count_older += 1
  else:
    count_minors += 1

print(f'Olders: {count_older}\nMinors: {count_minors}')
