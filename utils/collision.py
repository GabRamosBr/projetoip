fish_collided = 'nenhum'

def ColisaoPeixe(player, lista_peixes, lista_peixesrect, pontos): 
    
    global fish_collided
    temporizador_buff = False #variáveis de inicialização
    
    for peixe in lista_peixes:   #Verifica todos os peixes na tela

        if player.colliderect(peixe):   #Se o jogador colidir com um peixe
            print('colidiu')
            pontos += 1                 #Um ponto é adicionado
            lista_peixes.pop(player.collidelist(lista_peixes))   #E o peixe é removido da tela
            
def ColisaoCoração(anzol, lista_coracao):

    for coracao in lista_coracao:   #Verifica todos os corações na tela

        if anzol.rect.colliderect(coracao):   #Se o jogador colidir com um coração
            anzol.curar()
            lista_coracao.pop(anzol.rect.collidelist(lista_coracao))   #E o coração é removido da tela

def ColisaoObstaculo(anzol, lista_obstaculos):

    for obstaculo in lista_obstaculos[:]:

        if anzol.rect.colliderect(obstaculo.retangulo):
            anzol.tomar_dano()
            lista_obstaculos.remove(obstaculo)







