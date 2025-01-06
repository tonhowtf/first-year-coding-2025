import re
def separador(texto: str):
    separador = "-" * len(texto)
    print(f"{separador}{texto}{separador}")

texto = 'esse é o curso código.py'

separador('tamanho do texto')

print(len(texto))

separador('juntando strings')

print(texto + " e eu")

separador('substituindo texto')

texto_novo = texto.replace("código", "gCódigo.py 2.0")

print(texto_novo)

separador('contagem')

print(texto.count('código'))

separador('a string começa com "esse"?')

print(texto.startswith('esse'))

separador('a string termina com "python"?')

print(texto.endswith('python'))

separador('selecionando strings')

print(texto[0])
print(texto[0:4])
print(texto[-1])
print(texto[4:])


separador('letras maiusculas')

print(texto.upper())
print(texto.lower())
print(texto.title())

texto_1 = "Python"

texto_2 = "python"

print(texto_1 == texto_2)
print(texto_1 == texto_2.title())

separador('?')

bloco_texto = ''' brenno brennolima@gmail.com lucas lucasvgm@hotmail.com leandro leandropaulo@yahoo.com.br'''

padrao = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

expressao_regular = re.compile(padrao, flags=re.IGNORECASE)

print(expressao_regular.findall(bloco_texto))

separador('validar email')

email = ' str(input("Digite seu email: ")'

if re.fullmatch(expressao_regular, email):
    print("Seu e-mail é valido")
else:
    print('E-mail inválido')


separador('exercicio 16')

empresa = input("Digite o nome da empresa: ")

print(empresa[0])
print(empresa[-1])
print(len(empresa))
print(empresa.upper())
print(empresa.title())
print(empresa[:2].replace(empresa[:2], "tranqueira") + empresa[2:])

separador('exercicio 17')

telefone = input("Digite seu telefone: ")   
# padrao = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
#padrao_telefone = r'\d{2}-\d{9}'


padrao = r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}$'

padrao_telefone = re.compile(padrao)

telefone = str(input("Digite seu telefone: "))

if re.fullmatch(padrao_telefone, telefone):
    print("Telefone válido")
else:
    print("Telefone inválido")

