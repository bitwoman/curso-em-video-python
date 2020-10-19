#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
number = int(input('Enter a number to see the multiplication table: '))

for i in range(1,11):
    tabuada = number * i
    print(f'{number}x {i} = {tabuada}')
