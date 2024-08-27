# 8-Puzzle Simulator
Este projeto é uma implementação de um simulador do jogo 8-Puzzle, desenvolvido como parte do Grupo Simulador para uma avaliação prática. O objetivo do jogo é reorganizar um tabuleiro embaralhado para alcançar um estado final predefinido.

## Estado Final
O estado final do jogo é definido como:
```
1 | 2 | 3
4 | 5 | 6
7 | 8 | X
```

Onde "X" representa o espaço vazio.

## Requisitos
- Geração de Estado Inicial: O jogo deve gerar um tabuleiro inicial aleatório que seja resolvível.
- Definição de Estado, Ações e Funções Sucessoras: As estruturas e funções necessárias para manipulação e avaliação dos estados do jogo estão implementadas.
- Interface Gráfica: Uma interface amigável em Tkinter permite que o usuário visualize o estado atual do jogo e interaja para resolver o puzzle.
- Validação da Solução: O jogo avisa quando o estado final é atingido, indicando que o puzzle foi resolvido.
- Extras: O jogo conta o número de movimentos e oferece a opção de reiniciar o jogo sem fechar a interface.

## Funcionalidades Principais
- Estado: Representado por uma matriz 3x3 que contém os números de 1 a 8 e um espaço vazio ("X").
- Geração do Estado Inicial: O estado inicial é gerado aleatoriamente e verificado para garantir que é resolvível.
- Função Sucessora: Manipula o estado do jogo conforme o usuário faz movimentos válidos.
- Função de Avaliação: Verifica se o estado atual do tabuleiro corresponde ao estado final.

### Interface do Usuário
A interface gráfica foi construída usando Tkinter. O usuário pode ver o tabuleiro atual, clicar para mover as peças e visualizar mensagens de sucesso quando o jogo é completado.

## Implementação
### Arquivo `jogo_logica.py`
Este arquivo contém a lógica central do jogo:

- Classe JogoLogica: Gerencia a matriz do tabuleiro, verifica a validade dos estados, conta inversões para determinar a resolvibilidade e embaralha o tabuleiro quando necessário.
- Métodos:
    - gerar_matriz(): Gera o estado inicial do jogo.

    - verificar_conclusao(): Verifica se o tabuleiro atual é o estado final.

    - Inversion_Counter(): Conta o número de inversões no tabuleiro para verificar sua resolvibilidade.

    - jogo_resolvivel(): Garante que o tabuleiro inicial seja resolvível.

    - embaralhar(): Embaralha o tabuleiro até que ele seja resolvível.

    - fazer_jogada(i, j): Executa uma jogada, trocando peças adjacentes com o espaço vazio.
### Arquivo `jogo_gui.py`
Este arquivo contém a interface gráfica:

- Classe Jogo8PuzzleGUI: Gerencia a interface Tkinter.
- Métodos:
    - criar_botões(): Cria os botões que representam o tabuleiro.

    - botão_clicado(i, j): Gerencia os cliques do usuário, movendo as peças.

    - atualizar_interface(): Atualiza o tabuleiro após cada jogada.

    - exibir_mensagem_Nresolvivel(): Exibe uma mensagem quando o tabuleiro não é resolvível.

    - exibir_mensagem_conclusao(): Exibe uma mensagem de sucesso quando o jogo é resolvido.

### Instruções de Execução
1. Certifique-se de ter o Python instalado.

2. Clone este repositório:
```
git clone https://github.com/seu-usuario/8-puzzle-simulator.git
```

3. Navegue até o diretório do projeto:
```
cd 8-puzzle-simulator
```

4. Execute o jogo:
```
python front.py
```
## Avaliação
A implementação atende aos seguintes critérios:

 - Definição de Estado: Implementado com uma matriz 3x3.
 - Geração de Estado Inicial: Garantido que o tabuleiro inicial seja resolvível.
 - Função Sucessora: Implementada com manipulação de estados.
 - Função de Avaliação: Verifica se o estado final foi atingido.
 - Interface Amigável: Desenvolvida com Tkinter.
 - Jogo Jogável: Permite interação completa e reinício do jogo.

## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.