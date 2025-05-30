from model import Pessoa
class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):  
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = 'Tonho'
        idade = 40
        cpf = 131233455
        return Pessoa(nome, idade, cpf)
p1 = Pessoa('Tonho', 23, '2312312')