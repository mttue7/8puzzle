import time
import heapq
import numpy as np
from collections import deque


class EstadoBusca:
    def __init__(self,estado):
        self.estado  = estado
        self.estadoAnterior = None

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



    def calcAdjacentes(self, estadoOriginal,estadosVisitados):
            listaEstados = []
            x_i, x_j = np.where(estadoOriginal.estado == ' ')
            x_i, x_j = int(x_i[0]), int(x_j[0])
            matrizAux = estadoOriginal.estado.copy()

            for i in range(3):
                for j in range(3):
                    if abs(x_i - i) + abs(x_j - j) == 1:
                        matrizAux[i][j] = estadoOriginal.estado[x_i][x_j]
                        matrizAux[x_i][x_j] = estadoOriginal.estado[i][j]
                        
                        estadoTupla = tuple(matrizAux.flatten())  
                        
                        if not estadoTupla in estadosVisitados:
                            novoEstado = EstadoBusca(matrizAux.copy())
                            novoEstado.estadoAnterior = estadoOriginal
                            listaEstados.append(novoEstado)
                        
                        
                        matrizAux[i][j] = estadoOriginal.estado[i][j]
                        matrizAux[x_i][x_j] = estadoOriginal.estado[x_i][x_j]

            return listaEstados


    def printEstado(self,estadoBusca):
        filaEstados = [] 
        while(estadoBusca):
            filaEstados.append (estadoBusca.estado)
            estadoBusca = estadoBusca.estadoAnterior
        numEstados = 1
        while(filaEstados):
            print(' == Estado ',numEstados,' ==')
            numEstados+=1
            estado = filaEstados.pop()
            np.array(estado).reshape(3, 3)
            for linha in estado:
                print(" ".join(linha))
                print()


    def buscaLargura(self):
        filaEstados = deque()
        estadoAnalisado = EstadoBusca(self.estado_atual)
        visitados = set()
        visitados.add(tuple(estadoAnalisado.estado.flatten()))
        filaEstados.append(estadoAnalisado)
        listaAdjacentes = []
        estadoFinal = np.arange(1, 10).reshape(3, 3).astype(str)
        estadoFinal[estadoFinal == '9'] = ' '
        numVisitas = 0
        
        while filaEstados:
            numVisitas+=1
            estadoAnalisado = filaEstados.popleft()   
            if np.array_equal(estadoAnalisado.estado, estadoFinal):
                print("Estado final encontrado!")
                self.printEstado(estadoAnalisado)
                print('No total foram visitados ',numVisitas, 'estados')
                return True
            listaAdjacentes = self.calcAdjacentes(estadoAnalisado,visitados)

            for estadoAdj in listaAdjacentes:
                estadoTupla = tuple(estadoAdj.estado.flatten())
                filaEstados.append(estadoAdj)
                visitados.add(estadoTupla)


        print("Estado não encontrado")
        return False

    
    def buscaProfundidade(self):
   
        pilhaEstados = []  
        estadoAnalisado = EstadoBusca(self.estado_atual)
        visitados = set()
        visitados.add(tuple(estadoAnalisado.estado.flatten()))
        pilhaEstados.append(estadoAnalisado)  
        estadoFinal = np.arange(1, 10).reshape(3, 3).astype(str)
        estadoFinal[estadoFinal == '9'] = ' '
        visitados = set()
        numVisitas = 0
        
        while pilhaEstados:
            estadoAnalisado = pilhaEstados.pop()  
            numVisitas += 1
            if np.array_equal(estadoAnalisado.estado, estadoFinal):
                print("Estado final encontrado!")
                self.printEstado(estadoAnalisado)
                print('No total foram visitados ',numVisitas, 'estados')
                return True
            
            listaAdjacentes = self.calcAdjacentes(estadoAnalisado,visitados)
            
            for estadoAdj in listaAdjacentes:
                estadoTupla = tuple(estadoAdj.estado.flatten())
                pilhaEstados.append(estadoAdj)
                visitados.add(estadoTupla)
        
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
        visitados = set()
        visitados.add(tuple(estadoAnalisado.estado.flatten()))
        listaPrioridade.append((0,estadoAnalisado))
        estadoFinal = np.arange(1, 10).reshape(3, 3).astype(str)
        estadoFinal[estadoFinal == '9'] = ' '  
        prioridade = 0
        numVisitas = 0
        
        while listaPrioridade:
            indiceEstado = self.retornaPrioridade(listaPrioridade)
            estadoPrioridade = listaPrioridade.pop(indiceEstado)
            estadoAnalisado = estadoPrioridade[1]
            numVisitas+=1
            if np.array_equal(estadoAnalisado.estado, estadoFinal):
                print("Estado final encontrado!")
                self.printEstado(estadoAnalisado)
                print('No total foram visitados ',numVisitas, 'estados')
                return True
          
            listaAdjacentes = self.calcAdjacentes(estadoAnalisado,visitados)

            for estadoAdj in listaAdjacentes:
                prioridade = self.calcCusto(estadoAdj.estado) + self.contadorEstados(estadoAdj)
                estadoTupla = tuple(estadoAdj.estado.flatten())
                listaPrioridade.append((prioridade,estadoAdj))
                visitados.add(estadoTupla)
            
              
           
                
        print("Estado não encontrado")
        return False
        
        
    def contadorEstados(self,estadoBusca):
        contador = 0
        while(estadoBusca.estadoAnterior):
            contador+= 1
            estadoBusca = estadoBusca.estadoAnterior
        return contador




        



    






        

        

            

        



                    
                    
