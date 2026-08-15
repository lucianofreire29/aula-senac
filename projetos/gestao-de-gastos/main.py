import tkinter as tk
from tkinter import ttk
from datetime import datetime

class Gestao:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestão Pessoal")
        self.master.geometry("800x600")
        self.master.configure(bg="#d9d9d9")
        self.master.option_add("*Font", "Calibri 18 bold")

        style = ttk.Style()
        style.configure("Top.TFrame", background="#8c52ff")
        style.configure("Form.TFrame", background="#d9d9d9")

        # FRAME SUPERIOR
        self.frame_top = ttk.Frame(master, style="Top.TFrame")
        self.frame_top.pack(fill="x", side="top")

        # função do menu
        def selecionar(opcao):
            botao.config(text=opcao + " ▼")

        # BOTÃO MENU
        botao = tk.Menubutton(
            self.frame_top,
            text="Gastos ▼",
            relief="flat",
            bg="#8c52ff",
            fg="#d9d9d9",
            font="Calibri 12 bold"
        )
        botao.grid(row=0, column=0, padx=10, pady=10)

        menu = tk.Menu(
            botao,
            tearoff=0,
            bg="#8c52ff",
            fg="#d9d9d9",
            font="Calibri 12 bold"
        )

        menu.add_command(label="Gastos", command=lambda: selecionar("Gastos"))
        menu.add_command(label="Receitas", command=lambda: selecionar("Receitas"))
        menu.add_command(label="Investimentos", command=lambda: selecionar("Investimentos"))

        botao.config(menu=menu)


        











        # FRAME FORMULÁRIO
        self.frame_form = ttk.Frame(master, style="Form.TFrame")
        self.frame_form.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = Gestao(root)
    root.mainloop()