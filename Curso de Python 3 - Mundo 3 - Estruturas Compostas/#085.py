# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numbers = [[input('Enter a number: ') for i in range(0,7) if i % 2 == 0], [input('Enter a number: ') for i in range(0,7) if i % 2 != 0]]

numbers[0].sort()
numbers[1].sort()

print(f'\nEven numbers in ascending order: {numbers[0]}\nOdd numbers in ascending order: {numbers[1]}')
