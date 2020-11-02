# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
letters = ('APRENDER', 'programar', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATUITO', 'estudar', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U','u')

for v in range(0, len(letters)-1):
    print(f'\nIn the word {letters[v]} has the vowels: ', end='')
    for vw in range(0, len(vowels)-1):
        if(vowels[vw] in letters[v]):
          print(f'{vowels[vw]}', end=' ')
