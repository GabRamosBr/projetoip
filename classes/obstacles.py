import pygame
import random


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravidade = 1000
forca_pulo = -600
forca_normal = 0
cntg_pulo = 0
condicao_puloduplo = True


#variáveis que controlam a geração de obstáculos
lista_de_obstaculos = []

gerador_de_obstaculos = 0

dificuldade_quantidade = 4

dificuldade_velocidade = 200


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


    forca_normal += gravidade * dt


#AQUI É A PARTE DE GERAÇÃO DE OBSTÁCULOS ------------------------------------------------------------------------------------------

    gerador_de_obstaculos += dt

    if gerador_de_obstaculos >= dificuldade_quantidade:

        obstaculo = {'x' : 0, 'y' : random.randint(100 , 550)}

        lista_de_obstaculos.append(obstaculo)

        gerador_de_obstaculos = 0


    print(gerador_de_obstaculos, lista_de_obstaculos)


#AQUI TERMINA A PARTE DE GERAÇÃO E COMECA A PARTE DE POR COISAS NA TELA ------------------------------------------------------------
    screen.fill("black")

    for obstaculo in lista_de_obstaculos:

        obstaculo['x'] = dificuldade_velocidade * dt / 100

        pygame.draw.rect(screen, 'white', (obstaculo['x'], obstaculo['y'], 50, 50), width=0)




    pygame.draw.circle(screen, "red", player_pos, 30)

    
    pygame.draw.line(screen, 'pink', (0, 620), (1280, 620), width=5)


    keys = pygame.key.get_pressed()
   
    if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and condicao_puloduplo == True:
        forca_normal = forca_pulo
        cntg_pulo += 1
        if cntg_pulo >= 2:
            condicao_puloduplo = False
        
    if keys[pygame.K_s]:
        player_pos.y += 500 * dt


    if keys[pygame.K_a]:
        player_pos.x -= 500 * dt
    if keys[pygame.K_d]:
        player_pos.x += 500 * dt



    player_pos.y += forca_normal * dt

    if player_pos.y > 620 - 30:
        player_pos.y = 620 - 30
        condicao_puloduplo = True


    pygame.display.flip()



    dt = clock.tick(60) / 1000




pygame.quit()
