def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

lista_codigos_negociacao = ['WEGE3', 'PETR4', 'PETR3', 'PCAR3', 'ALPA4']

separador('como selecionar todos os itens da lista que são ON?')

nova_lista_codigos = []

for ticker in lista_codigos_negociacao:
    if "3" in ticker:
        nova_lista_codigos.append(ticker)
print(nova_lista_codigos)


nova_lista_codigos = [ticker for ticker in lista_codigos_negociacao if "3" in ticker]

print(nova_lista_codigos)

separador('como deixar todos os códigos em letra minúscula?')

minusculo_on = [ticker.lower() for ticker in lista_codigos_negociacao if "3" in ticker]
minusculo_todos = [ticker.lower() for ticker in lista_codigos_negociacao]

print(minusculo_on)
print(minusculo_todos)

separador('filter é uma opção para filtrar listas')

lista_restrita = ['WEGE3', 'PCAR3']

nova_lista_codigos = list(filter(lambda ticker: ticker not in lista_restrita, lista_codigos_negociacao))

print(nova_lista_codigos)

separador('map é uma opção para transformar listas')

lista_numeros = [9, 8, 3, 4]

separador('converter todos os numeros para string')

lista_string_numeros = list(map(lambda x: str(x), lista_numeros))

print(lista_string_numeros)

separador('somar dois a todos os números')

lista_somando_dois = list(map(lambda x: x + 2, lista_numeros))

separador('Exercício 25')

lista = [2, 4, 5, 6, 10]

nova_lista = list(filter(lambda x: x > 5, lista))

print(nova_lista)

separador('Exercício 26')

lista = [2, 4, 5, 6, 10]

nova_lista = list(map(lambda x: int(x), lista))

separador('Exercício 27')

lista = ['WEGE3', 'PCAR3', 'PETR4', 'PETR3', 'ALPA4']

lista_comeca_com_p = [ticker for ticker in lista if ticker.startswith('P')]

print(lista_comeca_com_p)
