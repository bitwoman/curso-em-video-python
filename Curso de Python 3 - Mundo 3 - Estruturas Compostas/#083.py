# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
mathematicalFormula = str(input('Enter a mathematical formula: ')).strip()
parenthesesOpen = parenthesesClosed = 0

for i in mathematicalFormula:
  if '(' == i:
    parenthesesOpen +=1
  if ')' == i:
    parenthesesClosed +=1

if parenthesesOpen == parenthesesClosed:
  print("It's correct!")
else:
  print("It's not correct!") 
