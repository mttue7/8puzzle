import numpy as np
import tkinter as tk
from tkinter import font

class Jogo8Puzzle(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do 8-Puzzle")
        self.geometry("350x350")
        self.config(bg="lightblue")

        # Desativa o redimensionamento da janela
        self.resizable(False, False) 

        self.contador_tentativas = 0
        self.custom_font = font.Font(family="Helvetica", size=16, weight="bold")

        # Label de título
        self.label_game = tk.Label(self, text="8 PUZZLE GAME", font=self.custom_font, bg="lightblue")
        self.label_game.grid(row=0, column=0, columnspan=3, pady=8)

        # Label de tentativas
        self.label_tentativas = tk.Label(self, text=f"Tentativas: {self.contador_tentativas}", font=self.custom_font, bg="lightblue")
        self.label_tentativas.grid(row=4, column=0, columnspan=3, pady=10)

        # Configura linhas e colunas para expansão
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)  # Faz com que as colunas se expandam igualmente
            self.grid_rowconfigure(i+1, weight=1)  # Faz com que as linhas se expandam igualmente

        self.matriz = self.gerar_matriz()
        self.criar_botões()

    def gerar_matriz(self):
        matriz = np.arange(1, 10)
        np.random.shuffle(matriz)
        matriz = matriz.reshape(3, 3).astype(str)
        matriz[matriz == '9'] = 'x'
        return matriz

    def criar_botões(self):
        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                botao = tk.Button(self, text=self.matriz[i, j], width=5, height=2, font=self.custom_font, bg="white", fg="black", relief="raised", bd=4)
                botao.config(command=lambda x=i, y=j: self.botão_clicado(x, y))
                botao.grid(row=i+1, column=j, padx=4, pady=4, sticky="nsew")  # Ajuste do preenchimento e expansibilidade
                linha.append(botao)
            self.botoes.append(linha)

    def botão_clicado(self, i, j):
        x_i, x_j = np.where(self.matriz == 'x')
        x_i, x_j = int(x_i[0]), int(x_j[0])
        
        # Verifica se o botão clicado é adjacente ao espaço vazio
        if abs(x_i - i) + abs(x_j - j) == 1:
            # Troca o texto dos botões e as posições na matriz
            self.matriz[x_i, x_j], self.matriz[i, j] = self.matriz[i, j], self.matriz[x_i, x_j]
            self.botoes[x_i][x_j].config(text=self.matriz[x_i, x_j])
            self.botoes[i][j].config(text=self.matriz[i, j])

            # Incrementa o contador de tentativas
            self.contador_tentativas += 1
            self.label_tentativas.config(text=f"Tentativas: {self.contador_tentativas}")

if __name__ == "__main__":
    app = Jogo8Puzzle()
    app.mainloop()
