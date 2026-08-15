# Q01. Faça um algoritmo que permita entrar com o nome, a nota da prova 1 e a nota da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1, a nota
# da prova 2, a média das notas e uma das mensagens: "Aprovado", "Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para reprovação e as
# demais em prova final)


# entrada de dados
nome = input("informe seu nome:")
n1 = float(input("informe a sua primeira nota:"))
n2 = float(input("informe a sua segunda nota:"))

# processamento

media = (n1+n2)/2
# saida
print("aluno", nome)
print("nota 1", n1)
print("nota 2", n2)
print("media", media)

if media >=7:
    print("aprovado")
elif media<7 and media>=3:
    print("recuperação")
else:
    print("reprovado")
