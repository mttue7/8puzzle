import tkinter as tk
from tkinter import font
from main import JogoLogica

class Jogo8PuzzleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do 8-Puzzle")
        self.geometry("350x350")
        self.config(bg="lightblue")

        self.front = JogoLogica()

        self.resizable(False, False)

        self.custom_font = font.Font(family="Helvetica", size=16, weight="bold")

        self.label_game = tk.Label(self, text="8 PUZZLE GAME", font=self.custom_font, bg="lightblue")
        self.label_game.grid(row=0, column=0, columnspan=3, pady=8)

        self.label_tentativas = tk.Label(self, text=f"Tentativas: {self.front.contador_tentativas}", font=self.custom_font, bg="lightblue")
        self.label_tentativas.grid(row=4, column=0, columnspan=3, pady=10)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i+1, weight=1)

        self.criar_botões()

    def criar_botões(self):
        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self, text=self.front.matriz[i, j], width=5, height=2, font=self.custom_font, bg="white", fg="black", relief="raised", bd=4)
                botao.config(command=lambda x=i, y=j: self.botão_clicado(x, y))
                botao.grid(row=i+1, column=j, padx=4, pady=4, sticky="nsew")
                linha.append(botao)
            self.botoes.append(linha)

    def botão_clicado(self, i, j):
        if self.front.fazer_jogada(i, j):
            self.atualizar_interface()

            if self.front.verificar_conclusao():
                self.exibir_mensagem_conclusao()

    def atualizar_interface(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=self.front.matriz[i, j])
        self.label_tentativas.config(text=f"Tentativas: {self.front.contador_tentativas}")

    def exibir_mensagem_conclusao(self):
        self.mensagem_jogo = tk.Toplevel(self)
        self.mensagem_jogo.title("Parabéns!")
        self.mensagem_jogo.geometry("300x150")
        self.mensagem_jogo.config(bg="lightgreen")

        mensagem = tk.Label(self.mensagem_jogo, text=f"Você completou o jogo!", font=self.custom_font, bg="lightgreen")
        mensagem.pack(pady=10)

        botao_reiniciar = tk.Button(self.mensagem_jogo, text="Jogar Novamente", command=self.reiniciar_jogo, font=self.custom_font)
        botao_reiniciar.pack(pady=10)

        botao_fechar = tk.Button(self.mensagem_jogo, text="Fechar", command=self.quit, font=self.custom_font)
        botao_fechar.pack(pady=10)

    def reiniciar_jogo(self):
        self.label_embaralhando.config(text="Embaralhando...")
        self.update_idletasks()  # Força a atualização da interface antes de prosseguir

        self.after(500, self.embaralhar_jogo)

    def embaralhar_jogo(self):
        self.front = JogoLogica() 
        self.atualizar_interface()
        self.label_tentativas.config(text=f"Tentativas: {self.front.contador_tentativas}")

if __name__ == "__main__":
    app = Jogo8PuzzleGUI()
    app.mainloop()
