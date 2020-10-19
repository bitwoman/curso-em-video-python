#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
number = int(input('Enter a number: '))
predecessor = number - 1
successor = number + 1

print(f'Analyzing the number, its predecessor is {predecessor} and and its successor is {successor}')