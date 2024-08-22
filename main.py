# jogo_logica.py

import numpy as np

class JogoLogica:
    def __init__(self):
        self.estado_atual = None
        self.estado_anterior = None
        self.contador_tentativas = 0

        self.matriz = self.gerar_matriz()
        self.estado_atual = self.matriz.copy()

    def gerar_matriz(self):
        matriz = np.arange(1, 10)
        np.random.shuffle(matriz)
        matriz = matriz.reshape(3, 3).astype(str)
        matriz[matriz == '9'] = 'x'
        return matriz

    def verificar_conclusao(self):
        correto = np.arange(1, 10).reshape(3, 3).astype(str)
        correto[correto == '9'] = 'x'
        return np.array_equal(self.matriz, correto)

    def Inversion_Counter(self, arr):
        arr = np.array(arr)
        arr = arr[arr != 'x']
        inversões = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inversões += 1
        return inversões

    def jogo_resolvivel(self):
        inver = self.Inversion_Counter(self.matriz.flatten())
        if inver % 2 == 0:
            return True
        return False

    

    def fazer_jogada(self, i, j):
        x_i, x_j = np.where(self.matriz == 'x')
        x_i, x_j = int(x_i[0]), int(x_j[0])

        if abs(x_i - i) + abs(x_j - j) == 1:
            self.estado_anterior = self.estado_atual.copy()
            print('anterior: \n',self.estado_anterior)
            print('=====')

            self.matriz[x_i, x_j], self.matriz[i, j] = self.matriz[i, j], self.matriz[x_i, x_j]
            self.estado_atual = self.matriz.copy()
            print('atual: \n',self.estado_atual)

            self.contador_tentativas += 1
            return True
        return False
