# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
full_name = str(input('Enter your full name: ')).title().split()
first_name = full_name[0]
last_name = full_name[-1] #or full_name[len(full_name) - 1]
print(f'First name: {first_name}\nLast name: {last_name}')
