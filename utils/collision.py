def ColisaoPeixe(player_red, peixe):
    for peixe in peixe.fish_list:
        if player_red.colliderect(peixe):
            print('colidiu peixe')



def ColisaoObst(player_red, lixo):
    for lixo in lixo.obst_list:
        if player_red.colliderect(lixo):
            print('colidiu lixo')
# colisão peixe-player
