# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tuple = (
'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    number = int(input('Enter a number between 0 and 20: '))

    if number >= 0 and number <= 20:
        print(f'You entered the number {tuple[number]}')
    else:
        break

print('Try again.')