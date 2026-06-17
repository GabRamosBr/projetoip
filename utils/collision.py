def ColisaoPeixe(player, lista_peixes, pontos):

    for peixe in lista_peixes:

        if player.colliderect(peixe):
            print('colidiu')
            pontos += 1
            lista_peixes.pop(player.collidelist(lista_peixes))

    return pontos
# colisão peixe-player




