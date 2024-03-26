print("*** Bem vindo ao sistema de gestão de dados acadêmicos! ***")
print("Digite o número indicado para a opção desejada: ")
print("1. ESTUDANTES")
print("2. DISCIPLINAS")
print("3. PROFESSORES")
print("4. TURMAS")
print("0. SAIR")

try:
    opcao1 = int(input("Opção desejada: "))
except ValueError:
    print("Você escolheu uma opção INVÁLIDA")
    exit()

if opcao1 >= 1 and opcao1 <= 4:
    print("Você escolheu a opção: ")
    print("Escolha a ação desejada: ")
    print("1. INCLUIR")
    print("2. LISTAR")
    print("3. ATUALIZAR")
    print("4. EXCLUIR")
    print("0. SAIR")
    try:
        opcao2 = int(input("Opção desejada: "))
    except ValueError:
        print("Você escolheu uma opção INVÁLIDA")
    exit()
    if opcao2 >= 1 and opcao2 <= 4:
        print("Você escolheu a ação: ", opcao2)
    elif opcao2 == 0:
        print("Você escolheu FINALIZAR a operação")
    else:
        print("Você escolheu uma ação INVÁLIDA")
elif opcao1 == 0:
    print("Você escolheu FINALIZAR a operação.")
else:
    print("Você escolheu uma opção INVÁLIDA")
