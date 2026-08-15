# Uma startup de tecnologia está desenvolvendo um sistema interno para gerenciar
# pedidos de uma cafeteria digital. O sistema precisa organizar os pedidos dos clientes,
# calcular valores, aplicar descontos e gerar relatórios básicos para os gestores.
# Você foi contratado como programador júnior e deverá implementar partes desse
# sistema utilizando Python, aplicando os conceitos aprendidos na UC 3.
# Objetivos
#  Aplicar lógica de programação em um problema real.
#  Utilizar estruturas condicionais para tomada de decisão.
#  Implementar laços de repetição para manipulação de dados.
#  Trabalhar com diferentes estruturas de dados (listas, dicionários, tuplas e
# conjuntos).
#  Criar funções para modularizar o código e facilitar a manutenção.
# Requisitos
# 1. Cadastro de Produtos
#  Crie uma lista com os produtos disponíveis na cafeteria (ex.: café,
# cappuccino, pão de queijo, bolo).
#  Cada produto deve ser armazenado em um dicionário, contendo: nome,
# preço e categoria.
#  Organize os produtos em uma lista de dicionários.
# 2. Registro de Pedidos
#  Permita que o usuário faça pedidos digitando o nome do produto.
#  Utilize um laço de repetição (while) para continuar registrando pedidos
# até que o cliente digite “sair”.
#  Caso o produto não exista, informe ao cliente com uma mensagem
# adequada (if-elif-else).
# 3. Aplicação de Descontos
#  Crie uma função que receba o valor total do pedido e aplique descontos
# conforme a forma de pagamento:
# i. Dinheiro: 10% de desconto
# ii. Cartão de crédito: sem desconto
# iii. Pix: 5% de desconto
#  Utilize a estrutura match-case para implementar essa lógica.

# Avaliação Prática

# Técnico em Desenvolvimento de Sistemas
# Profº Davi Saldanha

# 4. Relatório de Vendas
#  Crie uma função que receba todos os pedidos realizados e:
# i. Mostre o total de vendas.
# ii. Liste os produtos mais vendidos.
# iii. Utilize um set para identificar categorias únicas de
# produtos vendidos.



for i in range(3):
    if i ==1:
        i =int(input("digite um numero: "))
        print(f"{i+1}")
# Lista de produtos (lista de dicionários)
produtos = [
    {"nome": "café", "preco": 5.00, "categoria": "bebida"},
    {"nome": "cappuccino", "preco": 7.50, "categoria": "bebida"},
    {"nome": "pão de queijo", "preco": 4.00, "categoria": "lanche"},
    {"nome": "bolo", "preco": 6.00, "categoria": "doce"}
]

# Lista de pedidos realizados
pedidos = []


# ================== CADASTRO DE PRODUTO ==================
def cadastrar_produto():
    nome = input("Digite o nome do produto: ").lower()

    # Verifica se já existe
    for p in produtos:
        if p["nome"] == nome:
            print("Produto já cadastrado!")
            return

    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ").lower()

    produtos.append({
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    })

    print("Produto cadastrado com sucesso!")


# ================== REGISTRO DE PEDIDOS ==================
def registro_pedido():
    while True:
        pedido = input("Digite o produto desejado (ou 'sair'): ").lower()

        if pedido == "sair":
            break

        encontrado = False
        for p in produtos:
            if p["nome"] == pedido:
                pedidos.append(p)
                print(f"{pedido} adicionado ao pedido.")
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado!")


# ================== DESCONTO ==================
def aplicar_desconto(valor_total, forma_pagamento):
    match forma_pagamento:
        case "dinheiro":
            return valor_total * 0.90
        case "pix":
            return valor_total * 0.95
        case "credito":
            return valor_total
        case _:
            print("Forma de pagamento inválida!")
            return valor_total


# ================== RELATÓRIO DE VENDAS ==================
def relatorio_vendas():
    if not pedidos:
        print("Nenhum pedido realizado.")
        return

    total = sum(p["preco"] for p in pedidos)
    print(f"\nTotal de vendas: R$ {total:.2f}")

    # Produtos mais vendidos
    contagem = {}
    for p in pedidos:
        nome = p["nome"]
        contagem[nome] = contagem.get(nome, 0) + 1

    print("\nProdutos mais vendidos:")
    for produto, qtd in contagem.items():
        print(f"- {produto}: {qtd}x")

    # Categorias únicas (set)
    categorias = {p["categoria"] for p in pedidos}
    print("\nCategorias vendidas:")
    for c in categorias:
        print(f"- {c}")


# ================== MENU ==================
while True:
    print("\n======= MENU =======")
    print("1 - Cadastrar produto")
    print("2 - Registrar pedido")
    print("3 - Relatório de vendas")
    print("0 - Sair")
    print("____________________")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        registro_pedido()

        forma = input("Forma de pagamento (dinheiro / pix / credito): ").lower()
        total = sum(p["preco"] for p in pedidos)
        total_com_desconto = aplicar_desconto(total, forma)
        print(f"Total com desconto: R$ {total_com_desconto:.2f}")

    elif opcao == "3":
        relatorio_vendas()
    elif opcao == "0":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida!")








