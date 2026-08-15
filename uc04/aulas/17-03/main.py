import customtkinter as ctk



class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.geometry("400x300")
        self.title("janela ctk - 17/03")
        self.label = ctk.CTkLabel(self,
                                text="pagina inicial",
                                fg_color="transparent",
                                text_color=("black","white"),
                                font=("Berlin Sans FB",16))
        self.label.pack(padx=10, pady=10)


        self.button = ctk.CTkButton(self,text="clique-me!", fg_color="crimson", hover_color="dark red")
        # demais componentes serão adicionandos no construtor.
        self.button.pack(padx=10,pady=10)



    #metodos serão adicionados para criar componentes ligados ao frame



app = MainWindow()
app.mainloop()