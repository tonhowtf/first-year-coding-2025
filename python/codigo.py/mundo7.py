empresa = input("Digite o ticker da empresa: ")
cotacao = float(input("Digite a cotação: "))

valor_dobrado_da_empresa = cotacao * 2
caiu_50 = cotacao / 2
print(f"Caso a empresa suba 100%, a cotação será de {
      valor_dobrado_da_empresa}")
print(f"Caso a empresa caia 50%, a cotação será de {caiu_50}.")

print("--------------------------------")

numero = float(input("Digite um número: "))

print(numero*2)
print(numero**2)
print(numero/2)
print(f"{numero+1} e {numero - 1}")
