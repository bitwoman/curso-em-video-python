#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Enter temperature in Celsius to convert to Fahrenheit: '))
fahrenheit = (celsius * 9/5) + 32

print(f'The {celsius}ºC corresponds to {fahrenheit}ºF')
