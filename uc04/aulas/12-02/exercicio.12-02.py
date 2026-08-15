import tkinter as tk



# 1. Saudação Personalizada: Criar um Entry para nome, um Button 'Saudar' e um Label que exiba
# mensagem de boas-vindas personalizada.



# def main_window():
#     janela = tk.Tk()
#     janela.title('Boas-Vindas!!!!')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F5E1")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Seja bem vindo!",
#                         fg="#000000", bg="#04F5E1",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))



#     # Label Nome
#     name_lb = tk.Label(janela,
#                     text="Nome",
#                     fg="#000000", bg="#04F5E1",
#                     font=("Berlin Sans FB", 16),
#                     anchor="w")
#     name_lb.pack(pady=5, padx=10, fill="x")

#     # Entry Nome
#     var_name = tk.StringVar()
#     name_entry = tk.Entry(janela, textvariable=var_name,
#                         font=("Berlin Sans FB", 14))
#     name_entry.pack(padx=10, fill="x")

#     def event_button():
#         nome_digitado = var_name.get()
#         janela.destroy()
#         confirmation_window(nome_digitado)


#         # Botão
#     button = tk.Button(janela,
#                     bg="#0aca0a",
#                     text="Saudar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=10)

#     janela.mainloop()




# def confirmation_window(nome):
#     janela = tk.Tk()
#     janela.title("seja bem vindo!")
#     janela.geometry("500x300")
#     janela.configure(bg="#04F5E1")


#     # Título
#     title_pg = tk.Label(janela,
#                         text="seja muito bem vindo!!!!!!!!",
#                         fg="#000000", bg="#04F5E1",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))


#     # Mostrar Nome
#     nome_lb = tk.Label(janela,
#                     text=f"{nome}",
#                     fg="#000000", bg="#04F5E1",
#                     font=("Berlin Sans FB", 16))
#     nome_lb.pack(pady=5)




# 2. Calculadora de Soma Simples: Criar dois Entry para números, um Button 'Somar' e um Label
# exibindo o resultado.

# def main_window():
#     janela = tk.Tk()
#     janela.title('Calculadora')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Seja bem vindo!",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     #  Label Numero - 1
#     name_lb = tk.Label(janela,
#                     text="primeiro numero",
#                     fg="#000000", bg="#04F510",
#                     font=("Berlin Sans FB", 16),
#                     anchor="w")
#     name_lb.pack(pady=5, padx=10, fill="y")

#     # Entry Numero
#     var_numero1 = tk.IntVar()
#     numero1_entry = tk.Entry(janela, textvariable=var_numero1,
#                         font=("Berlin Sans FB", 14))
#     numero1_entry.pack(padx=10, fill="y")


#     #  Label Numero - 2
#     name_lb = tk.Label(janela,
#                     text="segundo numero",
#                     fg="#000000", bg="#04F510",
#                     font=("Berlin Sans FB", 16),
#                     anchor="w")
#     name_lb.pack(pady=5, padx=10, fill="y")

#     # Entry Numero
#     var_numero2 = tk.IntVar()
#     numero2_entry = tk.Entry(janela, textvariable=var_numero2,
#                         font=("Berlin Sans FB", 14))
#     numero2_entry.pack(padx=10, fill="y")


#     def event_button():
#         numero1 =var_numero1.get()
#         numero2 =var_numero2.get()
#         soma = numero1 +numero2
#         janela.destroy()
#         confirmation_window(soma)

# #   Botão
#     button = tk.Button(janela,
#                     bg="#f6fa06",
#                     text="somar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=10)

#     janela.mainloop()


# def confirmation_window(soma):
#     janela = tk.Tk()
#     janela.title("Resultado")
#     janela.geometry("500x300")
#     janela.configure(bg="#04F510")


#     # Título
#     title_pg = tk.Label(janela,
#                         text="RESULTADO DA SOMA",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     nome_lb = tk.Label(janela,
#                     text=f"{soma}",
#                     fg="#000000", bg="#04F510",
#                     font=("Berlin Sans FB", 16))
#     nome_lb.pack(pady=5)



# 3. Contador de Caracteres: Criar um Text para digitação, um Button 'Contar Caracteres' e um Label
# mostrando a quantidade total de caracteres.


# def main_window():
#     janela = tk.Tk()
#     janela.title('Contador de Caracteres')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Texto",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))


#     # Label Descrição
#     description_lb = tk.Label(janela,
#                             text="Digite um texto",
#                             fg="#000000", bg="#04F510",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
#     description_lb.pack(pady=5, padx=10, fill="x")

#     # Text Habilidades
#     description_text = tk.Text(janela, height=5,
#                             font=("Berlin Sans FB", 12))
#     description_text.pack(padx=10, fill="x")




#     # Evento do botão
#     def event_button():
#         texto = description_text.get("1.0", "end-1c")
#         quantidade = len(texto)
#         janela.destroy()
#         confirmation_window(texto, quantidade)

#     # Botão
#     button = tk.Button(janela,
#                     bg="#ffff00",
#                     text="Enviar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=10)

#     janela.mainloop()


# def confirmation_window(texto,quantidade):
#     janela = tk.Tk()
#     janela.title("quantidade de caracteres")
#     janela.geometry("500x300")
#     janela.configure(bg="#000000")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="quantidade de caracteres",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     # Mostrar quantidade de caracteres
#     nome_lb = tk.Label(janela,
#                     text=f"quantidade{quantidade}",
#                     fg="#000000", bg="#04F510",
#                     font=("Berlin Sans FB", 12))
#     nome_lb.pack(pady=5)




# 4. Verificador de Par ou Ímpar: Criar um Entry para número inteiro, um Button 'Verificar' e um Label
# exibindo se é par ou ímpar.

# def main_window():
#     janela = tk.Tk()
#     janela.title('PAR ou IMPAR')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Verificação Par ou Ímpar",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     # Label Número
#     name_lb = tk.Label(janela,
#                     text="Digite um Número",
#                     fg="#000000", bg="#04F510",
#                     font=("Berlin Sans FB", 16),
#                     anchor="w")
#     name_lb.pack(pady=5, padx=10, fill="x")

#     # Entry Número
#     var_numero = tk.StringVar()
#     numero_entry = tk.Entry(janela,
#                             textvariable=var_numero,
#                             font=("Berlin Sans FB", 14))
#     numero_entry.pack(padx=10, fill="x")

#     # Função do botão (AGORA dentro da main_window)
#     def event_button():
#         numero = int(var_numero.get())

#         if numero % 2 == 0:
#             resultado = "Par"
#         else:
#             resultado = "Ímpar"

#         janela.destroy()
#         confirmation_window(numero, resultado)

#     # Botão
#     button = tk.Button(janela,
#                     bg="#f6fa06",
#                     text="Verificar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=20)

#     janela.mainloop()


# def confirmation_window(numero, resultado):
#     janela = tk.Tk()
#     janela.title("Resultado")
#     janela.geometry("500x300")
#     janela.configure(bg="#04F510")

#     title_pg = tk.Label(janela,
#                         text="RESULTADO",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     resultado_lb = tk.Label(janela,
#                             text=f"O número {numero} é {resultado}",
#                             fg="#000000", bg="#04F510",
#                             font=("Berlin Sans FB", 16))
#     resultado_lb.pack(pady=20)

#     janela.mainloop()












# 5. Inversor de Texto: Criar um Entry para texto, um Button 'Inverter' e um Label exibindo o texto
# invertido.


# def main_window():
#     janela = tk.Tk()
#     janela.title('texto invertido')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Texto Invertido",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))


#     # Label Descrição
#     description_lb = tk.Label(janela,
#                             text="Digite um texto",
#                             fg="#000000", bg="#04F510",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
#     description_lb.pack(pady=5, padx=10, fill="x")

#     # Text Habilidades
#     description_text = tk.Text(janela, height=5,
#                             font=("Berlin Sans FB", 12))
#     description_text.pack(padx=10, fill="x")



#     def event_button():
#         texto=description_text.get("1.0", "end-1c")
#         invertido = texto[::-1]


#         janela.destroy()
#         confirmation_window(invertido)

#     # Botão
#     button = tk.Button(janela,
#                     bg="#f6fa06",
#                     text="inverter texto",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=20)

#     janela.mainloop()

# def confirmation_window(invertido):
#     janela = tk.Tk()
#     janela.title("Texto invertido")
#     janela.geometry("500x300")
#     janela.configure(bg="#04F510")

#     title_pg = tk.Label(janela,
#                         text="TEXTO INVERTIDO",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     resultado_lb = tk.Label(janela,
#                             text=f"O texto invertido: {invertido}",
#                             fg="#000000", bg="#04F510",
#                             font=("Berlin Sans FB", 16))
#     resultado_lb.pack(pady=20)

#     janela.mainloop()




# 6. Simulador de Login Simples: Criar Entry para usuário e senha, Button 'Entrar' e Label exibindo
# acesso permitido ou negado.


# def main_window():
#     janela = tk.Tk()
#     janela.title('Login')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Login",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 20))

#     # Label login
#     login_lb = tk.Label(janela,
#                         text="Login",
#                         fg="#ffffff", bg="#000000",
#                         font=("Berlin Sans FB", 12))
#     login_lb.pack(pady=5)

#     # Entry login
#     var_login = tk.StringVar()
#     login_entry = tk.Entry(janela,
#                         textvariable=var_login,
#                         font=("Berlin Sans FB", 12),
#                         justify="center")
#     login_entry.pack(padx=10)

#     # Label senha
#     senha_lb = tk.Label(janela,
#                         text="Senha",
#                         fg="#ffffff", bg="#000000",
#                         font=("Berlin Sans FB", 12))
#     senha_lb.pack(pady=5)

#     # Entry senha
#     var_senha = tk.StringVar()
#     senha_entry = tk.Entry(janela,
#                         textvariable=var_senha,
#                         font=("Berlin Sans FB", 12),
#                         justify="center",
#                         show="*")  #esconde o caractere
#     senha_entry.pack(padx=10)

#     # Label resultado
#     resultado_lb = tk.Label(janela,
#                             text="",
#                             fg="#ffffff",
#                             bg="#04F510",
#                             font=("Berlin Sans FB", 14))
#     resultado_lb.pack(pady=20)

#     def event_button():
#         confirmar_login = login_entry.get()
#         confirmar_senha = senha_entry.get()

#         if confirmar_login == "adm" and confirmar_senha == "9921":
#             resultado_lb.config(text="Acesso Permitido ✅", fg="green")
#         else:
#             resultado_lb.config(text="Acesso Negado ❌", fg="red")

#     # Botão
#     button = tk.Button(janela,
#                     bg="#f6fa06",
#                     text="Login",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=20)

#     janela.mainloop()


# 7. Mini Bloco de Notas: Criar um Text grande para anotações e um Button 'Limpar Texto' que
# apague todo o conteúdo.


# def main_window():
#     janela = tk.Tk()
#     janela.title('Bloco de Notas')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Bloco De Notas",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 20))

#     # Label Descrição
#     description_lb = tk.Label(janela,
#                             text="Digite seu texto",
#                             fg="#ffffff", bg="#000000",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
#     description_lb.pack(pady=5, padx=10, fill="y")

#     # Text Habilidades
#     description_text = tk.Text(janela, height=18,
#                             font=("Berlin Sans FB", 12))
#     description_text.pack(padx=10, fill="x")


#     def event_button():
#         description_text.delete("1.0", "end")

#     # Botão
#     button = tk.Button(janela,
#                     bg="#f6fa06",
#                     text="apagar Texto",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=20)

#     janela.mainloop()







# 8. Contador de Palavras: Criar um Text para digitação, Button 'Contar Palavras' e Label exibindo
# total de palavras.


# def main_window():
#     janela = tk.Tk()
#     janela.title('Contador de Caracteres')
#     janela.geometry('500x500')
#     janela.configure(bg="#04F510")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Texto",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))


#     # Label Descrição
#     description_lb = tk.Label(janela,
#                             text="Digite um texto",
#                             fg="#000000", bg="#04F510",
#                             font=("Berlin Sans FB", 12),
#                             anchor="w")
#     description_lb.pack(pady=5, padx=10, fill="x")

#     # Text Habilidades
#     description_text = tk.Text(janela, height=5,
#                             font=("Berlin Sans FB", 12))
#     description_text.pack(padx=10, fill="x")




#     # Evento do botão
#     def event_button():
#         texto = description_text.get("1.0", "end-1c")
#         quantidade = len(texto)
#         janela.destroy()
#         confirmation_window(texto, quantidade)

#     # Botão
#     button = tk.Button(janela,
#                     bg="#ffff00",
#                     text="Enviar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=10)

#     janela.mainloop()


# def confirmation_window(texto,quantidade):
#     janela = tk.Tk()
#     janela.title("quantidade de caracteres")
#     janela.geometry("500x300")
#     janela.configure(bg="#000000")

#     # Título
#     title_pg = tk.Label(janela,
#                         text="quantidade de caracteres",
#                         fg="#000000", bg="#04F510",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     # Mostrar quantidade de caracteres
#     nome_lb = tk.Label(janela,
#                     text=f"quantidade{quantidade}",
#                     fg="#000000", bg="#04F510",
#                     font=("Berlin Sans FB", 12))
#     nome_lb.pack(pady=5)











# 9. Simulador de Depósito Bancário: Criar Label com saldo inicial 0, Entry para valor e Button
# 'Depositar' que atualize o saldo.



# def main_window():
#     janela = tk.Tk()
#     janela.title('Deposito Bancário')
#     janela.geometry('500x500')
#     janela.configure(bg="#F1F504")

#     saldo = 0.00

#     # Título
#     title_pg = tk.Label(janela,
#                         text="Deposito bancário",
#                         fg="#000000", bg="#F1F504",
#                         font=("Berlin Sans FB", 18))
#     title_pg.pack(pady=(10, 5))

#     # saldo
#     saldo_pg = tk.Label(janela,
#                         text="Saldo",
#                         fg="#000000", bg="#F1F504",
#                         font=("Berlin Sans FB", 16))
#     saldo_pg.pack(pady=(10, 5))

#         # valor
#     valor_pg = tk.Label(janela,
#                         text=f"{saldo}",
#                         fg="#000000", bg="#F1F504",
#                         font=("Berlin Sans FB", 16))
#     valor_pg.pack(pady=(10, 5))


#     # Entry saldo
#     var_saldo = tk.StringVar()
#     saldo_entry = tk.Entry(janela,
#                         textvariable=var_saldo,
#                         font=("Berlin Sans FB", 12),
#                         justify="center")
#     saldo_entry.pack(padx=10)


#     def event_button():
#         nonlocal saldo
#         try:
#             valor = float(saldo_entry.get())
#             saldo += valor
#             valor_pg.config(text=f"R$ {saldo:.2f}")
#             saldo_entry.delete(0, tk.END)
#         except ValueError:
#             valor_pg.config(text="Valor inválido")

#     # Botão
#     button = tk.Button(janela,
#                     bg="#06fa57",
#                     text="depositar",
#                     font=("Berlin Sans FB", 12, "bold"),
#                     fg="#000000",
#                     command=event_button)
#     button.pack(pady=20)





#     janela.mainloop()








# 10. Gerador de Relatório Simples: Criar Entry para Nome, Idade e Curso, Button 'Gerar Relatório' e
# um Text exibindo relatório formatado.


import tkinter as tk

def main_window():
    janela = tk.Tk()
    janela.title('relatório')
    janela.geometry('500x500')
    janela.configure(bg="#049DF5")

    # Título
    title_pg = tk.Label(
        janela,
        text="relatório",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 18)
    )
    title_pg.pack(pady=(10, 5))

    # nome
    nome_pg = tk.Label(
        janela,
        text="Nome",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    nome_pg.pack(pady=(10, 5))

    var_nome = tk.StringVar()
    nome_entry = tk.Entry(
        janela,
        textvariable=var_nome,
        font=("Berlin Sans FB", 12),
        justify="center"
    )
    nome_entry.pack(padx=10)

    # idade
    idade_pg = tk.Label(
        janela,
        text="Idade",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    idade_pg.pack(pady=(10, 5))

    var_idade = tk.StringVar()
    idade_entry = tk.Entry(
        janela,
        textvariable=var_idade,
        font=("Berlin Sans FB", 12),
        justify="center"
    )
    idade_entry.pack(padx=10)

    # curso
    curso_pg = tk.Label(
        janela,
        text="Curso",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    curso_pg.pack(pady=(10, 5))

    var_curso = tk.StringVar()
    curso_entry = tk.Entry(
        janela,
        textvariable=var_curso,
        font=("Berlin Sans FB", 12),
        justify="center"
    )
    curso_entry.pack(padx=10)

    def event_button():
        rel_nome = var_nome.get()
        rel_idade = var_idade.get()
        rel_curso = var_curso.get()
        
        confirmation_window(janela, rel_nome, rel_idade, rel_curso)
        
    # Botão
    button = tk.Button(
        janela,
        bg="#06fafa",
        text="Gerar relatório",
        font=("Berlin Sans FB", 12, "bold"),
        fg="#000000",
        command=event_button
    )
    button.pack(pady=20)

    
    janela.mainloop()
    

def confirmation_window(parent, nome, idade, curso):
    janela = tk.Toplevel(parent)  
    janela.title("Relatório")
    janela.geometry("500x300")
    janela.configure(bg="#049DF5")
    
    # Título
    title_pg = tk.Label(
        janela,
        text="Relatório",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 18)
    )
    title_pg.pack(pady=(10, 5))

    # Mostrar dados
    nome_lb = tk.Label(
        janela,
        text=f"{nome} | {idade} anos | {curso}",
        fg="#000000", bg="#049DF5",
        font=("Berlin Sans FB", 16)
    )
    nome_lb.pack(pady=5)


main_window()














