fish_collided = 'nenhum'

def ColisaoPeixe(player, lista_peixes, lista_peixesrect, pontos): 
    
    global fish_collided
    temporizador_buff = False #variáveis de inicialização
    
    for peixe in lista_peixes:   #Verifica todos os peixes na tela

        if player.colliderect(peixe.fish_rect):   #Se o jogador colidir com um peixe
            pontos += 1                           #Um ponto é adicionado
            temporizador_buff = True


            if peixe.fish_buff == 'dourado':  #Se ele for dourado
                pontos += 9                   # Vale 9 pontos a mais que um normal
                fish_collided = 'golden'


            elif peixe.fish_buff == 'velocidade':  # Se ele for do tipo velocidade
                pontos += 2                        # Ele também vale mais pontos que um normal mas menos que um dourado
                fish_collided = 'speed'            # E ativa a condicao de velocidade
             

            elif peixe.fish_buff == 'invencibilidade': # Se ele for do tipo invencibilidade
                pontos += 2 
                fish_collided = 'invencibility'        # Ativa a condicao de invencibilidade


            else:
                fish_collided = 'normal'    
                temporizador_buff = False        
            
        
            lista_peixes.pop(player.collidelist(lista_peixesrect))   # Por fim, o peixe é removido da tela
            lista_peixesrect.pop(player.collidelist(lista_peixesrect))  


    return pontos, temporizador_buff, fish_collided
  

# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def ColisaoCoração(anzol, lista_coracao):

    for coracao in lista_coracao:   #Verifica todos os corações na tela

        if anzol.rect.colliderect(coracao):   #Se o jogador colidir com um coração
            anzol.curar()
            lista_coracao.pop(anzol.rect.collidelist(lista_coracao))   #E o coração é removido da tela


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def ColisaoObstaculo(anzol, lista_obstaculos, invencibility_buff):

    if not invencibility_buff:
        for obstaculo in lista_obstaculos[:]:
    
            if anzol.rect.colliderect(obstaculo.retangulo):
                anzol.tomar_dano()
                lista_obstaculos.remove(obstaculo)







