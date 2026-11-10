import pygame  # Importa a biblioteca Pygame
import random  # Importa a biblioteca random para gerar números aleatórios
import servidor

# ── 1. Inicialização ────────────────────────────────────────────────────────
pygame.init()  # Inicializa todos os módulos do Pygame

# ── 2. Configuração da janela ───────────────────────────────────────────────
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela
pygame.display.set_caption("Todos juntos")  # Define o título

# Define a cor de fundo (formato RGB: Vermelho, Verde, Azul — valores de 0 a 255)
COR_FUNDO = (30, 30, 30)  # Cinza escuro

# ── 3. Laço principal ───────────────────────────────────────────────────────
rodando = True

class Jogador:
    def __init__(self):
        self.posicao = (20, 20)  # Posição aleatória do jogador
        self.cor = (255, 0, 0)  # Cor do jogador (vermelho)

    @classmethod
    def criarComPosicaoAleatoria(classe):
        jogador = classe()
        jogador.posicao = (random.randint(0, LARGURA), random.randint(0, ALTURA))
        jogador.mudar_cor_aleatorio()  # Define uma cor aleatória para o jogador
        return jogador

    def mudar_cor_aleatorio(self):
        self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def x(self):
        return self.posicao[0]

    def y(self):
        return self.posicao[1]
        
    def mover(self, direcao):
        x, y = self.posicao
        if direcao == "baixo":
            self.posicao = (x, y + 10)
        elif direcao == "cima":
            self.posicao = (x, y - 10)
        elif direcao == "esquerda":
            self.posicao = (x - 10, y)
        elif direcao == "direita":
            self.posicao = (x + 10, y)

jogador = Jogador.criarComPosicaoAleatoria()  # Cria uma instância da classe Jogador

servidor.conectar(jogador.cor)

while rodando:
    # Preenche a tela com a cor de fundo a cada frame
    tela.fill(COR_FUNDO)

    # Processa todos os eventos pendentes
    for evento in pygame.event.get():

        # Clique no botão X da janela
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:  # Se a tecla SETA PARA BAIXO for pressionada
                jogador.mover("baixo")  # Move o jogador para baixo
            elif evento.key == pygame.K_UP:  # Se a tecla SETA PARA CIMA for pressionada
                jogador.mover("cima")  # Move o jogador para cima
            elif evento.key == pygame.K_LEFT:  # Se a tecla SETA PARA ESQUERDA for pressionada
                jogador.mover("esquerda")  # Move o jogador para a esquerda
            elif evento.key == pygame.K_RIGHT:  # Se a tecla SETA PARA DIREITA for pressionada
                jogador.mover("direita")  # Move o jogador para a direita
            servidor.enviar_posicao(jogador.x(), jogador.y())  # Envia a posição atual do jogador para o servidor            

        # Clique do mouse dentro da janela
        # if evento.type == pygame.MOUSEBUTTONDOWN:
        #     print(f"Clique detectado em: {evento.pos}")  # Exibe a posição do clique
        #     rodando = False

    # Desenha o jogador na tela
    pygame.draw.circle(tela, jogador.cor, jogador.posicao, 20)  # Desenha um círculo na cor do jogador

    # Atualiza o conteúdo exibido na janela
    pygame.display.flip()

# ── 4. Encerramento ─────────────────────────────────────────────────────────
pygame.quit()
print("Programa encerrado.")