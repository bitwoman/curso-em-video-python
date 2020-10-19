# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
name = str(input('Enter your full name: ')) #or name = str(input('Enter your full name: ')).strip()

print(name.upper())
print(name.lower())
print(len(name.replace(' ', ''))) #or print(len(name) - name.count(' ')
new_name = name.split()
print(len(new_name[0])) #or print(len(new_name.find(' '))
