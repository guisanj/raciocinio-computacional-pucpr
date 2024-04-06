import json

def mostrar_menu_principal():
    print("*** Bem vindo ao sistema de gestão de dados acadêmicos! ***")
    print("Digite o número indicado para a opção desejada: ")
    print("1. ESTUDANTES")
    print("2. DISCIPLINAS")
    print("3. PROFESSORES")
    print("4. TURMAS")
    print("5. MATRÍCULAS")
    print("0. SAIR")
    while True:
        try:
            return int(input("Escolha a opção desejada: "))
            break
        except ValueError:
            print("Você escolheu uma opção INVÁLIDA. Tente novamente.")

def mostrar_menu_secundario(opcao1):
    print(f"Você escolheu a opção {opcao1}.")
    print("Digite o número indicado para a ação desejada: ")
    print("1. INCLUIR")
    print("2. LISTAR")
    print("3. ATUALIZAR")
    print("4. EXCLUIR")
    print("0. VOLTAR AO MENU PRINCIPAL")
    while True:
        try:
            return int(input("Escolha a ação desejada: "))
            break
        except ValueError:
            print("Você escolhe uma ação INVÁLIDA. Tente novamente.")

def processar_menu_secundario(opcao2, arquivo_json):
    print(f"Você escolheu a ação: {opcao2}.")
    while True:
        try:
            if opcao2 == 1:
                cadastrar_estudante(arquivo_json)
            elif opcao2 == 2:
                listar_estudantes(arquivo_json)
            elif opcao2 == 3:
                atualizar_estudantes(arquivo_json)
            elif opcao2 == 4:
                excluir_estudante(arquivo_json)
            elif opcao2 == 0:
                print("Você escolheu SAIR.")
            break
        except ValueError:
            print("Você escolheu uma opção INVÁLIDA. Tente novamente.")


def cadastrar_estudante(arquivo_json):
    try:
        codigo_estudante = int(input("Digite o código dx estudante: "))
    except ValueError:
        print("Código digitado incorretamente.")
        return
    nome_estudante = input("Digite o nome dx estudante: ")
    cpf_estudante = input("Digite o CPF dx estudante: ")
    dados_estudante = {
        "codigo": codigo_estudante,
        "nome": nome_estudante,
        "cpf": cpf_estudante
         }
    lista_temp = ler_arquivo(arquivo_json)
    lista_temp.append(dados_estudante)
    print(f"Estudante {nome_estudante} adicionadx com sucesso!")
    salvar_arquivo(lista_temp, arquivo_json)

def listar_estudantes(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    if len(lista_temp) == 0:
        print("Não existem estudantes cadastrados no momento")
    else:
        print("***ESTUDANTES***")
        for i, estudante in enumerate(lista_temp, start = 1):
            print(i, estudante)

def atualizar_estudantes(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    try:
        codigo_atualizacao = int(input("Digite o código dx estudante que deseja atualizar: "))
    except ValueError:
        print("Código digitado incorretamente.")
    for cadastro_estudante in lista_temp:
        if cadastro_estudante["codigo"] == codigo_atualizacao:
            cadastro_estudante["codigo"] = int(input("Digite o novo código dx estudante: "))
            cadastro_estudante["nome"] = input("Digite o nome corrigido dx estudante: ")
            cadastro_estudante["cpf"] = input("Digite CPF correto dx estudante: ")  
            print(f"Cadastro atualizado com sucesso: {cadastro_estudante}")
            salvar_arquivo(lista_temp, arquivo_json)
            return
    print("Estudante não localizadx.")

def excluir_estudante(nome_arquivo):
    lista_temp = ler_arquivo(arquivo_json)
    estudante_para_remover = None
    try:
        codigo_exclusao = int(input("Digite o código dx estudante que deseja excluir: "))
    except ValueError:
        print("Código digita incorretamente.")
    for cadastro_estudante in lista_temp:
        if cadastro_estudante["codigo"] == codigo_exclusao:
            estudante_para_remover = cadastro_estudante
            print(f"Removendo {cadastro_estudante}...")
            break
    if estudante_para_remover is not None:
        lista_temp.remove(estudante_para_remover)
        salvar_arquivo(lista_temp, arquivo_json)
        print("Remoção efetuada com sucesso!")
    else:
        print("Não há registros para o código informado.")

def salvar_arquivo(lista_temp, arquivo_json):
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(lista_temp, f, ensure_ascii=False)
        f.close()

def ler_arquivo(arquivo_json):
    try:
        with open(arquivo_json, "r", encoding="utf-8") as f:
            lista_carregada = json.load(f)
            f.close()
            return lista_carregada
    except:
        return []        

arquivo_json = "estudantes.json"

while True: 
    opcao1 = mostrar_menu_principal()
    if opcao1 == 1:
        while True:
            opcao2 = mostrar_menu_secundario(opcao1)
            processar_menu_secundario(opcao2, arquivo_json)
            break
    elif opcao1 >= 2 and opcao1 <= 5:
        print("FUNCIONALIDADE EM DESENVOLVIMENTO")
    elif opcao1 == 0:
        print("Você escolheu SAIR.")
        break