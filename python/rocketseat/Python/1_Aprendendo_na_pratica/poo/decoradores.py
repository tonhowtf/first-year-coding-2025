from typing import Any

def meu_decorador(func):
    def wrapper():
        print("Antes da minha função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper


@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")


minha_funcao()


class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> Any:
        print("Antes da função ser chamada")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")

    