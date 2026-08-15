# Q03. Faça um programa que calcule o imposto de renda de um grupo de contribuintes, considerando que:
# a) os dados de cada contribuinte (CPF, número de dependentes e renda bruta anual) serão fornecidos pelo usuário via teclado;
# b) para cada contribuinte será feito um abatimento de R$600 por dependente;
# c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes da renda bruta anual;
# d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela a seguir:
# Renda Líquida                                 Imposto
# até R$1000                                      Isento
# de R$1001 a R$ 5000                      15%
# acima de R$ 5000                            25%
# e) o valor de CPF igual a zero indica final de dados;
# f ) o programa deverá imprimir, para cada contribuinte, o número do CPF e o imposto a ser pago;
# g) ao final o programa deverá imprimir o total do imposto arrecadado pela Receita Federal e o número de contribuintes isentos;



cpf = 1
while cpf != 0:

    cpf = int(input("Digite seu CPF ou 0 para sair:"))
    if cpf == 0 :
        break

    dependente = int(input("informe a qtde de independentes:"))
    renda_bruta = float(input("informe a renda bruta: "))
    if dependente > 0:
    # desconto
        desconto = dependente*600
    else:
        print("nao tem desconto!")
        desconto = 0
        rendaliquida = renda_bruta - desconto
    if rendaliquida >= 1000:
        print("insento")
    elif rendaliquida >= 1001 and rendaliquida <= 5000:
        imposto = rendaliquida* 0.15
    else:
        imposto = rendaliquida * 0.25
    total = total + imposto
    print("**********recibo do IR**********")
    print(f"CPF: {cpf}")
    print(f"dependente: {dependente}")
    print(f"renda bruta: R$ {renda_bruta}")
    print(f"desconto: R$ {desconto}")
    print(f"rendaliquida: R$ {rendaliquida}")
    print(f"IR: R$ {imposto}")
    print("********************************")