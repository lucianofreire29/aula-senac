lista = []
# valor zero das variaveis
aluno = aluno_idoso = vtotal = soma = 0

# entrada de dados
for i in range(2):
    nome = input("Informe o seu nome: ")

    idade = int(input("Informe a sua idade: "))
    while idade <= 0:
        print("Erro: Idade não pode ser inferior ou igual a 0.")
        idade = int(input("Informe a sua idade: "))

    valor = float(input("Informe o valor da sua mensalidade: "))
    while valor < 100:
        print("Erro: Mensalidade inválida.")
        valor = float(input("Informe o valor da sua mensalidade: "))

    # processamento
    if idade >= 60:
        desconto = valor * 0.20
        mensalidade_des = valor - desconto
        aluno_idoso += 1
    else:
        desconto = 0
        mensalidade_des = valor - desconto
        aluno += 1

    
    vtotal += mensalidade_des

    lista.append({
        "nome": nome,
        "idade": idade,
        "mensalidade": valor,
        "desconto":desconto,
        "valorPagar":mensalidade_des
    })
    print(lista)
    
    for item in lista:
        soma = soma + item["valorPagar"]

print("Total das mensalidades:", soma)

