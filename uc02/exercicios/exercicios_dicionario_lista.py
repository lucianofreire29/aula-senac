# 1. Crie uma lista de dicionários representando pessoas, contendo nome e idade. Cadastre três
# pessoas e exiba os dados.


pessoas = {}


for i in range(3):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))

    pessoas[i] = {
        "nome": nome,
        "idade": idade
    }


print("\nPessoas cadastradas:")
for i in pessoas.values():
    print(f"Nome: {i["nome"]} | Idade: {i["idade"]}")


    # 2. Crie uma lista de dicionários representando alunos com nome e nota. Exiba o nome e a nota de
# cada aluno.

alunos = []

def adicionar_aluno():

    qtd = int(input("Quantos alunos você quer cadastrar? "))
    for i in range(qtd):
        nome = input("digite o nome do aluno: ")


        nota = float(input("digite a nota do aluno: "))

        aluno = {
            "nome": nome,
            "nota": nota
        }

        alunos.append(aluno)
        print(" Aluno cadastrado com sucesso!")


def visualizar_aluno():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in alunos:
        print("\n-----------------------")
        print(f"Nome: {aluno['nome']}")
        print(f"Nota: {aluno['nota']}")






while True:
    print("1 - cadastrar aluno")
    print("2 - visualizar  aluno")
    print("3 - encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_aluno()
    if opcao == 2:
        visualizar_aluno()
    if opcao == 3:
        break


# 3. A partir da lista de alunos, exiba apenas os alunos com nota maior ou igual a 7.


alunos = []

def adicionar_aluno():

    qtd = int(input("Quantos alunos você quer cadastrar? "))
    for i in range(qtd):
        nome = input("digite o nome do aluno: ")


        nota = float(input("digite a nota do aluno: "))

        aluno = {
            "nome": nome,
            "nota": nota
        }

        alunos.append(aluno)
        print(" Aluno cadastrado com sucesso!")


def visualizar_aluno():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in alunos:
        print("\n-----------------------")
        print(f"Nome: {aluno['nome']}")
        print(f"Nota: {aluno['nota']}")






while True:
    print("1 - cadastrar aluno")
    print("2 - visualizar  aluno")
    print("3 - encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_aluno()
    if opcao == 2:
        visualizar_aluno()
    if opcao == 3:
        break

# 4. Crie uma lista de dicionários representando produtos com nome e preço. Calcule o valor total
# dos produtos.

list_produtos = list()

total = 0
print("***produtos***")

while True:
    nome = input("nome do produto: ")
    preco = float(input("digite o valor do produto: "))

    list_produtos.append({"nome": nome, "preço": preco})

    flag = input("deseja cadastrar mais produtos ? [S] sim ou [N] não.")

    if flag.upper() == "N":
        break


    for i in list_produtos:
        total += i["preço"]

    print (f"valor total ..: R${total}")
