# holerite
# INSS
# FGTS 8%
# ADICIONAL NOTURNO 20%
# ADICIONAL DE PERICULOSIDADE 30%
# SALARIO FAMILIA R$ 65.00




# entrada de dados
nome = input("Digite o seu nome: ")
matricula = int(input("Digite sua matrícula: "))
salario = float(input("Digite o seu salario: "))
print("Escolha uma opção: ")
adcnoturno = int(input("Digite 1 se possui adicional noturno e 2 se não possui: "))
adcperic = int(input("Digite 1 se possui adicional de periculosidade e 2 se não possui: "))
safamilia = int(input("Quantos filhos até 14 anos você tem? "))

#quantidade de dependentes.
if safamilia > 0:
    safamilia = safamilia * 65
if adcnoturno == 1:
    adcnoturno = salario * 0.2
else:
    adcnoturno = 0
    
if adcperic == 1:
    adcperic = salario*0.30
else:
    adcperic = 0

bruto = (salario+adcnoturno+adcperic+safamilia)
fgts = bruto*0.08
if bruto <= 1518:
    inss = (0.075*bruto)
elif bruto >= 1518.01 and bruto <= 2793.88:
    inss = (0.09*bruto)
elif bruto >= 2793.89 and bruto <= 4190.83:
    inss = (0.12*bruto)
elif bruto >= 4190.83:
    inss = (0.14*bruto)
desconto = inss+fgts
salariototal = bruto-inss-fgts

print("\n###################################################################################")
print("\nMATRÍCULA:", matricula, "  -   NOME FUNCIONÁRIO: ",nome, "\n")

print("DESCRIÇÃO           REFERÊNCIA         VENCIMENTOS             DESCONTOS")
print("-----------------------------------------------------------------------------------")
print(f"SALÁRIOS            30 dias            {salario}") 
print("ADICIONAL NOTURNO                     ", adcnoturno)
print("PERICULOSIDADE                        ", adcperic)
print("SALÁRIO FAMÍLIA                       ", safamilia)

print ("INSS                                                          ", inss)
print("FGTS                                                          ", fgts)
print("\n                                       TOTAL DE VENCIMENTOS    TOTAL DE DESCONTOS")
print("                                      ", bruto, "                ", desconto)
print(f"\n                                         VALOR LÍQUIDO:       {salariototal}")
print("\n###################################################################################")