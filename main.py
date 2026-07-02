import pygame
import os
import random

pygame.init()
pygame.mixer.init()
musica_fundo = pygame.mixer.music.load("assets/sounds/música_de_fundo.wav")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)
som_derrota = pygame.mixer.Sound("assets/sounds/derrota.wav")
som_derrota.set_volume(0.50)
som_obstaculos = pygame.mixer.Sound("assets/sounds/colisão_obstáculos.wav")
som_obstaculos.set_volume(0.50)
som_peixes = pygame.mixer.Sound("assets/sounds/colisão_peixes.wav")
som_peixes.set_volume(0.50)
som_derrota_tocado = False
largura = 1920
altura = 1080
chao = 920
screen = pygame.display.set_mode((largura, altura))
img_inicio = pygame.image.load(os.path.join("assets", "images", "tela_inicio.png")).convert()
img_inicio = pygame.transform.scale(img_inicio, (largura, altura))

img_tut1 = pygame.image.load(os.path.join("assets", "images", "tutorial1.png")).convert()
img_tut1 = pygame.transform.scale(img_tut1, (largura, altura))

img_tut2 = pygame.image.load(os.path.join("assets", "images", "tutorial2.png")).convert()
img_tut2 = pygame.transform.scale(img_tut2, (largura, altura))

estado = "inicio"

pygame.display.set_caption("Fish Hunter")
clock = pygame.time.Clock()
running = True
dt = 0


#Variáveis que influênciam nos peixes
invencibility_buff = False
fish_spawn_rate = 0.5

#Flag de hit
dano = False

pygame.font.init()
fonte_padrao = pygame.font.SysFont("Calibri", 30, bold=True)
fonte_tempo = pygame.font.SysFont("Calibri", 50, bold=True)
score = 0


# tiles do chão
tile_largura = 89
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


# Inicialização do gerador de peixes e do Buffer
from classes.fish import Buffing
from classes.fish import FishGenerator
gerador_de_peixes = FishGenerator()



# Aparição do jogador
from classes.player import Player
anzol = Player(largura, chao)


# Aparição dos corações
from classes.heart import Heart
coracao = Heart(screen)


# Aparição dos obstáculos
from classes.spawner import GeradorObstaculos
gerador = GeradorObstaculos()

#Funções de Texto na Tela
from utils.texts import VidaNaTela, BuffsNaTela, TempoNaTela, PontuacaoNaTela


tempo_dano = 0
tempo_dificuldade = 0
INTERVALO_DIFICULDADE = 20
INTERVALO_DANO = 3


# Chão 
x = 0
tiles_usados = []


# imagem do fundo
imagem_fundo = pygame.image.load(os.path.join(pasta_projeto, "assets", "images", "fundo-agua.png")).convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))


fundo_x = 0
velocidade_fundo = 55  # Velocidade da correnteza 


while x < largura:
    indice_tile = random.randint(0, 3)
    tiles_usados.append(indice_tile)
    x += tile_largura


game_over = False
caminho_gameover = os.path.join(pasta_projeto, "assets", "images", "tela-gameover.png")
imagem_gameover = pygame.image.load(caminho_gameover).convert()
imagem_gameover = pygame.transform.scale(imagem_gameover, (largura, altura))


estado = "inicio"

while running:  
    lista_eventos = pygame.event.get()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
            
            if event.key == pygame.K_r:  
                if estado == "inicio":
                    estado = "tutorial1"
                elif estado == "tutorial1":
                    estado = "tutorial2"
                elif estado == "tutorial2":
                    estado = "jogando"

            if event.key == pygame.K_r and game_over:
                anzol.vidas = anzol.vidas_maximas
                anzol.is_game_over = False
                score = 0
                tempo_dificuldade = 0
                tempo_dano = 0
                import utils.texts
                utils.texts.TEMPO_DE_JOGO = 0 
                dano = False
                som_derrota_tocado = False
                pygame.mixer.music.play(-1)
                
                gerador_de_peixes.fish_list.clear()
                gerador_de_peixes.fish_rect_list.clear()
                coracao.heart_list.clear()
                gerador.lista_obstaculos.clear()
                
                game_over = False
                estado = "jogando"

    if estado == "inicio":
        screen.blit(img_inicio, (0, 0))

    elif estado == "tutorial1":
        screen.blit(img_tut1, (0, 0))

    elif estado == "tutorial2":
        screen.blit(img_tut2, (0, 0))

    elif estado == "jogando":
        if not game_over:
            fundo_x -= velocidade_fundo * dt
            

            if fundo_x <= -largura:
                fundo_x = 0


            screen.blit(imagem_fundo, (fundo_x, 0))
            screen.blit(imagem_fundo, (fundo_x + largura, 0))


            # Movimentação do jogador
            anzol.andar(largura, chao, dt, dano)
            screen.blit(anzol.image, anzol.rect)


            # Geração e Movimentação dos peixes
            gerador_de_peixes.Generating_Fishs(dt,fish_spawn_rate)
            gerador_de_peixes.MovingAndDrawing_Fish(screen)

            
            #Coleta dos Peixes e dos Corações
            score, buff_timer, buff_type, colisao_peixe = ColisaoPeixe(anzol.rect, gerador_de_peixes.fish_list, gerador_de_peixes.fish_rect_list, score, dano)
            if colisao_peixe:
                som_peixes.play()
            colisao_coracao = ColisaoCoração(anzol, coracao.heart_list, dano)
            if colisao_coracao:
                som_peixes.play()


            # Gerenciamento dos Buffs
            anzol.vel_mov, anzol.vel_baixo, invencibility_buff, temporizador_buff1, temporizador_buff2 = Buffing(buff_timer, buff_type, dt)


            #Textos na tela
            VidaNaTela(fonte_padrao, screen, anzol)
            BuffsNaTela(fonte_padrao, screen, invencibility_buff, temporizador_buff2, anzol, temporizador_buff1)
            TempoNaTela(fonte_tempo, screen)
            PontuacaoNaTela(fonte_padrao, screen, score)


            # Movimentação do Coração
            coracao.spawn_time_counter(dt)
            coracao.spawn(dt)


            # Movimentação do Obstáculo
            gerador.atualizar()
            gerador.desenhar(screen)


            # Colisão com obstáculos
            dano, colisao_obstaculo = ColisaoObstaculo(anzol, gerador.lista_obstaculos, invencibility_buff, dano)
            if colisao_obstaculo:
                som_obstaculos.play()

            # Verifica se as vidas zeraram
            if anzol.is_game_over:
                game_over = True


            # Escalonamento de dificuldade
            tempo_dificuldade += dt
            if tempo_dificuldade >= INTERVALO_DIFICULDADE:
                gerador.aumentar_dificuldade()
                tempo_dificuldade = 0

            # Invulnerabilidade dano
            if dano:
                tempo_dano += dt
                if tempo_dano >= INTERVALO_DANO:
                    tempo_dano = 0
                    dano = False


            # Chão
            x = 0
            for indice_tile in tiles_usados:
                screen.blit(tiles_areia[indice_tile], (x, chao))
                x += tile_largura


        else:
        
            pygame.mixer.music.stop()
            if not som_derrota_tocado:   
                som_derrota.play()
                som_derrota_tocado = True
            
            screen.blit(imagem_gameover, (0, 0))

            fonte_gameover = pygame.font.SysFont("Arial", 48, bold=True)
            
            texto_score = fonte_gameover.render(f"Score Final: {score}", True, (35, 35, 35))
            
            texto_rect = texto_score.get_rect(center=(largura // 2, 420))
            
            screen.blit(texto_score, texto_rect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
