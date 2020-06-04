#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
width = float(input('Wall width: '))
height = float(input('Wall height: '))
area = width * height
paint = area/2

print(f'Dimensions: {width} x {height} and its area is {area}m².\nAmount of paint to paint a room is: {paint} liters')
