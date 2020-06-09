# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import *
angle = float(input('Enter a angle: '))
sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print(f'sin: %.2f' %sin)
print(f'cos: %.2f' %cos)
print(f'tan: %.2f' %tan)
