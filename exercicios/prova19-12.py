lista = []

i = 1

valor_total = produto_desconto = produto = total_dia = 0

for i in range(2):

    nome_produto = input("digite o nome do produto: ")
    quantidade_vendida = int(input("digite a quantidade vendida: "))

    while quantidade_vendida < 0:
        quantidade_vendida = int(input("digite a quantidade vendida: "))


    preco_unitario = float(input("digite o valor do preço unitário: "))
    while preco_unitario < 0:
        preco_unitario = float(input("digite o valor do preço unitário: "))

    if quantidade_vendida >= 10:
        desconto = preco_unitario *0.1* quantidade_vendida
        valor_total = (preco_unitario*quantidade_vendida)-desconto
        produto_desconto += 1
        i += 1

    else:
        desconto = preco_unitario *0* quantidade_vendida
        valor_total = (preco_unitario*quantidade_vendida)-desconto
        produto += 1
        i += 1

    lista.append({
        "nome do produto": nome_produto,
        "quantidade vendida": quantidade_vendida,
        "preço unitário": preco_unitario,
        "valor total": valor_total,
        "desconto": desconto
    })


for item in lista:
    total_dia = total_dia + item["valor total"]
    media = valor_total/ item["quantidade vendida"]

    lista.append({"media": media
    })


    print(f"Quantidade total de produtos cadastrados:{i}")
    print ("valor total arrecadado do dia", total_dia)
    print("media de faturamento por produto", media)
    print("Quantidade de produtos que receberam desconto:", produto_desconto)

if total_dia >= 1000:
    print("Dia com boas vendas!")
else:
    print("Vendas abaixo do esperado.")

# luciano
# lucas
# david
# beatiz