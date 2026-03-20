# ESTRUTURAS DE DADOS - SETS (CONJUNTOS)



# CARACTERISTICAS
    #- teoria dos conjuntos
    #- os elementos são únicos (á repetição não e levados em consideração)
    #- não são ordenados

# declaração

set_vazio = set()

print(type({1,3,4}))

set_notas = {4.5,4.5,6.0,3.0,6.0}

print(set_notas)


list_temp = [35, 50, 50, 50 ,35, 35, 60]

set_temp = set(list_temp)

print(set_temp)


#  formulas do conjunto
a.intersection(b)
a.union(b)
a.difference(b)

# exemplos

set_a = {10, 20, 45 , 60}
set_b = {20, 30, 40, 60}

print(set_a.union(set_b))

print(set_a.intersection(set_b))

print(set_a.difference(set_b))

import time as t

set_aleatorio = {40, 7, 22, 14, 12, 19, 25, 0}


for _ in range(len(set_aleatorio)):
    print("valor eliminado",set_aleatorio.pop())
    t.sleep(3)
    if len(set_aleatorio) == 1:
        print(f"o numero vencnedor é : {set_aleatorio}")
        break