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

        if len(self.alunos) == 0:
            return "Nenhum aluno matriculado.\n"
        aux_str = f'\nCurso: {self.nome}\n'
        for aluno in self.alunos:
            aux_str += (f'Nome: {aluno.nome} | E-mail: {aluno.email} | Telefone: {aluno.telefone}\n')
        return aux_str

    def exibir_info(self):
        return f'{self.codigo} | {self.nome} |R$ {self.preco}'


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
        
    def add_curso(self, curso: Curso):
        '''Matricular o aluno no curso'''
        for c in self.curso:
            if c.nome == curso.nome:
                raise Exception('Curso já cadastrado!')
        
        self.curso.append(curso)
        curso.alunos.append(self) 
            


import os

bd_cursos = []
bd_alunos = []

MENU = '''
[1] - CURSO
[2] - ALUNO
[3] - RELATÓRIO
[4] - SAIR
'''

def valitation_args(value):
    for curso in bd_cursos:
        if curso.codigo == value or curso.nome == value:
            return True
    return False

def valitation_args_aluno(value):
    for aluno in bd_alunos:
        if aluno.matricula == value or aluno.nome == value:
            return True
    return False


while True:
    print(MENU)
    opcao = int(input('-> '))

    match opcao:
        case 1:
            os.system('cls')
            print('#---------------- CURSO ----------------#')
            while True:
                codigo = int(input('Código..: '))

                if not valitation_args(codigo):
                    break
                
                os.system('cls')
                print('Código já cadastrado!❌')
            
            while True:
                nome = input('Nome..: ')

                if not valitation_args(nome):
                    break

                os.system('cls')
                print('Nome já cadastrado!❌')

            preco = float(input('Preço..: R$'))
            bd_cursos.append(Curso(codigo, nome, preco))

            os.system('cls')
            print('Curso Cadastrado com sucesso!✅')
        case 2:
            os.system('cls')
            print('#---------------- PORTFÓLIO DE CURSO ----------------#')
            for curso in bd_cursos:
                print(curso.exibir_info())

            input("pressione ENTER para coninuar:...")

            while True:
                matricula = int(input("matricula: "))

                if not valitation_args_aluno(matricula):
                    break
                
                os.system('cls')
                print('Aluno já cadastrado!❌')

            while True:
                nome = input("Nome: ")

                if not valitation_args_aluno(nome):
                    break
                
                os.system('cls')
                print('nome já cadastrado!❌')
            email = input("email: ")
            telefone = int(input("telefone: "))
            curso = int(input("codigo do Curso: "))


            for c in bd_cursos:
                if c.codigo == curso:
                    curso = c
                    bd_alunos.append(Aluno(matricula, nome, email ,telefone, [curso]))
                    os.system("cls")
                    print("aluno cadastrado com sucesso!!✅")
        case 3:
            os.system('cls')
            print('#---------------- Relatório ----------------#')

            if len(bd_cursos) == 0:
                print("Nenhum curso cadastrado.")
            else:
                for curso in bd_cursos:
                    print(curso.relatorio_alunos())

            input("\nPressione ENTER para continuar...")

        case 4:
            print("encerrando...")
            break
        case _:
            os.system("cls")
            print("opção invalidade!❌")
