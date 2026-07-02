import pygame
import random
import os

temporizador_buff_velocity = False
temporizador_buff_invencibility = False
contador_buff_velocity = 0
contador_buff_invencibility = 0



pasta_projeto = os.path.dirname(os.path.dirname(__file__))

pasta_sprites_peixes = os.path.join(pasta_projeto, "assets", "images", "peixes")



# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


class Fish:

    def __init__(self,dt):
        
        self.fish_buff = random.choices(('normal', 'dourado', 'invencibilidade', 'velocidade'), [80, 3, 2, 5])[0] #O buff do peixe é escolhido aleatóriamente )
        self.fish_speed = -300 * dt  # Velocidade padrao dos peixes
        self.fish_rect = pygame.Rect(1920, random.randint(100, 900), 65, 30) #O peixe é criado em uma altura aleatória

        self.fish_image = 'peixe-sprite-1.png'

        
        # Características para cada buff
        if self.fish_buff == 'normal':   
            self.fish_color = 'cyan'
            self.fish_effect = 'nada'
            self.fish_speed = random.randint(-350, -300 )* dt
            self.fish_image = 'peixe-sprite-1.png'



        elif self.fish_buff == 'dourado':
            self.fish_color = 'yellow'
            self.fish_effect = 'score 5x'
            self.fish_speed = -400 * dt
            self.fish_image = 'peixe-sprite-2.png'

        elif self.fish_buff == 'invencibilidade':
            self.fish_color = 'gray'
            self.fish_effect = 'invecibility'
            self.fish_speed = -400 * dt
            self.fish_image = 'peixe-sprite-4.png'


        elif self.fish_buff == 'velocidade':
            self.fish_color = 'light green'
            self.fish_effect = 'speed '
            self.fish_speed = -550 * dt
            self.fish_image = 'peixe-sprite-3.png'

        else:   #Se o peixe for vermelho é porque há algum erro no código
            self.fish_color = 'red'

        caminho_imagem = os.path.join(pasta_sprites_peixes, self.fish_image)
        self.image = pygame.image.load(caminho_imagem).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.fish_rect.width, self.fish_rect.height))


        
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

    def Generating_Fishs(self, dt, spawn_rate):

        self.spawn_timer += dt    


        if self.spawn_timer >= spawn_rate:  #Quando o temporizador chegar no spawn rate

            caixa = Fish(dt)  #Cria-se um peixe
            

            self.fish_list.append(caixa)     # E ele é adicionado às listas
            self.fish_rect_list.append(caixa.fish_rect)
            

            self.spawn_timer = 0

# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------

    def MovingAndDrawing_Fish(self,tela): 

        for fish in self.fish_list:

            fish.Move()
            tela.blit(fish.image, fish.fish_rect)  #Move o peixe na tela

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
        buff_invencibilidade = False  #Apenas para evitar erros


    return buff_velocidade, buff_descida, buff_invencibilidade, contador_buff_velocity, contador_buff_invencibility


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


