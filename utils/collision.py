def ColisaoPeixe(player, lista_peixes, lista_peixesrect, pontos, jogador): 


    for peixe in lista_peixes:   #Verifica todos os peixes na tela

        if player.colliderect(peixe.fish_rect):   #Se o jogador colidir com um peixe
            pontos += 1                 #Um ponto é adicionado

            if peixe.fish_buff == 'dourado':  #Se ele for dourado, ele recebe 5 pontos
                pontos += 4

            if peixe.fish_buff == 'velocidade':  # Se ele for do tipo velocidade, aumenta a velocidade do jogador
                jogador.vel_mov = 700
                condicao_temporizador_buff = True
            lista_peixes.pop(player.collidelist(lista_peixesrect))   #E o peixe é removido da tela
            lista_peixesrect.pop(player.collidelist(lista_peixesrect))

    return pontos, condicao_temporizador_buff


  





