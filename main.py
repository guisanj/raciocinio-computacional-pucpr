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
                codigo_estudante = int(input("Digite o código dx estudante: "))
                nome_estudante = input("Digite o nome dx estudante: ")
                cpf_estudante = input("Digite o CPF dx estudante: ")
                dados_estudante = {
                    "codigo": codigo_estudante,
                    "nome": nome_estudante,
                    "cpf": cpf_estudante
                }
                estudantes.append(dados_estudante)
                print(f"Estudante {nome_estudante} adicionadx com sucesso!")
                break
            elif opcao2 == "2":
                if len(estudantes) == 0:
                    print("Não existem estudantes cadastrados no momento")
                    break
                else:
                    print("***ESTUDANTES***")
                    for i, estudante in enumerate(estudantes, start = 1):
                        print(i, estudante)
            elif opcao2 =="3":
                codigo_atualizacao = int(input("Digite o código dx estudante que deseja atualizar: "))
                for cadastro_estudante in estudantes:
                    if cadastro_estudante["codigo"] == codigo_atualizacao:
                        cadastro_estudante["codigo"] = int(input("Digite o novo código dx estudante: "))
                        cadastro_estudante["nome"] = input("Digite o nome corrigido dx estudante: ")
                        cadastro_estudante["cpf"] = input("Digite CPF correto dx estudante: ")
                        codigo_atualizacao = cadastro_estudante["codigo"]
                        print(f"Cadastro atualizado com sucesso: {cadastro_estudante}")
                        break
                    else:
                        print("Estudante não localizadx.")
                        break
            elif opcao2 == "4":
                codigo_exclusao = int(input("Digite o código dx estudante que deseja excluir: "))
                for cadastro_estudante in estudantes:
                    if cadastro_estudante["codigo"] == codigo_exclusao:
                        estudantes.remove(cadastro_estudante)
                        print("Removeção efetuada com sucesso!")
                    else:
                        print("Estudante não localizadx.")       
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
         print("Você escolheu uma opção INVÁLIDA. Tente novamente.")
