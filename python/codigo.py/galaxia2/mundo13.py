import pandas
def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")


separador('criar dicionários')

dicionario_vazio = {}

dicionario_povoado = dict({'nome': 'tonho', 'sobrenome': 'albuquerque'})

dicionario_numerico = {1: 'brenno', 2: 'tonho', 3: 'bruno'} #pódio

dicionario_com_listas = {'empresas_novo_mercado':['Weg', 'Renner', 'Vale'], 'empresas_em_outros_segmentos': ['Petrobras', 'Alpargatas'] }


dicionario_empresas_na_carteira = {True: ['Pão de açúcar', 'Weg'], False: ['Lojas Renner', 'Guararapes']}

separador('pegando itens dentro dos dicionários')

print(dicionario_numerico[2])
print(dicionario_numerico.get(2))
print(dicionario_povoado.get('nome'))
print(dicionario_com_listas['empresas_novo_mercado'])
print(dicionario_com_listas['empresas_novo_mercado'][0])

separador('adicionar elementos em um dicionário')

dicionario_vazio['Curso'] = 'Codigo.py'

dicionario_vazio.update({'Galaxia': 2, 'Mundo': 13})

print(dicionario_vazio)


separador('removendo dados de um dicionário')

dicionario_vazio.pop('Curso')

print(dicionario_vazio)

separador('aplicabilidade dicionários')

import pandas as pd

#tabela de cotações

dicionario_cotacoes = {'WEGE3': [50.10, 49.09, 30.06], 'PCAR3': [20.05, 19.06, 21.39]}

tabela_cotacoes = pd.DataFrame(data = dicionario_cotacoes, index=pd.date_range(start="2022-07-05", end="2022-07-07"))

print(tabela_cotacoes)

separador('características de um objeto')

weg = {'Nome': 'Weg', 'Segmento de listagem': "Novo mercado", "Somente ações ON": True, "Conselho majoritariamente independente": True}

print(weg['Segmento de listagem'])

separador('catalogos de filmes')

dicionario_marvel = {'Filme': "Pantera negra", "Data estreia": "2018-02-15", 'Bilheteria (em bilhões US$)': 1.34, 'Ator principal': "Chadwick Boseman"}

separador('Exercício 14')

empresa_x = {'nome': 'Gato','cnpj': '23384615000164', 'codigo': 'gato3', 'ano de fundacao': "2018-02-15", 'Segmento de listagem': 'Novo Mercado', 'P/L': 30, 'ROE': 0.45}

separador('Exercício 15')

print(f'Nome da empresa: {empresa_x.get('nome')}')