def ColisaoPeixe(player, lista_peixes, pontos):

    for peixe in lista_peixes:

        if player.colliderect(peixe):
            print('colidiu')
            pontos += 1
            lista_peixes.pop(player.collidelist(lista_peixes))

    return pontos


  
def ColisaoObst(player_red, lixo):
    for lixo in lixo.obst_list:
        if player_red.colliderect(lixo):
            print('colidiu lixo')
# colisão peixe-player




