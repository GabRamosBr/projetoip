import pygame

#definição da classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self, largura_tela, chao): #inicialização e atributos
        super().__init__()

        self.largura = 50
        self.altura = 50

        #cria imagem retangulo branco pro player
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill((255, 255, 255))
        
        #pega o retangulo da imagem do player
        self.rect = self.image.get_rect()

        self.vel_mov = 500

        #posicoes iniciais
        self.x = largura_tela/2 - 50/2
        self.y =  chao - 80

        self.pos = pygame.Vector2(self.x, self.y)

        #forcas/velocidades
        self.gravity = 500
        self.forca_pulo = -700
        self.vel_y = 0

        #junta posicao imagem e retangulo da imagem
        self.rect.topleft = self.pos
        
        #vidas da varinha (e variável de game over)
        self.vidas_maximas = 3
        self.vidas = self.vidas_maximas
        self.is_game_over = False

    #metodo andar para movimentação
    def andar(self, largura_tela, chao, dt): #é preciso considerar a largura da tela
        
        #gravidade atuando
        self.vel_y += self.gravity * dt
        
        teclas = pygame.key.get_pressed()

        #movimentacao na horizontal
        if teclas[pygame.K_a]:
            self.pos.x -= self.vel_mov * dt

        if teclas[pygame.K_d]:
            self.pos.x += self.vel_mov * dt

        #verificacoes se atravessou bordas horizontais
        if self.pos.x < 0:
            self.pos.x = 0

        if self.pos.x > largura_tela - self.largura:
            self.pos.x = largura_tela - self.largura

        #verificacao se atravessou chao
        if (self.pos.y >= chao - self.altura):
            
            self.pos.y = chao - self.altura
            self.vel_y = 0
        
        #pulo
            if teclas[pygame.K_w]:
                self.vel_y = self.forca_pulo

        #movimentacao na vertical
        self.pos.y += self.vel_y * dt

        if (self.pos.y >= chao - self.altura):
            
            self.pos.y = chao - self.altura
            self.vel_y = 0

        else:
            if teclas[pygame.K_s]:
                self.vel_y += 60

        #atualizacao posicao
        self.rect.topleft = self.pos
    
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