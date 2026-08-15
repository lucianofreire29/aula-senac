# 01. Imprimir os pares e impares de 1 até 30;
# 02. Imprimir se o usuário é maior de idade ou não, 10 pessoas;
# 03. Faça um algoritmo que permita entrar com o nome, a idade e o sexo de 20 pessoas. O mesmo deve imprimir o nome da pessoa se ela for do sexo masculino
# e tiver mais de 21 anos.
i = 1
while i<20:
    nome = input("digite seu nome:")
    idade = int(input("digite sua idade:"))
    print("qual e o seu sexo ?")
    print ("1 - masculino")
    print ("2 - feminino")
    sexo = int(input(""))

    match sexo:
        case 1:
            if idade >21:
                print(f"{nome}, masculino, idade: {idade}")
            else:
                print ("não atende aos requisitos")    
        case _:
            print ("operção invalida")
    i = i +1