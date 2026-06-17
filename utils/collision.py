def ColisaoPeixe(player_red, peixe):
    for peixe in peixe.fish_list:
        if player_red.colliderect(peixe):
            print('colidiu')


