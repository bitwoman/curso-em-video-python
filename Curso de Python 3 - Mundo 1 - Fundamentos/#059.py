# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n_1 = int(input('Enter a first number: '))
n_2 = int(input('Enter a second number: '))
sum = mult = bigger = option = 0

while option != 5:
    print('[1] SUM \n[2] MULTIPLICATION\n[3] BIGGER\n[4] NEW NUMBERS\n[5] EXIT')
    option = int(input('Chose an option: '))

    if option == 1:
        sum = n_1 + n_2
        print(f'{n_1} + {n_2} = {sum}')
    elif option == 2:
        mult = n_1 * n_2
        print(f'{n_1} * {n_2} = {mult}')
    elif option == 3:
        bigger = n_1
        if n_2 > bigger:
            bigger = n_2
        else:
            bigger = n_1

        print(f'Bigger: {bigger}')
    elif option == 4:
      n_1 = int(input('Enter a first number: '))
      n_2 = int(input('Enter a second number: '))
    elif option == 5:
        print('FINISHING!!!!!!!')
        sleep(1)
        print('...')
    else:
        print('INVALID OPTION!!!!!!!!')
        print('=' * 20)
        sleep(3)

sleep(1)
print('GOOD BYE!')
