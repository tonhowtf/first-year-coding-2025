def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")


set_teste = {'weg', 'renner', 'c&a', 'SLC agricola'}
set_numero = {1, 4, 5, 8}

print(set_teste)

separador('remover duplicatas')

lista_duplicada = ['renner', 'renner', 'weg', 'weg']

lista_unica = list(set(lista_duplicada))

print(lista_unica)

separador('adicionando um ou mais elementos a sets')

set_numero.add(10)

print(set_numero)

set_numero.update([20, 25, 60])

print(set_numero)

separador('removendo elementos')
