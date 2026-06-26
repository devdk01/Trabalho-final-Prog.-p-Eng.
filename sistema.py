

from datetime import datetime


funcionarios = []



# FUNÇÃO: CADASTRAR FUNCIONÁRIO

def cadastrar():
    print("\n=== CADASTRAR FUNCIONÁRIO ===")

    nome = input("Digite o nome do funcionário: ")

    if nome == "":
        print("Erro: Digite um nome válido!")
        return

    id_func = len(funcionarios) + 1

    funcionario = {
        "id": id_func,
        "nome": nome,
        "pontos": []
    }

    funcionarios.append(funcionario)

    print(f"\nFuncionário cadastrado com sucesso!")
    print(f"ID: {id_func}")
    print(f"Nome: {nome}")



# FUNÇÃO: REGISTRAR ENTRADA

def entrada():
    print("\n=== REGISTRAR ENTRADA ===")

    try:
        id_func = int(input("Digite o ID do funcionário: "))
    except:
        print("Erro: ID inválido!")
        return

    for f in funcionarios:
        if f["id"] == id_func:

            hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

            registro = {
                "entrada": hora,
                "saida": ""
            }

            f["pontos"].append(registro)

            print("\nEntrada registrada com sucesso!")
            print("Horário:", hora)
            return

    print("Erro: Funcionário não encontrado!")



# FUNÇÃO: REGISTRAR SAÍDA

def saida():
    print("\n=== REGISTRAR SAÍDA ===")

    try:
        id_func = int(input("Digite o ID do funcionário: "))
    except:
        print("Erro: ID inválido!")
        return

    for f in funcionarios:
        if f["id"] == id_func:

            if len(f["pontos"]) == 0:
                print("Erro: Nenhuma entrada registrada!")
                return

            if f["pontos"][-1]["saida"] != "":
                print("Erro: A última entrada já possui saída registrada!")
                return

            agora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

            f["pontos"][-1]["saida"] = agora

            print("\nSaída registrada com sucesso!")
            print("Horário:", agora)
            return

    print("Erro: Funcionário não encontrado!")



# FUNÇÃO: VER HISTÓRICO

def historico():
    print("\n=== HISTÓRICO DE PONTO ===")

    try:
        id_func = int(input("Digite o ID do funcionário: "))
    except:
        print("Erro: ID inválido!")
        return

    for f in funcionarios:
        if f["id"] == id_func:

            print("\n====================================")
            print(f"Funcionário: {f['nome']}")
            print(f"ID: {f['id']}")
            print("====================================")

            if len(f["pontos"]) == 0:
                print("Nenhum registro encontrado.")
                return

            for i, p in enumerate(f["pontos"], start=1):
                print(f"\nRegistro {i}")
                print(f"Entrada: {p['entrada']}")
                print(f"Saída  : {p['saida']}")

            return

    print("Erro: Funcionário não encontrado!")


# MENU PRINCIPAL


opcao = 0

while opcao != 5:

    print("\n=================================")
    print("       SISTEMA DE PONTO")
    print("=================================")
    print("1 - Cadastrar Funcionário")
    print("2 - Registrar Entrada")
    print("3 - Registrar Saída")
    print("4 - Ver Histórico")
    print("5 - Sair")
    print("=================================")

    try:
        opcao = int(input("Escolha uma opção: "))
    except:
        print("Digite apenas números!")
        continue

    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        entrada()

    elif opcao == 3:
        saida()

    elif opcao == 4:
        historico()

    elif opcao == 5:
        print("\n=================================")
        print(" Sistema encerrado com sucesso!")
        print(" Obrigado por utilizar o sistema.")
        print("=================================")

    else:
        print("\nOpção inválida!")
