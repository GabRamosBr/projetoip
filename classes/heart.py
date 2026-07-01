import pygame
import random
import os

class Heart:

    def __init__(self, tela):

        self.screen = tela                   
        self.heart_spawn_rate = 30           
        self.heart_list = []                 
        self.heart_spawn_counter = 0         
        self.heart_speed = 50                

        pasta_atual = os.path.dirname(__file__)
        pasta_projeto = os.path.dirname(pasta_atual)
        pasta_imagens = os.path.join(pasta_projeto, "assets", "images")
        
        imagem_original = pygame.image.load(os.path.join(pasta_imagens, "coracao.png")).convert_alpha()
        
        self.largura = 65
        self.altura = 65
        
        self.imagem_coracao = pygame.transform.scale(imagem_original, (self.largura, self.altura))
        
        self.largura = self.imagem_coracao.get_width()
        self.altura = self.imagem_coracao.get_height()


    def spawn_time_counter(self, dt):
        self.heart_spawn_counter += dt       
        

#GERADOR DE CORAÇÕES

    def spawn(self, dt):

        if self.heart_spawn_counter >= self.heart_spawn_rate:       
                                                                     
            heart = pygame.Rect(random.randint(100, 1800), -self.altura, self.largura, self.altura)       

            self.heart_list.append(heart)         

            self.heart_spawn_counter = 0       

        for heart in self.heart_list:        

            heart.y += self.heart_speed * dt   
 
            self.screen.blit(self.imagem_coracao, (heart.x, heart.y)) 

            if heart.y > 1080:                       
                self.heart_list.remove(heart)
                
        return self.heart_list