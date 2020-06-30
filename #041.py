# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
current_date = date.today()

birth_year = int(input('Enter your birthday year: '))
age = (current_date.year - birth_year)

if age <= 9:
  print(f'You are {age} years old!')
  print('little!')
elif age > 9 and age <= 14:
  print(f'You are {age} years old!')
  print('childish!')
elif age > 14 and age <= 19:
  print(f'You are {age} years old!')
  print('junior!')
elif age > 19 and age <=25:
  print(f'You are {age} years old!')
  print('senior!')
else:
  print(f'You are {age} years old!')
  print('master')
