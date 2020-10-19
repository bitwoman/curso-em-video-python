# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

attempts = 0
computer = randint(1,10)

print("I'm your computer...")
sleep(2)
print('I thought of a number between 1 and 10.')
sleep(2)
print('Can you guess what was?')
sleep(2)
guess = int(input("What's your guess? "))

while guess != computer: 
  attempts += 1
  if guess > computer:
    print('Less...Try again.')
    guess = int(input("What's your guess? "))
    attempts += 1
  elif guess < computer:
    print('More. Try again')
    guess = int(input("What's your guess? "))
    attempts += 1
  else:
    continue

print(f'You got it right with {attempts} attempts. Congratulations!')
