import time
import numpy as np
from collections import deque


class EstadoBusca:
    def __init__(self,estado):
        self.estado  = estado
        self.estadosAnteriores = []
        self.profundidade = 0


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
            matriz[matriz == '9'] = ' '
            
            print("Tentando gerar uma matriz resolvível...")
            
            if self.jogo_resolvivel(matriz):
                print("Matriz resolvível encontrada!")
                break
            
        self.estado_atual = matriz.copy()
        return matriz

    def verificar_conclusao(self):

        correto = np.arange(1, 10).reshape(3, 3).astype(str)
        correto[correto == '9'] = ' '
        return np.array_equal(self.matriz, correto)

    def Inversion_Counter(self, arr):
        arr = np.array(arr)
        arr = arr[arr != ' ']
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
        x_i, x_j = np.where(self.matriz == ' ')
        x_i, x_j = int(x_i[0]), int(x_j[0])

        if abs(x_i - i) + abs(x_j - j) == 1:
            self.estado_anterior = self.estado_atual.copy()
            self.matriz[x_i, x_j], self.matriz[i, j] = self.matriz[i, j], self.matriz[x_i, x_j]
            self.estado_atual = self.matriz.copy()
            self.contador_tentativas += 1


            return True
        return False
    

    

    def calcCusto(self,matriz):
        matrizResposta = np.arange(1, 10).reshape(3, 3).astype(str)
        matrizResposta[matrizResposta == '9'] = ' '
        blocosCorreto = 0
        for i in range(3):
            for j in range(3):
                if matriz[i][j] != matrizResposta[i][j]:
                    blocosCorreto+=1
        return blocosCorreto



    def calcAdjacentes(self, estadoOriginal):
            listaEstados = []
            x_i, x_j = np.where(estadoOriginal.estado == ' ')
            x_i, x_j = int(x_i[0]), int(x_j[0])
            matrizAux = estadoOriginal.estado.copy()
            estadoOriginal.estadosAnteriores.append(tuple(estadoOriginal.estado.copy().flatten()))

            for i in range(3):
                for j in range(3):
                    if abs(x_i - i) + abs(x_j - j) == 1:
                        matrizAux[i][j] = estadoOriginal.estado[x_i][x_j]
                        matrizAux[x_i][x_j] = estadoOriginal.estado[i][j]
                        
                        estadoTupla = tuple(matrizAux.copy().flatten())  
                        
                        if not estadoTupla in estadoOriginal.estadosAnteriores:
                            
                            novoEstado = EstadoBusca(matrizAux.copy())
                            novoEstado.profundidade = estadoOriginal.profundidade + 1
                            novoEstado.estadosAnteriores = estadoOriginal.estadosAnteriores.copy()
                            listaEstados.append(novoEstado)
                        
                        
                        matrizAux[i][j] = estadoOriginal.estado[i][j]
                        matrizAux[x_i][x_j] = estadoOriginal.estado[x_i][x_j]

            return listaEstados


    def printEstado(self,estado):
        for linha in estado:
            print(" ".join(linha))
            print()

    def buscaLargura(self):
        filaEstados = deque()
        estadoAnalisado = EstadoBusca(self.estado_atual)
        filaEstados.append(estadoAnalisado)
        listaAdjacentes = []
        estadoFinal = np.arange(1, 10).reshape(3, 3).astype(str)
        estadoFinal[estadoFinal == '9'] = ' '
        numEstadosVisitados = 0
        while filaEstados:
            estadoAnalisado = filaEstados.popleft()
            numEstadosVisitados+= 1
            if np.array_equal(estadoAnalisado.estado, estadoFinal):
                print("Estado final encontrado!")
                numEstados = 1
               
                for estadoAnterior in estadoAnalisado.estadosAnteriores:
                    print(' == Estado ',numEstados,' ==')
                    numEstados+=1
                    self.printEstado(np.array(estadoAnterior).reshape(3, 3))
                print(' == Estado ',numEstados,' ==')
                self.printEstado(np.array(estadoAnalisado.estado).reshape(3, 3))
                print('Foram visitados no total ',numEstadosVisitados,' estados')
                return True
            listaAdjacentes = self.calcAdjacentes(estadoAnalisado)
    
            for estado in listaAdjacentes:
                filaEstados.append(estado)
        print("Estado não encontrado")
        return False

    
    def buscaProfundidade(self):
   
        pilhaEstados = []  
        estadoAnalisado = EstadoBusca(self.estado_atual)
        pilhaEstados.append(estadoAnalisado)  
        estadoFinal = np.arange(1, 10).reshape(3, 3).astype(str)
        estadoFinal[estadoFinal == '9'] = ' '  
        numEstadosVisitados = 0
        while pilhaEstados:
            estadoAnalisado = pilhaEstados.pop()  
            numEstadosVisitados+= 1
            if np.array_equal(estadoAnalisado.estado, estadoFinal):
                print("Estado final encontrado!")
                numEstados = 1
                for estadoAnterior in estadoAnalisado.estadosAnteriores:
                    print(' == Estado ',numEstados,' ==')
                    numEstados+=1
                    self.printEstado(np.array(estadoAnterior).reshape(3, 3))
                print(' == Estado ',numEstados,' ==')
                self.printEstado(np.array(estadoAnalisado.estado).reshape(3, 3))
                print('Foram visitados no total ',numEstadosVisitados,' estados')
                return True
            
            listaAdjacentes = self.calcAdjacentes(estadoAnalisado)
            
            for estado in listaAdjacentes:
                if estado.profundidade < 50:
                    pilhaEstados.append(estado)
        
        print("Estado não encontrado")
        return False
    
    def retornaPrioridade(self, lista):
        menorPrioridade = lista[0][0]
        indiceMenor = 0
        for i in range(len(lista)):
            if lista[i][0] < menorPrioridade:
                menorPrioridade = lista[i][0]
                indiceMenor = i
        return indiceMenor



    def buscaA(self):
        listaPrioridade = []
        estadoAnalisado = EstadoBusca(self.estado_atual)
        listaPrioridade.append((0,estadoAnalisado))
        estadoFinal = np.arange(1, 10).reshape(3, 3).astype(str)
        estadoFinal[estadoFinal == '9'] = ' '  
        prioridade = 0
        numEstadosVisitados = 0
        while listaPrioridade:

            indiceEstado = self.retornaPrioridade(listaPrioridade)
            estadoPrioridade = listaPrioridade.pop(indiceEstado)
            estadoAnalisado = estadoPrioridade[1]
            numEstadosVisitados += 1
            if np.array_equal(estadoAnalisado.estado, estadoFinal):
                print("Estado final encontrado!")
                numEstados = 1
                for estadoAnterior in estadoAnalisado.estadosAnteriores:
                    print(' == Estado ',numEstados,' ==')
                    numEstados+=1
                    self.printEstado(np.array(estadoAnterior).reshape(3, 3))
                print(' == Estado ',numEstados,' ==')
                self.printEstado(np.array(estadoAnalisado.estado).reshape(3, 3))
                print('Foram visitados no total ',numEstadosVisitados,' estados')
                return True
            
            listaAdjacentes = self.calcAdjacentes(estadoAnalisado)
         
            for estadoAdj in listaAdjacentes:
                prioridade = self.calcCusto(estadoAdj.estado) + estadoAdj.profundidade
                listaPrioridade.append((prioridade,estadoAdj))
                
        print("Estado não encontrado")
        return False
        

        
            
            



        



    






        

        

            

        



                    
                    
