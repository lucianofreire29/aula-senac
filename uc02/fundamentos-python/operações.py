# Q02. Receber 2 números inteiros, após isso realizar as 4 operações básicas da matemática,exibindo um menu de opções ao usuário, dizer se eles são iguais,
#  quem é o maior valor e quem é o menor valor e se o primeiro valor é par ou ímpar. Observações: na subtração NÃO pode dar como resultado um número negativo e nem dividir por 0.

# entrada de dados

n1 = int(input("informe o primeiro numero : "))
n2 = int(input("informe o segundo numero: "))
print("escola a operação")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
print("5 - igualdade: ")
print("6 - quem é o maior valor: ")
print("7 - quem é o menor valor: ")
print("8 - par ou impar: ")
print("9 - media: ")
operacao = int(input(""))
# processamento

if operacao == 1:
    soma = n1+n2
    print(f"o resultado  da operação: {soma}")
elif operacao == 2:
    if n1<n2:
        diminui = n2-n1
        print(f"o resultado da operação: {diminui}")
    else:
        diminui = n1-n2
        print(f"o resultado  da operação: {diminui}")
elif operacao == 3:
    mult = n1*n2
    print(f"o resultado  da operação: {mult}")
elif operacao == 4:
    if n1 != 0 or n2 != 0:
        divisao = n1/n2
    print(f"o resultado  da operação: {divisao}")
else:
    print(f"nao e possivel dividir por 0")
if operacao == 5:
    if n1 == n2:
        print("Números iguais")
    else:
        print("Números diferentes")
elif operacao == 6:
    if n1 > n2:
        print("Primeiro valor é o maior")
    elif n2 > n1:
        print("Segundo valor é o maior")
    else:
        print("Os valores são iguais")
elif operacao == 7:
    if n1 < n2:
        print("Primeiro valor é o menor")
    elif n2 < n1:
        print("Segundo valor é o menor")
    else:
        print("Os valores são iguais")
elif operacao == 8:
    if n1 % 2 == 0:
        print("Esse número é par")
    else:
        print("Esse número é ímpar")
elif operacao == 9:
    media = (n1+n2)/2
    print(media)
else:
    print("Opção inválida")
