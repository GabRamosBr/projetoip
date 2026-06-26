import pygame
import random

class Heart:

#    *ATRIBUTOS* ------------------------------------------------------------------------------
    def __init__(self, tela):

        self.screen = tela                   #tela onde os coraçãos serão desenhados
        self.heart_spawn_rate = 30           #tempo em segundos para o próximo coração aparecer
        self.heart_list = []                 #lista com os coraçãos que estão na tela
        self.heart_spawn_counter = 0         #temporizador para controlar o spawn dos coraçãos
        self.heart_speed = 50                #velocidade dos coraçãos (em pixels por segundo)


#    *TEMPORIZADOR DO SPAWN DE CORAÇÕES* ---------------------------------------------------------

    def spawn_time_counter(self, dt):
        self.heart_spawn_counter += dt       #função que inicializa o temporizador
        

#    *GERADOR DE coraçãoS* -----------------------------------------------------------------------

    def spawn(self, dt):

        if self.heart_spawn_counter >= self.heart_spawn_rate:        # se o temporizador for maior ou igual ao tempo de spawn
                                                             
            heart = pygame.Rect(random.randint(100, 1100), 0, 50, 10)       # um novo coração é gerado

            self.heart_list.append(heart)          # o coração é adicionado à lista de coraçãos na tela

            self.heart_spawn_counter = 0        # e o temporizador é reiniciado para gerar o próximo coração

        for heart in self.heart_list:        # para cada coração na lista de coraçãos

            heart.y += self.heart_speed * dt     # a posição X do coração é decrementada para ele andar para a esquerda
 
            pygame.draw.rect(self.screen, 'red', (heart.x, heart.y, 50, 10), width=0)   #o coração é desenhado com a nova posicao

            if heart.y > 750:                        # se o coração estiver fora da tela ele é removido da lista
                self.heart_list.remove(heart)
        return self.heart_list
