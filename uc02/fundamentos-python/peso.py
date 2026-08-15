# Q02. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
# que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
# jogadores, crie um programa que apresente as seguintes informações:
# • O peso médio e a idade média de cada um dos times;
# • O atleta mais pesado de cada time;
# • O atleta mais jovem de cada time;


# entrada de dados
i = 1
peso_total = idade_total = 0
while i <=3:
    
    print(f"competidor {i}")
    peso = int(input(f"insira o peso do competidor {i}: "))
    idade = int(input(f"insira a idade do competidor {i}: "))
    
    peso_total += peso
    idade_total += idade 
    peso_media = peso_total / i
    idade_media = idade_total / i
    
    i+= 1
    
    print(peso_media)
    print(idade_media)
# processamento



# saida