# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
number = int(input('Enter a number: '))
unity = (number//1 % 10)
ten = (number//10 % 10)
hundred = (number//100 % 10)
thousand = (number//1000 % 10)

print(f'Unity: {unity}, Ten: {ten}, Hundred: {hundred}, Thousand: {thousand}')
