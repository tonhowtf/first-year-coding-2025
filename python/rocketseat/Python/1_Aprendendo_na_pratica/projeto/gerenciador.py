def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionado com sucesso!")
    return

def ver_tarefas(tarefas):
    print(f"\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
        return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        pass
    elif escolha == "4":
        pass
    elif escolha == "5":
        pass

    elif escolha == "6":
        break

print("Programa finalizado")