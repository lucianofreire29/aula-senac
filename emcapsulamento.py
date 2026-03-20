# EXERCÍCIO 1 - Conta Bancária
# Crie uma classe ContaBancaria com os atributos: número da conta, nome do titular e saldo.
# • Encapsule os atributos.
# • Crie métodos para depositar e sacar valores.
# • Impedir que o saldo se torne negativo.


class ContaBancaria:
    def __init__(self, numero,nome,saldo):
        self._numero = numero
        self._nome = nome
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo


# EXERCÍCIO 2 - Produto
# Crie uma classe Produto contendo: nome, preço e quantidade em estoque.
# • Encapsule os atributos.
# • Crie métodos para adicionar e remover itens do estoque.
# • Garantir que quantidade não seja negativa.



class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque


    def adicionar_produto(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
        else:
            print("Quantidade inválida.")


    def remover_produto(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
        else:
            print("Estoque insuficiente.")

# EXERCÍCIO 3 - Aluno
# Crie uma classe Aluno com nome, matrícula e média final.
# • Encapsule os atributos.
# • Crie um método que retorne se o aluno está aprovado (média ≥ 7).


class Aluno:
    def __init__(self, nome, matricula, media_final):
        self.__nome = nome
        self.__matricula = matricula
        self.__media_final = media_final

    def aprovacao(self,media):
        if media > 7:
            media_final = media
            return media_final



# EXERCÍCIO 4 - Livro
# Crie uma classe Livro com título, autor e ano de publicação.
# • Permitir somente leitura dos atributos (apenas getters).


class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def ano(self):
        return self._ano


livro = Livro("harry potter", "j k", 2008)

print(livro.titulo)
print(livro.autor)
print(livro.ano)



# EXERCÍCIO 5 - Funcionário
# Crie uma classe Funcionário com nome, cargo e salário.
# • Encapsule os atributos.
# • Criar método para aumentar salário (percentual).
# • Impedir valores negativos.


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def aumentar_Salario(self, aumentar_salario):
        if aumentar_salario > 0:
            aumentar_salario += ((aumentar_salario/100)*self.__salario)+self.__salario
            return aumentar_salario


# EXERCÍCIO 6 - Carro
# Crie uma classe Carro com modelo, ano e velocidade.
# • Encapsular atributos.
# • Criar métodos para acelerar e frear.
# • A velocidade não pode ser negativa e não pode ultrapassar 200 km/h.


class Carro:
    def __init__(self, modelo, ano, velocidade):
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = velocidade

    def acelerar(self, acelerar):
        if self.__velocidade > 0:
            acelerar +=self.__velocidade
            return acelerar
        
# EXERCÍCIO 7 - Pessoa
# Crie uma classe Pessoa com nome, idade e CPF.
# • O CPF deve ter somente leitura (apenas getter).
# • A idade não pode ser negativa.


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf= cpf

    def pessoa (self):
        return self.nome
    
    def pessoa_idade(self):
        if self.idade > 0 :
            return self.idade
        
    @property
    def cpf(self):
        return self.__cpf
    


#     EXERCÍCIO 8 - Conta de Luz
# Crie uma classe ContaDeLuz com número da instalação, consumo (kWh) e valor.
# • Encapsule os atributos.
# • O valor deve ser calculado com base no consumo.
# • Permitir apenas leitura do valor calculado.


class ContaDeLuz:
    def __init__(self, numero, consumo):
        self.__numero = numero
        self.__consumo = consumo
        self.__valor = self.__calcular_valor()

    def __calcular_valor(self):
        tarifa = 0.75  # valor por kWh (exemplo)
        return self.__consumo * tarifa

    @property
    def valor(self):
        return self.__valor

# EXERCÍCIO 9 - Animal
# Crie uma classe Animal com nome, espécie e idade.
# • Encapsular atributos.
# • Criar um método para envelhecer (aumentar idade em 1).
# • Idade nunca pode ser negativa.


class Animal:
    def __init__(self, nome, especie, idade):
        self.__nome = nome
        self.__especie = especie
        
        if idade < 0:
            self.__idade = 0
        else:
            self.__idade = idade

    def envelhecer(self):
        self.__idade += 1

    def get_idade(self):
        return self.__idade




# EXERCÍCIO 10 - Caixa de Supermercado
# Crie uma classe Caixa que calcule o total de uma compra.
# • Encapsular atributos: lista de produtos e total.
# • Método para adicionar produtos.
# • O total deve ser calculado automaticamente (apenas leitura).


class Caixa:
    def __init__(self):
        self.__lista_produtos = []
        self.__total = 0.0

    def adicionar_produto(self, nome, preco):
        if preco > 0:
            self.__lista_produtos.append((nome, preco))
            self.__total += preco

    def get_total(self):
        return self.__total




