# Q01. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do livro que será emprestado, o tipo de usuário (professor ou aluno) e possa imprimir
# um recibo conforme mostrado a seguir. Considerar que o professor tem dez dias para devolver o livro e o aluno só três dias.

# • Nome do livro:
# • Tipo de usuário:
# • Total de dias:


# entrada de dados
livro = input("digite o nome do livro: ")
print("1 - professor")
print("2 - aluno")
cargo = int(input(""))
data = int(input("digite o dia em que está pegando: "))

# processamento
if cargo == 1:
    data_entrega = (data + 10)
    # if data_entrega == data_entrega >= 1 and data_entrega <= 31:
    print(f"nome do livro : {livro}")
    print(f"data de entrega: {data_entrega}")
elif cargo == 2:
    data_entrega1 = (data + 3)
    # if data_entrega1 == data_entrega1 >= 1 and data_entrega1 <= 31:
    print(f"nome do livro : {livro}")
    print(f"data de entrega: {data_entrega1}")
else:
    print("opção invalida")