import tkinter as tk


root = tk.Tk()
root.geometry ("400x300")

#frame superior
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x")

label = tk.Label(top_frame, text="area superior")
label.pack(pady=20)

# frame inferior

bottom_frame = tk.Frame(root, bg="lightgreen")
bottom_frame.pack(fill="both", expand=True)

btn = tk.Button(bottom_frame, text="botão no frame inferior")

btn.pack(pady=50)


root.mainloop()