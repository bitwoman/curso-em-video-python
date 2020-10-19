#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import *
number = int(input('Enter a number: '))
double = number**2
triple = number**3
square = sqrt(number) #or number**(1/2)

print(f'Double the number is {double}')
print(f'Triple the number is {triple}')
print(f'Square the number is {square}')