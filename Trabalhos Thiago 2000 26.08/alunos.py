# Lista para armazenar os alunos
alunos = []

# Função para cadastrar um aluno
def cadastrar_aluno():
    print("\n=== Cadastro de Aluno ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    endereco = input("Endereço: ")

    aluno = {
        "Nome": nome,
        "CPF": cpf,
        "Data de Nascimento": data_nascimento,
        "Endereço": endereco
    }
    alunos.append(aluno)
    print(f"\nAluno '{nome}' cadastrado com sucesso!")

# Função para listar todos os alunos
def listar_alunos():
    print("\n=== Lista de Alunos ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print(f"{'Nome':<20} {'CPF':<15} {'Data Nasc.':<15} {'Endereço'}")
    print("-"*70)
    for aluno in alunos:
        print(f"{aluno['Nome']:<20} {aluno['CPF']:<15} {aluno['Data de Nascimento']:<15} {aluno['Endereço']}")

# Programa principal
def main():
    while True:
        print("\n1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
