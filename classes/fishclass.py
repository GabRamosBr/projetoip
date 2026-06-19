import pygame
import random

class Fish:

    def __init__(self):
        
        self.fish_buff = 'normal'
        self.fish_speed = 200
        self.fish_rect = pygame.Rect(1280, random.randint(100, 500), 50, 10)

        if self.fish_buff == 'normal':
            self.fish_color = 'cyan'
        elif self.fish_buff == 'dourado':
            self.fish_color = 'golden'
        elif self.fish_color == 'invencibilidade':
            self.fish_color = 'silver'
        elif self.fish_color == 'velocidade':
            self.fish_color = 'light green'

        
    def buff_sorter(self):

        self.fish_buff = random.choices(('normal', 'dourado', 'invencibilidade', 'velocidade'), [80, 5, 5, 10])

    
class FishGenerator:

    def __init__(self):

        

    