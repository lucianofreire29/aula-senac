contador = 1
soma_media = 0
while contador<=15:

    nome = input("digite seu nome : ")
    n1 = float(input("digite a nota 1: "))
    n2 = float(input("digite a nota 2: "))
    if n1>0 and n1<=10:
        if n2>0 and n2<=10:   
            media = (n1+n2) / 2
            if media >=7:
                soma_media += media
                nf = "aprovado"
            else:
                nf = "reprovado"
            print(f"\n___Aluno {contador}___")
            print("\n___ Dados do aluno ___")
            print(f"Nome: {nome}")
            print(f"Nota Prova 1: {n1}")
            print(f"Nota Prova 2: {n2}")
            print(f"Média: {media}")
            print(f"você está: {nf}")
            print ("\n_______________________________")
        else:
            print("nota 2 invalida")
    else:
        print("nota 1 invalida")
    contador += 1
tmedia = soma_media/15
print ("\n_______________________________")


