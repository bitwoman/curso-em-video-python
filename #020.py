# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
students = []

for x in range(0,4):
  name = str(input("Enter a name's student: "))
  students.append(name)

random.shuffle(students)
print(students)
