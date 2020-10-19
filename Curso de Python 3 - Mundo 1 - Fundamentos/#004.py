#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
something = input('Enter something: ')

print(f'The primitive type of {something} is: ', type(something))
print('Are there just spaces?', something.isspace())
print('Is it a number?', something.isnumeric())
print('Is it alphabetical? ', something.isalpha())
print('Is it alphanumeric? ', something.isalnum())
print('Is it in uppercase?', something.isupper())
print('Is it in lower case? ', something.islower())
print('Is it capitalized? ', something.istitle())