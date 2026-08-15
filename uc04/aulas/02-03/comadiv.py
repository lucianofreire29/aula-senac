import tkinter as tk
import random
import time


class JogoIniciar:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Adivinhação")
        self.master.geometry("800x650")
        self.master.configure(bg="#ffffff")

        self.tela_inicial()

    # TELA INICIAL

    def tela_inicial(self):
        self.frame_inicio = tk.Frame(self, bg="#b1f7f3")
        self.frame_inicio.pack(fill="both", expand=True)

        tk.Label(
            self.frame_inicio,
            text="⭐ Jogo da Adivinhação ⭐",
            font="Helvetica 26 bold",
            bg="#b1f7f3"
        ).pack(pady=20)

        tk.Label(
            self.frame_inicio,
            text="Descubra o número secreto entre 1 e 100 em até 3 tentativas.\n"
                "Você começa com um palpite leve.\n"
                "A cada erro, recebe um novo palpite estratégico.\n"
                "Também receberá dica de temperatura (quente ou frio).",
            font="Helvetica 16",
            bg="#b1f7f3"
        ).pack(pady=20)

        tk.Button(
            self.frame_inicio,
            text="Iniciar",
            font="Helvetica 18 bold",
            bg="#0fbb0a",
            command=self.iniciar_jogo
        ).pack(pady=30)

    # INICIAR JOGO

    def iniciar_jogo(self):
        self.frame_inicio.destroy()

        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 3
        self.palpites_usados = set()
        self.numeros_tentados = set()
        self.dicas_usadas = 0
        self.inicio_tempo = time.time()
        self.jogo_ativo = True

        self.frame_jogo = tk.Frame(self.master, bg="#f0f8ff")
        self.frame_jogo.pack(fill="both", expand=True)

        tk.Label(
            self.frame_jogo,
            text="Digite um número entre 1 e 100",
            font="Helvetica 20 bold",
            bg="#f0f8ff"
        ).pack(pady=10)

        # CRONÔMETRO
        self.label_tempo = tk.Label(
            self.frame_jogo,
            text="⏱ Tempo: 0 s",
            font="Helvetica 16 bold",
            bg="#f0f8ff"
        )
        self.label_tempo.pack()

        self.atualizar_cronometro()

        self.entry = tk.Entry(self.frame_jogo, font="Helvetica 20")
        self.entry.pack(pady=10)

        tk.Button(
            self.frame_jogo,
            text="Confirmar",
            font="Helvetica 18",
            command=self.verificar_palpite
        ).pack(pady=10)

        self.label_resultado = tk.Label(
            self.frame_jogo,
            text="",
            font="Helvetica 18 bold",
            bg="#f0f8ff"
        )
        self.label_resultado.pack(pady=10)

        self.label_tentativas = tk.Label(
            self.frame_jogo,
            text="Tentativas restantes: 3",
            font="Helvetica 16",
            bg="#f0f8ff"
        )
        self.label_tentativas.pack(pady=5)

        self.label_palpites = tk.Label(
            self.frame_jogo,
            text="Palpites:\n",
            font="Helvetica 14",
            justify="left",
            bg="#f0f8ff"
        )
        self.label_palpites.pack(pady=10)

        tk.Button(
            self.frame_jogo,
            text="DICA",
            font="Helvetica 18 bold",
            bg="#0fbb0a",
            command=self.usar_dica
        ).pack(pady=5)

        tk.Button(
            self.frame_jogo,
            text="Reiniciar",
            font="Helvetica 14",
            bg="#ffcc00",
            command=self.reiniciar_jogo
        ).pack(pady=10)

    # CRONÔMETRO

    def atualizar_cronometro(self):
        if self.jogo_ativo:
            tempo_atual = int(time.time() - self.inicio_tempo)
            self.label_tempo.config(text=f"⏱ Tempo: {tempo_atual} s")
            self.master.after(1000, self.atualizar_cronometro)

    # TEMPERATURA

    def atualizar_temperatura(self, diferenca):
        if diferenca <= 5:
            cor = "#ff4d4d"
            texto = "🔥 Muito quente!"
        elif diferenca <= 15:
            cor = "#ff944d"
            texto = "🔥 Quente!"
        elif diferenca <= 30:
            cor = "#66b3ff"
            texto = "❄ Morno..."
        else:
            cor = "#3399ff"
            texto = "❄ Frio!"

        self.frame_jogo.configure(bg=cor)
        self.label_resultado.configure(bg=cor, text=texto)
        self.label_tentativas.configure(bg=cor)
        self.label_palpites.configure(bg=cor)
        self.label_tempo.configure(bg=cor)

    # GERAR PALPITE (dica)

    def gerar_palpite(self, tipo):
        n = self.numero_secreto

        if tipo == "leve":
            dica = "• O número está na metade inferior." if n <= 50 else "• O número está na metade superior."
        elif tipo == "medio":
            inicio = (n // 10) * 10
            fim = inicio + 9
            dica = f"• O número está entre {inicio} e {fim}."
        else:
            dica = "• O número é par." if n % 2 == 0 else "• O número é ímpar."

        if dica not in self.palpites_usados:
            self.palpites_usados.add(dica)
            atual = self.label_palpites.cget("text")
            self.label_palpites.config(text=atual + dica + "\n")

    # BOTÃO DICA

    def usar_dica(self):
        if not self.jogo_ativo:
            return

        if self.dicas_usadas == 0:
            self.gerar_palpite("leve")
        elif self.dicas_usadas == 1:
            self.gerar_palpite("medio")
        elif self.dicas_usadas == 2:
            self.gerar_palpite("forte")
        else:
            self.label_resultado.config(text="Você já usou todas as dicas!!!!!!")
            return

        self.dicas_usadas += 1

    # VERIFICAR PALPITE

    def verificar_palpite(self):
        if not self.jogo_ativo:
            return

        try:
            palpite = int(self.entry.get())
        except ValueError:
            self.label_resultado.config(text="Digite um número válido!")
            return

        # impede número repetido
        if palpite in self.numeros_tentados:
            self.label_resultado.config(
                text="⚠️ Você já tentou esse número!"
            )
            self.entry.delete(0, tk.END)
            return

        self.numeros_tentados.add(palpite)

        diferenca = abs(self.numero_secreto - palpite)

        if palpite == self.numero_secreto:
            self.jogo_ativo = False
            tempo_final = int(time.time() - self.inicio_tempo)

            cor_vitoria = "#90ee90"
            self.frame_jogo.configure(bg=cor_vitoria)

            self.label_resultado.config(
                text=f"🎉 Você acertou!\nTempo: {tempo_final} segundos",
                bg=cor_vitoria
            )

            self.label_tentativas.configure(bg=cor_vitoria)
            self.label_palpites.configure(bg=cor_vitoria)
            self.label_tempo.configure(bg=cor_vitoria)
            return

        self.tentativas -= 1
        self.label_tentativas.config(
            text=f"Tentativas restantes: {self.tentativas}"
        )

        self.atualizar_temperatura(diferenca)

        if self.tentativas == 0:
            self.jogo_ativo = False
            tempo_final = int(time.time() - self.inicio_tempo)
            self.label_resultado.config(
                text=f"💀 Fim de jogo!\nO número era {self.numero_secreto}\n"
                    f"Tempo: {tempo_final} segundos"
            )

        self.entry.delete(0, tk.END)

    # REINICIAR

    def reiniciar_jogo(self):
        self.frame_jogo.destroy()
        self.iniciar_jogo()


# EXECUTAR
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoIniciar(root)
    root.mainloop()