# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever 
# na tela se o usuário venceu ou perdeu.
import random
from time import sleep
computer = random.randint(0,5)
user = int(input('What number did I think? '))

print('LOADING...')
sleep(2)

if user == computer:
    print('CONGRATULATIONS! YOU GOT! You beat me!')
else:
  print(f'You lost! I thought of the number {computer}.')
