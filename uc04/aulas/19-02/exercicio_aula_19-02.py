import tkinter as tk
from tkinter import messagebox

# funções salvar usuario 

def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning("atenção", "preencha todos os campos!")
        return
    
    messagebox.showinfo("Sucesso", "cadastro realizado com sucesso!")

    limpar()

# função limpar

def limpar():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)


# janela principal

root = tk.Tk()
root.title("mini sistema de cadastro")
root.geometry("700x400")




# frame lateral
frame_lateral = tk.Frame(root, bg="#2c3e50", width=150)
frame_lateral.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_lateral, text="MENU", bg="#2c3e50", fg="white",
                        font=("arial", 14, "bold")).pack(pady=20)


tk.Button(frame_lateral, text="cadastro").pack(fill=tk.X, padx=10,pady=5)
tk.Button(frame_lateral, text="relatórios").pack(fill=tk.X, padx=10,pady=5)
tk.Button(frame_lateral, text="configurações").pack(fill=tk.X, padx=10,pady=5)


# frame principal

frame_principal = tk.Frame(root, bg="#ecf0f1")
frame_principal.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

#----------frame titulo -----------

frame_titulo = tk.Frame(frame_principal, bg="#bdc3c7", height=60)
frame_titulo.pack(fill=tk.X)

tk.Label(frame_titulo, text="Cadastro de Usuário", bg='#bdc3c7',
                        font=("Arial", 16, "bold")).pack(pady=15)

# ------frame formulario ---------

frame_form =tk.Frame(frame_principal, bg="#ecf0f1")
frame_form.pack(padx=30)




root.mainloop()

