time = 1
somaSalarios = qtdeOutrosFortaleza = qtdeCeara = qtdeFortaleza = qtdeMaracanau = qtdeFerroviario = qtdeOutros = 0
while time!=0:
    print("1-Ceará;\n2-Fortaleza;\n3-Maracanaú;\n4-Ferroviário;\n5-Outros\n0-Sair")
    time = int(input("Qual seu time de coração?"))
    if time==0:
        break
    print("1- Fortaleza\n2-Caucaia\n3-Outros")
    local = int(input("Onde você mora?"))
    salario = float(input("Qual o seu salário?"))
        #numero de pessoas moradoras de fortaleza, outros clubes;
    if time==5 and local==1:
        qtdeOutrosFortaleza=qtdeOutrosFortaleza+1
    if time==1:
        qtdeCeara=qtdeCeara+1
        somaSalarios=somaSalarios+salario
    elif time==2:
        qtdeFortaleza=qtdeFortaleza+1
    elif time==3:
        qtdeMaracanau=qtdeMaracanau+1
    elif time==4:
        qtdeFerroviario=qtdeFerroviario+1
    elif time==5:
        qtdeOutros=qtdeOutros+1
    else:
        print("Opção inválida!")

print("Qtde de torcedores do Ceará: ", qtdeCeara)
print("Qtde de torcedores do Fortaleza: ", qtdeFortaleza)
if qtdeCeara!=0:
    media = somaSalarios/qtdeCeara
    print("Média salarial do torcedor do Ceará: ", media)
