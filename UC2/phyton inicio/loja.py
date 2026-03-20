# Q01. Uma loja está implementando um sistema para calcular o valor final de uma compra com base nas seguintes regras:

# Se o cliente for VIP, ele recebe 20% de desconto.

# Se o cliente não for VIP, mas a compra for acima de R$ 500, ele recebe 10% de desconto.

# Se o cliente não for VIP e a compra for abaixo ou igual a R$ 500, não há desconto.

# Após o desconto, caso o valor final seja:

# Acima de R$ 800, aplicar um imposto adicional de 5%.

# Entre R$ 300 e R$ 800 (inclusive), aplicar 2% de imposto.

# Abaixo de R$ 300, não aplicar imposto.

# entrada de dados
produto = float(input("digite o valor da compra: "))
print("escolha uma das opções a baixo")
print("1 - VIP")
print("2 - normal")
cliente = int(input(""))

#processamento

if cliente == 1:
    desconto = produto - (produto*0.20)
    if desconto > 800:
        taxa1 = desconto - (desconto*0.5)
    print(f"o valor da sua compra e {taxa1}")
    if desconto > 300 and desconto < 800:
        taxa2 = desconto - (desconto*0.2)
        print(f"o valor da suacompra e {taxa2}")
else:
    print(f"o valor da sua compra e: {desconto}")