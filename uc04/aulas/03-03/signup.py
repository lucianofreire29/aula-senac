import tkinter as tk
from tkinter import messagebox as mg
from datetime import datetime as dt

'''
from tkinter import ttk

ttk - modulo criado com base no tkinter, porem trazendo mais possibilidades visuais

ttk.Label()
ttk.Entry()
ttk.Button()


'''

def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    genero = entry_genero.get()
    interesses = []


    if chk_python_var.get():
        interesses.append("Phyton")
    if chk_java_var.get():
        interesses.append("Java")
    if chk_javascript_var.get():
        interesses.append("JavaScript")

    comentarios = txt_comentarios.get("1.0", tk.END).strip()
    cidade = listbox_cidades.get(tk.ACTIVE)


    resumo =f'''
nome:{nome}
email: {email}
genero:{genero}
interesses:{", ".join(interesses)}
cidade{cidade}
comentarios:{comentarios}

Cadastrado em {dt.today().strftime("%d/%m/%y- %H:%M:%S")}
    '''

    mg.showinfo("Cadastro Salvo", resumo)



# janela principal

root = tk.Tk()
root.title("tela de cadastro")
root.geometry("500x340")
root.configure(bg="#35567C")
# MENU BAR

menubar = tk.Menu(root)
root.configure(menu=menubar)

menu_arquivo = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="salvar", command=salvar)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="sair", command=root.quit)

# FRAME principal
frame_form = tk.Frame(root, padx=10, pady=10,bg="#35567C")
frame_form.pack()


# entry nome
tk.Label(frame_form, text="Nome:",bg="#35567C").grid(row=0,column=0, sticky="e")
entry_nome = tk.Entry(frame_form, width= 30)
entry_nome.grid(row=0,column=1)

# entry email

tk.Label(frame_form, text="Email:",bg="#35567C").grid(row=1,column=0, sticky="e",pady=5)
entry_email = tk.Entry(frame_form, width= 30)
entry_email.grid(row=1,column=1,pady=5)

# FRAME principal
frame_form_1 = tk.Frame(root, padx=10, pady=10,bg="#35567C")
frame_form_1.pack()

# frame genero

tk.Label(frame_form_1, text="genero:", bg="#35567C").grid(row=2,column=0,sticky="e")
entry_genero = tk.StringVar(value="N/A")
tk.Radiobutton(frame_form_1,text="Masculino", 
            variable=entry_genero,
            value="Masculino", bg="#35567C",activebackground="#355678").grid(row=2, column=1,sticky="e")

tk.Radiobutton(frame_form_1,text="Feminino", 
            variable=entry_genero,
            value="Feminino", bg="#35567C",activebackground="#355678").grid(row=2, column=2,sticky="w")

tk.Label(frame_form_1, text="interesses:", bg="#35567C").grid(row=3,column=0,sticky="e")

chk_java_var = tk.BooleanVar()
chk_python_var = tk.BooleanVar()
chk_javascript_var = tk.BooleanVar()

tk.Checkbutton(frame_form_1, text="java", variable=chk_java_var, bg="#35567C",activebackground="#355678").grid(row=3,column=1)
tk.Checkbutton(frame_form_1, text="python", variable=chk_python_var, bg="#35567C",activebackground="#355678").grid(row=3,column=2)
tk.Checkbutton(frame_form_1, text="javascript", variable=chk_javascript_var, bg="#35567C",activebackground="#355678").grid(row=3,column=3)


tk.Label(frame_form_1, text="Cidade:", bg="#35567C",activeforeground="#355678").grid(row=4,column=0,sticky="e",pady=5)
listbox_cidades = tk.Listbox(frame_form_1,height=5,width=30,justify="center")
cidades = ["Fortaleza","Sao Paulo", "Rio de Janeiro", "Belo horizonte", "Curitiba" ]

for cidade in cidades:
    listbox_cidades.insert(tk.END, cidade)
listbox_cidades.grid(row=4,column=1,columnspan=3,sticky="nsew")

# texto (comentario)

tk.Label(frame_form_1, text="Comentários: ", bg="#35567C").grid(row=5,column=0,sticky="e")
txt_comentarios = tk.Text(frame_form_1,width=40,height=5)
txt_comentarios.grid(row=5,column=1,columnspan=3,pady=2)

# botão salvar
tk.Button(frame_form_1,text="Salvar",border=2,bg="#0583f8",borderwidth=4,activebackground="#0583f8",command=salvar).grid(row=6,column=2,pady=5)









root.mainloop()