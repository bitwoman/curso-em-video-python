# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = ''

while sex != 'M' and sex != 'F':
  sex = str(input('Enter your sex: ')).upper()

  if sex != 'M' and sex != 'F':
    sex = str(input('Invalid. Please, enter your sex: ')).upper()

print(f'Sex {sex} registred with success.')
