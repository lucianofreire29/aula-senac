# entrada de dados

comp1 = input("informe o nome do competidor")
pont1 = int(input("informe a pontuação"))
comp2 = input("informe o nome do competidor")
pont2 = int(input("informe a pontuação"))
comp3 = input("informe o nome do competidor")
pont3 = int(input("informe a pontuação"))

# processamento

if pont1 > pont2 and pont1 > pont3 and pont2 > pont3:
    print(comp1 , pont1)
    print(comp2 , pont2)
    print(comp3 , pont3)
elif pont2 > pont1 and pont2 > pont3 and pont1 > pont3:
    print (comp2, pont2)
    print (comp1, pont1)
    print (comp3, pont3)
elif pont2 > pont1 and pont2 > pont3 and pont3 > pont1:
    print (comp2, pont2)
    print (comp3, pont3)
    print (comp1, pont1)
elif pont3 > pont1 and pont3 > pont2 and pont1 > pont2:
    print (comp3, pont3)
    print (comp1, pont1)
    print (comp2, pont2)
elif pont3 > pont1 and pont3 > pont2 and pont2 > pont1:
    print (comp3, pont3)
    print (comp2, pont2)
    print (comp1, pont1)
else:
    print (comp1, pont1)
    print (comp3, pont3)
    print (comp2, pont2)

#     Q03. Arco e flexa
# j1 = int(input("Informe a pontuação: "))
# j2 = int(input("Informe a pontuação: "))
# j3 = int(input("Informe a pontuação: "))

# if j1>j2 and j1>j3:
#     if j2>j3:
#         print(j1,j2,j3)
#     else:
#         print(j1,j3,j2)
# elif j2>j1 and j2>j3:
#     if j1>j3:
#         print(j2,j1,j3)
#     else:
#         print(j2,j3,j1)
# elif j3>j1 and j3>j2:
#     if j1>j2:
#         print(j3,j1,j2)
#     else:
#         print(j3,j2,j1)