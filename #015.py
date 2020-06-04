#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km_traveled = float(input('Enter km travaled by car: '))
days_used = int(input('Enter the days that the car was used: '))
rent_day = (days_used * 60.00)
rent_km = km_traveled * 0.15
rent_total =  rent_day + rent_km

print('Total to pay is: R$ %.2f' %rent_total)
