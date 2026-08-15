# revisão


# Declaração de uma lista

lista_vazia = [] #lista vazia
lista_vazia_1 = list() #lista vazia com construtor

# print(lista_vazia_1. __str__)

lista_num = [1, 2, 3] #lista com valores


n = [10, 30, 20, 50]

# for i in n:
#     print(i)

# for i in range(-1, -5, -1): #ordem decresente dos index
#     print(n[i])

for i in range(3, -1,-1): #ordem decresente dos index
    print(n[i])

# funções para adicionar valores

n.append()

n.insert()


# funções para remover valores

n.pop()

n.remove() #remove a primeira ocorrencia do valor.

# função para informar o tamanho da lista

len(n)

# função para ordenar.
n.sort()

# estrutura de tupla

temp_tupla = (10, 45, 30 ,25)

for i in temp_tupla:
    print(i)

# funções de tupla

temp_tupla.index() #retorna o index do valor

temp_tupla.count() #retorna a quantidade do valor na tupla

# saber os index de um determinado valor na tupla

num_sorteados = (10, 30, 10, 45, 50 , 10, 35, 35, 60, 70)

for i in range(len(num_sorteados)):
    if num_sorteados[i] == 10:
        print (f"o numero 10 está no index [{i}]")  
