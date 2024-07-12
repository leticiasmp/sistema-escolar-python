import json

listaestudantes = {'codest': {'nome': 'nomeest', 'cpf': 'cpfest'}}
listaprofessores = {'codpro': {'nome': 'nomepro', 'cpf': 'cpfpro'}}
listadisciplinas = {'coddis': {'nome': 'nomedis'}}
listaturmas = {'codtur': {'coddis': 'coddis', 'codpro': 'codpro'}}
listamatriculas = {'codtur': {'codest': 'codest'}}

def escrever_json(lista, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(lista, f, indent=4) 
        f.close()

def ler_arquivo_json(arquivo):
    lista = {}
    try:
        with open(arquivo, 'r') as f: 
            lista = json.load(f) 
        return lista
    except FileNotFoundError:
        escrever_json({}, arquivo)
        return lista

def criar_registro_est(codest, nomeest, cpfest, arquivo):
    listaestudantes = ler_arquivo_json('listaestudantes.json')
    if codest in listaestudantes.keys(): 
        print("Código já cadastrado, verificar sistema!")
        return False
    if nomeest in [d['nome'] for d in listaestudantes.values()]:
        print("Nome já cadastrado, verificar sistema!")
        return False
    if cpfest in [d['cpf'] for d in listaestudantes.values()]:
        print("CPF já cadastrado, verificar sistema!")
        return False

    listaestudantes[codest] = {'nome': nomeest, 'cpf': cpfest}
    escrever_json(listaestudantes, 'listaestudantes.json')
    return True

def criar_registro_pro(codpro, nomepro, cpfpro, arquivo):
    listaprofessores = ler_arquivo_json('listaprofessores.json')
    if codpro in listaprofessores.keys(): 
        print("Código já cadastrado, verificar sistema!")
        return False
    if nomepro in [d['nome'] for d in listaprofessores.values()]:
        print("Nome já cadastrado, verificar sistema!")
        return False
    if cpfpro in [d['cpf'] for d in listaprofessores.values()]:
        print("CPF já cadastrado, verificar sistema!")
        return False

    listaprofessores[codpro] = {'nome': nomepro, 'cpf': cpfpro}
    escrever_json(listaprofessores, arquivo)

def criar_registro_dis(coddis, descdis, arquivo):
    listadisciplinas = ler_arquivo_json('listadisciplinas.json')
    if coddis in listadisciplinas.keys(): 
        print("Código já cadastrado, verificar sistema!")
        return False
    if descdis in [d['desc'] for d in listaprofessores.values()]:
        print("Descrição já cadastrada, verificar sistema!")
        return False
    listaprofessores[coddis] = {'desc': descdis}
    escrever_json(listadisciplinas, arquivo)

def criar_registro_tur(codtur, codpro, coddis, arquivo):
    listaturmas = ler_arquivo_json('listaturmas.json')
    if codtur in listaturmas.keys(): 
        print("Código já cadastrado, verificar sistema!")
        return False
    if codpro in listaprofessores.keys():
        return True
    if codpro not in listaprofessores.keys():
        print("O código deste professor não existe!")
        return False
    if coddis in listadisciplinas.keys():
        return True
    if coddis not in listadisciplinas.keys():
        print("O código desta disciplina não existe!")
        return False
    listaturmas[codtur] = {'codpro': codpro, 'coddis': coddis}
    escrever_json(listaturmas, arquivo)

def criar_registro_mat(codtur, codest, arquivo):
    listamatriculas = ler_arquivo_json('listamatriculas.json')
    if codtur in listaturmas.keys():
        return True
    if codtur not in listaturmas.keys():
        print("O código desta turma não existe!")
        return False
    if codest in listaestudantes.keys():
        return True
    if codest not in listaestudantes.keys():
        print("O código deste professor não existe!")
        return False
    listamatriculas[codtur] = {'codest': codest}
    escrever_json(listamatriculas, arquivo)

def alterar_registro(cod, arquivo):
    with open(arquivo, "r") as f:
        lista = json.load(f)
    if cod in lista:
        registro = lista[cod]
        print(f"O código {cod} está relacionado ao registro: {registro}")
        if input("Deseja seguir com a alteração(s/n)? ") == "s":
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo cpf: ")
            registro["nome"] = novo_nome
            registro["cpf"] = novo_cpf
            lista[cod] = registro
            print("Registro atualizado com sucesso!")
            return True
        else:
            print("Operação cancelada pelo usuário.")
            return False
    else:
        print(f"O código {cod} não foi encontrado nos registros!")
        return False

def alterar_registro_dis(coddis, arquivo):
    with open(arquivo, "r") as f:
        lista = json.load(f)
    if coddis in listadisciplinas:
        registro = listadisciplinas[coddis]
        print(f"O código {coddis} está relacionado ao registro: {registro}")
        if input("Deseja seguir com a alteração(s/n)? ") == "s":
            nova_desc = input("Digite o nova desc: ")
            registro["desc"] = nova_desc
            listadisciplinas[coddis] = registro
            print("Registro atualizado com sucesso!")
            return True
        else:
            print("Operação cancelada pelo usuário.")
            return False
    else:
        print(f"O código {coddis} não foi encontrado nos registros!")
        return False
    
def alterar_registro_tur(codtur, arquivo):
    with open(arquivo, "r") as f:
        lista = json.load(f)
    if codtur in listaturmas:
        registro = listaturmas[codtur]
        print(f"O código {codtur} está relacionado ao registro: {registro}")
        if input("Deseja seguir com a alteração(s/n)? ") == "s":
            nova_disc = input("Digite o nova disciplina: ")
            novo_pro = input("Digite o código do novo professor: ")
            registro["coddis"] = nova_disc
            registro["codpro"] = novo_pro
            lista[codtur] = registro
            print("Registro atualizado com sucesso!")
            return True
        else:
            print("Operação cancelada pelo usuário.")
            return False
    else:
        print(f"O código {codtur} não foi encontrado nos registros!")
        return False

def alterar_registro_mat(codtur, codest, arquivo):
    with open(arquivo, "r") as f:
        lista = json.load(f)
    if codtur in listamatriculas:
        registro = listamatriculas[codtur]
        print(f"O código {codtur} está relacionado ao registro: {registro}")
        if input("Deseja seguir com a alteração(s/n)? ") == "s":
            novo_est = input("Digite o novo estudante: ")
            registro["codest"] = novo_est
            listamatriculas[codtur] = registro
            print("Registro atualizado com sucesso!")
            return True
        else:
            print("Operação cancelada pelo usuário.")
            return False
    else:
        print(f"O código {codtur} não foi encontrado nos registros!")
        return False

def excluir_registro(cod: int, arquivo: str):
    with open(arquivo, "r") as f:
        lista = json.load(f)

    registro = lista.get(cod)
    if registro is not None:
        del lista[cod]
        print("Registro excluído com sucesso!")
        print(f"Essa é a sua lista de registros: {lista}")
        with open(arquivo, "w") as f:
            json.dump(lista, f)
        return True
    else:
        print("Registro não encontrado! Digite o código novamente.")
        return False

def listar_registro(listar, arquivo):
    if listar == "s":
        with open(arquivo, "r") as f:
            dados = json.load(f)
            if len(dados) > 0:
                for cod, registro in dados.items(): 
                    print(f"Código: {cod} - Nome: {registro['nome']} - CPF: {registro['cpf']}")
                print("Fim da listagem") 
                return True
            else: 
                print("Não há registros para exibir!")
    return False


def finalizar_programa():
    print('Finalizando o programa...')
    exit(0)

def limpar_tela():
    print('\n' * 100)

def menu_principal():
    while True:
        opcaomp = int(input('Qual área você quer trabalhar hoje na base do estudante?\n\n'
                      '(1) Estudantes.\n'
                      '(2) Professores.\n'
                      '(3) Disciplinas.\n'
                      '(4) Turmas.\n'
                      '(5) Matrículas.\n'
                      '(6) Sair.\n'
                      'Faça sua escolha: '))
        if opcaomp == 1:
            listaestudantes = ler_arquivo_json('listaestudantes.json')
            estudantes(listaestudantes)
        elif opcaomp == 2:
            listaprofessores = ler_arquivo_json('listaprofessores.json')
            professores(listaprofessores)
        elif opcaomp == 3:
            listadisciplinas = ler_arquivo_json('listadisciplinas.json')
            disciplinas(listadisciplinas)
        elif opcaomp == 4:
            listaturmas = ler_arquivo_json('listaturmas.json')
            turmas(listaturmas)
        elif opcaomp == 5:
            listamatriculas = ler_arquivo_json('listamatriculas.json')
            matriculas(listamatriculas)
        elif opcaomp == 6:
            finalizar_programa()
            print("Programa encerrado!")
            break
        else:
            print('Opção inválida! Tente novamente ...')

def menu_operacoes():
    while True:
        opcaomo = int(input('\nQuais funções você deseja executar com o menu de operações?'
                      '\n\n(1) Criar novo registro.'
                      '\n(2) Alterar um registro.'
                      '\n(3) Excluir um registro.'
                      '\n(4) Listar registros.'
                      '\n(5) Voltar ao menu principal.'
                      '\n(6) Sair.'
                      '\nFaça sua escolha: '))
        return opcaomo


def voltar_ao_menu(opcaovm):
     opcaovm = input('Deseja voltar ao menu principal? (s/n)')
     while True: 
        if opcaovm == 's':
            menu_principal()
        else:
            break

def estudantes(listaestudantes):
    opcaomo = menu_operacoes()
    if opcaomo == 1:
        while True:
            codest = input("Digite o código do estudante:")
            if codest:
                try:
                    codest = int(codest)
                except ValueError:
                    print("Código inválido. Digite um número inteiro.")
            else:
                print("Código não digitado. Tente novamente.")
                continue
            while True: 
                nomeest = input("Digite o nome do estudante: ")
                if nomeest:
                    nomeest = nomeest
                    break
                else:
                    print("Nome não digitado. Tente novamente.")
                    continue
            while True:
                cpfest = input("Digite o cpf do estudante: ")
                if cpfest:
                    try:
                        cpfest = int(cpfest)
                        break
                    except ValueError:
                        print("CPF inválido. Digite um número inteiro.")
                        continue
                else:
                    print("CPF não digitado. Tente novamente.")
                    continue
            novo_registro = criar_registro_est(codest, nomeest, cpfest, 'listaestudantes.json')
            if novo_registro:
                print("Parabéns, registro realizado com sucesso!")
            else: 
                print("Falha ao tentar adicionar o contato!")
            continuar = input("Deseja criar mais um registro (s/n)?")
            if continuar != "s":
                break
    elif opcaomo == 2:
        while True:
            codpro = int(input("Digite o código do registro a ser alterado: "))
            if alterar_registro(codpro, 'listaestudantes.json'):
                break
            else: 
                print("Falha ao tentar alterar o registro!")
    elif opcaomo == 3:
        while True: 
            codest = int(input("Digite o código do estudante que deseja excluir:"))
            if excluir_registro(codest, 'listaestudantes.json'):
                break
            else: 
                print("Falha ao tentar excluir o registro!")
    elif opcaomo == 4:
        while True: 
            listar = input("Deseja listar os registros? (s/n)")
            if listar == "s":
                listar_registro(listar, 'listaestudantes.json')
                print("Esses são todos os seus registros")
                break
            elif listar == "n":
                print("Você optou por não listar seus registros.")
                break
            else:
                print("Opção inválida. Tente novamente.") 
    return ler_arquivo_json('listaestudantes.json')

def professores(listaprofessores):
    opcaomo = menu_operacoes()
    if opcaomo == 1: 
        while True:
            codpro = input("Digite o código do professor:")
            if codpro:
                try:
                    codpro = int(codpro)
                except ValueError:
                    print("Código inválido. Digite um número inteiro.")
                    continue
            else:
                print("Código não digitado. Tente novamente.")
                continue
            while True: 
                nomepro = input("Digite o nome do professor: ")
                if nomepro:
                    nomepro = nomepro
                    break
                else:
                    print("Nome não digitado. Tente novamente.")
                    continue
            while True:
                cpfpro = input("Digite o cpf do professor: ")
                if cpfpro:
                    try:
                        cpfpro = int(cpfpro)
                        break
                    except ValueError:
                        print("CPF inválido. Digite um número inteiro.")
                        continue
                else:
                    print("CPF não digitado. Tente novamente.")
                    continue
            novo_registro = criar_registro_pro(codpro, nomepro, cpfpro, 'listaprofessores.json')
            if novo_registro:
                print("Parabéns, registro realizado com sucesso!")
            else: 
                print("Falha ao tentar adicionar o contato!")
            continuar = input("Deseja criar mais um registro (s/n)?")
            if continuar != "s":
                break
    elif opcaomo == 2:
        while True:
            codpro = int(input("Digite o código do registro a ser alterado: "))
            if alterar_registro(codpro, 'listaprofessores.json'):
                break
            else: 
                print("Falha ao tentar alterar o registro!")
    elif opcaomo == 3:
        while True: 
            codpro = int(input("Digite o código do professor que deseja excluir:"))
            if excluir_registro(codpro, 'listaprofessores.json'):
                break
            else: 
                print("Falha ao tentar excluir o registro!")
    elif opcaomo == 4:
        while True: 
            listar = input("Deseja listar os registros? (s/n)")
            if listar == "s":
                listar_registro(listar, 'listaprofessores.json')
                print("Esses são todos os seus registros")
                break
            elif listar == "n":
                print("Você optou por não listar seus registros.")
                break
            else:
                print("Opção inválida. Tente novamente.")  
    return ler_arquivo_json('listaprofessores.json') 

def disciplinas(lista):
    opcaomo = menu_operacoes()
    if opcaomo == 1: 
        while True:
            coddis = input("Digite o código da disciplina:")
            if coddis:
                try:
                    coddis = int(coddis)
                except ValueError:
                    print("Código inválido. Digite um número inteiro.")
                    continue
            else:
                print("Código não digitado. Tente novamente.")
                continue
            while True: 
                descdis = input("Digite a descrição da disciplina: ")
                if descdis:
                    descdis = descdis
                    break
                else:
                    print("Nome não digitado. Tente novamente.")
                    continue
            novo_registro = criar_registro_dis(coddis, descdis, 'listadisciplinas.json')
            listadisciplinas = 'listadisciplinas.json'
            if novo_registro:
                listadisciplinas = novo_registro
                print("Parabéns, registro realizado com sucesso!")
            else: 
                print("Falha ao tentar adicionar o contato!")
            continuar = input("Deseja criar mais um registro (s/n)?")
            if continuar != "s":
                break
    elif opcaomo == 2:
        while True:
            coddis = int(input("Digite o código do registro a ser alterado: "))
            if alterar_registro_dis(coddis, 'listadisciplinas.json'):
                break
            else: 
                print("Falha ao tentar alterar o registro!")
    elif opcaomo == 3:
        while True: 
            coddis = int(input("Digite o código da disciplina que deseja excluir:"))
            if excluir_registro(coddis, 'listadisciplinas.json'):
                break
            else: 
                print("Falha ao tentar excluir o registro!")
    elif opcaomo == 4:
        while True: 
            listar = input("Deseja listar os registros? (s/n)")
            if listar == "s":
                listar_registro(listar, 'listadisciplinas.json')
                print("Esses são todos os seus registros")
                break
            elif listar == "n":
                print("Você optou por não listar seus registros.")
                break
            else:
                print("Opção inválida. Tente novamente.")  
    return ler_arquivo_json('listadisciplinas.json') 

def turmas(lista):
    opcaomo = menu_operacoes()
    if opcaomo == 1: 
        while True:
            codtur = input("Digite o código da turma:")
            if codtur:
                try:
                    codtur = int(codtur)
                except ValueError:
                    print("Código inválido. Digite um número inteiro.")
            else:
                print("Código não digitado. Tente novamente.")
                continue
            while True: 
                coddis = input("Digite o código da disciplina: ")
                if coddis:
                    coddis = coddis
                    break
                else:
                    print("Código não digitado. Tente novamente.")
                    continue
            while True: 
                codpro = input("Digite o código do professor: ")
                if codpro:
                    codpro= codpro
                    break
                else:
                    print("Código não digitado. Tente novamente.")
                    continue
            novo_registro = criar_registro_tur(codtur, coddis, codpro, 'listaturmas.json')
            if novo_registro:
                listaturmas = novo_registro
                print("Parabéns, registro realizado com sucesso!")
            else: 
                print("Falha ao tentar adicionar o contato!")
            continuar = input("Deseja criar mais um registro (s/n)?")
            if continuar != "s":
                break
    elif opcaomo == 2:
        while True:
            codtur = int(input("Digite o código do registro a ser alterado: "))
            if alterar_registro_tur(codtur, 'listaturmas.json'):
                break
            else: 
                print("Falha ao tentar alterar o registro!")
    elif opcaomo == 3:
        while True: 
            codtur = int(input("Digite o código da turma que deseja excluir:"))
            if excluir_registro(codtur, 'listaturmas.json'):
                break
            else: 
                print("Falha ao tentar excluir o registro!")
    elif opcaomo == 4:
        while True: 
            listar = input("Deseja listar os registros? (s/n)")
            if listar == "s":
                listar_registro(listar, 'listaturmas.json')
                print("Esses são todos os seus registros")
                break
            elif listar == "n":
                print("Você optou por não listar seus registros.")
                break
            else:
                print("Opção inválida. Tente novamente.")  
    return ler_arquivo_json('listaturmas.json') 

def matriculas(lista):
    opcaomo = menu_operacoes()
    if opcaomo == 1: 
        while True:
            codtur = input("Digite o código da turma:")
            if codtur:
                try:
                    codtur = int(codtur)
                except ValueError:
                    print("Código inválido. Digite um número inteiro.")
            else:
                print("Código não digitado. Tente novamente.")
                continue
            while True: 
                codest = input("Digite o código do estudante: ")
                if codest:
                    codest = codest
                    break
                else:
                    print("Código não digitado. Tente novamente.")
                    continue
            novo_registro = criar_registro_mat(codtur, codest, 'listamatriculas.json')
            if novo_registro:
                listamatriculas = novo_registro
                print("Parabéns, registro realizado com sucesso!")
            else: 
                print("Falha ao tentar adicionar o contato!")
            continuar = input("Deseja criar mais um registro (s/n)?")
            if continuar != "s":
                break
    elif opcaomo == 2:
        while True:
            codtur = int(input("Digite o código do registro a ser alterado: "))
            if alterar_registro_tur(codtur, 'listaturmas.json'):
                break
            else: 
                print("Falha ao tentar alterar o registro!")
    elif opcaomo == 3:
        while True: 
            codtur = int(input("Digite o código da turma da matrícula que deseja excluir:"))
            if excluir_registro(codtur, 'listamatriculas.json'):
                break
            else: 
                print("Falha ao tentar excluir o registro!")
    elif opcaomo == 4:
        while True: 
            listar = input("Deseja listar os registros? (s/n)")
            if listar == "s":
                listar_registro(listar, 'listamatriculas.json')
                print("Esses são todos os seus registros")
                break
            elif listar == "n":
                print("Você optou por não listar seus registros.")
                break
            else:
                print("Opção inválida. Tente novamente.")  
    return ler_arquivo_json('listamatriculas.json') 

menu_principal()
voltar_ao_menu()
finalizar_programa()
