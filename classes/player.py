import pygame

#definição da classe Player
class Player:
    def __init__(self, largura, altura, vel_mov, x, y, gravity): #inicialização e atributos

        self.largura = largura #largura do retangulo de colisão
        self.altura = altura #altura do retangulo de colisao
        self.vel_mov = vel_mov #velocidade de movimento
        self.x = x #posição x
        self.y = y #posição y
        self.gravity = gravity #velocidade da gravidade

    #metodo andar para movimentação
    def andar(self, largura_tela): #é preciso considerar a largura da tela
        
        #se a posição x não atravessar a borda esquerda da tela
        if not(self.x <= 0): 

            #se o jogador estiver pressionando a tecla "a"
            if pygame.key.get_pressed()[pygame.K_a]:
                self.x -= self.vel_mov #posição x diminui baseado na velocidade de movimento

        #se a posição x não atravessa a borda direta da tela
        if not(self.x >= largura_tela - self.largura):

            #se o jogador estiver pressionando a tecla "d"
            if pygame.key.get_pressed()[pygame.K_d]:
                self.x += self.vel_mov #posição x aumenta baseado na velocidade de movimento

        #se a posição y não atravessa a borda superior da tela
        if not(self.y <= 0):

            #se o jogador estiver pressionando a tecla "w"
            if pygame.key.get_pressed()[pygame.K_w]:
                self.y -= self.vel_mov #posição y diminui baseado na velocidade de movimento

    #metodo gravidade para implementar gravidade
    def gravidade(self, altura_tela): #precisa-se considerar a altura da tela

        #se a posição y for menor ou igual que a altura da tela - altura do retangulo de colisão
        #ou seja, se o objeto não estiver tocando o chão
        if self.y <= altura_tela - self.altura:

            #a gravidade age sobre o personagem aumentando sua posição y
            self.y += self.gravity