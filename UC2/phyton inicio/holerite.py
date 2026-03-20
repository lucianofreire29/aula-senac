# holerite
# INSS
# FGTS 8%
# ADICIONAL NOTURNO 20%
# ADICIONAL DE PERICULOSIDADE 30%
# SALARIO FAMILIA R$ 65.00




# entrada de dados
nome = input("Digite seu nome")
matricula = int(input("Digite matricula"))
salario = float(input("digite o seu salario: "))
print("escolha uma opção")
adcnoturno = int(input("Digite 1 se possui adcional noturno e 2 se não possui"))
adcperic = int(input("Digite 1 se possui adcional periculosidade e 2 se não possui"))
safamilia = int(input("Possui quantos filhos até 14 anos vc tem?"))
# familia = int(input("quantos dependes você tem ?: "))

if safamilia > 0:
    safamilia = safamilia * 65
if adcnoturno == 1:
    adcnoturno = salario * 0.20
else:
    adcnoturno == 0
if adcperic == 1:
    adcperic = salario*0.30
else:
    adcperic == 0

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

print("MATRICULA        NOME FUNCIONARIO       ")
print(matricula, "      ", nome)
print("DESCRICAO           REFERENCIA         VENCIMENTOS      DESCONTOS")
print(f"SALARIOS           30 dias            {salario}") 
print("ADICIONAL NOTURNO                    ", adcnoturno)
print("PERICULOSIDADE                       ", adcperic)
print("SALARIO FAMILIA                      ", safamilia)

print ("INSS                                                  ", inss)
print("FGTS                                                   ", fgts)
print("                                TOTAL DE VENCIMENTOS  TOTAL DE DESCONTOS")
print("                                   ", bruto, "        ", desconto)
print(f"                                     VALOR LIQUIDO     {salariototal}")