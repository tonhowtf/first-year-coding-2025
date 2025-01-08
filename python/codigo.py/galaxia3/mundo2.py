import numpy as np

def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

separador("a partir de uma lista ou tupla")

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4)

array_a_partir_de_lista = np.array(lista)

array_a_partir_de_tupla = np.array(tupla)

print(array_a_partir_de_tupla)

separador('Usando um range')

array_simples = np.arange(10)
array_sequencial = np.arange(10, 100, 10)

print(array_simples, array_sequencial)

separador('criando arrays de zeros ou ums')

vetor_zero = np.zeros(5)
vetor_um = np.ones(5)

print(vetor_zero, vetor_um)

