# Você foi contratado para desenvolver um sistema simples de controle financeiro pessoal. O usuário deseja registrar suas despesas mensais, 
# classificá-las por categoria e verificar se está dentro ou fora do orçamento.

# Implemente em Python um programa que:
# 1. Solicite ao usuário o orçamento mensal disponível

# 2. Utilize um laço de repetição (while) para registrar despesas.
# - Para cada despesa, o usuário deve informar:
#   - Valor da despesa
#   - Categoria da despesa (ex. alimentação, transporte, lazer, contas fixas)
# - O programa deve somar os valores e comparar com o orçamento.

# 3. Após cada despesa registrada:
# - Se o total for menor ou igual ao orçamento, exiba:
#   - "Você ainda está dentro do orçamento. Total gasto: X"
# - Se o total ultrapassar o orçamento, exiba:
#   - "Atenção! Você ultrapassou seu orçamento. Total gasto: X"

# 4. O programa deve parar quando o usuário digitar 0 como valor da despesa.

# 5. Ao final, o programa deve mostrar um relatório resumido:
# - Total gasto.
# - Quanto sobrou ou quanto ultrapassou do orçamento.
# - Quantidade de despesas registradas em cada categoria.



# despesas = []



# orcamento = float(input("digite o orçamento mensal disponível: "))



# while True:


#     despesa = input("digite o nome da despesa ou [0] para finalizar: ")
#     if despesa != "0":
    
#         valor_despesa = float(input("digite o valor da despesa: "))
#         categoria_despesa = input("digite a categoria da despesa: ")

#         despesas.append({

#             "despesa": despesa,
#             "valor despesa": valor_despesa,
#             "categoria": categoria_despesa
#         })

#         total_despesa = sum(d["valor despesa"] for d in despesas)

#     else:
#         print("finalizado!")
#     break

# print(f"seu orçamento é de:R$ {orcamento}, e sua despesa total é de:R$ {total_despesa}")







orcamento = float(input("Digite o orçamento mensal disponível: "))

total_gasto = 0
despesas_por_categoria = {}

while True:
    valor = float(input("Digite o valor da despesa (0 para finalizar): "))

    
    if valor == 0:
        break

    categoria = input("Digite a categoria da despesa: ")

    
    total_gasto += valor

    
    if categoria in despesas_por_categoria:
        despesas_por_categoria[categoria] += 1
    else:
        despesas_por_categoria[categoria] = 1

    
    if total_gasto <= orcamento:
        print(f"Você ainda está dentro do orçamento. Total gasto: R$ {total_gasto:.2f}")
    else:
        print(f"Atenção! Você ultrapassou seu orçamento. Total gasto: R$ {total_gasto:.2f}")


print("\n--- RELATÓRIO FINAL ---")
print(f"Total gasto: R$ {total_gasto:.2f}")

diferenca = orcamento - total_gasto

if diferenca >= 0:
    print(f"Você ainda tem R$ {diferenca:.2f} disponíveis.")
else:
    print(f"Você ultrapassou o orçamento em R$ {abs(diferenca):.2f}")

print("\nDespesas por categoria:")
for categoria, quantidade in despesas_por_categoria.items():
    print(f"- {categoria}: {quantidade} despesa(s)")
