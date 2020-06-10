# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
name_city = str(input("Enter a name's city: ")).strip().split()

if name_city[0].upper() == 'SANTO':
  print("It has a first name 'Santo'")
else:
  print("It doens't have a first name 'Santo'")
