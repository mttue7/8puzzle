import numpy as np
import time

class JogoLogica:
    def __init__(self):
        self.estado_atual = None
        self.estado_anterior = None
        self.contador_tentativas = 0

        self.matriz = self.gerar_matriz()

    def gerar_matriz(self):
        while True:
            matriz = np.arange(1, 10)
            np.random.shuffle(matriz)
            matriz = matriz.reshape(3, 3).astype(str)
            matriz[matriz == '9'] = ''
            
            print("Tentando gerar uma matriz resolvível...")
            
            if self.jogo_resolvivel(matriz):
                print("Matriz resolvível encontrada!")
                break
            
        self.estado_atual = matriz.copy()
        return matriz

    def verificar_conclusao(self):
        correto = np.arange(1, 10).reshape(3, 3).astype(str)
        correto[correto == '9'] = ''
        return np.array_equal(self.matriz, correto)

    def Inversion_Counter(self, arr):
        arr = np.array(arr)
        arr = arr[arr != '']
        inversões = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inversões += 1
        return inversões

    def jogo_resolvivel(self, matriz):
        inver = self.Inversion_Counter(matriz.flatten())
        # Se o número de inversões for par, o jogo é resolvível
        return inver % 2 == 0

    def embaralhar(self):
        while True:
            print('embaralhei')
            np.random.shuffle(self.matriz)
            time.sleep(2)
            if self.jogo_resolvivel():
                break


    def fazer_jogada(self, i, j):
        x_i, x_j = np.where(self.matriz == '')
        x_i, x_j = int(x_i[0]), int(x_j[0])

        if abs(x_i - i) + abs(x_j - j) == 1:
            self.estado_anterior = self.estado_atual.copy()
            print("anterior: \n", self.estado_anterior)
            self.matriz[x_i, x_j], self.matriz[i, j] = self.matriz[i, j], self.matriz[x_i, x_j]
            self.estado_atual = self.matriz.copy()
            print("\n\natual: \n", self.estado_atual)
            print("\n")
            self.contador_tentativas += 1
            return True
        return False
