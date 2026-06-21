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

temporizador_peixes = 0


pygame.font.init()
fonte_padrão = pygame.font.SysFont("Calibri", 30, bold=True)
score = 0


#Inicialização das Colisões
from utils.collision import ColisaoPeixe



#Inicialização do gerador de peixes
from classes.fishclass import FishGenerator
temporizador_buff = 0

gerador_de_peixes = FishGenerator()


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

        # Movimentação do jogador
    anzol.andar(largura, chao, dt)
    screen.blit(anzol.image, anzol.rect)





    temporizador_peixes += dt

    # Geração dos peixes
    
    if temporizador_peixes >= 0.5:

        gerador_de_peixes.Generate_Fish(screen,dt)
        temporizador_peixes = 0

    gerador_de_peixes.MovingAndDrawing_Fish(screen)



    #Coleta dos peixes

    score = ColisaoPeixe(anzol.rect, gerador_de_peixes.fish_list, gerador_de_peixes.fish_rect_list, score, anzol)


    #Pontuação na Tela
    texto = fonte_padrão.render(f"Score: {score}", True, "white")
    screen.blit(texto, (1100, 20))

    caixa_teste = fonte_padrão.render(f'{anzol.vel_mov}', True, 'white')
    screen.blit(caixa_teste, (1000, 20))

  
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