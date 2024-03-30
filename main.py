estudantes = []

while True: 
    print("*** Bem vindo ao sistema de gestão de dados acadêmicos! ***")
    print("Digite o número indicado para a opção desejada: ")
    print("1. ESTUDANTES")
    print("2. DISCIPLINAS")
    print("3. PROFESSORES")
    print("4. TURMAS")
    print("5. MATRÍCULAS")
    print("0. SAIR")

    opcao1 = input("Opção desejada: ")

    if opcao1 == "1":
        while True: 
            print(f"Você escolheu a opção: {opcao1}") 
            print("Escolha a ação desejada: ")
            print("1. INCLUIR")
            print("2. LISTAR")
            print("3. ATUALIZAR")
            print("4. EXCLUIR")
            print("0. SAIR")
            opcao2 = input("Escolha a ação desejada: ")
            print(f"Você escolheu a opção: {opcao2}")
            if opcao2 == "1":
                nome_estudante = input("Digite o nome dx estudante: ")
                estudantes.append([nome_estudante])
                print(f"Estudante {nome_estudante} adicionado com sucesso!")
                break
            elif opcao2 == "2":
                if len(estudantes) == 0:
                    print("Não existem estudantes cadastrados no momento")
                    break
                else:
                    print("***ESTUDANTES***")
                    for i, estudante in enumerate(estudantes, start = 1):
                        print(i, estudante)
            elif opcao2 =="3" or opcao2 == "4":
                print("FUNCIONALIDADE EM DESENVOLVIMENTO")
            elif opcao2 == "0":
                print("Você escolheu SAIR")
                break
            else:
                print("Você escolheu uma opção INVÁLIDA. Tente novamente")
    elif opcao1 == "2" or opcao1 == "3" or opcao1 == "4" or opcao1 == "5":
        print("FUNCIONALIDADE EM DESENVOLVIMENTO")
    elif opcao1 == "0":
        print("Você escolheu SAIR.")
        break
    else:
         print("Você escolheu uma opção inválida. Tente novamente.")
