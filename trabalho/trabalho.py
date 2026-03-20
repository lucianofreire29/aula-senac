
# importar data e hora, e tipar as listas que eu usei.

from datetime import date, time
from typing import List, Optional

# classe aluno

class Aluno:
    def __init__(self, id_aluno: int, nome: str, matricula: str,data_nascimento: date, email: str):
        self._id_aluno = id_aluno
        self._nome = nome
        self._matricula = matricula
        self._data_nascimento = data_nascimento
        self._email = email
        self._turma: Optional[Turma] = None
        self._notas: List[Nota] = []
        self._frequencias: List[Frequencia] = []

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        if nome:
            self._nome = nome

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        if "@" in email:
            self._email = email

    def get_turma(self) -> Optional["turma"]:
        return self._turma

    def set_turma(self, turma: "turma"):
        self._turma = turma

    # Métodos
    def adicionar_nota(self, nota: "nota"):
        self._notas.append(nota)

    def registrar_frequencia(self, frequencia: "frequencia"):
        self._frequencias.append(frequencia)

    def calcular_media(self) -> float:
        if not self._notas:
            return 0.0
        return sum(n.valor for n in self._notas) / len(self._notas)


# classe professor

class Professor:
    def __init__(self, id_professor: int, nome: str, email: str):
        self._id_professor = id_professor
        self._nome = nome
        self._email = email
        self._disciplinas: List[disciplina] = []
        self._aulas: List[aula] = []

    def get_nome(self) -> str:
        return self._nome

    def adicionar_disciplina(self, disciplina: "disciplina"):
        self._disciplinas.append(disciplina)

    def ministrar_aula(self, aula: "aula"):
        self._aulas.append(aula)




class Turma:
    def __init__(self, id_turma: int, nome: str, ano_letivo: int, turno: str):
        self._id_turma = id_turma
        self._nome = nome
        self._ano_letivo = ano_letivo
        self._turno = turno
        self._alunos: List[Aluno] = []
        self._aulas: List[aula] = []

    def adicionar_aluno(self, aluno: Aluno):
        self._alunos.append(aluno)
        aluno.set_turma(self)

    def adicionar_aula(self, aula: "aula"):
        self._aulas.append(aula)


class Disciplina:
    def __init__(self, id_disciplina: int, nome: str, carga_horaria: int):
        self._id_disciplina = id_disciplina
        self._nome = nome
        self._carga_horaria = carga_horaria
        self._aulas: List[Aula] = []
        self._notas: List[Nota] = []

    def adicionar_aula(self, aula: "Aula"):
        self._aulas.append(aula)

    def adicionar_nota(self, nota: "Nota"):
        self._notas.append(nota)


class Aula:
    def __init__(self, id_aula: int, data: date,horario_inicio: time, horario_fim: time,conteudo: str, professor: Professor,disciplina: Disciplina, turma: Turma):
        self._id_aula = id_aula
        self._data = data
        self._horario_inicio = horario_inicio
        self._horario_fim = horario_fim
        self._conteudo = conteudo
        self._professor = professor
        self._disciplina = disciplina
        self._turma = turma
        self._frequencias: List[Frequencia] = []

        professor.ministrar_aula(self)
        disciplina.adicionar_aula(self)
        turma.adicionar_aula(self)

    def registrar_frequencia(self, frequencia: "Frequencia"):
        self._frequencias.append(frequencia)


class Nota:
    def __init__(self, id_nota: int, valor: float,tipo_avaliacao: str, data: date,aluno: Aluno, disciplina: Disciplina):
        self._id_nota = id_nota
        self.valor = valor
        self._tipo_avaliacao = tipo_avaliacao
        self._data = data
        self._aluno = aluno
        self._disciplina = disciplina

        aluno.adicionar_nota(self)
        disciplina.adicionar_nota(self)

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if 0 <= valor <= 10:
            self._valor = valor



class Frequencia:
    def __init__(self, id_frequencia: int, data: date,status: str, aluno: Aluno, aula: Aula):
        self._id_frequencia = id_frequencia
        self._data = data
        self._status = status
        self._aluno = aluno
        self._aula = aula

        aluno.registrar_frequencia(self)
        aula.registrar_frequencia(self)



class Evento:
    def __init__(self, id_evento: int, titulo: str,descricao: str, data_inicio: date,data_fim: date, tipo: str):
        self._id_evento = id_evento
        self._titulo = titulo
        self._descricao = descricao
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._tipo = tipo
        self._turmas: List[Turma] = []

    def associar_turma(self, turma: Turma):
        self._turmas.append(turma)



class Calendario:
    def __init__(self, id_calendario: int, data: date,descricao: str, tipo: str):
        self._id_calendario = id_calendario
        self._data = data
        self._descricao = descricao
        self._tipo = tipo
        self._eventos: List[Evento] = []

    def adicionar_evento(self, evento: Evento):
        self._eventos.append(evento)




class UsuarioAdministrativo:
    def __init__(self, id_usuario: int, nome: str, cargo: str, email: str):
        self._id_usuario = id_usuario
        self._nome = nome
        self._cargo = cargo
        self._email = email

    def criar_evento(self, evento: Evento, calendario: Calendario):
        calendario.adicionar_evento(evento)
