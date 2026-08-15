# 1 - Crie uma classe chamada Pessoa que possua dois atributos públicos:
# nome
# idade
# Instancie um objeto dessa classe e atribua valores aos atributos. Em seguida, imprima os valores.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Pedro", 21)

print(f"nome:",pessoa.nome, "idade:",pessoa.idade)


# 2 - Crie uma classe Animal que receba, no método __init__, os atributos:
# especie
# nome
# Crie um objeto da classe e exiba seus dados.

class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome

animal = Animal("cascavel", "Crotalus durissus")

print(f"especie: {animal.especie} nome: {animal.nome} ")

# 3 - Crie uma classe Carro com os atributos:
# modelo
# ano
# Implemente um método exibir_informacoes() que mostre os dados do carro.

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano


    def exibir_informacoes(self):
        return (f"modelo: {self.modelo} ano: {self.ano}")

carro = Carro("Civic", "2012")

print(carro.exibir_informacoes())

# 4 - Crie uma classe Produto com:
# nome
# preco
# Implemente um método aplicar_desconto(percentual) que atualize o preço do produto com base no percentual informado. 

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def aplicar_desconto(self, percentual):
        self.preco = self.preco -(self.preco * percentual/100)



percentual = float(input("digite o desconto: "))
produto_1 = Produto("caderno", 10.00)

produto_1.aplicar_desconto(percentual)

print(f"produto: {produto_1.nome} valor: {produto_1.preco}")





# 5 - Crie uma classe Aluno com:
# nome
# nota
# Implemente um método verificar_situacao() que retorne:
# "Aprovado" se a nota for maior ou igual a 7
# "Reprovado" caso contrário


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_situacao(self):
        if self.nota >= 7:
            return "Aprovado"
        else:
            return "reprovado"


aluno = Aluno("luciano", 10)
print(aluno.verificar_situacao())



# 6 - Crie uma classe ContaBancaria com:
# titular
# saldo
# Implemente os métodos:
# depositar(valor)
# sacar(valor) (não permitir saque se o saldo for insuficiente)

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):

        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            return "Saque insuficiente"

conta_1 = ContaBancaria("jean", 2000)
print(conta_1.sacar(5000))
conta_1.depositar(10000)
conta_1.sacar(5000)
print(conta_1.saldo)

# 7 - Crie uma classe Lampada com o atributo:
# ligada (booleano)
# Implemente os métodos:
# ligar()
# desligar()
# Crie um objeto e simule a mudança de estado da lâmpada.

class Lampada:
    def __init__(self):
        self.ligada = False  

    def ligar(self):
        if self.ligada == True:
            return "lampada se encontra ligada"
        self.ligada = True


    def desligar(self):
        if self.ligada == False:
            return "lampada se encontra desligada"
        self.ligada = False


lamp = Lampada()

print(lamp.desligar())
print(lamp.ligar())
print(lamp.ligar())
print(lamp.desligar())




# 8 - Crie uma classe Retangulo com:
# largura
# altura
# Implemente um método calcular_area() que retorne a área do retângulo.

class Retangulo:
    def __init__(self, largura, altura,):
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        return  self.largura * self.altura


retangulo = Retangulo (60, 40)

print(retangulo.calcular_area())

# 9 - Crie uma classe Livro com:
# titulo
# autor
# Implemente um método detalhes() que retorne uma string formatada com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def metodo_detalhes(self) -> str:
        return f"{self.titulo} |  {self.autor}"

livro = Livro("harry poter", "j k rowling")

print(livro.metodo_detalhes())

# 10 - Crie uma classe Funcionario com:
# nome
# salario
# Instancie três objetos Funcionario e armazene-os em uma lista.
# Percorra a lista exibindo o nome e o salário de cada funcionário.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

lista_funcionario = []

while True:
    nome = input("digite o nome do funcionario: ")
    salario = float(input("digite o salario do funcionario: "))

    lista_funcionario.append(Funcionario(nome , salario))

    flag = input("deseja continuar ? (s) sim ou (n) NÃO.")

    if flag.lower() == "n":
        break

for i in lista_funcionario: 
    print(f"nome: {i.nome}  salário: R${i.salario}")