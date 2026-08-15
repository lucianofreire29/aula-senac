# Faça um algoritmo que leia o destino do passageiro, se a viagem inclui retorno (ida e volta) e informe o preço da passagem conforme a tabela a seguir:

# CÓD.                              DESTINO                           DESTINO IDA                                   IDA E VOLTA
# 1                               Região Norte                         500,00                                         900,00
# 2                               Região Nordeste                      350,00                                         650,00
# 3                               Região Centro-oeste                  350,00                                         600,00
# 4                               Região Sul                           300,00                                         550,00


# entrada de dados
print("Escolha uma opção:")
print("1 - região norte")
print("2 - nordeste")
print("3 - centro-oeste")
print("4 - sul")
destino = int(input("escolha uma opção: "))
print("Escolha uma opção:")
print("1 - ida")
print("2 - ida e volta")
passagem = int(input("escolha uma opção: "))


if destino == 1 and passagem == 1:
    print("região norte")
    print("R$500.0")
elif destino == 1 and passagem == 2:
    print("região norte")
    print ("R$900.0")
if destino == 2 and passagem == 1:
    print("região nordeste")
    print("R$350.0")
elif destino == 2 and passagem == 2:
    print("região nordeste")
    print ("R$650.0")
if destino == 3 and passagem == 1:
    print("região centro-oeste")
    print("R$350.0")
elif destino == 3 and passagem == 2:
    print("região centro-oeste")
    print ("R$600.0")
if destino == 4 and passagem == 1:
    print("região sul")
    print("R$300.0")
elif destino == 4 and passagem == 2:
    print("região sul")
    print ("R$550.0")
else:
    print("opção invalida")
