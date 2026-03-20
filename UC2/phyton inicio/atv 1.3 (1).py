lista = []
i=1
# valor zero das variaveis
aluno = aluno_idoso = vtotal = valor = mensalidade_des = 0
# entrada de dados
while i != 0:
	nome = input("Informe o seu nome: ")
	idade = int(input("Informe a sua idade: "))
	# se idade for menor ou igual a zero, volta a pedir idade.
	while idade <= 0 :
		print("Erro: Idade não pode ser inferior ou igual a 0.")
		idade = int(input("Informe a sua idade: "))
	valor = float(input("Informe o valor da sua mensalidade: "))
	# se valor for menor que 100, gera mensagem errada, volta a pedir o valor.
	while valor < 100:
		print("Erro: Mensalidade inválida.")
		valor = float(input("Informe o valor da sua mensalidade: "))
		


	
# processamento
# valor de idade maior que 60 gera desconto, alimenta variavel de aluno idoso, e alimenta variavel de valor total
	if idade >= 60:
		desconto = (valor*0.20)
		mensalidade_des = valor - desconto
		vtotal += mensalidade_des
		aluno_idoso += 1
# se não o desconto fica valor 0, alimenta variavel aluno pois é menor que 60 anos, e alimenta variavel vtotal sem o valor do desconto de 20% 
	else:
		desconto = 0
		mensalidade_des = valor - desconto
		vtotal += mensalidade_des
		aluno += 1

	lista.append(nome)
	lista.append(idade)
	lista.append(valor)
	lista.append(desconto)
# soma do aluno idoso com os não idosos, gerando aluno total, e media e a soma do valor total dividido pelo aluno total
	aluno_total = aluno + aluno_idoso
	media_f = vtotal/aluno_total

	print("digite zero para fechar o programa ou 1 para continuar")
	i = int(input(""))


# saida de dados
print("__________________________________________________")
print(f"quantidade total de alunos:  {aluno_total}")
print(f"valor total arrecadado:   R$ {round(vtotal,2)}")
print(f"medida das mensalidades:  R$ {round(media_f,2)}")
print(f"quantidade de alunos idosos: {aluno_idoso}")
if vtotal > 500:
	print("\nboa arrecadação!!!!!!")
else:
	print("\narrecadação a baixo do esperado!!!!!")
print("__________________________________________________")
print(f"\n{lista}")	
print("\n__________________________________________________")


# luciano
# david
# lucas

