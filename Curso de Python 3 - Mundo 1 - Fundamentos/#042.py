# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
straight_line = []

for x in range(0,3):
  line = float(input('Enter the size of the line: '))
  straight_line.append(line)

ab = straight_line[0] + straight_line[1]
bc = straight_line[1] + straight_line[2]
ca = straight_line[2] + straight_line[0]

if ab > straight_line[2] and bc > straight_line[0] and ca > straight_line[1]:
  print("It's possible to create a triangle!")

  if straight_line[0] == straight_line[1] == straight_line[2]:
    print("It's a equilateral triangle")
  elif (straight_line[0] == straight_line[1] and straight_line[0] != straight_line[2]) or (straight_line[0] != straight_line[1] and straight_line[0] == straight_line[2]):
    print("It's a isosceles triangle")
  else:
    print("It's a scalene triangle")
else:
  print("It isn't possible to create a triangle!")
