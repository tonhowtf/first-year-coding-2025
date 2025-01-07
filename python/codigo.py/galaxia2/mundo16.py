def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")


separador('criando uma condição')

#banco de dados

"""weg = {"ticker": "WEGE3", "Lucro": 1700.00, 'Segmento de listagem': "Novo mercado", 'ROE': 0.20}

vale = {"ticker": "VALE3", "Lucro": 21700.00, 'Segmento de listagem': "Novo mercado", 'ROE': 0.19}

petrobras = {"ticker": "PETR3", "Lucro": 6700.00, 'Segmento de listagem': "Nível 2", 'ROE': 0.15}

tranqueira_fc = {"ticker": "TRNQ3", "Lucro": -20000.00, 'Segmento de listagem': "Tradicional", 'ROE': 0.02}

empresa_escolhida = str(input("Digite o nome da empresa: ")).lower()

if empresa_escolhida == "weg":
    porcentagem_roe = "{:.0%}".format(weg['ROE'])

    print(f"O ticker da empresa é {weg['ticker']}, o lucro é de {weg['Lucro']} e o ROE é de {porcentagem_roe}")

elif empresa_escolhida == "vale":
    porcentagem_roe = "{:.0%}".format(vale['ROE'])

    print(f"O ticker da empresa é {vale['ticker']}, o lucro é de {vale['Lucro']} e o ROE é de {porcentagem_roe}")
elif empresa_escolhida == "petrobras":
    porcentagem_roe = "{:.0%}".format(petrobras['ROE'])

    print(f"O ticker da empresa é {petrobras['ticker']}, o lucro é de {petrobras['Lucro']} e o ROE é de {porcentagem_roe}")
else:
    print('Por favor, digite uma empresa válida!')

empresa_escolhida = str(input("Digite o nome da empresa: ")).lower()

if empresa_escolhida == "tranqueira":

    usuario_escolha = str(input("Tem certeza que deseja saber sobre a Tranqueira? Digite 'S' para sim e 'N' para não ")).lower()

    if usuario_escolha == 'n':

        escolha = False
    else:
        pass"""

separador('exercício 18')

codigo_de_negociacao = int(input("Digite o código de negociação: "))
codigos = ['PN', 'ON', 'UNIT']

if codigo_de_negociacao[-1] == 4:
    print('PN')
elif codigo_de_negociacao[-1] == 11:
    print('UNIT')
elif codigo_de_negociacao[-1] == 3:
    print('ON')
else: 
    print('Código inválido')

separador('exercício 19')  

nome_da_empresa = str(input("Digite o nome da empresa: "))
ROE = float(input("Digite o ROE da empresa: "))
preco_lucro = float(input("Digite o preço/lucro da empresa: "))

if ROE > 0.20 and preco_lucro > 10 and preco_lucro > 0:
    print(f"{nome_da_empresa} é uma boa empresa para se investir")

if ROE > 0.10 and preco_lucro <= 5 or preco_lucro < 0:
    print(f"{nome_da_empresa} não é uma boa empresa para se investir")


