# Q02. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
# mesmo número de pontos, criar um algoritmo que informe se uma equipe foi classificada, de acordo com a seguinte especificação:

# • Ler os pontos obtidos por cada jogador da equipe;
# • Mostrar esses valores em ordem decrescente;
# • Se a soma dos pontos for maior do que 100, imprimir a média aritmética
# entre eles, caso contrário, imprimir a mensagem "Equipe desclassificada".



# entrada de dados

p1 = int(input("digite a sua pontuação:"))
p2 = int(input("digite a sua pontuação:"))
p3 = int(input("digite a sua pontuação:"))

# processamento

if p1>p2 and p1>p3:
    if p2>p3:
        print(p3)
        print(p2)
        print(p1)
    else:
        print(p2)
        print(p3)
        print(p1)
elif p2>p1 and p2>p3:
    if p1>p3:
        print(p3)
        print(p1)
        print(p2)
    else:
        print(p1)
        print(p3)
        print(p2)
elif p3>p1 and p3>p2:
    if p1>p2:
        print(p3)
        print(p1)
        print(p3)
    else:
        print(p1)
        print(p2)
        print(p3)
# processamento
media = (p1+p2+p3)/3
if media > 100:
    print (media,"classificado")
else:
    print("desclassificado")