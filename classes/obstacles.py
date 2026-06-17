import pygame
import random

# Tamanho da tela (tem que bater com o resto do jogo)
LARGURA_TELA = 1920
ALTURA_TELA = 1040

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
    """Pedra que vem da direita e vai pra esquerda"""

    # Cor temporária pra teste — marrom
    COR = (139, 90, 43)
    COR_BORDA = (90, 55, 20)

    def __init__(self):
        largura = 80
        altura = 80

        # Começa fora da tela na direita
        posicao_x = LARGURA_TELA + 10
        # aparece um pouco acima do chão
        posicao_y = ALTURA_TELA - altura - 87


        # Velocidade horizontal
        velocidade = random.randint(4, 7)

        super().__init__(posicao_x, posicao_y, largura, altura, velocidade, "pedra")

    def atualizar(self):
        # Faz a pedra vir da direita pra esquerda
        self.posicao_x -= self.velocidade
        super().atualizar()

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.COR, self.retangulo, border_radius=6)
        pygame.draw.rect(tela, self.COR_BORDA, self.retangulo, width=2, border_radius=6)


class Lixo(Obstaculo):
    """Lixo que cai do topo da tela pra baixo"""

    # Cor temporária pra teste — verde escuro de saco de lixo
    COR = (34, 120, 50)
    COR_BORDA = (10, 60, 20)

    def __init__(self):
        largura = random.randint(25, 45)
        altura = random.randint(35, 55)

        # Aparece em qualquer lugar no topo
        posicao_x = random.randint(20, LARGURA_TELA - 50)
        posicao_y = -altura  # começa acima da tela

        # Velocidade vertical, cai pra baixo
        velocidade = random.randint(4, 8)

        super().__init__(posicao_x, posicao_y, largura, altura, velocidade, "lixo")

    def atualizar(self):
        # Faz o lixo cair de cima pra baixo
        self.posicao_y += self.velocidade
        super().atualizar()

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.COR, self.retangulo, border_radius=4)
        pygame.draw.rect(tela, self.COR_BORDA, self.retangulo, width=2, border_radius=4)

        # Detalhe da amarração do saco no topo
        amarracao_x = self.retangulo.centerx - 8
        amarracao_y = self.retangulo.top
        pygame.draw.rect(tela, (20, 80, 30), (amarracao_x, amarracao_y, 16, 8), border_radius=2)
