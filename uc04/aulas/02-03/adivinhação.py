import tkinter as tk
import random as rd



class JogoIniciar:
    def __init__(self,master):
        self.master = master
        self.master.title ("jogo da adivinhação")
        self.master.geometry("800x600")
        self.master.option_add  ("*Font", "Helvica 24 bold")
        self.master.configure ( bg="#ffffff")

        # titulo 
        self.master_titulo =tk.Label(master, text="⭐Jogo da advinhação⭐",font="Helvica 24 bold")
        self.master_titulo.pack(padx=10,pady=10)


        # frame
        self.master_frame = tk.Frame(master,bg="#b1f7f3")
        self.master_frame.pack(fill="both", expand=True)



        # subtitulo
        self.master_subtitulo =tk.Label(self.master_frame, text="regras do jogo",font="Helvica 20 bold", bg="#b1f7f3")
        self.master_subtitulo.pack(padx=10,pady=(10,5))

        # regras
        self.master_regra =tk.Label(self.master_frame, text="Descubra o número secreto entre 1 e 100 em até 3 tentativas." \
        " \nNo início, você recebe uma dica para se orientar. " \
        "\n A cada erro, novas dicas matemáticas serão reveladas para ajudar. " \
        "\nAcerte dentro das três tentativas para vencer " \
        "— caso contrário," \
        "\n o número será revelado. Boa sorte! "
        ,font="Helvica 18 bold",bg="#b1f7f3")
        self.master_regra.pack(padx=10,pady=(10))


        # button
        self.master_button_iniciar=tk.Button(self.master_frame, text="iniciar",bg="#0fbb0a",command=self.iniciar_jogo)
        self.master_button_iniciar.pack(pady=50)

        # iniciar jogo
    def iniciar_jogo(self):
        self.master_frame.destroy()

        self.frame_jogo = tk.Frame(self.master, bg="#ffe4b5")
        self.frame_jogo.pack(fill="both", expand=True)

        tk.Label(
            self.frame_jogo,
            text="🎮 Jogo iniciado!",
            font="Helvetica 24 bold",
            bg="#ffe4b5"
        ).pack(pady=50)



    def numero_aleatorio():
        random_num = random_num.randint(0, 100)






















            # executar
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoIniciar(root)
    root.mainloop()