import pygame
import random

class Fish:

#    *ATRIBUTOS* ------------------------------------------------------------------------------

    def __init__(self, tela):

        self.fish_types = []
        self.screen = tela 
        self.fish_spawn_rate = 1
        self.fish_list = []
        self.fish_spawn_counter = 0


#    *TEMPORIZADOR DO SPAWN DE PEIXES* ---------------------------------------------------------

    def fish_spawn_time_counter(self, dt):
        self.fish_spawn_counter += dt
        


#    *GERAÇAO DE PEIXES* -----------------------------------------------------------------------

    def spawn_fish(self, dt):

        if self.fish_spawn_counter >= self.fish_spawn_rate:

            fish = pygame.Rect(1280, random.randint(100, 500), 1, 5)

            self.fish_list.append(fish(self.screen, self.fish_spawn_counter))

            self.fish_spawn_counter = 0

        for fish in self.fish_list:

            fish.x -= self.fish_speed * dt

            pygame.draw.rect(self.screen, 'cyan', (fish.x, fish.y, 50, 10), width=0)

            if fish.x < -50:
                self.fish_list.remove(fish)

