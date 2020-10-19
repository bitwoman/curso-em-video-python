# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
velocity = float(input('Enter a velocity of the car: '))

if velocity > 80:
  traffic_ticket = (velocity - 80) * 7
  print(f'Fined! The traffic ticket is R$%.2f' %traffic_ticket)
