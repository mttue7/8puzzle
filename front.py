import tkinter as tk
from tkinter import font
from main import JogoLogica

class Jogo8PuzzleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo do 8-Puzzle")
        self.geometry("350x350")
        self.config(bg="lightblue")
        self.resizable(False, False)

        self.front = JogoLogica()
        self.custom_font = font.Font(family="Helvetica", size=16, weight="bold")

        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        # Tela inicial com opções de jogo
        self.frame_inicial = tk.Frame(self, bg="lightgreen")
        self.frame_inicial.place(relwidth=1, relheight=1)

        mensagem = tk.Label(self.frame_inicial, text="Bem vindo ao 8-puzzle game\n\nComo quer jogar?", font=self.custom_font, bg="lightgreen")
        mensagem.pack(pady=20)

        botao_jogar_sozinho = tk.Button(self.frame_inicial, text="Sozinho", command=self.iniciar_jogo_sozinho, font=self.custom_font)
        botao_jogar_sozinho.pack(pady=10)

        botao_jogar_ia = tk.Button(self.frame_inicial, text="Com IAs", command=self.ir_para_tela_ia, font=self.custom_font)
        botao_jogar_ia.pack(pady=10)

    def ir_para_tela_ia(self):
        self.frame_inicial.destroy()
        self.criar_tela_ia()

    def criar_tela_ia(self):
        self.frame_ia = tk.Frame(self, bg="lightgreen")
        self.frame_ia.place(relwidth=1, relheight=1)

        mensagem2 = tk.Label(self.frame_ia, text="Qual a IA deseja utilizar?", font=self.custom_font, bg="lightgreen")
        mensagem2.pack(pady=20)

        botao_ia1 = tk.Button(self.frame_ia, text="Busca em largura", command=self.iniciar_jogo_com_ia, font=self.custom_font)
        botao_ia1.pack(pady=10)

        botao_ia2 = tk.Button(self.frame_ia, text="Busca em profundidade", command=self.iniciar_jogo_com_ia, font=self.custom_font)
        botao_ia2.pack(pady=10)

        botao_ia3 = tk.Button(self.frame_ia, text="Heurística", command=self.iniciar_jogo_com_ia, font=self.custom_font)
        botao_ia3.pack(pady=10)

    def iniciar_jogo_sozinho(self):
        self.frame_inicial.destroy()
        self.inicio_jogo()

    def iniciar_jogo_com_ia(self):
        self.frame_ia.destroy()
        self.inicio_jogo()

    def inicio_jogo(self):
        self.label_game = tk.Label(self, text="8 PUZZLE GAME", font=self.custom_font, bg="lightblue")
        self.label_game.grid(row=0, column=0, columnspan=3, pady=8)

        self.label_embaralhando = tk.Label(self, text="", font=self.custom_font, bg="lightblue")
        self.label_embaralhando.grid(row=3, column=0, columnspan=3, pady=10)

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
                botao.config(command=lambda x=i, y=j: self.botao_clicado(x, y))
                botao.grid(row=i+1, column=j, padx=4, pady=4, sticky="nsew")
                linha.append(botao)
            self.botoes.append(linha)

    def botao_clicado(self, i, j):
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
        self.janela_conclusao = tk.Toplevel(self) 
        self.janela_conclusao.title("Parabéns!")
        self.janela_conclusao.geometry("300x250")
        self.janela_conclusao.config(bg="lightgreen")

        mensagem = tk.Label(self.janela_conclusao, text=f"Você completou o jogo!", font=self.custom_font, bg="lightgreen")
        mensagem.pack(pady=10)

        botao_reiniciar = tk.Button(self.janela_conclusao, text="Jogar Novamente", command=self.reiniciar_jogo, font=self.custom_font)
        botao_reiniciar.pack(pady=10)

        botao_fechar = tk.Button(self.janela_conclusao, text="Fechar", command=self.quit, font=self.custom_font)
        botao_fechar.pack(pady=10)

    def criar_tela_embaralhando(self):
        self.frame_embaralhando = tk.Frame(self, bg="lightblue")
        self.frame_embaralhando.place(relx=0, rely=0, relwidth=1, relheight=1) #para cobrir toda a página

        label_msg = tk.Label(self.frame_embaralhando, text="Embaralhando...", font=self.custom_font, bg="lightblue")
        label_msg.pack(expand=True) #centralizar mensagem

    def reiniciar_jogo(self):
        if self.janela_conclusao is not None: #serve para não sobrescrever janelas
            self.janela_conclusao.destroy()
            
        self.criar_tela_embaralhando()
        print("\n novo jogo \n\n")
        self.update_idletasks()
        self.after(1000, self.embaralhar_jogo)

    def embaralhar_jogo(self):
        self.front = JogoLogica()
        self.atualizar_interface()
        self.label_tentativas.config(text=f"Tentativas: {self.front.contador_tentativas}")

        self.frame_embaralhando.destroy()

if __name__ == "__main__":
    app = Jogo8PuzzleGUI()
    app.mainloop()
