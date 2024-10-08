import tkinter as tk
from tkinter import font
from main import JogoLogica

class Jogo8PuzzleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.custom_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.iniciar_tela_inicial()

    def iniciar_tela_inicial(self):
        self.title("Jogo do 8-Puzzle")
        self.geometry("500x350")  
        self.config(bg="lightblue")
        self.front = JogoLogica()
        self.resizable(False, False)
        
        # Limpa todos os widgets da janela, caso já tenha algo na tela
        for widget in self.winfo_children():
            widget.destroy()

        # Cria a interface da tela inicial
        self.label_inicial = tk.Label(self, text="Bem-vindo ao 8-Puzzle", font=self.custom_font, bg="lightblue")
        self.label_inicial.pack(pady=20)

        botao_jogar = tk.Button(self, text="Jogar", command=self.iniciar_jogo, font=self.custom_font, bg="black", fg="white", width=15)
        botao_jogar.pack(pady=10)

        botao_sair = tk.Button(self, text="Sair", command=self.quit, font=self.custom_font, bg="black", fg="red", width=15)
        botao_sair.pack(pady=10)

    def iniciar_jogo(self):
        # Limpa todos os widgets da janela para iniciar o jogo
        for widget in self.winfo_children():
            widget.destroy()

        self.label_game = tk.Label(self, text="8 PUZZLE GAME", font=self.custom_font, bg="lightblue")
        self.label_game.grid(row=0, column=0, columnspan=3, pady=8)

        self.label_tentativas = tk.Label(self, text=f"Tentativas: {self.front.contador_tentativas}", font=self.custom_font, bg="lightblue")
        self.label_tentativas.grid(row=4, column=0, columnspan=3, pady=10)

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i+1, weight=1)

        self.criar_botões()
        self.criar_botoes_busca()

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

    def criar_botoes_busca(self):
        # Botão para busca em largura
        botao_busca_largura = tk.Button(self, text="Busca Largura", command=self.executar_busca_largura, font=self.custom_font, bg="orange", fg="black", relief="raised", bd=4)
        botao_busca_largura.grid(row=1, column=3, padx=10, pady=5)

        # Botão para busca em profundidade
        botao_busca_profundidade = tk.Button(self, text="Busca Profundidade", command=self.executar_busca_profundidade, font=self.custom_font, bg="orange", fg="black", relief="raised", bd=4)
        botao_busca_profundidade.grid(row=2, column=3, padx=10, pady=5)

        # Botão para busca A*
        botao_busca_a = tk.Button(self, text="Busca A*", command=self.executar_busca_a, font=self.custom_font, bg="orange", fg="black", relief="raised", bd=4)
        botao_busca_a.grid(row=3, column=3, padx=10, pady=5)

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
        self.mensagem_jogo.geometry("300x200")
        self.mensagem_jogo.config(bg="lightgreen")
        self.mensagem_jogo.resizable(False,False)

        mensagem = tk.Label(self.mensagem_jogo, text=f"Você completou o jogo!", font=self.custom_font, bg="lightgreen")
        mensagem.pack(pady=10)

        botao_reiniciar = tk.Button(self.mensagem_jogo, text="Jogar Novamente", command=self.reiniciar_jogo, font=self.custom_font)
        botao_reiniciar.pack(pady=10)

        botao_fechar = tk.Button(self.mensagem_jogo, text="Fechar", command=self.quit, font=self.custom_font)
        botao_fechar.pack(pady=10)

    def reiniciar_jogo(self):
        self.mensagem_jogo.destroy()  # Fecha a janela de mensagem
        self.iniciar_tela_inicial()   # Mostra a tela inicial novamente

    # Funções para executar as buscas
    def executar_busca_largura(self):
        self.front.buscaLargura()  # Chama a função busca em largura da lógica do jogo
        self.exibir_mensagem_conclusao()

    def executar_busca_profundidade(self):
        self.front.buscaProfundidade()  # Chama a função busca em profundidade da lógica do jogo
        self.exibir_mensagem_conclusao()

    def executar_busca_a(self):
        self.front.buscaA()  # Chama a função busca A* da lógica do jogo
        self.exibir_mensagem_conclusao()

if __name__ == "__main__":
    app = Jogo8PuzzleGUI()
    app.mainloop()
