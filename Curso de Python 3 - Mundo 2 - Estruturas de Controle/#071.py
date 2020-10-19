# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
price = int(input('Enter the amount of money you will withdraw: '))
total = price
money_bill = 50
total_mb = 0

while True:
    if total >= money_bill:
        total -= money_bill
        total_mb += 1
    else:
        if total_mb > 0:
            print(f'Total: {total_mb} de {money_bill}')
        if money_bill == 50:
            money_bill = 20
        elif money_bill == 20:
            money_bill = 10
        elif money_bill == 10:
            money_bill = 1
        total_mb = 0

        if total == 0:
            break
        else:
            continue

print('BYE!')