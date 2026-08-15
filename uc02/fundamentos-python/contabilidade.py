#entrada de dado
salario = float(input("informe o seu salário:"))
cargo = int(input("escolha o numero do seu cargo auxiliar de escritorio[1], secretaria[2] cozinheiro[3], entregador[4],"))

#processamento

if cargo == 1:
    print(salario*7/100+salario)
elif cargo == 2:
    print(salario*9/100+salario)
elif cargo == 3:
    print(salario*5/100+salario)
elif cargo == 4:
    print(salario*12/100+salario)
else:
    print("opção invalida")

# cargos
# auxiliar de escritorio 1 7%
# secretaria 2 9%
# cozinheiro 3 5%
# entregador 4 12%


# salario = float(input("Informe o salario: "))
# print("Escolha uma opção:")
# print("1 - Auxiliar de escritório")
# print("2 - Secretario(a)")
# print("3 - Cozinheiro(a)")
# print("4 - Entregador")
# cargo = input("")
# if cargo == 1:
#     #7%
#     reajuste = salario * 0.07
#     novoSalario = salario + reajuste
#     print(novoSalario)
# elif cargo == 2:
#     #9%
# elif cargo == 3:
#     #5%
# elif cargo== 4:
#     #12%
# else:
#     print("Opção inválida!!")