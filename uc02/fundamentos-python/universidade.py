# Q02. Em uma Universidade, os alunos das turmas de informática fizeram uma prova de algoritmos. Cada turma possui um número de alunos. Criar um programa que
# imprima:
# • quantidade de alunos aprovados;
# • média de cada turma;
# • percentual de reprovados.

# Obs.: Considere aprovado com nota >= 7.0 

qtdeAprovadosGeral = somaNotasGeral = qtdeAlunosGeral = 0
qtdeTurmas = int(input("Informe a qtde de turmas: "))
for i in range(qtdeTurmas):
    print("Turma ", i+1)
    print("******************")
    qtdeAlunos = int(input("Informe a qtde de alunos: "))
    qtdeAprovado = somaNotas = 0
    for i in range(qtdeAlunos):        
        print("Aluno(a) ", i+1)
        print("******************")
        nota = float(input("Informe a nota: "))
        somaNotas = somaNotas + nota
        somaNotasGeral=somaNotasGeral+nota
        qtdeAlunosGeral=qtdeAlunosGeral+1
        if nota>=7:
            print("Aprovado")
            qtdeAprovado = qtdeAprovado + 1
            qtdeAprovadosGeral=qtdeAprovadosGeral+1
        else: 
            print("Reprovado")
        print("******************")
    print("Qtde de aprovados: ", qtdeAprovado)
    mediaTurma = somaNotas/qtdeAlunos
    print("Média da turma: ", mediaTurma)
print("Qtde geral de alunos aprovados: ", qtdeAprovadosGeral)
print("Média geral de alunos: ", somaNotasGeral/qtdeAlunosGeral)