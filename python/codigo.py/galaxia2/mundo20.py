def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

numero_digitado = int(input('Digite um número: '))

def soma_numeros(numero, soma = 2):
    return numero + soma

novo_numero = soma_numeros(numero = numero_digitado)
novo_numero_opcional = soma_numeros(numero = numero_digitado, soma = 6)

print(f'O novo número é {novo_numero}.')
print(f'O novo número opcional é {novo_numero_opcional}.')

separador('calcula rentabilidade')

def calcula_rentabilidade(valor_inicial, valor_final):
    
    rentabilidade = valor_final/valor_inicial - 1
    rentabilidade_em_porcentagem = "{:.2%}".format(rentabilidade)

    return rentabilidade_em_porcentagem

valor_inicial = float(input('Digite o valor inicial: '))
valor_final = float(input('Digite o valor final: '))

rentabilidade = calcula_rentabilidade(valor_inicial=valor_inicial, valor_final=valor_final)

print(rentabilidade)

separador('funções lambda')

'''o principal motivo para usar funções lambda é a simplicidade e a facilidade de uso.'''

def calcular_desconto(preco):
    return preco*0.2

calcular_desconto2 = lambda x: x*0.2

desconto = calcular_desconto(10)
desconto2 = calcular_desconto2(10)

print(desconto)
print(desconto2)

separador('aplicação prática')

precos = [10, 20, 30, 40]

descontos = list(map(calcula_desconto, precos))

descontos = list(map(lambda x: x*0.2, precos))

print(descontos)

separador('Exercício 22')

celsisus_para_fahrenheit = lambda celsius: celsius*9/5 + 32

separador('Exercício 23')

def calcula_retorno(cotacoes):
    retorno = []