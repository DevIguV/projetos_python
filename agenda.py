def adicionar_contato(agenda, nome_contato, telefone_contato, email):
    contato = {"Nome": nome_contato, "Telefone" : telefone_contato, "Email" : email, "favorito": False}
    agenda.append(contato)
    print(f"O contato {nome_contato} foi adicionado!")
    return
def ver_contato(agenda):
    print("\n Listas de Contatos")
    for indice, agenda in enumerate(agenda, start=1):
        status = "✪" if agenda ["favorito"] else " "
        nome_contato = agenda ["Nome"]
        telefone_contato = agenda ["Telefone"]
        email = agenda ["Email"]
        print(f"{indice}. [{status}] {nome_contato}, {telefone_contato}, {email}")
def editar_contato(agenda, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email):    
    indice_contato_ajustado = int(indice_contato) - 1 
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["Nome"] = novo_nome_contato
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["Telefone"] = novo_telefone_contato
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["Email"] = novo_email
        print(f"Dados do contato {indice_contato} foram atualizados para {novo_nome_contato}, {novo_telefone_contato}, {novo_email}")
    else:
        print("Contato selecionada inexistente")
    return
def favoritar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado] ["favorito"] = not agenda[indice_contato_ajustado] ["favorito"]
        print(f"Contato {indice_contato} marcado/desmarcado como favoritado!!")
    return
def ver_favoritos(): 
    print("\n Listas de Favoritos")
    favoritos = [contato for contato in agenda if contato ["favorito"]]
    for indice, contato in enumerate(agenda, start=1):
        status = "✪" if contato ["favorito"] else " "
    for contato in favoritos:
        print(f"{indice}. [{status}] {contato['Nome']}, {contato['Telefone']}, {contato['Email']}")
def remover_contato():
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(agenda):    
        del agenda[indice_contato_ajustado]
        print("O contato selecionado foi removido!!")

agenda = []

while True:
    print ("\nBem-vindo a Agenda de Contatos")
    print("\n°° MENU °°")
    print("Selecione abaixo a opção desejada:")
    print("1. Adicionar Contato")
    print("2. Ver Contato")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Ver Favoritos")
    print("6. Remover Contato")
    print("7. Finalizar")

    escolha = input ("\nDigite sua opção:")
    
    if escolha == "1":
       while True:
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite os dados (Telefone): ")
        email = input("Digite os dados (Email): ")
        adicionar_contato(agenda, nome_contato, telefone_contato, email)
        break
    elif escolha == "2":
        ver_contato(agenda)
    elif escolha == "3":
        while True:
            ver_contato(agenda)
            indice_contato = input("Selecione o contato à atualizar: ")
            novo_nome_contato = input("Digite o novo nome do contato: ")
            novo_telefone_contato = input("Digite o novo telefone do contato: ")
            novo_email = input("Digite o novo email do contato: ")
            editar_contato(agenda, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email)
            break
    elif escolha == "4":
        ver_contato(agenda)
        indice_contato = input("Escolha o contato a marcar/desmarcar como favorito: ")
        favoritar_contato(agenda, indice_contato)
    elif escolha == "5":  
        ver_favoritos()   
    elif escolha == "6":
        while True:   
            ver_contato(agenda)
            indice_contato = input("Selecione o contato à remover: ")
            remover_contato()
            break   
    elif escolha == "7":
        break
    else:
        print("Selecione uma opção válida!!")

print("\nPrograma Finalizado, Até a Proxima!!!!")