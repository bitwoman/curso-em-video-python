# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, e 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
current_date = date.today()

birth_year = int(input('Enter your birthday year: '))
age = (current_date.year - birth_year)

print(f'You are {age} years old!')

if age < 18:
  time_left = (18 - age)
  year_enlistment = (current_date.year + time_left)
  
  print(f'You must enlist in {time_left} years!')
  print(f'Your enlistment is in {year_enlistment}!')
elif age > 18:
  time_left = (age - 18)
  year_enlistment = (current_date.year - time_left)
  
  print(f'You should have enlist in {time_left} years!')
  print(f'Your enlistment was in {year_enlistment}!')
else:
  print(f'You are 18 years old now!')
  print(f'You have to enlist IMMEDIATELY!')
