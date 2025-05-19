def adicionar_tarefa(tarefas, nome_tarefa):

    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionado com sucesso")
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
        pass
    elif escolha == "3":
        pass
    elif escolha == "4":
        pass
    elif escolha == "5":
        pass

    elif escolha == "6":
        break

print("Programa finalizado")