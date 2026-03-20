# Desafio: Sistema de Cadastro de Alunos

# Você deve criar um programa que gerencie um cadastro de alunos usando dicionários.

# Regras do programa
# Cada aluno terá:
# Matrícula (chave única, tipo int)
# Nome (string)
# Idade (int)
# Notas (lista de floats)
# O programa deve permitir:
# Adicionar um novo aluno.
# Atualizar dados de um aluno existente.
# Remover um aluno pelo número de matrícula.
# Buscar um aluno pelo número de matrícula.
# Listar todos os alunos cadastrados.
# Calcular a média das notas de um aluno.
# Exemplo de Estrutura do Dicionário
# alunos = { 
# 101: {"nome": "Ana", "idade": 20, "notas": [8.5, 7.0, 9.0]},
# 102: {"nome": "Bruno", "idade": 22, "notas": [6.0, 5.5, 7.5]}
#  }




alunos = {}



def adicionar_aluno():
    matricula = int(input("Digite a matrícula: "))
    
    if matricula in alunos:
        print("Matrícula já cadastrada!")
        return
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    notas = []
    qtd = int(input("Quantas notas deseja cadastrar? "))
    for i in range(qtd):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    alunos[matricula] = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }
    
    print(" Aluno cadastrado com sucesso!")


def atualizar_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
    
    print("1 - Atualizar nome")
    print("2 - Atualizar idade")
    print("3 - Atualizar notas")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        alunos[matricula]["nome"] = input("Novo nome: ")
    elif opcao == 2:
        alunos[matricula]["idade"] = int(input("Nova idade: "))
    elif opcao == 3:
        notas = []
        qtd = int(input("Quantas notas deseja cadastrar? "))
        for i in range(qtd):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)
        alunos[matricula]["notas"] = notas
    else:
        print(" Opção inválida!")
        return
    
    print("Dados atualizados com sucesso!")


def remover_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    
    if matricula in alunos:
        del alunos[matricula]
        print(" Aluno removido com sucesso!")
    else:
        print(" Aluno não encontrado!")


def buscar_aluno():
    matricula = int(input("Digite a matrícula do aluno: "))
    
    if matricula in alunos:
        aluno = alunos[matricula]
        print(f"\nMatrícula: {matricula}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: {aluno['notas']}")
    else:
        print(" Aluno não encontrado!")


def listar_alunos():
    if not alunos:
        print(" Nenhum aluno cadastrado!")
        return
    
    for matricula, dados in alunos.items():
        print("\n-----------------------")
        print(f"Matrícula: {matricula}")
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
        print(f"Notas: {dados['notas']}")


def calcular_media():
    matricula = int(input("Digite a matrícula do aluno: "))
    
    if matricula not in alunos:
        print(" Aluno não encontrado!")
        return
    
    notas = alunos[matricula]["notas"]
    
    if len(notas) == 0:
        print(" Aluno não possui notas!")
        return
    media = sum(notas) / len(notas)
    print(f" Média do aluno: {media:.2f}")


while True:
    print("\n======= MENU =======")
    print("1 - Adicionar aluno")
    print("2 - Atualizar aluno")
    print("3 - Remover aluno")
    print("4 - Buscar aluno")
    print("5 - Listar alunos")
    print("6 - Calcular média")
    print("0 - Sair")
    print("____________________")

    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        adicionar_aluno()
    elif opcao == 2:
        atualizar_aluno()
    elif opcao == 3:
        remover_aluno()
    elif opcao == 4:
        buscar_aluno()
    elif opcao == 5:
        listar_alunos()
    elif opcao == 6:
        calcular_media()
    elif opcao == 0:
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")

