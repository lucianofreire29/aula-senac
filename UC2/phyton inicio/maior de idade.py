idade= int(input("informe a sua idade ?"))

i = 0

while i < 10:
    if idade >=18:
        print(f"sua idade é {idade}, você e maior de idade.")
    else:
        print(f"sua idade é {idade}, você e menor de idade.")
    i += 1