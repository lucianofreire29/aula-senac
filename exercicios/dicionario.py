# coleção de dados - dicionario

# declarando um dicionario

dict_empty = {}
dict_empty_1 = dict()


# declarar dicionario com dados

aluno = {
    "matricula" : 1001,
    "nome" : "joão",
    "idade" : 18,

}


print(f"nome do aluno: {aluno["nome"]}")

aluno["nome"] = "joao paulo"

print(f"nome do aluno: {aluno["nome"]}")

aluno["dt_nasc"] = "2000-01-13"

print(f"data de nascimento: {aluno["dt_nasc"]}")



curso = {
    "nome": "tecnico em DEVs",
    "descricao" : "desenvolver profissionais na area de TI",
    "ch_horaria" : 1200
}

aluno["curso"] = curso

print(aluno["curso"]["nome"])

print(aluno.items())

# descompressao de dados com FOR

for i in aluno.items():
    print (i)


for k, v in aluno.items():
    if k == "curso":
        for key, value in v.items():
            print(f"{key}: {value}")
        continue

    print(f"chave {k} | valor: {v}")




