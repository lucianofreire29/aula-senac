''' exemplo de uso de treeview'''
import tkinter as tk
from tkinter import ttk

ICON_CITY ="./UC4/aula 06-03/assets/city.png"
ICON_FEMALE = "./UC4/aula 06-03/assets/female.png"
ICON_MALE = "./UC4/aula 06-03/assets/male.png"

root =tk.Tk()
root.title("exemplo treeview 🌲")
root.geometry("500x400")
root.state("zoomed") #abrir janela maximizada

frame = tk.Frame(root)

treeview = ttk.Treeview(frame, columns=("salary", "bonus"))


#adicionando texto do cabeçalho
treeview.heading ("#0", text="employee")
treeview.heading ("salary", text="salary")
treeview.heading ("bonus", text="bonus")


# carregar icones
icon_cidade = tk.PhotoImage(file=ICON_CITY)
icon_female = tk.PhotoImage(file=ICON_FEMALE)
icon_male = tk.PhotoImage(file=ICON_MALE)



# ADICIONANDO ITENS AO treeview

level1 = treeview.insert("",tk.END,text="san jose",image=icon_cidade)
treeview.insert(level1,tk.END,text="John Doe",values=(f"${100000: ,}",f"${8000: ,}"),image=icon_male)
treeview.insert(level1,tk.END,text="Jane Doe",values=(f"${120000: ,}",f"${9000: ,}"), image=icon_female)



# adicionar um scrolbar

v_scrollbar =ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)


treeview.pack(side=tk.LEFT,fill="both",expand=True)
v_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

frame.pack(padx=10,pady=10,fill="both", expand=True)






root.mainloop()