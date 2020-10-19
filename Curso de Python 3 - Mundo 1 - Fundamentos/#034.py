# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salary = float(input('Enter your salary: '))

if salary > 1250.00: 
  new_salary = salary + (salary * (10/100))
elif salary <= 1250.00:
  new_salary = salary + (salary * (15/100))

print(f'New salary: R$ %.2f'%new_salary)
