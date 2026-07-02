TEMPO_DE_JOGO = 0


def PontuacaoNaTela(fonte_padrao, screen, score):
    pontuacao_na_tela = fonte_padrao.render(f"Score: {score}", True, "black")
    screen.blit(pontuacao_na_tela, (1750, 20))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def BuffsNaTela(fonte_padrao, screen, invencibility_buff, temporizador_buff2, anzol, temporizador_buff1 ):

    if invencibility_buff == True:

        buff_invencibilidade_na_tela = fonte_padrao.render(f"{(10 - temporizador_buff2):.1f}", True, 'gray')
        screen.blit(buff_invencibilidade_na_tela, (1600, 20))


    if anzol.vel_mov > 500:

        buff_velocidade_na_tela = fonte_padrao.render(f"{(10 - temporizador_buff1):.1f}", True, 'red')
        screen.blit(buff_velocidade_na_tela, (1500,20))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def TempoNaTela(fonte_tempo, screen):
    global TEMPO_DE_JOGO    
    
    tempo_de_jogo_na_tela = fonte_tempo.render(f'{int(TEMPO_DE_JOGO)}', True, 'black')
    TEMPO_DE_JOGO += 1/60
    screen.blit(tempo_de_jogo_na_tela,(920,20))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------


def VidaNaTela(fonte_padrao, screen, anzol):
    vida_na_tela = fonte_padrao.render(f"Vidas: {anzol.vidas}", True, "red")
    screen.blit(vida_na_tela, (30, 20))


# ----------------------------- // ---------------------------------------- // --------------------------------- // ----------------------------------------------- // --------------------------------------------- // ---------------------------------------

