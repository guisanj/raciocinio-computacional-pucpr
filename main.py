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

def processar_menu_secundario(opcao1, opcao2):
    print(f"Você escolheu a ação: {opcao2}.")
    if opcao1 == 1:
        arquivo_json = "estudantes.json"
    elif opcao1 == 2:
        arquivo_json = "disciplinas.json"
    elif opcao1 == 3: 
        arquivo_json = "professores.json"
    elif opcao1 == 4:
        arquivo_json = "turmas.json"
    elif opcao1 == 5:
        arquivo_json = "matriculas.json"
    while True:
        try:
            if (opcao1 == 1 or opcao1 == 3) and (opcao2 == 1 or opcao2 == 3): 
                if opcao2 == 1:
                    cadastrar_estudante_professor(arquivo_json)
                elif opcao2 == 3:
                    atualizar_estudantes_professor(arquivo_json)
            elif opcao1 == 2 and (opcao2 == 1 or opcao2 == 3):
                if opcao2 == 1:
                    cadastrar_disciplina(arquivo_json)
                elif opcao2 == 3:
                    atualizar_disciplina(arquivo_json)
            elif opcao1 == 4:
                    if opcao2 == 1:
                        cadastrar_turma(arquivo_json)
                    elif opcao2 == 3:
                        atualizar_turma(arquivo_json)
            elif opcao1 == 5:
                if opcao2 == 1:
                    cadastrar_matricula(arquivo_json)
                elif opcao2 == 3:
                    atualizar_matricula(arquivo_json)
            elif (opcao1 >= 1 and opcao1 <= 5) and (opcao2 == 2 or opcao2 == 4):
                if opcao2 == 2:
                    listar_grupo_escolhido(arquivo_json)
                elif opcao2 == 4:
                    excluir_estudante_professor(arquivo_json)
            elif opcao2 == 0:
                print("Você escolheu VOLTAR ao menu principal.")
            break
        except ValueError:
            print("Você escolheu uma opção inválida.")

def cadastrar_estudante_professor(arquivo_json):
    while True:
        try:
            codigo_estudante_professor = int(input("Digite o código desejado: "))
            break
        except ValueError:
            print("Código digitado incorretamente.")
    for cadastro_estudante_professor in ler_arquivo(arquivo_json):
        if cadastro_estudante_professor["codigo"] == codigo_estudante_professor:
            print(f"Já existe um registro na base utilizando o código desejado.: {cadastro_estudante_professor}")
            return
    nome_estudante_professor = input("Digite o nome: ")
    cpf_estudante_professor = input("Digite o CPF: ")
    dados_estudante_professor = {
        "codigo": codigo_estudante_professor,
        "nome": nome_estudante_professor,
        "cpf": cpf_estudante_professor
         }
    lista_temp = ler_arquivo(arquivo_json)
    lista_temp.append(dados_estudante_professor)
    print(f"{nome_estudante_professor} adicionadx com sucesso!")
    salvar_arquivo(lista_temp, arquivo_json)

def atualizar_estudantes_professor(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    try:
        codigo_atualizacao = int(input("Digite o código do registro que deseja atualizar: "))
    except ValueError:
        print("Código digitado incorretamente.")
    for cadastro_estudante_professor in lista_temp:
        if cadastro_estudante_professor["codigo"] == codigo_atualizacao:
            print(f"Atualizando o registro {cadastro_estudante_professor}")
            while True:
                try:
                    novo_codigo_estudante_professor = int(input("Digite o novo código: "))
                    for cadastro2_estudante_professor in lista_temp:
                        if cadastro2_estudante_professor["codigo"] == novo_codigo_estudante_professor:
                            print(f"Já existe um registro utilizando o código informado: {cadastro2_estudante_professor}.")
                            return
                    break
                except ValueError:
                    print("Código digitado incorretamente.")
            cadastro_estudante_professor["codigo"] = novo_codigo_estudante_professor
            cadastro_estudante_professor["nome"] = input("Digite o nome corrigido: ")
            cadastro_estudante_professor["cpf"] = input("Digite CPF correto: ")  
            print(f"Cadastro atualizado com sucesso: {cadastro_estudante_professor}")
            salvar_arquivo(lista_temp, arquivo_json)
            return
    print("Não foi localizado um registro com o código informado.")

def excluir_estudante_professor(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    estudante_professor_para_remover = None
    try:
        codigo_exclusao = int(input("Digite o código do registro que deseja excluir: "))
    except ValueError:
        print("Código digitado incorretamente.")
    for cadastro_estudante_professor in lista_temp:
        if cadastro_estudante_professor["codigo"] == codigo_exclusao:
            estudante_professor_para_remover = cadastro_estudante_professor
            print(f"Removendo {cadastro_estudante_professor}...")
            break
    if estudante_professor_para_remover is not None:
        lista_temp.remove(estudante_professor_para_remover)
        salvar_arquivo(lista_temp, arquivo_json)
        print("Remoção efetuada com sucesso!")
    else:
        print("Não há registros para o código informado.")

def cadastrar_disciplina(arquivo_json):
    while True:
        try:
            codigo_discplina = int(input("Digite o código da disciplina: "))
            break
        except ValueError:
            print("Código digitado incorretamente.")
    nome_disciplina = input("Digite o nome da disciplina: ")
    dados_disciplina = {
        "codigo": codigo_discplina,
        "nome": nome_disciplina,
         }
    lista_temp = ler_arquivo(arquivo_json)
    lista_temp.append(dados_disciplina)
    print(f"Disciplina de {nome_disciplina} adicionada com sucesso!")
    salvar_arquivo(lista_temp, arquivo_json)

def atualizar_disciplina(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    try:
        codigo_atualizacao = int(input("Digite o código da disciplina que deseja atualizar: "))
    except ValueError:
        print("Código digitado incorretamente.")
    for cadastro_disciplina in lista_temp:
        if cadastro_disciplina["codigo"] == codigo_atualizacao:
            print(f"Atualizando a disciplina {cadastro_disciplina}")
            cadastro_disciplina["codigo"] = int(input("Digite o novo código da disciplina: "))
            cadastro_disciplina["nome"] = input("Digite o nome da disciplina corrigido: ")
            print(f"Cadastro atualizado com sucesso: {cadastro_disciplina}")
            salvar_arquivo(lista_temp, arquivo_json)
            return
    print("Não foi localizada uma disciplina com o código informado.")

def cadastrar_turma(arquivo_json):
    while True:
        try:
            codigo_turma = int(input("Digite o código da turma: "))
            codigo_professor = int(input("Digite o código do professor: "))
            codigo_disciplina = int(input("Digite o código da disciplina: "))
            break
        except ValueError:
            print("Código digitado incorretamente.")
    for cadastro_professor in ler_arquivo("professores.json"):
        if cadastro_professor["codigo"] == codigo_professor:
            print(f"Localizado discente com o código informado!")
            break
        else:
            print("Não há professor registrado com o código informado.")
            return
    for cadastro_disciplina in ler_arquivo("disciplinas.json"):
        if cadastro_disciplina["codigo"] == codigo_disciplina:
            print("Localizada disciplina com o código informado.")
            break
        else:
            print("Não há disciplina registrada com o código informado.")
            return
    dados_disciplina = {
        "codigo_turma": codigo_turma,
        "codigo_professor": codigo_professor,
        "codigo_disciplina": codigo_disciplina
    }
    lista_temp = ler_arquivo(arquivo_json)
    lista_temp.append(dados_disciplina)
    print(f"Turma de código {codigo_turma} adicionada com sucesso!")
    salvar_arquivo(lista_temp, arquivo_json)

def atualizar_turma(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    try:
        codigo_atualizacao = int(input("Digite o código da turma que deseja atualizar: "))
    except ValueError:
        print("Código digitado incorretamente.")
    for cadastro_turma in lista_temp:
        if cadastro_turma["codigo_turma"] == codigo_atualizacao:
            print(f"Atualizando a turma de código {cadastro_turma}")
            while True:
                try:
                    novo_codigo_turma = int(input("Digite o código correto da turma: "))
                    novo_codigo_professor = int(input("Digite o código correto do professor: "))
                    novo_codigo_disciplina = int(input("Digite o código correto da disciplina: "))
                    break
                except ValueError:
                    print("Código digitado incorretamente.")
            for cadastro_professor in ler_arquivo("professor.json"):
                if cadastro_professor["codigo"] == novo_codigo_professor:
                    print("Localizado discente com o código informado!")
                    break
                else:
                    print("Não há professor registrado com o código informado.")
                    return
            for cadastro_disciplina in ler_arquivo("disciplinas.json"):
                if cadastro_disciplina["codigo"] == novo_codigo_disciplina:
                    print("Localizada disciplina com o código informado.")
                    break
                else:
                    print("Não há disciplina registrada com o código informado.")
                    return
            cadastro_turma["codigo_turma"] = novo_codigo_turma
            cadastro_turma["codigo_professor"] = novo_codigo_professor
            cadastro_turma["codigo_disciplina"] = novo_codigo_disciplina
            print(f"Registro da turma atualizado com sucesso: {cadastro_turma}")
            salvar_arquivo(lista_temp, arquivo_json)
            return
    print("Não foi localizada uma turma com o código informado.")

def cadastrar_matricula(arquivo_json):
    while True:
        try:
            codigo_turma = int(input("Digite o código da turma: "))
            codigo_estudante = int(input("Digite o código do estudante: "))
            break
        except ValueError:
            print("Código digitado incorretamente.")
    for cadastro_turma in ler_arquivo("turmas.json"):
        if cadastro_turma["codigo_turma"] == codigo_turma:
            print(f"Localizada turma com o código informado!")
            break
        else:
            print("Não há turma registrada com o código informado.")
            return
    for cadastro_estudante in ler_arquivo("estudantes.json"):
        if cadastro_estudante["codigo"] == codigo_estudante:
            print("Localizado estudante com o código informado.")
            break
        else:
            print("Não há estudante registrado ocom o código informado.")
            return
    dados_turma = {
        "codigo_turma": codigo_turma,
        "codigo_estudante": codigo_estudante
    }
    lista_temp = ler_arquivo(arquivo_json)
    lista_temp.append(dados_turma)
    print(f"Matrícula {dados_turma} adicionada com sucesso!")
    salvar_arquivo(lista_temp, arquivo_json)

def atualizar_matricula(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    try:
        codigo_atualizacao = int(input("Digite o código do estudante para localizarmos sua matrícula: "))
    except ValueError:
        print("Código digitado incorretamente.")
    for cadastro_matricula in lista_temp:
        if cadastro_matricula["codigo_estudante"] == codigo_atualizacao:
            print(f"Localizada matrícula: {cadastro_matricula}")
            while True:
                try:
                    novo_codigo_turma = int(input("Digite a turma correta: "))
                    for turma in ler_arquivo("turmas.json"):
                        if turma["codigo_turma"] == novo_codigo_turma:
                            print(f"Localizada turma: {turma}")
                            turma["codigo_turma"] == novo_codigo_turma
                            print(f"Matrícula atualizada com sucesso: {cadastro_matricula}")
                            break
                        else:
                            print("Não há turma registrada com o código informado.")
                            return
                except ValueError:
                        print("Código digitado incorretamente.")
        else:
            print("Não foi localizado um registro com o código informado.")   

def listar_grupo_escolhido(arquivo_json):
    lista_temp = ler_arquivo(arquivo_json)
    if len(lista_temp) == 0:
        print("Não existem registros no momento")
    else:
        print("***LISTAGEM***")
        for i, cadastro in enumerate(lista_temp, start = 1):
            print(i, cadastro)

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

while True: 
    opcao1 = mostrar_menu_principal()
    if opcao1 >= 1 and opcao1 <= 4:
        while True:
            opcao2 = mostrar_menu_secundario(opcao1)
            processar_menu_secundario(opcao1, opcao2)
            break
    elif opcao1 == 5:
        print("FUNCIONALIDADE EM DESENVOLVIMENTO")
    elif opcao1 == 0:
        print("Você escolheu SAIR.")
        break