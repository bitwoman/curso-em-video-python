# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
weight = float(input('Enter a number of your weight: '))
height = float(input('Enter a number of your height: '))
imc = weight/(height**2) #or import math -> math.pow(x, y)

print('Your imc is %.1f' %imc)

if imc < 18.5:
  print('Under weight!')
elif imc >= 18.5 and imc <=25:
  print('Ideal weight!')
elif imc > 25 and imc <=30:
  print('Overweight!')
elif imc >= 30 and imc <=40:
  print('Obesity!')
else:
  print('Morbid obesity!')
