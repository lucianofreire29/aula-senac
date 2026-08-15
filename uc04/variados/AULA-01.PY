import os
import tkinter as tk


def main_window():
    janela = tk.Tk()
    janela.title("minha primeira GUI")
    janela.geometry("400x300")
    janela.resizable(False, False)
    janela.configure(bg="#120a8f")
    janela.option_add("*Font", "Californian 24")

    pg_title = tk.Label(janela, text="Olá mundo!!!!", bg="#120a8f")
    pg_title.pack(pady=20)

    # caminho absoluto da imagem
    pasta_atual = os.path.dirname(__file__)
    caminho_imagem = os.path.join(pasta_atual, "angelfoto.png")

    image = tk.PhotoImage(file=caminho_imagem)
    img_label = tk.Label(janela, image=image, bg="#120a8f")
    img_label.image = image
    img_label.pack(pady=10)

    janela.mainloop()


if __name__ == "__main__":
    main_window()











import tkinter as tk

def main_window():
    root = tk.Tk()
    root.title("Aula 02 - Tkinter")
    root.geometry("500x300")
    root.configure(bg="#000000")

    # Título
    title_pg = tk.Label(root,
                        text="Aula 02 - Tkinter",
                        fg="#ffffff", bg="#000000",
                        font=("Berlin Sans FB", 18))
    title_pg.pack(pady=(10, 5))

    # Label Nome
    name_lb = tk.Label(root,
                       text="Nome Completo",
                       fg="#ffffff", bg="#000000",
                       font=("Berlin Sans FB", 12),
                       anchor="w")
    name_lb.pack(pady=5, padx=10, fill="x")

    # Entry Nome
    var_name = tk.StringVar()
    name_entry = tk.Entry(root, textvariable=var_name,
                          font=("Berlin Sans FB", 12))
    name_entry.pack(padx=10, fill="x")

    # Label Descrição
    description_lb = tk.Label(root,
                              text="Descreva suas habilidades",
                              fg="#ffffff", bg="#000000",
                              font=("Berlin Sans FB", 12),
                              anchor="w")
    description_lb.pack(pady=5, padx=10, fill="x")

    # Text Habilidades
    description_text = tk.Text(root, height=5,
                               font=("Berlin Sans FB", 12))
    description_text.pack(padx=10, fill="x")

    # Evento do botão
    def event_button():
        nome_digitado = var_name.get()
        texto_digitado = description_text.get("1.0", tk.END)

        root.destroy()
        confirmation_window(nome_digitado, texto_digitado)

    # Botão
    button = tk.Button(root,
                       bg="#ffff00",
                       text="Enviar",
                       font=("Berlin Sans FB", 12, "bold"),
                       fg="#000000",
                       command=event_button)
    button.pack(pady=10)

    root.mainloop()


def confirmation_window(nome, texto):
    root = tk.Tk()
    root.title("Segunda Janela")
    root.geometry("500x300")
    root.configure(bg="#000000")

    # Título
    title_pg = tk.Label(root,
                        text="Segunda Janela - Tkinter",
                        fg="#ffffff", bg="#000000",
                        font=("Berlin Sans FB", 18))
    title_pg.pack(pady=(10, 5))

    # Mostrar Nome
    nome_lb = tk.Label(root,
                       text=f"Nome: {nome}",
                       fg="#ffffff", bg="#000000",
                       font=("Berlin Sans FB", 12))
    nome_lb.pack(pady=5)

    # Mostrar Habilidades
    texto_lb = tk.Label(root,
                        text="Habilidades:",
                        fg="#ffffff", bg="#000000",
                        font=("Berlin Sans FB", 12))
    texto_lb.pack()

    texto_mostrado = tk.Label(root,
                              text=texto,
                              fg="#ffffff", bg="#000000",
                              font=("Berlin Sans FB", 12),
                              wraplength=450,
                              justify="left")
    texto_mostrado.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_window()
