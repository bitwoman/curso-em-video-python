# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
media = 0
realList = []
auxList = []

print('-=' * 20)
print(' '*15, 'School Report')
print('-=' * 20)

while True:
  name = str(input("Enter the student's name: "))
  grade1 = float(input('Enter the first grade: '))
  grade2 = float(input('Enter the second grade: '))
  media = (grade1+grade2)/2

  auxList.append([name, [grade1, grade2], media])
  
  answer = str(input('\nDo you want to continue? [Y/N] \n')).strip().upper()

  if(answer == 'N'):
    print('-='*20)
    break

print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-='*20)

for i, x in enumerate(auxList):
  print(f'{i:<4}{x[0]:<10}{x[2]:>8.1f}')

while True:
  print('-'*40)
  student = int(input('Which student do you wanna see? (999 break): '))
  
  if(student == 999):
    print('BYE....')
    break

  if(student <=len(auxList)-1):
    print(f'Grades of {auxList[student][0]} are {auxList[student][1]}')

print('<<< COME BACK ALWAYS >>>')
