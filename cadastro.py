import sys

clientes = []

def cadastrar_cliente():
    print("\n=== Cadastro de Cliente ===")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")


def listar_clientes():
    print("\n=== Lista de Clientes ===")
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")
    print()


def buscar_cliente():
    print("\n=== Buscar Cliente ===")
    nome_busca = input("Digite o nome do cliente: ")

    encontrados = [c for c in clientes if nome_busca.lower() in c["nome"].lower()]

    if encontrados:
        for cliente in encontrados:
            print(f"Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")
    else:
        print("Cliente não encontrado.")
    print()


def remover_cliente():
    print("\n=== Remover Cliente ===")
    nome = input("Digite o nome do cliente para remover: ")

    for cliente in clientes:
        if cliente["nome"].lower() == nome.lower():
            clientes.remove(cliente)
            print("Cliente removido com sucesso!\n")
            return

    print("Cliente não encontrado.\n")


def menu():
    while True:
        print("=== Sistema de Cadastro de Clientes ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Remover cliente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "5":
            print("Saindo do sistema...")
            sys.exit()
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()