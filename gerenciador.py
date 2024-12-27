def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {nome_tarefa} foi adicionada!")
    return
def listar_tarefas(tarefas):
    print("\n Listas de tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa ["completada"] else " "
        nome_tarefa = tarefa ["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustada = int(indice_tarefa) - 1
    if indice_tarefa_ajustada >=0 and indice_tarefa_ajustada < len(tarefas):
        tarefas[indice_tarefa_ajustada] ["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Tarefa selecionada inexistente")
    return
def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustada = int(indice_tarefa) - 1
    if indice_tarefa_ajustada >=0 and indice_tarefa_ajustada < len(tarefas):
        tarefas[indice_tarefa_ajustada] ["completada"] = True
    print(f"Tarefa {indice_tarefa} completada!!")
    return
def editar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustada = int(indice_tarefa) - 1
    if indice_tarefa_ajustada >=0 and indice_tarefa_ajustada < len(tarefas):
        
        tarefas[indice_tarefa_ajustada] ["não completada"] = True
    print(f"Tarefa {indice_tarefa} não completada!!")
def remover_tarefa_completada(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("As tarefas completadas foram removidas!!")
    return
tarefas = []
while True:
    print ("\n Bem-vindo ao seu Gerenciador de Tarefas")
    print("1.Adicionar Tarefas")
    print("2.Ver Tarefas")
    print("3.Atualizar Tarefas")
    print("4.Completar Tarefas")
    print("5.Editar Tarefas")
    print("6.Remover tarefas Completadas")
    print("7.Sair do Gerenciador")

    escolha = input ("\nDigite sua opção:")
    
    if escolha == "1":
        nome_tarefa = input("Digite a tarefa a ser adicionada: ")
        adicionar_tarefas(tarefas, nome_tarefa)
    elif escolha == "2":
        listar_tarefas(tarefas)
    elif escolha == "3":
        listar_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa à atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        listar_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa à completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        listar_tarefas(tarefas)
        indice_tarefa = int(input("Digite o numero da tarefa à editar: "))
        editar_tarefa(tarefas, indice_tarefa)
    elif escolha == "6":
        remover_tarefa_completada(tarefas)
        listar_tarefas(tarefas)
    elif escolha == "7":
        break
print("\nPrograma Finalizado, Até a Proxima")

