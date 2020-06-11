# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('How far is the trip? '))

if km <= 200:
  ticket_price = (km * 0.50)
  print(f'Ticket price is R$ %.2f' %ticket_price)
elif km > 200:
  ticket_price = (km * 0.45)
  print(f'Ticket price is R$ %.2f' %ticket_price)
