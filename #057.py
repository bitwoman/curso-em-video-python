# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = ''

while sex != 'M' and sex != 'F':
  sex = str(input('Informe seu sexo: ')).upper()

  if sex != 'M' and sex != 'F':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()

print(f'Sexo {sex} registrado com sucesso.')
