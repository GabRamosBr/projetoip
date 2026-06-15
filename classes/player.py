import pygame

#definição da classe Player
class Player():
    def __init__(self, largura, altura, vel_mov, x, y, gravity): #inicialização e atributos
        self.largura = largura #largura do retangulo de colisão
        self.altura = altura #altura do retangulo de colisao
        self.vel_mov = vel_mov 
        self.x = x 
        self.y = y 
        self.gravity = gravity #velocidade da gravidade
        
        #vidas da varinha (e variável de game over)
        self.vidas_maximas = 3
        self.vidas = self.vidas_maximas
        self.is_game_over = False

    #metodo andar para movimentação
    def andar(self, largura_tela): #é preciso considerar a largura da tela
        #se a posição x não atravessar a borda esquerda da tela
        if not(self.x <= 0): 

            if pygame.key.get_pressed()[pygame.K_a]:
                self.x -= self.vel_mov 

        #se a posição x não atravessa a borda direta da tela
        if not(self.x >= largura_tela - self.largura):

            if pygame.key.get_pressed()[pygame.K_d]:
                self.x += self.vel_mov 

        #se a posição y não atravessa a borda superior da tela
        if not(self.y <= 0):

            if pygame.key.get_pressed()[pygame.K_w]:
                self.y -= self.vel_mov 

    #metodo gravidade para implementar gravidade
    def gravidade(self, altura_tela): #precisa-se considerar a altura da tela

        #se o objeto não estiver tocando o chão
        if self.y <= altura_tela - self.altura:
            self.y += self.gravity
    
    # Parte de vida

    def tomar_dano(self):
        if self.vidas > 0:
            self.vidas -= 1
            print(f"Obstáculo. Vidas restantes: {self.vidas}")

        if self.vidas <= 0:
            self.is_game_over = True
            print("perdeu")

    def curar(self):
        if self.vidas < self.vidas_maximas:
            self.vidas += 1
            print(f"Coração coletado. Vidas restantes: {self.vidas}")
        #Essa função nao permite a vida passar de 3 corações)