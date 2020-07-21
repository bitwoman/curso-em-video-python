# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
f = m = older = 0

while True:
  age = int(input('Enter a age: '))
  sex = ' '

  while sex not in 'FM':
    sex = str(input('Enter a sex: [F/M]')).strip().upper()[0]

    if age > 18:
      older += 1
    if sex == 'M':
      m += 1
    if sex == 'F' and age < 20:
      f += 1

  to_continue = ' '
  while to_continue not in 'YN':
    to_continue = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
  
  if to_continue == 'N':
    break 
  else:
    continue
  
print(f'Older people: {older}')
print(f'Men: {m}')
print(f'Women under 20 years old: {f}')
