# Q03 . Construa um algoritmo que leia o percurso em quilómetros, o tipo do carro e informe o consumo estimado de combustível, sabendo-se que um carro tipo C
# faz 12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C, 8 km por litro.

# entrada de dados
print("Escolha o veiculo:")
print("1 - renegade")
print("2 - corolla")
print("3 - duster")
carro = int(input("escolha uma opção: "))
km = float(input("informe quantos quilometros da viagem: "))

# processamento
tipa = 12
tipb = 9
tipc = 8

if carro == 1:
    consumo = tipa*km
    print("renegade")
    print("irá precisar de:", consumo)
elif carro == 2:
    consumo = tipb*km
    print("corolla")
    print("irá precisar de:", consumo)
elif carro == 3:
    consumo = tipc*km
    print("duster")
    print("irá precisar de:", consumo)
else:
    print("opção invalida")