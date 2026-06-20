import pygame
import random

class Fish:

    def __init__(self,dt):
        
        self.fish_buff = random.choices(('normal', 'dourado', 'invencibilidade', 'velocidade'), [80, 5, 5, 10])[0]
        self.fish_speed = -200 * dt
        self.fish_rect = pygame.Rect(1280, random.randint(100, 500), 50, 10)

        

        if self.fish_buff == 'normal':
            self.fish_color = 'cyan'
            self.fish_effect = 'nada'


        elif self.fish_buff == 'dourado':
            self.fish_color = 'yellow'
            self.fish_effect = 'score 5x'


        elif self.fish_buff == 'invencibilidade':
            self.fish_color = 'gray'
            self.fish_effect = 'invecibility'

        elif self.fish_buff == 'velocidade':
            self.fish_color = 'light green'
            self.fish_effect = 'speed '
        
        else: 
            self.fish_color = 'red'
        


        
    def Buff_Sorter(self):

        self.fish_buff = random.choices(('normal', 'dourado', 'invencibilidade', 'velocidade'), [80, 5, 5, 10])

    def Move(self):

        self.fish_rect.move_ip(self.fish_speed, 0)

    
class FishGenerator:

    def __init__(self):

        self.fish_list = []
        self.fish_rect_list = []
        
        

        #Modelo do peixe: (fish_type, fish_color, fish_effect)  
    
    def Generate_Fish(self, tela, dt):


        Fish.Buff_Sorter(self)
        caixa = Fish(dt)
        

        self.fish_list.append(caixa)
        self.fish_rect_list.append(caixa.fish_rect)
        
        for fish in self.fish_list:

            pygame.draw.rect(tela, f"{fish.fish_color}", fish.fish_rect, width=0)
    
    def MovingAndDrawing_Fish(self,tela):

        for fish in self.fish_list:

            fish.Move()
            pygame.draw.rect(tela, f"{fish.fish_color}", fish.fish_rect, width=0)




