class Pessoas:
    def __init__(self, nome):
        self.nome = nome
        
    def logar_sistema(self):
        print(f'Estou logando no sistema')

p1 = Pessoas('tonho')

print(p1.nome)
