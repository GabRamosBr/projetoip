import pygame

pygame.init()
largura = 1280
altura = 720
chao = 620
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Fish Hunter")
clock = pygame.time.Clock()
running = True
dt = 0

#Aparição dos peixes
from classes.fish import Fish
fish = Fish(screen)

#Aparição do jogador
from classes.player import Player
anzol = Player(largura, altura)

#Aparição dos corações
from classes.heart import Heart
coracao = Heart(largura)

#Aparição dos obstáculos
from classes.spawner import GeradorObstaculos
gerador = GeradorObstaculos()

while running:

    lista_eventos = pygame.event.get()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Movimentação dos peixes
    fish.spawn_time_counter(dt)
    fish.spawn(dt)

    # Movimentação do jogador
    anzol.andar(largura, chao, dt)
    screen.blit(anzol.image, anzol.rect)

    # Movimentação do coração
    screen.blit(coracao.image, coracao.rect)
    coracao.update()

    # Movimentação do obstáculo
    gerador.atualizar()
    gerador.desenhar(screen)

    # Chão
    pygame.draw.line(screen, 'pink', (0, 620), (1280, 620), width=5)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()