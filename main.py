while True:
    print("*** Bem vindo ao sistema de gestão de dados acadêmicos! ***")
    print("Digite o número indicado para a opção desejada: ")
    print("1. ESTUDANTES")
    print("2. DISCIPLINAS")
    print("3. PROFESSORES")
    print("4. TURMAS")
    print("0. SAIR")

    opcao1 = input("Opção desejada: ")

    if int(opcao1) >= 1 and int(opcao1) <= 4:
        while True:
            print("Você escolheu a opção:", opcao1)
            print("Escolha a ação desejada: ")
            print("1. INCLUIR")
            print("2. LISTAR")
            print("3. ATUALIZAR")
            print("4. EXCLUIR")
            print("0. SAIR")
            opcao2 = input("Escolha a ação desejada: ")
            if int(opcao2) >= 1 and int(opcao2) <= 4:
                print("Você escolheu a ação:", opcao2)
            elif int(opcao2) == 0:
                print("Você escolheu SAIR")
                break
            else:
                print("Você escolheu uma opção INVÁLIDA.")
    elif int(opcao1) == 0:
            print("Você escolheu SAIR.")
            break
    else:
         print("Você escolheu uma opção inválida")
