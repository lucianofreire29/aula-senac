# 05. Crie um algoritmo que permita entrar com o nome, a nota da prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, 
# contendo: nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final, imprimir a média geral da turma.


# entrada de dados
contador = 1
soma_media = 0
while contador<=15:

   
    nome = input("digite seu nome : ")
    n1 = float(input("digite a nota 1: "))
    n2 = float(input("digite a nota 2: "))
    if n1>0 and n1<=10:
        if n2>0 and n2<=10:   
            media = (n1+n2) / 2
            soma_media += media
            print(f"\n___Aluno {contador}___")
            print("\n___ Dados do aluno ___")
            print(f"Nome: {nome}")
            print(f"Nota Prova 1: {n1}")
            print(f"Nota Prova 2: {n2}")
            print(f"Média: {media}")
            print(f"{aprovado}")
            print ("\n_______________________________")
        else:
            print("nota 2 invalida")
    else:
        print("nota 1 invalida")
        contador += 1
tmedia = soma_media/15
print ("\n_______________________________")
print(f"media da turma {tmedia}")
print ("\n_______________________________")