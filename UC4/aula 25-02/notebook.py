import tkinter as tk
from tkinter import ttk


# root = tk.Tk()
# root.geometry("500x300")
# root.title("exemplo notebook")




# notebook = ttk.Notebook(root)
# notebook.pack(fill="both", expand=True)

# frame_1 = ttk.Frame(notebook,width=500, height=280)
# frame_1.pack(fill="both",expand=True)


# frame_2 = ttk.Frame(notebook, width=500, height=280)
# frame_2.pack(fill="both",expand=True)




# notebook.add(frame_1, text="General Information")
# notebook.add(frame_2, text="profile")


# tk.Label(frame_1,text="label of the general information"). pack(pady=20)
# tk.Label(frame_2,text="edit profile"). pack(pady=20)



#  1 a janela principal deve ser divida em dois paineis ajustaveis:
# painel esquerdo area de navegação 
# painel direito area de conteudo



import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

root = tk.Tk()
root.geometry("700x500")
root.title("Programa de Anotações")


paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.pack(fill="both", expand=True)


frame_left = tk.Frame(paned, bg="#dcdcdc", width=200)

titulo_left = ttk.Label(frame_left, text="MENU de Navegações",
                        font=("Berlin Sans FB", 14))
titulo_left.pack(pady=(10, 20))

btn1 = ttk.Button(frame_left, text="Ir para Anotações")
btn1.pack(pady=5)

btn2 = ttk.Button(frame_left, text="Ir para Tarefas")
btn2.pack(pady=5)

btn3 = ttk.Button(frame_left, text="Ir para Configurações")
btn3.pack(pady=5)


frame_right = tk.Frame(paned)
paned.add(frame_left)
paned.add(frame_right)


notebook = ttk.Notebook(frame_right)
notebook.pack(fill="both", expand=True)


frame_1 = ttk.Frame(notebook)
notebook.add(frame_1, text="Anotações")

text_area = tk.Text(frame_1)
text_area.pack(fill="both", expand=True, padx=10, pady=10)


frame_2 = ttk.Frame(notebook)
notebook.add(frame_2, text="Tarefas")

lista_tarefas = tk.Listbox(frame_2)
lista_tarefas.pack(fill="both", expand=True, padx=10, pady=10)

lista_tarefas.insert(tk.END, "Estudar Python")
lista_tarefas.insert(tk.END, "Reunião às 14h")
lista_tarefas.insert(tk.END, "Enviar relatório")


frame_3 = ttk.Frame(notebook)
notebook.add(frame_3, text="Configurações")

def mudar_cor():
    cor = colorchooser.askcolor()[1]
    if cor:
        text_area.config(bg=cor)

def limpar_texto():
    text_area.delete("1.0", tk.END)

btn_cor = ttk.Button(frame_3, text="Alterar Cor de Fundo",
                    command=mudar_cor)
btn_cor.pack(pady=10)

btn_limpar = ttk.Button(frame_3, text="Limpar Anotações",
                        command=limpar_texto)
btn_limpar.pack(pady=10)


btn1.config(command=lambda: notebook.select(frame_1))
btn2.config(command=lambda: notebook.select(frame_2))
btn3.config(command=lambda: notebook.select(frame_3))




root.mainloop()