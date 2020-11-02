# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
products = ('Lápis', 1.75, 'Borracha', 2.0,'Caderno', 15.90,'Estojo', 25.00, 'Transferidor', 4.20, 
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30 , 'Livro', 34.90, 'Apontador', 5.00)

print('='*50)
print(' '*15, "PRODUCTS'S PRICES")
print('='*50)

for x in range(0, len(products)-1, 2):
  print(f'{products[x]:.<40}', f'R$ {products[x+1]:>.2f}')

print('='*50)
