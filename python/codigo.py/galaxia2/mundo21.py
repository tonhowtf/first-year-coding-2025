def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

separador('calculadora')


# numero1 = float(input('Digite o primeiro número: '))
# numero2 = float(input('Digite o segundo número: '))

# divisao = numero1/numero2

# print(f'A divisão dos números é {divisao}.')

# separador('calculadora 2')

# try:
#     numero1 = float(input('Digite o primeiro número: '))
#     numero2 = float(input('Digite o segundo número: '))

#     divisao = numero1/numero2

# except ZeroDivisionError:
#     print('Não é possível dividir por zero.')
# except ValueError: 
#     print('Digite apenas números.')
# else:
#     print(f'A divisão dos números é {divisao}.')
# finally:
#     print('Fim do programa.')


# separador('calculadora 3')

# try:

#     numero1 = float(input('Digite o primeiro número: '))
#     numero2 = float(input('Digite o segundo número: '))

#     divisao = numero1/numero2

# except Exception as erro:
#     print(f'Ocorreu um erro: {erro.__class__}')

separador('exercicio 24')

try:
    nome = input('Digite o seu nome: ').title()
    idade = int(input('Digite a sua idade: '))
except ValueError:
    "Digite apenas números para a idade."
except Exception as erro:
    print(f'Ocorreu um erro: {erro.__class__}')
else:
    print(f'Parabéns por ter participado {nome}')
finally:
    print(f'Em mais 3 anos quando você tiver {idade + 3} anos, você será um ótimo programador Python.')


