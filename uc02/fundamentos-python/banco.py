# entrada de dados
salario = float(input("informe o seu salario:"))
parcela = float(input("informe o valor da sua parcela:"))

#processamento
parmax = salario*0.30

if parcela <= parmax:
    print("aprovado")
else:
    print("reprovado")