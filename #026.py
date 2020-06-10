# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", e 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
phrase = str(input('Enter a phrase: ')).upper().strip()
count_letter = phrase.count('A')
first_letter = phrase.find('A') + 1 
last_letter = phrase.rfind('A') + 1
print(count_letter, first_letter, last_letter)
