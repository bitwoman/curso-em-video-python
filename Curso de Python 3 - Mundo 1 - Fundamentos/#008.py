#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
number = float(input('Enter the number in meters:'))
#Quilômetros
km = number/1000
#Hectometros
hm = number/100
#Decametro
dam = number/10
#Decímetro
dm = number * 10 
#Centímetro
cm = number * 100
#Milímetro
mm = number * 1000

print(f'KM = {km}, HM = {hm}, DAM = {dm}, DM = {dm}, CM = {cm}, MM = {mm}')
