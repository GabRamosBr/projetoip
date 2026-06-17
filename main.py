import pygame
import random
from utils.collision import ColisaoPeixe

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fish Hunter")
clock = pygame.time.Clock()
running = True
dt = 0
gravidade = 675
forca_pulo = -575
forca_normal = 0
cntg_pulo = 0
condicao_puloduplo = True


from classes.fish import Fish
fish = Fish(screen)



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    lista_eventos = pygame.event.get()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    forca_normal += gravidade * dt


    player_red = pygame.draw.rect(screen, "red", (player_pos.x, player_pos.y, 30, 30))

    retangulo_teste = pygame.draw.rect(screen, 'white', (100, 400, 100, 200))
  
    pygame.draw.line(screen, 'pink', (0, 620), (1280, 620), width=5)


    keys = pygame.key.get_pressed()
    
    for event in lista_eventos:
        if event.type == pygame.KEYDOWN:

            if (event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP) and condicao_puloduplo:
                forca_normal = forca_pulo
                cntg_pulo += 1
            
                if cntg_pulo >= 2:
                    condicao_puloduplo = False
                    cntg_pulo = 0



    fish.spawn_time_counter(dt)
    fish.spawn(dt)

    if keys[pygame.K_s]:
        player_pos.y += 450 * dt

    if keys[pygame.K_p]:
        pygame.Rect.move_ip(retangulo_teste, 1000, 400)  


    if keys[pygame.K_a]:
        player_pos.x -= 350 * dt
    if keys[pygame.K_d]:
        player_pos.x += 350 * dt



    player_pos.y += forca_normal * dt

    if player_pos.y > 620 - 30:
        player_pos.y = 620 - 30
        condicao_puloduplo = True






    ColisaoPeixe(player_red, fish)
    #colisão peixe player





    pygame.display.flip()



    dt = clock.tick(60) / 1000



pygame.quit()