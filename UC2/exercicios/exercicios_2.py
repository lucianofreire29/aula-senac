
pessoas = {}
import os

while True:

    MENU = '''
    ===== MENU =====
    [1] Adicionar uma pessoa
    [2] Visualizar uma pessoa

    '''





    print(MENU)
    opcao = int(input("digite uma opção: "))


    match opcao:
        case 1:
            os.system
            print("cadastrar uma pessoa")
            nome = input("digite um nome: ")
            idade = int(input("digite a idade: "))


            pessoas[nome]={
            "idade": idade
            }

            print("pessoa cadastrada com sucesso!!")
        
        case 2:
            os.system('cls')
            print("visualizar uma pessoa")