#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salary = float(input('Enter your salary: '))
percent = (15/100)
salary_increase = salary * percent 
new_salary = salary + salary_increase

print('New salary is: %.2f' %new_salary)
