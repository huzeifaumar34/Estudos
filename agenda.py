agenda = {}

def menu():
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("0 - Sair")

def adicionar(agenda):
    nome = input("Nome do contato: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def buscar(agenda):
    nome = input("Nome para buscar: ")
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado")

def listar(agenda):
    if not agenda:
        print("Agenda vazia")
    else:
        print("Contatos:")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")

def remover(agenda):
    nome = input("Nome para remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido")
    else:
        print("Contato não encontrado")

while True:
    menu()
    op = input(">> ")
    if op == "1":
        adicionar(agenda)
    elif op == "2":
        listar(agenda)
    elif op == "3":
        buscar(agenda)
    elif op == "4":
        remover(agenda)
    elif op == "0":
        print("Até mais!")
        break
    else:
        print("Opção inválida")

