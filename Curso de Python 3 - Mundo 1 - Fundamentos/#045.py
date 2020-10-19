# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import choice
import emoji
# print(emoji.emojize(':neutral_face:', use_aliases=True))

computer = ['Stone', 'Paper', 'Scissors']
print('Your options are: \n[0] Stone\n[1] Paper\n[2] Scissors\n')
move_user = int(input('Which is your move? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('=========================')

move_computer = choice(computer)
stone = emoji.emojize(':punch:', use_aliases=True)
paper = emoji.emojize(':hand:', use_aliases=True)
scissors = emoji.emojize(':v:', use_aliases=True)

if move_computer == 'Stone':
  print(f'Computer threw {stone}')
elif move_computer == 'Paper':
  print(f'Computer threw {paper}')
else:
  print(f'Computer threw {scissors}')

if move_user == 'Stone':
  print(f'You threw {stone}')
elif move_user == 'Paper':
  print(f'You threw {paper}')
else:
  print(f'You threw {scissors}')

print('=========================')

if move_computer == 'Stone' and move_user == 'Paper':
  print('Congratulations! You won!')
elif move_computer == 'Stone' and move_user == 'Scissors':
  print('Computer won!')
elif move_computer == 'Stone' and move_user == 'Stone':
  print('The game tied')
elif move_computer == 'Paper' and move_user == 'Stone':
  print("Computer won!")
elif move_computer == 'Paper' and move_user == 'Scissors':
  print('Congratulations! You won!')
elif move_computer == 'Paper' and move_user == 'Paper':
  print('The game tied')
elif move_computer == 'Scissors' and move_user == 'Paper':
  print("Computer won!")
elif move_computer == 'Scissors' and move_user == 'Stone':
  print('Congratulations! You won!')
else:
  print('The game tied')
