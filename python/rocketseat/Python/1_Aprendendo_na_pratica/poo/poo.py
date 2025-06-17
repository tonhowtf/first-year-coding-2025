# POO

# Classe exemplo

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        nome = 2
        self.idade + nome

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


    

pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()

print(mensagem)