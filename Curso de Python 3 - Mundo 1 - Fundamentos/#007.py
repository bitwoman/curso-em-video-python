#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
grade_1 = float(input('Enter a first grade: '))
grade_2 = float(input('Enter a first grade: '))
average = (grade_1 + grade_2)/2 
'''#or 
from statistics import mean
sum = grade_1 + grade_2
average = mean(sum)
'''
print(f'The mean between {grade_1} and {grade_2} is {average}.')
