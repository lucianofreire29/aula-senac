import tkinter as tk
import json
from tkinter import messagebox


PATH_JSON = "alunos.json"

#funções

def salvar_dados_json(path, data):
    alunos_json = None

    # Ler o conteúdo do json
    with open(path, 'r', encoding='utf-8') as f:
        alunos_json = json.load(f) 

    
    alunos_json.append(data)

    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(alunos_json, f, ensure_ascii=False, indent=4)




def salvar(nome, email, curso, codigo_turma):

    if nome == "" or email == "" or curso == "" or codigo_turma == "":
        messagebox.showwarning("Aviso", "Campos obrigatórios!")
        return

    if email_ja_cadastrado(PATH_JSON, email):
        messagebox.showwarning("Aviso", "Este email já está cadastrado!")
        return

    novo_id = gerar_id(PATH_JSON)
    
    dict_aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "curso": curso,
        "codigo turma": codigo_turma
    }

    try:
        salvar_dados_json(PATH_JSON, dict_aluno)
        messagebox.showinfo("Sucesso", "Cadastro realizado!")
    except Exception as e:
        print("ERRO:", e)
        messagebox.showerror("Erro", "Erro ao cadastrar aluno")

def gerar_id(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data_json = json.load(f)
            return len(data_json) + 1
    except (FileNotFoundError, json.JSONDecodeError):
        return 1


def adicionar_notas_por_id(path, aluno_id, nota1, nota2, nota3):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data_json = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Erro", "Arquivo de alunos não encontrado.")
        return

    aluno_encontrado = False

    for aluno in data_json:
        if str(aluno.get("id")) == str(aluno_id):
            aluno["nota1"] = float(nota1)
            aluno["nota2"] = float(nota2)
            aluno["nota3"] = float(nota3)
            aluno["media"] = round((float(nota1) + float(nota2) + float(nota3)) / 3, 2)
            aluno_encontrado = True
            break

    if not aluno_encontrado:
        messagebox.showwarning("Aviso", "ID do aluno não encontrado.")
        return

    # salva de volta
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)

    messagebox.showinfo("Sucesso", "Notas adicionadas com sucesso!")


def email_ja_cadastrado(path, email):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data_json = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False  

    for aluno in data_json:
        if aluno.get("email", "").lower() == email.lower():
            return True

    return False












def main_window():
    root = tk.Tk()
    root.title("escola tecnica")
    root.geometry("800x600")



    frame_principal = tk.Frame(root, bg="#405F70")
    frame_principal.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    # Frame Lateral da 

    frame_lateral = tk.Frame(root, bg="#2c3e50", width=150)
    frame_lateral.pack(side=tk.LEFT, fill=tk.Y)


    tk.Label(frame_lateral, text='MENU', bg="#2c3e50", fg='white',
                            font=('Corbel', 18, 'bold')).pack(pady=20)

    def event_button_notas():

        root.destroy()
        notas_window()

    def event_button_destroy_root():
        root.destroy()

    tk.Button(frame_lateral, text="Cadastrar Aluno").pack(fill=tk.X, padx=10, pady=5)
    tk.Button(frame_lateral, text="Notas", command=event_button_notas).pack(fill=tk.X, padx=10, pady=5)
    tk.Button(frame_lateral, text="Sair",command=event_button_destroy_root).pack(fill=tk.X, padx=10, pady=5)



    #--- Frame Título ---
    frame_titulo = tk.Frame(frame_principal, bg="#bdc3c7", height=60)
    frame_titulo.pack(fill=tk.X)


    tk.Label(frame_titulo, text="Escola Tecnica", bg="#bdc3c7",
                        font=('Corbel', 18, )).pack(pady=15)


    #--- Frame Formulário ---
    frame_form = tk.Frame(frame_principal, bg='#405F70')
    frame_form.pack(pady=30)

    tk.Label(frame_form, text="Nome:", bg="#405F70",font=("corbel", 14)).grid(row=0, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_nome = tk.Entry(frame_form, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10,columnspan=3)


    tk.Label(frame_form, text="Email:", bg="#405F70",font=("corbel", 14)).grid(row=1, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_email = tk.Entry(frame_form, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=10,columnspan=3)

    tk.Label(frame_form, text="Curso:", bg="#405F70",font=("corbel", 14)).grid(row=2, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_curso = tk.Entry(frame_form, width=30)
    entry_curso.grid(row=2, column=1, padx=10, pady=10,columnspan=3)

    tk.Label(frame_form, text="cod.Turma:", bg="#405F70",font=("corbel", 14)).grid(row=3, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_cod_turma = tk.Entry(frame_form, width=30)
    entry_cod_turma.grid(row=3, column=1, padx=10, pady=10,columnspan=3)

    def event_button_limpar_pagina():
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_curso.delete(0, tk.END)
        entry_cod_turma.delete(0, tk.END)
        
    



    tk.Button(frame_form,text="cadastrar",command=lambda: salvar(entry_nome.get(),entry_email.get(),entry_curso.get(),entry_cod_turma.get())).grid(row=4, column=2)
    tk.Button(frame_form, text="Limpar", command=event_button_limpar_pagina).grid(row=4,column=3)




    root.mainloop()



def notas_window():
    root_1 = tk.Tk()
    root_1.title("escola tecnica")
    root_1.geometry("800x600")


    # frame principal da segunda pagina

    frame_principal_1 = tk.Frame(root_1, bg="#405F70")
    frame_principal_1.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    # Frame Lateral segunda pagina

    frame_lateral_1 = tk.Frame(root_1, bg="#2c3e50", width=150)
    frame_lateral_1.pack(side=tk.LEFT, fill=tk.Y)


    tk.Label(frame_lateral_1, text='MENU', bg="#2c3e50", fg='white',
                            font=('Corbel', 18, 'bold')).pack(pady=20)



    def event_button_cadastrar_aluno():
        root_1.destroy()
        main_window()

    def event_button_destroy_root_1():
        root_1.destroy()

    def salvar_notas():
        aluno_id = entry_ID.get()
        n1 = entry_nota_1.get()
        n2 = entry_nota_2.get()
        n3 = entry_nota_3.get()

        if aluno_id == "" or n1 == "" or n2 == "" or n3 == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        if not (nota_valida(n1) and nota_valida(n2) and nota_valida(n3)):
            messagebox.showwarning("Aviso","As notas devem ser números entre 0 e 10!")
            return

        adicionar_notas_por_id(PATH_JSON, aluno_id, n1, n2, n3)

    def calcular_media_entry():
        n1 = entry_nota_1.get()
        n2 = entry_nota_2.get()
        n3 = entry_nota_3.get()

        if n1 == "" or n2 == "" or n3 == "":
            messagebox.showwarning("Aviso", "Preencha as três notas!")
            return
        
        if not (nota_valida(n1) and nota_valida(n2) and nota_valida(n3)):
            messagebox.showwarning("Aviso","As notas devem ser números entre 0 e 10!")
            return


        try:
            media = (float(n1) + float(n2) + float(n3)) / 3
        except ValueError:
            messagebox.showerror("Erro", "Digite apenas números nas notas!")
            return

        entry_media.delete(0, tk.END)
        entry_media.insert(0, f"{media:.2f}")


    def nota_valida(valor):
        try:
            n = float(valor)
            return 0 <= n <= 10
        except ValueError:
            return False











    tk.Button(frame_lateral_1, text="Cadastrar Aluno",command=event_button_cadastrar_aluno).pack(fill=tk.X, padx=10, pady=5)
    tk.Button(frame_lateral_1, text="Notas").pack(fill=tk.X, padx=10, pady=5)
    tk.Button(frame_lateral_1, text="Sair",command=event_button_destroy_root_1).pack(fill=tk.X, padx=10, pady=5)



    #--- Frame Título segunda pagina---
    frame_titulo_1 = tk.Frame(frame_principal_1, bg="#bdc3c7", height=60)
    frame_titulo_1.pack(fill=tk.X)


    tk.Label(frame_titulo_1, text="Escola Tecnica", bg="#bdc3c7",
                        font=('Corbel', 18, )).pack(pady=15)


    #--- Frame Formulário segunda pagina---
    frame_form_1 = tk.Frame(frame_principal_1, bg='#405F70')
    frame_form_1.pack(pady=30)

    tk.Label(frame_form_1, text="ID:", bg="#405F70",font=("corbel", 14)).grid(row=0, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_ID = tk.Entry(frame_form_1, width=30)
    entry_ID.grid(row=0, column=1, padx=10, pady=10,columnspan=3)


    tk.Label(frame_form_1, text="Nota 1", bg="#405F70",font=("corbel", 14)).grid(row=1, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_nota_1 = tk.Entry(frame_form_1, width=30)
    entry_nota_1.grid(row=1, column=1, padx=10, pady=10,columnspan=3)

    tk.Label(frame_form_1, text="nota 2", bg="#405F70",font=("corbel", 14)).grid(row=2, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_nota_2 = tk.Entry(frame_form_1, width=30)
    entry_nota_2.grid(row=2, column=1, padx=10, pady=10,columnspan=3)

    tk.Label(frame_form_1, text="nota 3", bg="#405F70",font=("corbel", 14)).grid(row=3, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_nota_3 = tk.Entry(frame_form_1, width=30)
    entry_nota_3.grid(row=3, column=1, padx=10, pady=10,columnspan=3)

    tk.Label(frame_form_1, text="media", bg="#405F70",font=("corbel", 14)).grid(row=4, column=0, 
                                                sticky='e', padx=10, pady=10)
    entry_media = tk.Entry(frame_form_1, width=30)
    entry_media.grid(row=4, column=1, padx=10, pady=10,columnspan=3)

    def event_button_limpar_pagina_1():
        entry_ID.delete(0, tk.END)
        entry_nota_1.delete(0, tk.END)
        entry_nota_2.delete(0, tk.END)
        entry_nota_3.delete(0, tk.END)
        entry_media.delete(0, tk.END)







    tk.Button(frame_form_1, text="Salvar",command=salvar_notas).grid(row=5,column=1)
    tk.Button(frame_form_1,text="Media",command=calcular_media_entry).grid(row=5, column=2)
    tk.Button(frame_form_1, text="Limpar",command=event_button_limpar_pagina_1).grid(row=5,column=3)






if __name__ == "__main__":
    main_window()
