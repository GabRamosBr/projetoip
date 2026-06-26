import pygame
import random
import os

# Tamanho da tela (tem que bater com o resto do jogo)
LARGURA_TELA = 1280
ALTURA_TELA = 720

pasta_atual = os.path.dirname(__file__)
pasta_projeto = os.path.dirname(pasta_atual)
pasta_obstacles = os.path.join(pasta_projeto, "assets", "images", "obstacles")

class Obstaculo:
    """Classe base pra todos os obstáculos do jogo"""

    def __init__(self, posicao_x, posicao_y, largura, altura, velocidade, tipo):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.tipo = tipo  # "pedra" ou "lixo"

        # Cria o retângulo pra colisão e desenho
        self.retangulo = pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura)

    def atualizar(self):
        # Atualiza o retângulo com a posição atual
        self.retangulo.x = int(self.posicao_x)
        self.retangulo.y = int(self.posicao_y)

    def desenhar(self, tela):
        # Cada subclasse sobrescreve esse método
        pass

    def saiu_da_tela(self):
        # Pedra sai pela esquerda
        if self.tipo == "pedra" and self.posicao_x + self.largura < 0:
            return True
        # Lixo sai pelo fundo
        if self.tipo == "lixo" and self.posicao_y > ALTURA_TELA:
            return True
        return False


class Pedra(Obstaculo):
    """Obstáculo que vem da direita e vai pra esquerda"""

    IMAGENS_AEREAS = ["fishbone-side.png", "bottle.png", "trash.png", "apple.png"]

    def __init__(self):
        no_chao = random.choice([True, False])

        if no_chao:
            arquivo = "stone.png"
        else:
            arquivo = random.choice(self.IMAGENS_AEREAS)

        imagem_original = pygame.image.load(os.path.join(pasta_obstacles, arquivo)).convert_alpha()
        proporcao = imagem_original.get_height() / imagem_original.get_width()

        largura = random.randint(80, 100)
        altura = int(largura * proporcao)

        posicao_x = LARGURA_TELA + 10

        if no_chao:
            posicao_y = ALTURA_TELA - altura - 87
        else:
            posicao_y = random.randint(100, ALTURA_TELA - altura - 150)

        velocidade = random.randint(4, 7)

        super().__init__(posicao_x, posicao_y, largura, altura, velocidade, "pedra")

        self.imagem = pygame.transform.scale(imagem_original, (largura, altura))

    def atualizar(self):
        # Faz a pedra vir da direita pra esquerda
        self.posicao_x -= self.velocidade
        super().atualizar()

    def desenhar(self, tela):
        tela.blit(self.imagem, self.retangulo)


class Lixo(Obstaculo):
    """Lixo que cai do topo da tela pra baixo"""

    IMAGENS_LIXO = ["apple.png", "bottle.png", "fishbone.png", "trash.png"]

    def __init__(self):
        arquivo = random.choice(self.IMAGENS_LIXO)
        imagem_original = pygame.image.load(os.path.join(pasta_obstacles, arquivo)).convert_alpha()
        proporcao = imagem_original.get_height() / imagem_original.get_width()

        largura = random.randint(50, 70)
        altura = int(largura * proporcao)

        # Aparece em qualquer lugar no topo
        posicao_x = random.randint(20, LARGURA_TELA - 50)
        posicao_y = -altura  # começa acima da tela

        # Velocidade vertical, cai pra baixo
        velocidade = random.randint(4, 8)

        super().__init__(posicao_x, posicao_y, largura, altura, velocidade, "lixo")

        self.imagem = pygame.transform.scale(imagem_original, (largura, altura))

    def atualizar(self):
        # Faz o lixo cair de cima pra baixo
        self.posicao_y += self.velocidade
        super().atualizar()

    def desenhar(self, tela):
        tela.blit(self.imagem, self.retangulo)
