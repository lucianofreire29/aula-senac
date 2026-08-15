# • Atividade 01 – Explorando o pack(): Criar janela com 3 Labels e 2 Buttons utilizando pack(),
# testando side, fill, expand, padx e pady.
import tkinter as tk

# root = tk.Tk()
# root.title("explorando o pack")
# root.geometry("700x400")
# root.configure(bg="#8104F5")


#     # Título
# title_pg = tk.Label(root,
#                         text="Texto",
#                         fg="#000000", bg="#8104F5",
#                         font=("Berlin Sans FB", 18))
# title_pg.pack(pady=(10, 5))


#     # Label Descrição
# description_lb = tk.Label(root,
#                             text="Digite um nome",
#                             fg="#000000", bg="#8104F5",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
# description_lb.pack(pady=5, padx=10, fill="x")


# description_text = tk.Text(root, height=1,
#                             font=("Berlin Sans FB", 12))
# description_text.pack(padx=2, fill="x")

# def event_button():
#     description_text.delete("1.0", "end")
    
    

#     # Botão
# button = tk.Button(root,
#                     bg="#ffff00",
#                     text="Enviar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
# button.pack(side="left")


# description_text = tk.Text(root, height=5,
#                             font=("Berlin Sans FB", 12))
# description_text.pack(expand=True)




# root.mainloop()


# • Atividade 02 – Layout vertical e horizontal com pack(): Construir menu com título no topo, três
# botões centrais e botão sair no rodapé.

# root = tk.Tk()
# root.title("layout vertical e horizontal")
# root.geometry("800x600")


# # frame lateral
# frame_lateral = tk.Frame(root, bg="#2a2d30", width=150)
# frame_lateral.pack(side=tk.LEFT, fill=tk.Y)

# tk.Label(frame_lateral, text="MENU LATERAL", bg="#2a2d30", fg="white",
#                         font=("arial", 14, "bold")).pack(pady=20)


# tk.Button(frame_lateral, text="enviar").pack(fill=tk.X, padx=10,pady=5)
# tk.Button(frame_lateral, text="confirmar").pack(fill=tk.X, padx=10,pady=5)
# tk.Button(frame_lateral, text="sair").pack(side="bottom",fill=tk.X, padx=10,pady=5)



# frame_principal = tk.Frame(root, bg="#9de1f1")
# frame_principal.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# frame_form =tk.Frame(frame_principal, bg="#ecf0f1")
# frame_form.pack(padx=30)


# tk.Button(frame_principal, text="botão 1").pack(padx=10,pady=5)
# tk.Button(frame_principal, text="botão 2").pack(padx=10,pady=5)
# tk.Button(frame_principal, text="botão 3").pack(padx=10,pady=5)
# tk.Button(frame_principal, text="sair").pack(side="bottom",fill=tk.X, padx=10,pady=5)





# • Atividade 03 – Introdução ao grid(): Criar formulário com Nome, Email e botão Enviar utilizando
# grid(), padx, pady e sticky.

# root = tk.Tk()
# root.title("layout vertical e horizontal")
# root.geometry("800x600")
# root.configure(bg="#8104F5")

#     # Label Descrição
# description_lb = tk.Label(root,
#                             text="Digite um nome",
#                             fg="#000000", bg="#F7F5F8",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
# description_lb.grid(row=0, column=0, padx=5, pady=5)


# description_text = tk.Text(root, height=1,
#                             font=("Berlin Sans FB", 12))
# description_text.grid(row=0, column=1,sticky="w")

# description_lb = tk.Label(root,
#                             text="Digite um email",
#                             fg="#000000", bg="#F7F5F8",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
# description_lb.grid(row=1, column=0, padx=5, pady=5)


# description_text = tk.Text(root, height=1,
#                             font=("Berlin Sans FB", 12))
# description_text.grid(row=1, column=1,sticky="w")

# tk.Button(root, text="enviar").grid(row=2, column=1,sticky="ew")

# • Atividade 04 – Calculadora com grid(): Criar layout visual de calculadora com Entry e botões
# organizados em matriz 4x4 usando columnspan.


# root = tk.Tk()
# root.title("Calculadora")
# root.geometry("280x320")
# root.configure(bg="#049DF5")

# frame_principal = tk.Frame(root, bg="#049DF5")
# frame_principal.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# #----------frame titulo -----------

# frame_titulo = tk.Frame(frame_principal, bg="#049DF5", height=60)
# frame_titulo.pack(fill=tk.X)

# tk.Label(frame_titulo, text="Calculadora", bg='#049DF5',
#                         font=("Arial", 16, "bold")).pack(pady=15)


# #----------frame calculadora ------
# frame_calc =tk.Frame(frame_principal, bg="#049DF5")
# frame_calc.pack(padx=30)

# var_nome = tk.StringVar()
# nome_entry = tk.Entry(
#                         frame_calc,
#                         textvariable=var_nome,
#                         font=("Berlin Sans FB", 12),
#                         justify="center"
#                     )
# nome_entry.grid(row=0, column=0, columnspan=4)




# list_button = ["0","c", "=","+",
#                 "1","2","3","-",
#                 "4","5","6","*",
#                 "7","8","9","/"]

# cont = 0

# for i in range(4, 0, -1):
#     for j in range(0, 4):
#         tk.Button(frame_calc, text=list_button[cont]).grid(row=i,column=j,ipady=10,ipadx=10,pady=5,padx=5)        
#         cont+=1



# codigo para criar commands para a calculadora.
# cont = 

# for i in range(4, 0, -1):
#     for j in range(0, 4):
#         cont+=1
#         match list_button[cont]:
#             case '+':
#                 tk.Button(frame_calc, text=list_button[cont], command=somar).grid(row=i,column=j,ipady=10,ipadx=10,pady=5,padx=5)
#                 continue 



#         tk.Button(frame_calc, text=list_button[cont]).grid(row=i,column=j,ipady=10,ipadx=10,pady=5,padx=5)        
        



# • Atividade 05 – Explorando place(): Criar janela com Label centralizado e dois botões
# posicionados com x, y, relx, rely e anchor.

# root = tk.Tk()
# root.title("Calculadora")
# root.geometry("500x600")
# root.configure(bg="#049DF5")

# tk.Label(root, text="Centralizado", bg='#049DF5',
#                         font=("Arial", 16, "bold")).place(anchor="center",relx=0.5, rely=0.5)

# tk.Button(root, text="botão 1", bg="#06B806").place(anchor="center",relx=0.4, rely=0.6)
# tk.Button(root, text="botão 1", bg="#06B806").place(anchor="center",relx=0.6, rely=0.6)



# • Atividade 06 – Comparação entre pack, grid e place: Desenvolver três versões da mesma
# interface utilizando cada gerenciador separadamente.

# root = tk.Tk()
# root.title("Calculadora")
# root.geometry("500x600")
# root.configure(bg="#062D44")

# tk.Label(root, text="janela 1 - PLACE", bg='#062D44',
#                         font=("Arial", 16, "bold")).place(anchor="n",relx=0.5)

# var_nome = tk.StringVar()
# nome_entry = tk.Entry(
#                         root,
#                         textvariable=var_nome,
#                         font=("Berlin Sans FB", 12),
#                         justify="center"
#                     ).place(anchor="n", relx=0.5,rely=0.1)

# tk.Label(root, text="janela 1 - PLACE", bg='#062D44',
#                         font=("Arial", 16, "bold")).pack(pady=0.5)

# var_nome = tk.StringVar()
# nome_entry = tk.Entry(
#                         root,
#                         textvariable=var_nome,
#                         font=("Berlin Sans FB", 12),
#                         justify="center"
#                     ).pack(pady= 0.5)



# tk.Label(root, text="janela 1 - PLACE", bg='#062D44',
#                         font=("Arial", 16, "bold")).grid(row=0)

# var_nome = tk.StringVar()
# nome_entry = tk.Entry(
#                         root,
#                         textvariable=var_nome,
#                         font=("Berlin Sans FB", 12),
#                         justify="center"
#                     ).grid(row=1,padx=0.5)















# • Atividade 07 – Introdução ao Frame: Criar interface com Frame superior (título), central
# (formulário) e inferior (botões).

# root = tk.Tk()
# root.title("Calculadora")
# root.geometry("500x600")
# root.configure(bg="#062D44")




# frame_principal = tk.Frame(root, bg="#049DF5")
# frame_principal.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# #----------frame titulo -----------

# frame_titulo = tk.Frame(frame_principal, bg="#F504F5", height=60)
# frame_titulo.pack(fill=tk.X)

# #----------frame inferior -----------

# frame_inferior = tk.Frame(frame_principal, bg="#04F504",height=60)
# frame_inferior.pack(anchor="s",side=tk.BOTTOM, expand=True, fill=tk.X)




# • Atividade 08 – Layout complexo com múltiplos Frames: Criar menu lateral, área principal e
# barra superior utilizando combinação de layouts.



# def main():
#     root = tk.Tk()
#     root.title("Layout Complexo")
#     root.geometry("800x500")
#     root.configure(bg="#dddddd")

#     top_bar = tk.Frame(root, bg="#2c3e50", height=60)
#     top_bar.pack(side="top", fill="x")

#     title = tk.Label(
#         top_bar,
#         text="Sistema de Exemplo",
#         bg="#2c3e50",
#         fg="white",
#         font=("Arial", 16, "bold")
#     )
#     title.pack(pady=15)


#     container = tk.Frame(root, bg="#dddddd")
#     container.pack(fill="both", expand=True)


#     menu_lateral = tk.Frame(container, bg="#34495e", width=200)
#     menu_lateral.pack(side="left", fill="y")

#     tk.Label(
#         menu_lateral,
#         text="MENU",
#         bg="#34495e",
#         fg="white",
#         font=("Arial", 14, "bold")
#     ).pack(pady=10)


#     for item in ["Home", "Cadastro", "Relatórios", "Sair"]:
#         tk.Button(
#             menu_lateral,
#             text=item,
#             width=18,
#             bg="#5d6d7e",
#             fg="white"
#         ).pack(pady=5)


#     area_principal = tk.Frame(container, bg="white")
#     area_principal.pack(side="right", fill="both", expand=True, padx=5, pady=5)

#     tk.Label(area_principal,text="Área Principal",bg="white",font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)


#     tk.Label(area_principal, text="Nome:", bg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
#     tk.Entry(area_principal, width=30).grid(row=1, column=1, padx=5, pady=5)

#     tk.Label(area_principal, text="Email:", bg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
#     tk.Entry(area_principal, width=30).grid(row=2, column=1, padx=5, pady=5)

#     tk.Button(area_principal, text="Salvar", bg="#27ae60", fg="white").grid(row=3, column=0, columnspan=2, pady=15)

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# • Atividade 09 – Responsividade básica: Implementar redimensionamento utilizando weight,
# expand e fill.



# def main():
#     root = tk.Tk()
#     root.title("Responsividade Básica")
#     root.geometry("800x500")


#     root.grid_rowconfigure(1, weight=1)
#     root.grid_columnconfigure(0, weight=1)


#     top_bar = tk.Frame(root, bg="#2c3e50", height=60)
#     top_bar.grid(row=0, column=0, sticky="nsew")

#     tk.Label(
#         top_bar,
#         text="Sistema Responsivo",
#         bg="#2c3e50",
#         fg="white",
#         font=("Arial", 16, "bold")
#     ).pack(expand=True)


#     container = tk.Frame(root, bg="#bdc3c7")
#     container.grid(row=1, column=0, sticky="nsew")

#     container.grid_rowconfigure(0, weight=1)
#     container.grid_columnconfigure(1, weight=1)


#     menu = tk.Frame(container, bg="#34495e", width=200)
#     menu.grid(row=0, column=0, sticky="ns")

#     tk.Label(menu, text="MENU", bg="#34495e", fg="white",
#             font=("Arial", 14, "bold")).pack(pady=10)

#     for item in ["Home", "Cadastro", "Relatórios", "Sair"]:
#         tk.Button(menu, text=item, width=18).pack(pady=5)


#     main_area = tk.Frame(container, bg="white")
#     main_area.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


#     main_area.grid_columnconfigure(1, weight=1)

#     tk.Label(main_area, text="Nome:", bg="white").grid(
#         row=0, column=0, padx=5, pady=5, sticky="e"
#     )
#     tk.Entry(main_area).grid(
#         row=0, column=1, padx=5, pady=5, sticky="ew"
#     )

#     tk.Label(main_area, text="Email:", bg="white").grid(
#         row=1, column=0, padx=5, pady=5, sticky="e"
#     )
#     tk.Entry(main_area).grid(
#         row=1, column=1, padx=5, pady=5, sticky="ew"
#     )

#     tk.Button(main_area, text="Salvar").grid(
#         row=2, column=0, columnspan=2, pady=15
#     )

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# • Atividade 10 – Projeto Final: Mini sistema de cadastro com menu lateral, formulário e botões,
# respeitando boas práticas de layout.

import tkinter as tk
from tkinter import messagebox


def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    curso = entry_curso.get()

    if not nome or not email or not curso:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    messagebox.showinfo(
        "Sucesso",
        f"Cadastro realizado!\n\nNome: {nome}\nEmail: {email}\nCurso: {curso}"
    )
    limpar_campos()


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_curso.delete(0, tk.END)


def mostrar_cadastro():
    messagebox.showinfo("Menu", "Você já está na tela de cadastro.")



root = tk.Tk()
root.title("Mini Sistema de Cadastro") 
root.geometry("900x550")

# Responsividade do root
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


topo = tk.Frame(root, bg="#2c3e50", height=60)
topo.grid(row=0, column=0, sticky="nsew")

titulo_topo = tk.Label(
    topo,
    text="Sistema de Cadastro",
    bg="#2c3e50",
    fg="white",
    font=("Arial", 16, "bold")
)
titulo_topo.pack(expand=True)


container = tk.Frame(root, bg="#bdc3c7")
container.grid(row=1, column=0, sticky="nsew")

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(1, weight=1)

menu = tk.Frame(container, bg="#34495e", width=220)
menu.grid(row=0, column=0, sticky="ns")

tk.Label(
    menu,
    text="MENU",
    bg="#34495e",
    fg="white",
    font=("Arial", 14, "bold")
).pack(pady=15)

botoes_menu = [
    ("Cadastro", mostrar_cadastro),
    ("Limpar", limpar_campos),
    ("Sair", root.quit)
]

for texto, comando in botoes_menu:
    tk.Button(
        menu,
        text=texto,
        width=18,
        command=comando
    ).pack(pady=6)


main = tk.Frame(container, bg="white")
main.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

main.grid_columnconfigure(1, weight=1)

titulo_form = tk.Label(
    main,
    text="Formulário de Cadastro",
    bg="white",
    font=("Arial", 16, "bold")
)
titulo_form.grid(row=0, column=0, columnspan=2, pady=15)

# Campos
tk.Label(main, text="Nome:", bg="white").grid(
    row=1, column=0, sticky="e", padx=5, pady=5
)
entry_nome = tk.Entry(main)
entry_nome.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

tk.Label(main, text="Email:", bg="white").grid(
    row=2, column=0, sticky="e", padx=5, pady=5
)
entry_email = tk.Entry(main)
entry_email.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

tk.Label(main, text="Curso:", bg="white").grid(
    row=3, column=0, sticky="e", padx=5, pady=5
)
entry_curso = tk.Entry(main)
entry_curso.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# Botões
frame_botoes = tk.Frame(main, bg="white")
frame_botoes.grid(row=4, column=0, columnspan=2, pady=20)

tk.Button(
    frame_botoes,
    text="Salvar",
    bg="#27ae60",
    fg="white",
    width=12,
    command=salvar
).pack(side="left", padx=5)

tk.Button(
    frame_botoes,
    text="Limpar",
    bg="#e67e22",
    fg="white",
    width=12,
    command=limpar_campos
).pack(side="left", padx=5)


root.mainloop()











