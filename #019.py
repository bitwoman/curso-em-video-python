# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
name_list = []

for x in range(0,3):
  name = str(input('Enter a name: '))
  name_list.append(name) 

chosen = random.choice(name_list) 
print(chosen)
