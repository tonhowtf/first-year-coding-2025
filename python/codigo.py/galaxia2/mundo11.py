import random


def separador():
    separador = "------------------------------------"

    print(separador)


def separador2():
    separador = "--------------desafio---------------"
    print(separador)


lista_base = ['Tonho', 'bruno', 'caio']
lista_base = list(['Conho', 'Sonho', 'Donho'])

print(lista_base)

separador()

lista_vazia = []
lista_tipos_diferentes = ['flamengo', 8, 'campeonatos brasileiros']

separador()

lista_dentro_de_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in lista_dentro_de_lista:
    for item in lista:
        print(item, end=' ')
    print()

separador()

lista_sinais = []

lista_sinais.append('Oi')
lista_sinais.append('Bom dia')


print(lista_sinais)

separador()

print(lista_sinais[0])
print(lista_sinais[1])
print(lista_sinais[-1])

print(lista_dentro_de_lista[0])
print(lista_dentro_de_lista[0][0])

separador()

print(lista_sinais[0:2])
print(lista_sinais[1:])
print(lista_sinais[:3])
print(lista_sinais[-2:])

separador()

lista_sinais.insert(2, "Compra até acabar o caixa")

print(lista_sinais)

separador()

verificando = "compra tudo" in lista_sinais
verificando2 = "compra tudo" not in lista_sinais

print(verificando, verificando2)


separador()

lista_desordenada = [56, 45, 1, 75, 23]

lista_ordenada_crscente = sorted(lista_desordenada)
print(lista_ordenada_crscente)

lista_desordenada_decrescente = sorted(lista_desordenada, reverse=True)
print(lista_desordenada_decrescente)

separador()
print(len(lista_desordenada))

separador()

print(max(lista_desordenada))
print(min(lista_desordenada))
print(sum(lista_desordenada)/len(lista_desordenada))


separador()

# tuplas

tupla = (2, 3, 5, 2, 2)

print(tupla[0])
print(tupla.count(2))
print(tupla.index(2))

separador()

print(tupla.count(2))
print(tupla.index(2))
print(len(tupla))

separador2()
tickers = []
for i in range(0, 4):
    ticker = input(f"Digite o {i}° nome: ")
    tickers.append(ticker)
empresa_escolhida = random.choice(tickers)

print('Sua recomendação é {empresa_escolhida}!')

separador2()
lista_pls = []
for i in range(0, 4):
    pls = int(input(f"Digite o {i}° nome: "))
    lista_pls.append(ticker)
lista_pls_ordenada = lista_pls.sort()
