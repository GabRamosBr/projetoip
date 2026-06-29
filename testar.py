
import pygame
import pygame.gfxdraw
import math
import sys

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Setor Circular Correto no Pygame")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

def desenhar_setor_preenchido(superficie, x, y, raio, angulo_inicio, angulo_fim, cor):
    """
    Desenha um setor circular preenchido.
    Ângulos devem ser passados em GRAUS.
    """
    # No Pygame, o eixo Y é invertido, então multiplicamos os ângulos por -1
    # para que eles sigam o sentido anti-horário padrão da matemática.
    
    pontos = [(x, y)]
    # Calcula os pontos ao longo do arco para fechar o polígono
    for grau in range(angulo_inicio, angulo_fim + 1):
        # Converte para radianos para o cálculo matemático dos pontos
        rad = math.radians(grau)
        px = x + raio * math.cos(rad)
        py = y - raio * math.sin(rad) # Subtrai porque o Y cresce para baixo
        pontos.append((px, py))
    
    # Desenha o polígono preenchido que forma a fatia
    pygame.draw.polygon(superficie, cor, pontos)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(BRANCO)

    # Desenha um setor com centro em (200, 200), raio 100, indo de 0° a 120°
    desenhar_setor_preenchido(tela, 200, 200, 100, 0, 120, VERMELHO)

    pygame.display.flip()

pygame.quit()
sys.exit()