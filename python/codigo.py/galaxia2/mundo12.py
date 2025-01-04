def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")


set_teste = {'weg', 'renner', 'c&a', 'SLC agricola'}
set_numero = {1, 4, 5, 8}

print(set_teste)

separador('remover duplicata')

lista_duplicada = ['renner', 'renner', 'weg', 'weg']
lista_unica = list(set(lista_duplicada))

print(lista_unica)

separador('adicionando um ou mais elementos a sets')

set_numero.add(15)

print(set_numero)

set_numero.update([20, 25, 60])

print(set_numero)

separador('removendo elementos')

set_numero.discard(1)

print(set_numero)

separador('operações matemáticas de união, interseção, diferença')

meu_set = {1, 2, 3, 5, 8, 9}
meu_set_2 = {1, 4, 5, 6, 8, 11, 12}

separador('União')

print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

separador('Interseção - tem que estar nos dois ao mesmo tempo')

print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

separador('Diferença - só pode estar presente no set 1')

print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

separador('Desafio 1')

nome = input("Nome: ")

carteira1 = set()
carteira2 = set()
for i in range(0,3):
    empresa = input("Digite o nome da empresa: ")
    carteira1.add(empresa)
for i in range(0,3):
    empresa = input("Digite o nome da empresa: ")
    carteira2.add(empresa)

print(f"Diferença: {carteira1 - carteira2}")
print(f"Interseção: {carteira1 & carteira2}")
print(f"uniao: {carteira1 | carteira2}")
