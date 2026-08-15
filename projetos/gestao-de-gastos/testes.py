import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

def selecionar(opcao):
    botao.config(text=opcao + " ▼")

# botão principal
botao = tk.Menubutton(root, text="Gastos ▼", relief="flat")
botao.pack(padx=20, pady=20)

menu = tk.Menu(botao, tearoff=0)

menu.add_command(label="Gastos", command=lambda: selecionar("Gastos"))
menu.add_command(label="Receitas", command=lambda: selecionar("Receitas"))
menu.add_command(label="Investimentos", command=lambda: selecionar("Investimentos"))

botao.config(menu=menu)

root.mainloop()