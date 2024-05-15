times = (
    'Palmeiras',
    'Gremio',
    'Atletico-MG',
    'Flamengo',
    'Botafogo',
    'Fluminense',
    'Athletico-PR',
    'Internacional',
    'Fortaleza',
    'Sao Paulo',
    'Cuiaba',
    'Corinthians',
    'Cruzeiro',
    'Vasco',
    'Bahia',
    'Santos',
    'Goias',
    'Coritiba',
    'America-MG'
)

pontuacao = (
    70,
    68,
    66,
    66,
    64,
    62,
    56,
    56,
    55,
    54,
    53,
    51,
    50,
    47,
    45,
    44,
    43,
    38,
    30,
    24
)

print('-'*40)
print(f'{'TABELA BRASILEIRÃO':^30}')
print('-'*40)

print('\n')
 

for i in range(0, len(times)):
    print(f'{times[i]:.<30}', end='')

    if i < 6:
        print(f'\033[1;32m{pontuacao[i]}\033[0m Pontos')
        
    elif i < 12:
        print(f'\033[1;34m{pontuacao[i]}\033[0m Pontos')
    elif i >= 16:
        print(f'\033[1;31m{pontuacao[i]}\033[0m Pontos')
    else:
        print(f'\033[1;33m{pontuacao[i]}\033[0m Pontos')

print('\n')

print('-'*40)
print(f'{'G6 do Brasileirão':30}')
