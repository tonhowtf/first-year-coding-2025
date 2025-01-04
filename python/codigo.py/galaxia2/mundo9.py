import random

from random import choice


def separador():
    separador = "------------------------------------"

    print(separador)


def separador2():
    separador = "--------------desafio---------------"
    print(separador)


separador()


valor_entre_0_ou_1 = random.random()

print(valor_entre_0_ou_1)

separador()

valor_decimal_de_igual_probabilidade_entre_valores = random.uniform(10, 100)

print(valor_decimal_de_igual_probabilidade_entre_valores)


separador()

valor_inteiro_de_igual_probabilidade_entre_valores = random.randint(10, 10)
print(valor_inteiro_de_igual_probabilidade_entre_valores)

separador()

valor_dist_normal = random.gauss(10, 30)
print(valor_dist_normal)

# sorteio, importando a função direto.

tickers = ['WEGE3', 'PCAR3', 'LREN3']

empresa_escolhida = choice(tickers)
print(empresa_escolhida)

separador2()

moeda = ['cara', 'coroa']
moeda_escolhida = choice(moeda)
print(moeda_escolhida)

separador2()

nota = random.randint(0, 10)
print(f"sua nota foi {nota}!")
