import pygame
import random


temporizador_buff_velocity = False
temporizador_buff_invencibility = False
contador_buff_velocity = 0
contador_buff_invencibility = 0

class Fish:

    def __init__(self,dt):
        
        self.fish_buff = random.choices(('normal', 'dourado', 'invencibilidade', 'velocidade'), [80, 5, 5, 10])[0]
        self.fish_speed = -300 * dt
        self.fish_rect = pygame.Rect(1280, random.randint(100, 500), 50, 10)

        

        if self.fish_buff == 'normal':
            self.fish_color = 'cyan'
            self.fish_effect = 'nada'
            self.fish_speed = -300 * dt


        elif self.fish_buff == 'dourado':
            self.fish_color = 'yellow'
            self.fish_effect = 'score 5x'
            self.fish_speed = -400 * dt
            

        elif self.fish_buff == 'invencibilidade':
            self.fish_color = 'gray'
            self.fish_effect = 'invecibility'
            self.fish_speed = -400 * dt

        elif self.fish_buff == 'velocidade':
            self.fish_color = 'light green'
            self.fish_effect = 'speed '
            self.fish_speed = -550 * dt
        
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
        self.timer = 0
        
        

        #Modelo do peixe: (fish_type, fish_color, fish_effect)  
    
    def Generating_Fishs(self, tela, dt, spawn_rate):

        self.timer += dt


        if self.timer >= spawn_rate:

            Fish.Buff_Sorter(self)
            caixa = Fish(dt)
            

            self.fish_list.append(caixa)
            self.fish_rect_list.append(caixa.fish_rect)
            
            for fish in self.fish_list:

                pygame.draw.rect(tela, f"{fish.fish_color}", fish.fish_rect, width=0)

            self.timer = 0
    
    def MovingAndDrawing_Fish(self,tela): 

        for fish in self.fish_list:

            fish.Move()
            pygame.draw.rect(tela, f"{fish.fish_color}", fish.fish_rect, width=0)

            if fish.fish_rect.x <= -50:
                self.fish_rect_list.pop(self.fish_list.index(fish))
                self.fish_list.remove(fish)



def Buffing(buff_timer, buff_type, dt):

    global temporizador_buff_invencibility
    global temporizador_buff_velocity
    global contador_buff_invencibility
    global contador_buff_velocity
    

    if buff_timer == True:
        if buff_type == 'speed':
            temporizador_buff_velocity = True

        elif buff_type == 'invencibility':
            temporizador_buff_invencibility = True
    
    if temporizador_buff_velocity == True:
        contador_buff_velocity += dt
        buff_velocidade = 700


        if contador_buff_velocity >= 10:
            temporizador_buff_velocity = False
            contador_buff_velocity = 0
            

    else:
        buff_velocidade = 500

    if temporizador_buff_invencibility == True:
        contador_buff_invencibility += dt
        buff_invencibilidade = True


        if contador_buff_invencibility >= 5:
            temporizador_buff_invencibility = False
            contador_buff_invencibility = 0
            buff_invencibilidade = False
    else:
        buff_invencibilidade = False


    return buff_velocidade, buff_invencibilidade, 



