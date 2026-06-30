import pygame
import os

#definição da classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self, largura_tela, chao): #inicialização e atributos
        super().__init__()

        self.largura = 50
        self.altura = 80

        pasta_atual = os.path.dirname(__file__)
        pasta_projeto = os.path.dirname(pasta_atual)

        self.pasta_player = os.path.join(pasta_projeto, "assets", "images", "player")

        #cria imagem retangulo branco pro player
        # self.image = pygame.image.load(caminho_imagem).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        self.animacoes = {
            "idle": [self.carregar_imagem("anzol-idle.png")],

            "running" : [
                self.carregar_imagem("anzol-running-1.png"),
                self.carregar_imagem("anzol-idle-side.png"),
                self.carregar_imagem("anzol-running-2.png"),
            ],

            "jump_facing": [
            self.carregar_imagem("anzol-facing-jump-1.png"),
            self.carregar_imagem("anzol-facing-jump-2.png")
            ],

            "jump_side": [
            self.carregar_imagem("anzol-side-jump-1.png"),
            self.carregar_imagem("anzol-side-jump-2.png")
            ]
        }

        self.estado = "idle"
        self.frame_atual = 0
        self.tempo_animacao = 0
        self.vel_animacao = 0.15
        self.olhando_direita = True

        self.image = self.animacoes[self.estado][self.frame_atual]
        
        #pega o retangulo da imagem do player
        self.rect = self.image.get_rect()

        self.vel_mov = 500

        #posicoes iniciais
        self.x = largura_tela/2 - 50/2
        self.y =  chao - 80

        self.pos = pygame.Vector2(self.x, self.y)

        #forcas/velocidades
        self.gravity = 500
        self.forca_pulo = -900
        self.vel_y = 0
        self.vel_baixo = 60
        self.no_chao = True

        #junta posicao imagem e retangulo da imagem
        self.rect.topleft = self.pos
        
        #vidas da varinha (e variável de game over)
        self.vidas_maximas = 3
        self.vidas = self.vidas_maximas
        self.is_game_over = False

    def carregar_imagem(self, nome_arquivo):
        caminho = os.path.join(self.pasta_player, nome_arquivo)

        imagem = pygame.image.load(caminho).convert_alpha()
        imagem = pygame.transform.scale(imagem, (self.largura, self.altura))

        return imagem

    #metodo andar para movimentação
    def andar(self, largura_tela, chao, dt): #é preciso considerar a largura da tela
        
        movendo = False

        #gravidade atuando
        self.vel_y += self.gravity * dt
        
        teclas = pygame.key.get_pressed()

        #movimentacao na horizontal
        if teclas[pygame.K_a]:
            self.pos.x -= self.vel_mov * dt
            self.olhando_direita = False
            movendo = True

        if teclas[pygame.K_d]:
            self.pos.x += self.vel_mov * dt
            self.olhando_direita = True
            movendo = True

        #verificacoes se atravessou bordas horizontais
        if self.pos.x < 0:
            self.pos.x = 0

        if self.pos.x > largura_tela - self.largura:
            self.pos.x = largura_tela - self.largura

        #pulo
        if (teclas[pygame.K_w] or teclas[pygame.K_SPACE]) and self.no_chao:
            self.vel_y = self.forca_pulo
            self.no_chao = False

        if teclas[pygame.K_s] and not(self.no_chao):
            self.vel_y += self.vel_baixo

        #movimentacao na vertical
        self.pos.y += self.vel_y * dt

        #verificacao se atravessou chao
        if (self.pos.y >= chao - self.altura):
            
            self.pos.y = chao - self.altura
            self.vel_y = 0
            self.no_chao = True
        
        if not(self.no_chao):
            if movendo:
                self.mudar_estado("jump_side")
            else:
                self.mudar_estado("jump_facing")
        else:
            if movendo:
                self.mudar_estado("running")
            else:
                self.mudar_estado("idle")

        self.atualizar_animacao(dt)

        #atualizacao posicao
        self.rect.topleft = self.pos

    def atualizar_animacao(self, dt):
        self.tempo_animacao += dt

        if self.tempo_animacao >= self.vel_animacao:
            self.tempo_animacao = 0
            self.frame_atual += 1

            if self.frame_atual >= len(self.animacoes[self.estado]):
                self.frame_atual = 0

        imagem = self.animacoes[self.estado][self.frame_atual]

        if not self.olhando_direita:
            imagem = pygame.transform.flip(imagem, True, False)

        self.image = imagem

    def mudar_estado(self, novo_estado):
        if self.estado != novo_estado:
            self.estado = novo_estado
            self.frame_atual = 0
            self.tempo_animacao = 0
           
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
