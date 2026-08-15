'''Relacionamentos entre Classes'''

# from curso import Curso

'''Associativo Simples - Unilateral
# Classe Curso
class Curso:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.codigo = codigo,
        self.nome = nome,
        self.preco = preco

# Classe Aluno
class Aluno:
    def __init__(self, matricula: int, nome: str, email: str, telefone: str, curso: Curso):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.curso = curso


#----------## Teste ##----------#

curso_a = Curso(1001, 'Testes de Software', 1500.50)
curso_b = Curso(1002, 'Back-End com Python', 500.50)
curso_c = Curso(1003, 'Front-End com Vue.js', 650.50)


aluno_1 = Aluno(2001, 'João Paulo', 'jp@gmail.com', '', curso_c)

print(aluno_1.curso.nome)

'''
'''Associativo Simples - Bilateral'''
# Classe Curso
class Curso:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.alunos = list()

    def relatorio_alunos(self):
        aux_str = " "

        for aluno in self.alunos:
            aux_str += f"nome:{aluno.nome} | email: {aluno.email} telefone: {aluno.telefone}\n "

            return aux_str


    def exibir_info(self):
        return f"{self.codigo} | {self.nome | {self.preco}}"


# Classe Aluno
class Aluno:
    def __init__(self, matricula: int, nome: str, email: str, telefone: str, curso: list):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.telefone = telefone
        if len(curso) == 0:
            raise Exception('Atributo vazio! - :curso')
        self.curso = curso

        for c in curso:
            c.alunos.append(self)

    def add_curso(curso: Curso):


import os


bd_cursos = []
bd_alunos = []



MENU = '''
[1] - curso
[2] - aluno
[3] - sair
'''

def validation_arg(value):
    for curso in bd_cursos:
        if curso.codigo == value or curso.nome == value:
            return True
        
    return False





while True:
    print(MENU)
    opcao = int(input("-> "))

    match opcao:
        case 1:
            os.system("cls")
            print("#-------------------------Curso-------------------------#")
            while True:
                codigo = int(input("codigo..: "))

                if not validation_arg(codigo):
                    break
                os.system("cls")
                print ("codigo já cadastrado!")

            while True:
                nome = input("nome..: ")
                if not validation_arg(nome):
                    break
                os.system("cls")
                print ("nome já cadastrado!")


            preco = float(input("preço..: "))
            bd_cursos.append(Curso(codigo, nome, preco))

            print("curso cadastrado com sucesso!")
        case 2:
            print("#-------------------------Portifólio de Cursos-------------------------#")
            for curso in bd_cursos:
                print(curso.exibir_info())


            os.system("cls")
            while True:
                matricula = input("matricula: ")
                nome = input("nome: ")
                email = input("email: ")
                telefone = input("telefone: ")
