import tkinter as tk
from datetime import datetime as dt

class Clock:
    def __init__(self, master):
        self.master = master
        self.master.title  ("clock")
        self.master.geometry  ("300x150")
        self.master.option_add  ("*Font", "Helvica 24 bold")
        self.master.configure ( bg="#222222")
        self.master.attributes("-topmost", True)

        self.texto_dinamico =tk.StringVar()
        self.Label_relogio = tk.Label(master, textvariable=self.texto_dinamico, fg="#00ff00",bg="#222222")
        self.Label_relogio.pack (pady=20)
        self.atualizar_relogio()


    def atualizar_relogio(self):
        dt_now = dt.now()
        str_format = dt_now.strftime("%H:%M:%S")
        self.texto_dinamico.set(str_format)


        self.master.after (1000,self.atualizar_relogio)




    # executar
if __name__ == "__main__":
    root = tk.Tk()
    app = Clock(root)
    root.mainloop()