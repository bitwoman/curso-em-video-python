# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
year = int(input('Enter a year: '))

if year % 4 == 0 and year % 100 != 0: #or if year == 0: year = date.today().year if isleap(year) == True:
  print('"Bissexto"!')
else:
  print('Not is "Bissexto".')
