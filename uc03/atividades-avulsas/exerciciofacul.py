import tkinter as tk

def main_window():
    janela = tk.Tk()
    janela.title('relatório')
    janela.geometry('500x500')
    janela.configure(bg="#049DF5")

    # Título
    title_pg = tk.Label(
        janela,
        text="relatório",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 18)
    )
    title_pg.pack(pady=(10, 5))

    # nome
    nome_pg = tk.Label(
        janela,
        text="Nome",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    nome_pg.pack(pady=(10, 5))

    var_nome = tk.StringVar()
    nome_entry = tk.Entry(
        janela,
        textvariable=var_nome,
        font=("Berlin Sans FB", 12),
        justify="center"
    )
    nome_entry.pack(padx=10)

    # idade
    idade_pg = tk.Label(
        janela,
        text="Idade",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    idade_pg.pack(pady=(10, 5))

    var_idade = tk.StringVar()
    idade_entry = tk.Entry(
        janela,
        textvariable=var_idade,
        font=("Berlin Sans FB", 12),
        justify="center"
    )
    idade_entry.pack(padx=10)

    # curso
    curso_pg = tk.Label(
        janela,
        text="Curso",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    curso_pg.pack(pady=(10, 5))

    var_curso = tk.StringVar()
    curso_entry = tk.Entry(
        janela,
        textvariable=var_curso,
        font=("Berlin Sans FB", 12),
        justify="center"
    )
    curso_entry.pack(padx=10)

    def event_button():
        rel_nome = var_nome.get()
        rel_idade = var_idade.get()
        rel_curso = var_curso.get()
        confirmation_window(janela, rel_nome, rel_idade, rel_curso)

    # Botão
    button = tk.Button(
        janela,
        bg="#06fa57",
        text="Gerar relatório",
        font=("Berlin Sans FB", 12, "bold"),
        fg="#000000",
        command=event_button
    )
    button.pack(pady=20)

    janela.mainloop()


def confirmation_window(parent, nome, idade, curso):
    janela = tk.Toplevel(parent)  # ✅ correto
    janela.title("Relatório")
    janela.geometry("500x300")
    janela.configure(bg="#049DF5")

    # Título
    title_pg = tk.Label(
        janela,
        text="Relatório",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 18)
    )
    title_pg.pack(pady=(10, 5))

    # Mostrar dados
    nome_lb = tk.Label(
        janela,
        text=f"{nome} | {idade} | {curso}",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    nome_lb.pack(pady=5)


main_window()


# cont = 

# for i in range(4, 0, -1):
#     for j in range(0, 4):
#         cont+=1
#         match list_button[cont]:
#             case '+':
#                 tk.Button(frame_calc, text=list_button[cont], command=somar).grid(row=i,column=j,ipady=10,ipadx=10,pady=5,padx=5)
#                 continue 



#         tk.Button(frame_calc, text=list_button[cont]).grid(row=i,column=j,ipady=10,ipadx=10,pady=5,padx=5)        
        

