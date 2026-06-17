import pygame
import random

class Obstaculo:

#    *ATRIBUTOS* ------------------------------------------------------------------------------
    def __init__(self, tela):

        self.obst_types = []
        self.screen = tela 
        self.obst_spawn_rate = 1
        self.obst_list = []
        self.obst_spawn_counter = 0
        self.obst_speed = 100
#    *TEMPORIZADOR DO SPAWN DE PEIXES* ---------------------------------------------------------

    def spawn_time_counter(self, dt):
        self.obst_spawn_counter += dt
        

#    *GERADOR DE PEIXES* -----------------------------------------------------------------------

    def spawn(self, dt):

        if self.obst_spawn_counter >= self.obst_spawn_rate:

            obst = pygame.Rect(1280, random.randint(100, 500), 50, 10)

            self.obst_list.append(obst)

            self.obst_spawn_counter = 0

        for obst in self.obst_list:

            obst.x -= self.obst_speed * dt

            pygame.draw.rect(self.screen, 'Brown', (obst.x, obst.y, 50, 10), width=0)

            if obst.x < -50:
                self.obst_list.remove(obst)
        return self.obst_list
