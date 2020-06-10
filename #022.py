# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
name = str(input('Enter your name: '))

print(name.upper())
print(name.lower())
print(len(name.replace(' ', '')))
new_name = name.split()
print(len(new_name[0]))
