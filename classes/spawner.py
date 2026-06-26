import pygame
import random
from classes.obstacles import Pedra, Lixo

# Tamanho da tela pra saber quando remover os obstáculos
LARGURA_TELA = 1280
ALTURA_TELA = 720

# Intervalo em milissegundos entre cada geração de obstáculo
INTERVALO_GERACAO = 1500


class GeradorObstaculos:
    """
    Controla o surgimento e remoção dos obstáculos no jogo.
    Sorteia entre pedra e lixo e decide quando criar um novo.
    """

    def __init__(self):
        # Lista com todos os obstáculos que estão na tela agora
        self.lista_obstaculos = []

        # Começa com 0 pra já gerar o primeiro obstáculo imediatamente
        self.tempo_ultimo_gerado = 0

        # Intervalo atual entre gerações
        self.intervalo_atual = INTERVALO_GERACAO

        # Bonus de velocidade que aumenta com a dificuldade
        self.bonus_velocidade = 0

    def gerar_obstaculo(self):
        # Sorteia qual obstáculo vai aparecer
        sorteio = random.randint(0, 1)

        if sorteio == 0:
            # Cria uma pedra vindo da direita
            novo = Pedra()
        else:
            # Cria um lixo caindo do topo
            novo = Lixo()

        novo.velocidade += self.bonus_velocidade
        self.lista_obstaculos.append(novo)

    def atualizar(self):
        tempo_agora = pygame.time.get_ticks()

        # Vê se já passou tempo suficiente pra gerar um novo obstáculo
        if tempo_agora - self.tempo_ultimo_gerado >= self.intervalo_atual:
            self.gerar_obstaculo()
            self.tempo_ultimo_gerado = tempo_agora

        # Atualiza a posição de cada obstáculo
        for obstaculo in self.lista_obstaculos:
            obstaculo.atualizar()

        # Remove os que já saíram da tela
        self.lista_obstaculos = [
            obs for obs in self.lista_obstaculos if not obs.saiu_da_tela()
        ]

    def desenhar(self, tela):
        # Manda cada obstáculo se desenhar
        for obstaculo in self.lista_obstaculos:
            obstaculo.desenhar(tela)

    def aumentar_dificuldade(self):
        # Diminui o intervalo pra gerar obstáculos mais rápido (mínimo de 500ms)
        if self.intervalo_atual > 500:
            self.intervalo_atual -= 100
        # Aumenta a velocidade dos novos obstáculos
        self.bonus_velocidade += 1

    def obter_retangulos(self):
        """
        Retorna a lista de retângulos dos obstáculos ativos.
        Útil pra verificar colisão com o personagem.
        """
        return [obs.retangulo for obs in self.lista_obstaculos]

    def obter_obstaculos(self):
        """Retorna a lista completa de obstáculos ativos (com tipo e retângulo)"""
        return self.lista_obstaculos

    def reiniciar(self):
        # Limpa tudo e volta ao estado inicial
        self.lista_obstaculos = []
        self.tempo_ultimo_gerado = 0
        self.intervalo_atual = INTERVALO_GERACAO
