# 1. Uma loja armazena os nomes dos produtos em uma lista e os preços em outra lista
# correspondente. Crie um programa que permita buscar o preço de um produto pelo nome
# e exibir o valor médio dos preços.


produto = ["arroz", "feijao", "macarrao", "cafe", "ovo", "leite"]
preço = [5, 8, 7, 12, 10, 4]

busca = input("digite o nome do produto: ")

if busca in produto:
    indice = produto.index(busca)
    print (f"o preço do {busca}: R${preço[indice]}")
else:
    print("produto não encontrado. ")

media = sum(preço) / len(preço)
print(f"media dos preços: R${media:.2f}")

# 2. Dada uma tupla com temperaturas de uma semana, exiba a maior, a menor e a
# # quantidade de dias acima de 32°C.
temp = 0
temperatura = (28, 29, 32, 33, 35, 34, 29)

maior = max(temperatura)
menor = min(temperatura)

for i in range(len(temperatura)):
    if temperatura[i] > 32:
        temp += 1
print (f"quantidades de dias a cima de 32°C: {temp} dias")

print(f"maior temperatura {maior}\nmenor temperatura: {menor}")


# 3. Crie listas com nomes de vendedores e quantidades de vendas. Exiba o vendedor com
# mais e menos vendas e o total de vendas.

vendedores = ["carlos", "perdo", "francisco", "fernando"]
vendas = [300, 150, 800, 200]

maior = vendas.index(max(vendas))
menor = vendas.index(min(vendas))
total = sum(vendas)

print(f"vendedor com mais venda {vendedores[maior]} ({max(vendas)} vendas)")
print (f"vendedor com a menor venda {vendedores[menor]} ({min(vendas)} vendas)")
print (f"numero total de vendas {total}")


# 4. Cadastre alunos em uma lista de tuplas (nome, idade, média). Exiba os alunos com
# média acima de 7 e a média geral da turma.



aluno_lista = []
idade_lista = []
media_lista = []


aluno = input("digite o nome do aluno: ")
idade = int(input("digite a idade do aluno: "))
media = float(input("digite a media do aluno: "))

aluno_lista.append(aluno)
idade_lista.append(idade)
media_lista.append(media)

media_total = sum(media_lista)


for i in range(len(media_lista)):
    if media_lista[i] >=7:
        print(f"o aluno {aluno_lista} está aprovado com media de {media_lista}")


# 5. Usando uma lista com valores gastos em semanas de um mês, exiba o total e a
# semana com maior gasto.

gastos_semana =[400, 300, 200, 500]
semana =[1, 2, 3, 4 ]


maior = gastos_semana.index(max(gastos_semana))
total = sum(gastos_semana)


print (f"semana com maior gasto {semana[maior]}")
print (f"valor total gasto no mes:R$ {total}")

# 6. Converta uma tupla de notas em lista, substitua a menor nota pela média das notas e
# exiba o resultado.

notas = (10, 7, 8, 6, 9)

media = sum(notas) / len(notas)
menor = notas.index(min(notas))

notas_lista = list(notas)

notas_lista.insert(menor,media)

print(notas_lista)

# 7. Dada uma playlist representada por uma lista de tuplas (música, duração), exiba a
# música mais longa e o tempo total da playlist.

playlist = ("longa vida", "highway to hell", "in the end", "papercut")
duraçao = (2.20, 1.20, 2.00 , 1.40)


musica_longa = duraçao.index(max(duraçao))
tempo_total = sum(duraçao)

print(f"musica mais longa é : {playlist[musica_longa]}\ne o tempo total da playlisy e de:{tempo_total}")


# 8. Receba uma lista de notas (1 a 5) e mostre a frequência de cada nota e a média geral.


nota_lista = []
i = 0

for i in range(5):
    notas = float(input(f"digite a nota numero {i}: "))

    



# 9. Dada uma tupla com 10 times, exiba os 3 primeiros, os 3 últimos e a posição de um
# time digitado.

times = ("fortaleza", "ceara","flamengo", "palmeiras", "sao paulo", "corinthias", "botafogo" , "vasco" ,"ferroviario", "cruzeiro")
posiçao = (1, 10, 3, 4, 5 ,8 ,9 ,7 , 2)


x={}













# 20. Receba uma lista de números, remova valores duplicados e exiba o resultado em
# ordem crescente.


list_nums = []


quant_num = int(input("quantidade de números: "))

for _ in range(quant_num):
    list_nums.append(int(input("->")))

nums_unique = []

for i in list_nums:
    if i not in nums_unique:
        nums_unique.append(i)

nums_unique.sort()

print(f"lista sem duplicatas: {nums_unique} ")