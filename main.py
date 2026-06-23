import pygame
import os



pygame.init()
largura = 1280
altura = 720
chao = 620
screen = pygame.display.set_mode((largura, altura))


pygame.display.set_caption("Fish Hunter")
clock = pygame.time.Clock()
running = True
dt = 0


pygame.font.init()
fonte_padrão = pygame.font.SysFont("Calibri", 30, bold=True)
score = 0
vidas = 3

#tiles do chão
tile_largura = 64
tile_altura = altura - chao

pasta_tiles = os.path.join("assets", "images", "tiles")

tiles_areia = [
    pygame.image.load(os.path.join(pasta_tiles, "areia-1.png")).convert_alpha(),
    pygame.image.load(os.path.join(pasta_tiles, "areia-2.png")).convert_alpha(),
    pygame.image.load(os.path.join(pasta_tiles, "areia-3.png")).convert_alpha(),
    pygame.image.load(os.path.join(pasta_tiles, "areia-1.png")).convert_alpha()
]

for i in range(len(tiles_areia)):
    tiles_areia[i] = pygame.transform.scale(tiles_areia[i], (tile_largura, tile_altura))

#Inicialização das Colisões
from utils.collision import ColisaoPeixe
from utils.collision import ColisaoCoração


#Inicialização do gerador de peixes
from classes.fish import Fish
fish = Fish(screen)


#Aparição do jogador
from classes.player import Player
anzol = Player(largura, altura)

#Aparição dos corações
from classes.heart import Heart
coracao = Heart(screen)

#Aparição dos obstáculos
from classes.spawner import GeradorObstaculos
gerador = GeradorObstaculos()




while running:  

    lista_eventos = pygame.event.get()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    # Geração dos peixes
    fish.spawn_time_counter(dt)
    fish.spawn(dt)

    
    # Movimentação do jogador
    anzol.andar(largura, chao, dt)
    screen.blit(anzol.image, anzol.rect)

    #Coleta dos peixes

    score = ColisaoPeixe(anzol.rect, fish.fish_list, score)
    vidas = ColisaoCoração(anzol.rect, coracao.heart_list, vidas)

    #Pontuação na Tela
    texto = fonte_padrão.render(f"Score: {score}", True, "white")
    texto2 = fonte_padrão.render(f"Vidas: {vidas}", True, "green")
    screen.blit(texto, (1100, 20))
    screen.blit(texto2,(30, 20))
  
    # Movimentação do coração
    coracao.spawn_time_counter(dt)
    coracao.spawn(dt)

    # Movimentação do obstáculo
    gerador.atualizar()
    gerador.desenhar(screen)

    # Chão 
    x = 0
    indice_tile = 0

    while x < largura:
        screen.blit(tiles_areia[indice_tile], (x, chao))

        x += tile_largura
        indice_tile += 1

        if indice_tile >= len(tiles_areia):
            indice_tile = 0



    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
