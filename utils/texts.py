TEMPO_DE_JOGO = 0


def PontuacaoNaTela(fonte_pontuacao, screen, score):
    pontuacao_na_tela = fonte_pontuacao.render(f"{score}", True, "black")
    screen.blit(pontuacao_na_tela, (960, 20))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def BuffsNaTela(fonte_buffs, screen, invencibility_buff, temporizador_buff2, anzol, temporizador_buff1 ):

    if invencibility_buff == True:

        buff_invencibilidade_na_tela = fonte_buffs.render(f"{int(11 - temporizador_buff2)}", True, (112, 128, 144))
        screen.blit(buff_invencibilidade_na_tela, (940, 70))


    if anzol.vel_mov > 500:

        buff_velocidade_na_tela = fonte_buffs.render(f"{int(11 - temporizador_buff1)}", True, 'red')
        screen.blit(buff_velocidade_na_tela, (985, 70))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def TempoNaTela(fonte_tempo, screen):
    global TEMPO_DE_JOGO    
    
    tempo_de_jogo_na_tela = fonte_tempo.render(f'{int(TEMPO_DE_JOGO)}', True, 'black')
    TEMPO_DE_JOGO += 1/60
    screen.blit(tempo_de_jogo_na_tela,(1850,20))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def VidaNaTela(imagem_vida, imagem_vida_perdida, screen, anzol):
    if anzol.vidas == 3:
        screen.blit(imagem_vida, (20, 10))
        screen.blit(imagem_vida, (70, 10))
        screen.blit(imagem_vida, (120, 10))

    elif anzol.vidas == 2:
        screen.blit(imagem_vida, (20, 10))
        screen.blit(imagem_vida, (70, 10))
        screen.blit(imagem_vida_perdida, (120, 10))

    elif anzol.vidas == 1:
        screen.blit(imagem_vida, (20, 10))
        screen.blit(imagem_vida_perdida, (70, 10))
        screen.blit(imagem_vida_perdida, (120, 10))



# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------

