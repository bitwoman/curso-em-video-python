# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
avr = 0
count_w = 0
older_man = 0
older_man_name = ''

for x in range(1,5):
  print(f'===={x}ª person====')
  name = str(input('Enter a name: '))
  age = int(input('Enter a age: '))
  sex = str(input('Enter a sex: '))

  avr += age/4

  if x == 1 and sex == 'm' or sex == 'M': #or sex in 'Mm:'
    older_man = age
    older_man_name = name
  else:
    if age > older_man and sex == 'm' or sex == 'M':
      older_man = age
      older_man_name = name

  if age < 20:
    if sex == 'f' or sex == 'F':
      count_w += 1 
      
print('=====================')  
print(f"Average's age: {avr}")
print(f'{older_man_name}')
print(f'Women under 20 years old: {count_w}')
