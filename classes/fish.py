import pygame
import random


temporizador_buff_velocity = False
temporizador_buff_invencibility = False
contador_buff_velocity = 0
contador_buff_invencibility = 0

# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


class Fish:

    def __init__(self,dt):
        
        self.fish_buff = random.choices(('normal', 'dourado', 'invencibilidade', 'velocidade'), [80, 3, 2, 3])[0] #O buff do peixe é escolhido aleatóriamente
        self.fish_speed = -300 * dt  # Velocidade padrao dos peixes
        self.fish_rect = pygame.Rect(1920, random.randint(100, 800), 50, 30) #O peixe é criado em uma altura aleatória

        
        # Características para cada buff
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
        
        else:   #Se o peixe for vermelho é porque há algum erro no código
            self.fish_color = 'red'
        
# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------
    
    def Move(self):

        self.fish_rect.move_ip(self.fish_speed, 0)



# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


class FishGenerator:

    def __init__(self):

        self.fish_list = []
        self.fish_rect_list = []
        self.spawn_timer = 0
    
# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------

    def Generating_Fishs(self, tela, dt, spawn_rate):

        self.spawn_timer += dt    


        if self.spawn_timer >= spawn_rate:  #Quando o temporizador chegar no spawn rate

            caixa = Fish(dt)  #Cria-se um peixe
            

            self.fish_list.append(caixa)     # E ele é adicionado às listas
            self.fish_rect_list.append(caixa.fish_rect)
            
            for fish in self.fish_list:

                pygame.draw.rect(tela, f"{fish.fish_color}", fish.fish_rect, width=0) #Criam-se os peixes na tela

            self.spawn_timer = 0

# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------

    def MovingAndDrawing_Fish(self,tela): 

        for fish in self.fish_list:

            fish.Move()
            pygame.draw.rect(tela, f"{fish.fish_color}", fish.fish_rect, width=0)  #Move o peixe na tela

            if fish.fish_rect.x <= -50:                         # Se ele sair da tela
                self.fish_rect_list.pop(self.fish_list.index(fish))
                self.fish_list.remove(fish)         # Ele é removido                  



# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def Buffing(buff_spawn_timer, buff_type, dt):

    global temporizador_buff_invencibility
    global temporizador_buff_velocity
    global contador_buff_invencibility          # Variáveis de inicialização
    global contador_buff_velocity
    

    if buff_spawn_timer == True:   # Verifica se precisa iniciar um temporizador de buff

        if buff_type == 'speed':      # Vê se o temporizador de velocidade
            temporizador_buff_velocity = True
            contador_buff_velocity = 0

        elif buff_type == 'invencibility': # Ou de invencibilidade
            temporizador_buff_invencibility = True 
            contador_buff_invencibility = 0
    
# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


    if temporizador_buff_velocity == True:  #Se o temporizador de velocidade for iniciado
        contador_buff_velocity += dt        #Inicia-se a contagem
        buff_velocidade = 700               #E a velocidade do jogador é aumentada
        buff_descida = 85


        if contador_buff_velocity >= 10:   #Quando acabar o buff
            temporizador_buff_velocity = False  # O temporizador/buff é desligado
            contador_buff_velocity = 0          # E resetado
            

    else:
        buff_velocidade = 500 #Apenas para evitar erros
        buff_descida = 85

# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


    if temporizador_buff_invencibility == True: #Se o temporizador de velocidade for iniciado
        contador_buff_invencibility += dt       #Inicia-se a contagem
        buff_invencibilidade = True             #E o buff é ativado


        if contador_buff_invencibility >= 10:    #Quando acabar o buff
            temporizador_buff_invencibility = False  # O temporizador é desligado
            contador_buff_invencibility = 0          # E resetado
            buff_invencibilidade = False             # E o buff é desligado


    else:
        buff_invencibilidade = False  # Apenas para evitar erros


    return buff_velocidade, buff_descida, buff_invencibilidade, contador_buff_invencibility, contador_buff_velocity


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


