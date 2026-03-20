# classe produto

class Produto:
    def __init__(self, nome, descricao, valor, dt_validade):
        self.nome = nome
        self.descricao = descricao
        self.dt_validade = dt_validade

        if valor > 0:
            self.valor = valor
        else:
            raise Exception("valor invalido")




# ___________________________________________________________________________________________________________________________________________________________________________________________________
"""TESTES"""


var_prod1 = Produto("Leite integral", "Leite Integral", 5.89, "2026-01-31")
var_prod2 = Produto("Pao Integral", "Pão Saudável na sua mesa", 9.89, "2026-01-31")

nome = input("Nome: ")
descricao = input("Descrição: ")
valor = float(input("Valor..: "))
dt_validade = input("Data Validade..: ")

var_prod3 = Produto(nome, descricao, valor, dt_validade)

# ___________________________________________________________________________________________________________________________________________________________________________________________________


lista_produtos = []

while True:

    nome = input("Nome: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor..: "))
    dt_validade = input("Data Validade..: ")


    lista_produtos.append(Produto(nome, descricao, valor, dt_validade))

    flag = input("deseja continuar ? SIM ou NÃO.")

    if flag.lower() == "não":
        break



    # lista_produtos[1].nome   (achar produto dentro da lista)


# listar o nome dos produtos cadastrados.

for i in range(len(lista_produtos)):
    print(lista_produtos[i].nome)

for i in lista_produtos: 
    print(i.nome)



    