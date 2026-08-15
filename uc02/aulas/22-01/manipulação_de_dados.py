'''Manipulação de Arquivos com Python'''

import os

os.system('cls')

'''
     open() -> para abrir conexão com arquivos
    - ler o arquivo (read)
    - escrever no arquivo (write)
    - adicionar conteúdo (append)
'''

PATH_ARCHIVE = 'dataset_alunos.txt'

def save_student(data: (str | list)):
    with open(PATH_ARCHIVE, 'a', encoding='utf-8', newline='\n') as arq:
        if isinstance(data, str):
            arq.write(data)
        else:
            arq.writelines(data)
    
    print('Dados cadastrados com sucesso!✅')

def read_student():
    with open(PATH_ARCHIVE, 'r', encoding='utf-8') as arq:
        print('#--------- ALUNOS CADASTRADOS ---------#')
        for i in arq.readlines():
            print(i)

        arq.seek(0)
        print(f'\nTotal de {len(arq.readlines())} alunos!')

def find_student_by_firstname(firstname: str):
    with open(PATH_ARCHIVE, 'r', encoding='utf-8') as arq:
        print(f'Alunos com primeiro nome: {firstname}')
        for i in arq.readlines():
            if i.startswith(firstname):
                print(i)

find_student_by_firstname('Aline')