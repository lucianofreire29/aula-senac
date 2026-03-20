# 0.3 residencial
# 0.5 comecial
# 0.7 industrial
# qual numero do consumidor ou do cpf.
# quantos kw foram consumido por mes.
# qual o tipo de consumidor ?

# entrada de dados 


consumidor = 1
consresidencial = conscomercial = consindustrial = somavalor = 0
while consumidor!=0:
    consumidor = int(input("digite o numero do consumidor: "))
    
    if consumidor==0:
        break
    kw = int(input("digite o consumo de kw do mes: "))
    print("escolha o tipo de consumidor")
    print("1- residencial")
    print("2- comercial")
    print("3- industrial")
    tipo = int(input(""))

# processamento de dados
    if tipo == 1:
        consresidencial+= kw
        valor = (kw)*0.3
        somavalor += valor
        print ("\n_______________________________")
        print (f"cliente: {consumidor}")
        print ("consumidor residencial")
        print(f"o valor a pagar e de R${valor}")
        print ("_______________________________")
    elif tipo == 2:
        conscomercial += kw
        valor = kw*0.5
        somavalor += valor
        print ("\n_______________________________")
        print (f"cliente: {consumidor}")
        print ("consumidor comercial")
        print(f"o valor a pagar e de R${valor}")
        print ("_______________________________")
    elif tipo == 3:
        consindustrial+= kw
        valor = kw*0.7
        somavalor += valor
        print ("\n_______________________________")
        print (f"cliente: {consumidor}")
        print ("consumidor industrial")
        print(f"o valor a pagar e de R${valor}")
        print ("_______________________________")
    else:
        print("valor invalido")
print ("______________________________________________________")
print(f"o total de consumo residencial e de:{consresidencial}")
print(f"o total de consumo comercial e de:{conscomercial}")
print(f"o total de consumo industrial e de:{consindustrial}")
print ("______________________________________________________")
