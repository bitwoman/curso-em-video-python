# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
phrase = str(input('Enter a phrase: '))
phrase = phrase.replace(' ', '')
print(phrase)
invert = ''

for letter in range(len(phrase) - 1, -1, -1):
    invert += phrase[letter]
print(invert)

if phrase == invert:
    print('ok, palíndromo')
else:
    print('not palíndromo')

#For example:
#Apos a sopa, a sacada da casa, a torre da derrota, o lobo ama bolo, anotaram a data da maratona.
