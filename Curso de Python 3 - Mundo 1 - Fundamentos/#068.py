# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias 
# consecutivas que ele conquistou no final do jogo.
import random
count = 0

while True:
  print('=' * 20)

  number = int(input('Enter a number between 1 and 10: '))
  computer_number = random.randint(1,10)
  computer_choice = random.randint(1,2)
  sum = number + computer
  option = ''

  while option not in (1,2):
    option = int(input('Enter an option: \n[1] ODD\n[2] EVEN ')) 

  print('=' * 20)
  print(f'You played {number} and computer played {computer}')
  print(f'The total is {sum}')

  if option == 1 and computer_choice == 1 and sum % 2 == 0:
    print('TIED!!')
  elif option == 1 and computer_choice == 2 and sum % 2 == 0:
    print('COMPUTER WINS!!')
    break
  elif option == 1 and computer_choice == 1 and sum % 2 != 0:
    print('TIED!!')
  elif option == 1 and computer_choice == 2 and sum % 2 != 0:
    print('YOU WIN! CONGRATULATIONS!')
    count += 1
  elif option == 2 and computer_choice == 1 and sum % 2 == 0:
    print('YOU WIN! CONGRATULATIONS!')
    count += 1
  elif option == 2 and computer_choice == 2 and sum % 2 == 0:
    print('TIED!!')
  elif option == 2 and computer_choice == 1 and sum % 2 != 0:
    print('COMPUTER WINS!!')
    break
  else:
    if option == 2 and computer_choice == 2 and sum % 2 != 0:
      print('TIED!!') 

print(f'GAME OVER\nTotal: {count}')
