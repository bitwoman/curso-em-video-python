# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 
# para cada jogo, cadastrando tudo em uma lista composta.
import random
from time import sleep


realList = []

print('-=' * 30)
print(' '*20, 'JOGO NA MEGA SENA')
print('-=' * 30)

games = int(input('How many games do you want me to draw? '))

if games != 0 or games > 0:
    for i in range(0, games):
      if len(realList) < games:
        gamesList = []
        
        while len(gamesList) < 6: 
          randomNumber = random.randrange(1,60)
          if randomNumber not in gamesList:
            gamesList.append(randomNumber)
        
      realList.append(gamesList)
        
sleep(2)
print('-=' *9, f' SORTEANDO {games} JOGOS ', '-='*11)

for i in range(0, games):
  print(f'Jogo[{i}]: {realList[i]}')

print('-='*10, ' < BOA SORTE > ', '-=' *12)
