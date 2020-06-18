# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
number = int(input('Enter a number: '))
option = int(input('and chose the option: \n[1]: Binary\n[2]: Octal\n[3]: Hexadecimal'))

#0b -> binary
#0o -> octal
#0x -> hexadecimal

if option == 1:
  print(bin(number))
elif option == 2:
  print(oct(number))
elif option == 3:
  print(hex(number)) #[2:] slice first two characters
else:
  print('Invalid number!')
