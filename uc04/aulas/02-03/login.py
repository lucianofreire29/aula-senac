"""CLASSE REPRESENTATIVA DE UMA TELA DE LOGIN"""

import tkinter as tk
from tkinter import messagebox as mg
import os


class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de login")
        self.master.geometry("280x280")
        self.master.option_add("*Font", "helvetica 12")
        self.master.configure(bg="#444444")



        # ================= IMAGE =================
        try:
            caminho_imagem = os.path.join(os.path.dirname(__file__), "login.png")
            self.image = tk.PhotoImage(file=caminho_imagem)
            self.image = self.image.subsample(3)

            self.label_image = tk.Label(master, image=self.image, bg="#444444")
            self.label_image.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        except Exception as e:
            print("Imagem não encontrada:", e)

        # ================= FORM LOGIN =================
        self.label_user = tk.Label(master, text="Usuário", fg="#ffffff", bg="#444444")
        self.label_user.grid(row=1, column=0, pady=5, padx=5)

        self.input_user = tk.Entry(master)
        self.input_user.grid(row=1, column=1, pady=5, padx=5)

        self.label_password = tk.Label(master, text="Senha", fg="#ffffff", bg="#444444")
        self.label_password.grid(row=2, column=0, pady=5, padx=5)

        self.input_password = tk.Entry(master, show="*")
        self.input_password.grid(row=2, column=1, pady=5, padx=5)

        self.check_login = tk.IntVar()
        self.check_button_login = tk.Checkbutton(
            master,
            text="Remember me",
            variable=self.check_login,
            bg="#444444",
            fg="#ffffff",
            activebackground="#444444",
            activeforeground="#ffffff",
            selectcolor="#444444"
        )
        self.check_button_login.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky="w")

        # ================= BUTTON =================
        self.btn_login = tk.Button(master, text="Login", command=self.validation_login)
        self.btn_login.grid(row=4, column=0, columnspan=2, pady=10)

        # 🔥 ENTER PARA LOGAR
        self.master.bind("<Return>", lambda event: self.validation_login())

    # ================= FUNÇÃO LOGIN =================
    def validation_login(self):
        user = self.input_user.get()
        password = self.input_password.get()

        if user == "admin" and password == "admin":
            mg.showinfo("Login bem sucedido", "Bem-vindo, admin")
        else:
            mg.showerror("Erro de login", "Usuário ou senha incorretos")

    # ================= CENTRALIZAR =================


# ================= MAIN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()