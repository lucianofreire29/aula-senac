import os

dict_setor = {}

while True:

    MENU = '''
=============== MENU CONSUMO ===============
[1] Cadastrar consumo de um setor.
[2] Exibir relatório geral.
[3] Exibir setores que ultrapassaram a meta.
[4] Calcular consumo total e média de consumo.
[5] Sair do programa.
============================================
'''
    print(MENU)
    opcao = int(input("Digite a opção desejada: "))

    match opcao:

        case 1:
            os.system("cls")
            print("============== CADASTRAR CONSUMO DE UM SETOR ==============")

            while True:
                setor = input("Digite o nome do setor: ")
                if setor not in dict_setor:
                    break
                print("Setor já cadastrado!")

            meta = float(input("Digite a meta desejada para o setor: "))
            kwh = float(input("Digite o consumo do setor: "))

            dict_setor[setor] = {
                "consumo": [],
                "meta": meta
            }

            dict_setor[setor]["consumo"].append(kwh)

            print("Setor cadastrado com sucesso!")

        case 2:
            os.system("cls")
            print("============== RELATÓRIO GERAL ==============")

            for k, v in dict_setor.items():
                total_setor = sum(v["consumo"])
                status = "DENTRO da meta!" if total_setor <= v["meta"] else "FORA da meta!"
                print(f"Setor: {k} | Consumo: {total_setor} kWh | Meta: {v['meta']} | {status}")

        case 3:
            os.system("cls")
            print("============== SETORES FORA DA META ==============")

            for k, v in dict_setor.items():
                total_setor = sum(v["consumo"])
                if total_setor > v["meta"]:
                    print(f"Setor: {k} | Consumo: {total_setor} | Meta: {v['meta']} | FORA DA META!")

        
        case 4:
            os.system("cls")
            print("============== CONSUMO TOTAL E MÉDIA ==============")

            kwh_total = 0
            qtd_consumos = 0

            for k, v in dict_setor.items():
                print(f"Setor: {k} | Consumos: {v['consumo']} | Meta: {v['meta']}")
                kwh_total += sum(v["consumo"])
                qtd_consumos += len(v["consumo"])

            if qtd_consumos > 0:
                media = kwh_total / qtd_consumos
            else:
                media = 0

            print("==============================================")
            print(f"Consumo total: {kwh_total} kWh")
            print(f"Média de consumo: {media:.2f} kWh")
            print("==============================================")
        case 5:
            print("Encerrando aplicação...")
            break

        case _:
            print("Opção inválida!")
