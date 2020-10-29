# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
print('='*50)
print(' '*12, 'BRAZILIAN CHAMPIONSHIP!')
print('='*50)

team = ('São Paulo FC', 'Santos FC', 'Corinthians', 'Palmeiras', 'Flamengo', 'Fluminense', 'Guarani', 'Goiás', 'Chapecoense', 'Fortaleza',
        'Botafogo', 'Ceará', 'Bahia', 'Cruzeiro', 'Grêmio', 'Internacional', 'Vasco da Gama', 'Avaí', 'Atlético MG', 'Atlético Paranaense')

while True:
  print('\nChoose an option: ')
  print('a) The first 5 teams.\nb) The last 4 placed.\nc) Teams in alphabetical order.\nd) In what position is the Chapecoense team.')
  option = str(input('Enter an option: ')).upper().strip()

  if option not in ('A', 'B', 'C', 'D'):
    print('Try again')
    break
  else:
    if option == 'A':
      for x in (team[0:5]):
        print(x, end=' ')
    elif option == 'B':
      for x in (team[-4:]):
        print(x, end=' ')
    elif option == 'C':
      print(sorted(team))
    else:
      if option == 'D':
        print(f"It's positiion is: {team.index('Chapecoense')}")
      else:
          break