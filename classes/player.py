import pygame

#definição da classe Player
class Player():
    def __init__(self, largura_tela, altura_tela): #inicialização e atributos
        super().__init__()

        self.largura = 50
        self.altura = 80

        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill((255, 255, 255))
        
        self.rect = self.image.get_rect()

        self.vel_mov = 500

        self.x = largura_tela/2 - 50/2
        self.y =  altura_tela - 80

        self.pos = pygame.Vector2(self.x(), self.y())

        self.gravity = 1000
        self.forca_pulo = -600
        self.forca_normal = 0
        
        #vidas da varinha (e variável de game over)
        self.vidas_maximas = 3
        self.vidas = self.vidas_maximas
        self.is_game_over = False

    #metodo andar para movimentação
    def andar(self, largura_tela): #é preciso considerar a largura da tela
        #se a posição x não atravessar a borda esquerda da tela
        if not(self.rect.x <= 0): 

            if pygame.key.get_pressed()[pygame.K_a]:
                self.pos.x = self.vel_mov * dt

        #se a posição x não atravessa a borda direta da tela
        if not(self.rect.x >= largura_tela - self.largura):

            if pygame.key.get_pressed()[pygame.K_d]:
                self.pos.x += self.vel_mov * dt

        #se a posição y não atravessa a borda superior da tela
        if not(self.rect.y <= 0):

            if pygame.key.get_pressed()[pygame.K_w]:
                self.pos.y -= self.vel_mov 

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