# 04. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas sucessivas, crie um programa que calcule o produto de dois números inteiros
# # lidos. Suponha que os números lidos sejam positivos e que o multiplicando seja menor do que o multiplicador.


# entrada de dados
# if n1 %2 == 0 and n2 % 2 == 0:
#     if n1 < n2:
#         r1 = n1*n2
#         print(r1)
#     else:
#         print("numero invalido")



n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo: "))

resultado = 0
contador = 0

if n1 < 0:
    print("Não pode ser número negativo")
elif n2 < 0:
    print("Não pode ser número negativo")
elif n1 > n2:
    print("Multiplicando deve ser menor que multiplicador")
else:     
        print("resultado invalido")
        while contador < n2:
            resultado = resultado + n1
            contador = contador + 1
            print("O produto é:", resultado)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
