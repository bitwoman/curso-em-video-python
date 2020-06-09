#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.
from math import sqrt
opposite_side = float(input('Enter the value of the opposite side: '))
adjacent_side = float(input('Enter the value of the adjacent side:'))
sum = (opposite_side**2) + (adjacent_side**2)
#or (opposite_side**2) + (adjacent_side**2) * (1/2)
#or hypot(opposite_side, adjacent_side)
h = sqrt(sum)

print(f' %.2f' %h)
