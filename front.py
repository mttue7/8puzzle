# jogo_gui.py

import tkinter as tk
from tkinter import font
from main import JogoLogica  # Importa a lógica do jogo

class Jogo8PuzzleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do 8-Puzzle")
        self.geometry("350x350")
        self.config(bg="lightblue")

        self.front = JogoLogica()  # Instancia a lógica do jogo

        # Desativa o redimensionamento da janela
        self.resizable(False, False)

        self.custom_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Label de título
        self.label_game = tk.Label(self, text="8 PUZZLE GAME", font=self.custom_font, bg="lightblue")
        self.label_game.grid(row=0, column=0, columnspan=3, pady=8)

        # Label de tentativas
        self.label_tentativas = tk.Label(self, text=f"Tentativas: {self.front.contador_tentativas}", font=self.custom_font, bg="lightblue")
        self.label_tentativas.grid(row=4, column=0, columnspan=3, pady=10)

        # Configura linhas e colunas para expansão
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

            if not self.front.jogo_resolvivel():
                self.exibir_mensagem_Nresolvivel()

            if self.front.verificar_conclusao():
                self.exibir_mensagem_conclusao()

    def atualizar_interface(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text=self.front.matriz[i, j])
        self.label_tentativas.config(text=f"Tentativas: {self.front.contador_tentativas}")

    def exibir_mensagem_Nresolvivel(self):
        mensagem_jogo1 = tk.Toplevel(self)
        mensagem_jogo1.title("Não é resolvível!")
        mensagem_jogo1.geometry("280x160")
        mensagem_jogo1.config(bg="lightgreen")

        mensagem = tk.Label(mensagem_jogo1, text="Não é resolvível!", font=self.custom_font, bg="blue")
        mensagem.pack(pady=10)

        botao_fechar = tk.Button(mensagem_jogo1, text="Fechar", command=mensagem_jogo1.destroy, font=self.custom_font)
        botao_fechar.pack(pady=10)

    def exibir_mensagem_conclusao(self):
        mensagem_jogo = tk.Toplevel(self)
        mensagem_jogo.title("Parabéns!")
        mensagem_jogo.geometry("300x150")
        mensagem_jogo.config(bg="lightgreen")

        mensagem = tk.Label(mensagem_jogo, text=f"Você completou o jogo", font=self.custom_font, bg="lightgreen")
        mensagem.pack(pady=10)

        botao_fechar = tk.Button(mensagem_jogo, text="Fechar", command=mensagem_jogo.destroy, font=self.custom_font)
        botao_fechar.pack(pady=10)

if __name__ == "__main__":
    app = Jogo8PuzzleGUI()
    app.mainloop()
