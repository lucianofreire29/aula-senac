import tkinter as tk
from datetime import datetime as dt
from tkinter import messagebox


def verificar_checkbutton():
    estado = var_check.get()

    if estado == 1:
        messagebox.showinfo("selecionado", "você selecionou o item!")
    else:
        messagebox.showinfo("não selecionado", "você não selecionou o item!")


def mostrar_opcao_radio():
    messagebox.showinfo("Opção selecionada", f"selecionado:{var_radio.get()}")














root = tk.Tk()
root.title("revisão widgets")
root.geometry("700x400")

# label
date_now = dt.now()
dias_semana = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
]

label_data = tk.Label(
    root,
    text=f"{dias_semana[date_now.weekday()]} - {dt.strftime(date_now, '%d/%m/%Y')}",
    font=("Caprasimo", 16),
    fg="green"
)
label_data.pack(fill="both", pady=(20, 5))

# frame
frame = tk.Frame(root, bg="#333333", padx=10, pady=10, width=500, height=100)
frame.pack(pady=20)
frame.pack_propagate(False)

# variável do checkbutton (ANTES de usar)
var_check = tk.IntVar()

# botão dentro do frame
btn_frame = tk.Button(
    frame,
    text="botão do frame",
    command=verificar_checkbutton
)
btn_frame.pack(pady=5)

# checkbutton
checkbutton = tk.Checkbutton(
    frame,
    text="opção",
    variable=var_check,
    bg="#75701b"
)
checkbutton.pack()

# frame 2

frame2 = tk.Frame(root, bg="#555555", padx=10, pady=10, width=500, height=120)
frame2.pack_propagate(False)
frame2.pack(pady=20)


#radiobutton dentro do frame2
var_radio = tk.StringVar(value="opção 1")
radio1 = tk.Radiobutton(frame2, text="opção 1", variable=var_radio,value="opção 1", bg="#555555")
radio2 = tk.Radiobutton(frame2, text="opção 2", variable=var_radio,value="opção 2", bg="#555555")
radio1.pack()
radio2.pack()



# mostrar opção selecionada

btn_radio = tk.Button(
    frame2,
    text="mostrar oção selecionada",
    command=mostrar_opcao_radio
)
btn_radio.pack(pady=10)


root.mainloop()
