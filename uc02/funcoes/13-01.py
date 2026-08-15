# FUNÇÕES EM PHYTON
# a sintaxe para declarar uma função:
# def nome da função(var_1,var_2):
# //corpo da função
# funções podem retornar valores ou apenas realizar um procedimento para definir uma função om retorno deve-se utilizar a palavara reservada return

# declaração de uma função:
# def media():
#     return "A média é X!"


'''
    dada uma lista de dicionarios , criaremos uma função para calcular o valor
    total de um pedido.

'''


# pedido = [
#     {
#         "nome": "arroz"
#         "quantidade": 10
#         "preco_unitario": 4.99
#     },
#     {
#         "nome": "leite"
#         "quantidade": 5
#         "preco_unitario": 5.50
#     }
# ]

# def calc_pedido(pedido):


#     if len(pedido)  == 0:
#         return 0
    
#     vlr_total = 0

#     for i in pedido:
#         vlr_total += i["quantidade"] * i["preco_unit"]

#     return vlr_total

# print("valor total r$", calc_pedido(pedido))



# def seq_num(qtd):

    
#     for i in range(1, qtd +1):
#         print(str(i) * i)

# qtd = int(input("digite o valor desejado: "))
# seq_num(qtd)

'''
    revero do numero
'''



def num_inverso():

    num = (input("digite um numero: "))
    print(num[::-1])

num_inverso()