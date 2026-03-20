# Q02. Depois da liberação do governo para as mensalidades dos planos de saúde, as pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito
# caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Faça um algoritmo que entre com o nome e a idade de uma pessoa e imprima o nome e o
# valor que ela deverá pagar.
# Idade Valor
# Até 10 anos R$30,00
# Acima de 10 até 29 anos R$60,00
# Acima de 29 até 45 anos R$120,00
# Acima de 45 até 59 anos R$150,00
# Acima de 59 até 65 anos R$250,00
# Maior que 65 anos R$400,00

# entrada de dados
nome = input("digite seu nome:")
idade = int(input("digite sua idade:"))

# processamento
if idade <=10:
    valor1 = 30.00
    print("senhor(a)", nome)
    print("o seu valor a pagar R$",valor1)
elif idade >10 and idade <=29:
    valor2 = 60.00
    print("senhor(a)", nome)
    print("o seu valor a pagar R$",valor2)
elif idade >29 and idade <=45:
    valor3 = 120.00
    print("senhor(a)", nome)
    print("o seu valor a pagar R$",valor3)
elif idade >45 and idade <=59:
    valor4 = 150.00
    print("senhor(a)", nome)
    print("o seu valor a pagar R$",valor4)
elif idade >59 and idade <=65:
    valor4 = 250.00
    print("senhor(a)", nome)
    print("o seu valor a pagar R$",valor4)
else:
    valor5 = 400.00
    print("senhor(a)", nome)
    print("o seu valor a pagar R$",valor5)