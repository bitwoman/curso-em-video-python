# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = str(input('Enter your sex [F/M]: ')).strip().upper()[0]

while sex != 'M' and sex != 'F':
  sex = str(input('Invalid. Please, enter your sex: ')).strip().upper()[0]

print(f'Sex {sex} registred with success.')
