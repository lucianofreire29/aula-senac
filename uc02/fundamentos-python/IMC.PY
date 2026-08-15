# Q03. Faça um algoritmo que calcule o IMC do usuario e mostre o resultado. 
# Observação: para calcular o IMC vc deve multiplicar o peso pelo o peso e dividir pela altura.

# IMC (kg/m²) 	                                Resultado
# Abaixo de 18,5	                        Abaixo do peso
# 18,5 a 24,9	                                Peso normal
# 25,0 a 29,9	                                Sobrepeso
# 30,0 a 34,9	                                Obesidade Grau I
# 35,0 a 39,9	                                Obesidade Grau II
# Acima de 40	                                Obesidade Grau III


# entrada de dados
altura = float(input("digite sua altura: "))
peso = float(input("digita seu peso: "))

# processamento

imc = (altura*altura) / peso

if imc< 18.5:
    print("abaixo do peso")
elif imc >= 18.5:
    if imc <= 24.9:
        print("peso normal")
elif imc >= 25:
    if imc <= 29.9:
        print("sobrepeso")
elif imc >= 30:
    if imc <= 34.9:
        print("obesidade grau I")
elif imc >= 35:
    if imc <= 39.9:
        print("obesidade grau II")
elif imc > 40:
        print("obesidade grau III")
else:
    print("operação invalida")

