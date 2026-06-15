import pygame
import random

class Heart():
    def __init__(self, largura_tela):
        super().__init__()
        
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0, largura_tela - 30)
        self.rect.y = -50 
        
        self.velocidade_y = 3

    def update(self):
        self.rect.y += self.velocidade_y
        
        if self.rect.y > 600:
            self.kill()