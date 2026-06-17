import pygame
import random

class Fish:

#    *ATRIBUTOS* ------------------------------------------------------------------------------
    def __init__(self, tela):

        self.fish_types = []                #lista com os tipos de peixes (ainda vou preencher)
        self.screen = tela                  #tela onde os peixes serão desenhados
        self.fish_spawn_rate = 1            #tempo em segundos para o próximo peixe aparecer
        self.fish_list = []                 #lista com os peixes que estão na tela
        self.fish_spawn_counter = 0         #temporizador para controlar o spawn dos peixes
        self.fish_speed = 200               #velocidade dos peixes (em pixels por segundo)


#    *TEMPORIZADOR DO SPAWN DE PEIXES* ---------------------------------------------------------

    def spawn_time_counter(self, dt):
        self.fish_spawn_counter += dt       #função que inicializa o temporizador
        

#    *GERADOR DE PEIXES* -----------------------------------------------------------------------

    def spawn(self, dt):

        if self.fish_spawn_counter >= self.fish_spawn_rate:        # se o temporizador for maior ou igual ao tempo de spawn
                                                             
            fish = pygame.Rect(1280, random.randint(100, 500), 50, 10)       # um novo peixe é gerado

            self.fish_list.append(fish)          # o peixe é adicionado à lista de peixes na tela

            self.fish_spawn_counter = 0        # e o temporizador é reiniciado para gerar o próximo peixe

        for fish in self.fish_list:        # para cada peixe na lista de peixes

            fish.x -= self.fish_speed * dt     # a posição X do peixe é decrementada para ele andar para a esquerda
 
            pygame.draw.rect(self.screen, 'cyan', (fish.x, fish.y, 50, 10), width=0)   #o peixe é desenhado com a nova posicao

            if fish.x < -50:                        # se o peixe estiver fora da tela ele é removido da lista
                self.fish_list.remove(fish)
        return self.fish_list
