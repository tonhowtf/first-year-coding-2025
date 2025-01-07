import time
import pandas as pd
import datetime

def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

lista_empresas = ['Weg', 'Vale', 'Petrobras']

for empresa in lista_empresas:
    print(empresa.upper())
    time.sleep(1)

separador('loop em um range.')

print(range(0, 3))

for i in range(0, len(lista_empresas)):
    print(lista_empresas[i])

separador('por que usar um range?')

lista_cotacoes = [20, 30, 45]

lista_dicionarios = []

for i in range(0, 3):
    lista_dicionarios.append(pd.DataFrame({'Nome empresa': lista_empresas[i], 'Cotação': lista_cotacoes[i]}, index=[0]))

tabela = pd.concat(lista_dicionarios)

print(tabela)

separador('enumerate usa os dois mundos')

lista_dicionarios = []

for indice, cotacao in enumerate(lista_cotacoes):

    print(indice, cotacao)

    lista_dicionarios.append(pd.DataFrame({'Nome empresa': lista_empresas[indice], 'Cotação': cotacao}, index=[0]))

tabela = pd.concat(lista_dicionarios)

print(tabela)

separador('usando while')

tempo = datetime.datetime.now()

# while True:
#     tempo_rodando = datetime.datetime.now() - tempo
#     print(f'O programa está rodando há {tempo_rodando} segundos.')
#     time.sleep(5)

separador('usando while sem ser infinito')
contador = 0

while lista_cotacoes[contador] < 35:
    print(lista_cotacoes[contador])
    contador += 1

separador('exercício 20')
cotacoes = []
for i in range(0,5):
    cotacao = float(input('Digite a cotação da ação: '))
    cotacoes.append(cotacao)
cotacoes.sort()
print(cotacoes)

separador('exercício 21')

carteira = {nome_da_empresa:None, p_l:None, roe:None}

carteira["nome_da_empresa"] = input('Digite o nome da empresa: ')
carteira["p_l"] = float(input('Digite o P/L da empresa: '))
carteira["roe"] = float(input('Digite o ROE da empresa: '))