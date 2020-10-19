# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
straight_line = []

for x in range(0,3):
  line = float(input('Enter the size of the line: '))
  straight_line.append(line)

ab = straight_line[0] + straight_line[1]
bc = straight_line[1] + straight_line[2]
ca = straight_line[2] + straight_line[0]

if ab > straight_line[2] and bc > straight_line[0] and ca > straight_line[1]:
  print("It's possible to create a triangle!")
else:
  print("It isn't possible to create a triangle!")
