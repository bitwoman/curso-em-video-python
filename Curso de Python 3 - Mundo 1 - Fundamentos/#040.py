# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
note_1 = float(input('Enter your first note: '))
note_2 = float(input('Enter your second note: '))
average = (note_1 + note_2)/2

if average < 5.0:
  print(f'Average: {average}')
  print('disapproved!')
elif average >= 5.0 and average <= 6.9:
  print(f'Average: {average}')
  print('recovery!')
else:
  print(f'Average: {average}')
  print('approved!')
