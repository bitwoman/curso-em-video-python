# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
price_shopping = float(input('Enter the price of shopping: '))
method_payment = int(input('PAYMENT METHODS: \n [1] in cash money/check \n [2] in cash card\n [3] 2x in card\n [4] 3x or more in card\n What is the option? '))
 
if method_payment == 1:
  in_cash_money = price_shopping - (price_shopping * (10/100))
  print('Total: R$ %.2f' %in_cash_money) 

elif method_payment == 2:
  in_cash_card = price_shopping - (price_shopping * (5/100))
  print('Total: R$ %.2f' %in_cash_card)

elif method_payment == 3:
  in_card_twice = price_shopping
  print('Total: R$ %.2f' %in_card_twice)

elif method_payment == 4:
  parcels = int(input('How many parcels? '))
  each_parcel = (price_shopping/parcels) + ((price_shopping/parcels) * (20/100))  
  total_with_interest = price_shopping + (price_shopping * (20/100))
  
  print(f'{parcels} parcels of R$ %.2f' %each_parcel)
  print(f'Your shopping of {price_shopping} was R$ %.2f' %total_with_interest)
else:
  print('Invalid option!!!!')
