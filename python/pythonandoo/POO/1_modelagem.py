class Pessoas:
    possui_olho = True
    possui_boca = True

    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
    
    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'Estou logando no sistema')
    @classmethod
    def andar(cls):
        print("Estou andando")

#p1 = Pessoas('tonho', 25)
#p2 = Pessoas('Tonhoca', 21)
print(Pessoas.possui_boca)
