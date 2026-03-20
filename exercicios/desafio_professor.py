'''
Desafio: Sistema de Cadastro de Alunos
Você deve criar um programa que gerencie um cadastro de alunos usando dicionários.

Regras do programa
    - Cada aluno terá:
        - Matrícula (chave única, tipo int)
        - Nome (string)
        - Idade (int)
        - Notas (lista de floats)
    - O programa deve permitir:
        - Adicionar um novo aluno.
        - Atualizar dados de um aluno existente.
        - Remover um aluno pelo número de matrícula.
        - Buscar um aluno pelo número de matrícula.
        - Listar todos os alunos cadastrados.
        - Calcular a média das notas de um aluno.

Exemplo de Estrutura do Dicionário
alunos = { 
    101: {"nome": "Ana", "idade": 20, "notas": [8.5, 7.0, 9.0]},
    102: {"nome": "Bruno", "idade": 22, "notas": [6.0, 5.5, 7.5]}
}
'''
import time, os


alunos = {
    101: {"nome": "Ana", "idade": 20, "notas": [8.5, 7.0, 9.0]},
    102: {"nome": "Bruno", "idade": 22, "notas": [6.0, 5.5, 7.5]}
}


while True:

    MENU = '''
    ==== ESCOLA SENAC ====
    [1] Adicionar um novo aluno.
    [2] Atualizar dados de um aluno existente.
    [3] Remover um aluno pelo número de matrícula.
    [4] Buscar um aluno pelo número de matrícula.
    [5] Listar todos os alunos cadastrados.
    [6] Calcular a média das notas de um aluno.
    [7] Encerrar programa
    '''
    MENUUPDATE = '''
[1] Nome
[2] Idade
[3] Notas
[4] Sair
'''

    print(MENU)
    opcao = int(input('Escolha uma opção..: '))

    match opcao:
        case 1:
            os.system('cls')
            print('== CADASTRAR ALUNO ==')
            while True:
                matricula = int(input('Matrícula: '))

                if matricula not in alunos:
                    break
                print('Matrícula já cadastrada! ')

            nome = input('Nome: ')
            idade = int(input('Idade: '))

            notas = list()

            for i in range(3):
                notas.append(float(input(f'{i+1}º Nota:')))
            
            alunos[matricula] = {'nome': nome, 'idade': idade, 'notas': notas}

            print('Carregando dados... ')
            time.sleep(3)
            print('Aluno cadastrado com sucesso!')             

        case 2:
            os.system('cls')
            print('== EDITAR DADOS DO ALUNO ==')

            while True:
                matricula = int(input('Matrícula: '))

                print('Carregando dados... ')
                time.sleep(3)

                if matricula in alunos:
                    print(f'Aluno {alunos[matricula]['nome']} selecionado!')
                    print(MENUUPDATE)
                    opcao_update = int(input('->'))

                    match opcao_update:
                        case 1:
                            print(f'Nome atual: {alunos[matricula]['nome']}')
                            alunos[matricula]['nome'] = input('Nome:')
                            print('Carregando dados... ')
                            time.sleep(3)
                        case 2:
                            print(f'Idade atual: {alunos[matricula]['idade']}')
                            alunos[matricula]['idade'] = int(input('Idade:'))
                            print('Carregando dados... ')
                            time.sleep(3)
                        case 3:
                            print(f'Notas atuais: {alunos[matricula]['notas']}')
                            index = int(input('Qual nota deseja atualizar [1, 2, 3]: ')) - 1
                            alunos[matricula]['notas'][index] = float(input('Nota Atualizada:'))
                            print('Carregando dados... ')
                            time.sleep(3)
                        case 4:
                            break
                        case _:
                            print('Opção Inválida!')
                    break
                
                
                print('Matrícula desconhecida!')
        case 3:
            os.system('cls')
            print('== EXCLUIR ALUNO ==')

            while True:
                matricula = int(input('Matrícula: '))

                print('Carregando dados... ')
                time.sleep(3)

                if matricula in alunos:
                    print(f'Aluno {alunos[matricula]['nome']} excluído com sucesso! ')
                    del alunos[matricula]
                    break
                
                print('Matrícula desconhecida!')
        case 4:
            os.system('cls')
            print('== BUSCAR ALUNO ==')

            while True:
                matricula = int(input('Matrícula: '))

                print('Carregando dados... ')
                time.sleep(3)

                if matricula in alunos:
                    media = (sum(alunos[matricula]['notas'])/3)
                    print(f'Matrícula: {matricula} | Nome: {alunos[matricula]['nome']} | Idade: {alunos[matricula]['idade']} | Notas: {alunos[matricula]['notas']}')
                    print(f'Média do {alunos[matricula]['nome']}: {media:.2f}')
                    print(f'Situação: {'Aprovado' if media >= 7 else 'Reprovado'}')
                    input('Digite ENTER para continuar...')
                    break

                print('Matrícula desconhecida!⚠️')
        case 5:
            os.system('cls')
            print('== ALUNOS CADASTRADOS ==')

            for k, v in alunos.items():
                print(f'Matrícula: {k} | Nome: {v['nome']} | Idade: {v['idade']} | Notas: {v['notas']}')
                print(f'Média do  {v['nome']}: {(sum(v['notas'])/3):.2f}')

        case 6:
            os.system('cls')
            print('== MÉDIA DO ALUNO ==')

            while True:
                matricula = int(input('Matrícula: '))

                print('Carregando dados... ')
                time.sleep(3)

                if matricula in alunos:
                    media = (sum(alunos[matricula]['notas'])/3)
                    print(f'Aluno: {alunos[matricula]['nome']}  | Média: {media:.2f}')
                    print(f'Situação: {'Aprovado' if media >= 7 else 'Reprovado'}')
                    input('Digite ENTER para continuar ...')
                    break

                print('Matrícula desconhecida!')
                
        case 7:
            print('Encerrando aplicação...')
            time.sleep(2)
            break
        case _:
            os.system('cls')
            print('Valor Inválido!')