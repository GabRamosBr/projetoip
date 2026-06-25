def ColisaoPeixe(player, lista_peixes, pontos): 

    for peixe in lista_peixes:   #Verifica todos os peixes na tela

        if player.colliderect(peixe):   #Se o jogador colidir com um peixe
            print('colidiu')
            pontos += 1                 #Um ponto é adicionado
            lista_peixes.pop(player.collidelist(lista_peixes))   #E o peixe é removido da tela

    return pontos
def ColisaoCoração(player, lista_coracao, vidas): 

    for peixe in lista_coracao:   #Verifica todos os corações na tela

        if player.colliderect(peixe):   #Se o jogador colidir com um coração
            print('colidiu')
            if vidas < 3:
                vidas += 1                 #Um ponto é adicionado
            lista_coracao.pop(player.collidelist(lista_coracao))   #E o coração é removido da tela

    return vidas

def ColisaoObstaculo(player, lista_obstaculos, vidas):

    for obstaculo in lista_obstaculos[:]:

        if player.colliderect(obstaculo.retangulo):
            print('colidiu com obstáculo')
            vidas -= 1
            lista_obstaculos.remove(obstaculo)

    return vidas







