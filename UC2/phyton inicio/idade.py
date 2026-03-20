i = 1
while i<=10:
    idade = int(input("informe a idade :"))
    match idade:
        case 1:
            idade<18
            print("menor de idade!")
        case _:
            print("maior de idade")
    i += 1