import pygame
import os
import random

pygame.init()
largura = 1280
altura = 720
chao = 620
screen = pygame.display.set_mode((largura, altura))


pygame.display.set_caption("Fish Hunter")
clock = pygame.time.Clock()
running = True
dt = 0


temporizador_peixes = 0
invencibility_buff = False

fish_spawn_rate = 0.5

pygame.font.init()
fonte_padrão = pygame.font.SysFont("Calibri", 30, bold=True)
score = 0

# tiles do chão
tile_largura = 64
tile_altura = altura - chao

pasta_projeto = os.path.dirname(__file__)
pasta_tiles = os.path.join(pasta_projeto, "assets", "images", "tiles")

tiles_areia = [
    pygame.image.load(os.path.join(pasta_tiles, "areia-1.png")).convert_alpha(),
    pygame.image.load(os.path.join(pasta_tiles, "areia-2.png")).convert_alpha(),
    pygame.image.load(os.path.join(pasta_tiles, "areia-3.png")).convert_alpha(),
    pygame.image.load(os.path.join(pasta_tiles, "areia-4.png")).convert_alpha()
]

for i in range(len(tiles_areia)):
    tiles_areia[i] = pygame.transform.scale(tiles_areia[i], (tile_largura, tile_altura))

# Inicialização das Colisões
from utils.collision import ColisaoPeixe
from utils.collision import ColisaoCoração
from utils.collision import ColisaoObstaculo

# Inicialização do gerador de peixes
from classes.fish import FishGenerator
gerador_de_peixes = FishGenerator()

# Aparição do jogador
from classes.player import Player
anzol = Player(largura, altura)

# Aparição dos corações
from classes.heart import Heart
coracao = Heart(screen)

# Aparição dos obstáculos
from classes.spawner import GeradorObstaculos
gerador = GeradorObstaculos()

tempo_dificuldade = 0
INTERVALO_DIFICULDADE = 20

# Chão 
x = 0
tiles_usados = []

# imagem do fundo
imagem_fundo = pygame.image.load(os.path.join(pasta_projeto, "assets", "images", "fundo-agua.png")).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

fundo_x = 0
velocidade_fundo = 40  # Velocidade da correnteza 

while x < largura:
    indice_tile = random.randint(0, 3)
    tiles_usados.append(indice_tile)
    x += tile_largura

game_over = False
caminho_gameover = os.path.join(pasta_projeto, "assets", "images", "tela-gameover.png")
imagem_gameover = pygame.image.load(caminho_gameover).convert()
imagem_gameover = pygame.transform.scale(imagem_gameover, (largura, altura))

while running:  

    lista_eventos = pygame.event.get()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False
        
        # Apertar tecla R para reiniciar o jogo
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restaura os valores iniciais
                anzol.vidas = anzol.vidas_maximas
                anzol.is_game_over = False
                score = 0
                tempo_dificuldade = 0
                
                # Esvazia as listas para os itens antigos sumirem da tela
                fish.fish_list.clear()
                coracao.heart_list.clear()
                gerador.lista_obstaculos.clear()
                
                # Volta o estado para jogando
                game_over = False

    # Verifica o estado do jogo
    if not game_over:
        fundo_x -= velocidade_fundo * dt
        
        # Se a primeira imagem saiu completamente da tela, reseta a posição
        if fundo_x <= -largura:
            fundo_x = 0

        # DESENHA AS DUAS CÓPIAS (uma colada na outra)
        screen.blit(imagem_fundo, (fundo_x, 0))
        screen.blit(imagem_fundo, (fundo_x + largura, 0))


    # Movimentação do jogador
    anzol.andar(largura, chao, dt)
    screen.blit(anzol.image, anzol.rect)

    # Geração e Movimentação dos peixes
    gerador_de_peixes.Generating_Fishs(screen,dt,fish_spawn_rate)
    gerador_de_peixes.MovingAndDrawing_Fish(screen)

    #Coleta dos peixes
    score, buff_timer, buff_type = ColisaoPeixe(anzol.rect, gerador_de_peixes.fish_list, gerador_de_peixes.fish_rect_list, score)

    #Pontuação na Tela
    pontuacao_na_tela = fonte_padrão.render(f"Score: {score}", True, "white")
    screen.blit(pontuacao_na_tela, (1100, 20))
    vida_na_tela = fonte_padrão.render(f"Vidas: {anzol.vidas}", True, "green")
    screen.blit(vida_na_tela, (30, 20))


  
    # Movimentação do coração
    screen.blit(coracao.image, coracao.rect)
    coracao.update()

    # Movimentação do obstáculo
    gerador.atualizar()
    gerador.desenhar(screen)

        # Colisão com obstáculos
        ColisaoObstaculo(anzol, gerador.lista_obstaculos)

        # Verifica se as vidas zeraram
        if anzol.is_game_over:
            game_over = True

        # Escalonamento de dificuldade
        tempo_dificuldade += dt
        if tempo_dificuldade >= INTERVALO_DIFICULDADE:
            gerador.aumentar_dificuldade()
            tempo_dificuldade = 0

        # Chão
        x = 0
        for indice_tile in tiles_usados:
            screen.blit(tiles_areia[indice_tile], (x, chao))
            x += tile_largura

    else:
        screen.blit(imagem_gameover, (0, 0))

    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()