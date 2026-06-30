TEMPO_DE_JOGO = 0


def PontuacaoNaTela(fonte_padrão, screen, score):
    pontuacao_na_tela = fonte_padrão.render(f"Score: {score}", True, "black")
    screen.blit(pontuacao_na_tela, (1750, 20))




def BuffsNaTela(fonte_padrão, screen, invencibility_buff, temporizador_buff2, anzol, temporizador_buff1 ):

    if invencibility_buff == True:

        buff_invencibilidade_na_tela = fonte_padrão.render(f"{(10 - temporizador_buff2):.2f}", True, 'gray')
        screen.blit(buff_invencibilidade_na_tela, (1600, 20))


    if anzol.vel_mov > 500:

        buff_velocidade_na_tela = fonte_padrão.render(f"{(10 - temporizador_buff1):.2f}", True, 'dark green')
        screen.blit(buff_velocidade_na_tela, (1500,20))



def TempoNaTela(fonte_padrão, screen, dt):
    global TEMPO_DE_JOGO    
    
    tempo_de_jogo_na_tela = fonte_padrão.render(f'{TEMPO_DE_JOGO:.1f}', True, 'black')
    TEMPO_DE_JOGO += dt
    screen.blit(tempo_de_jogo_na_tela,(920,20))





def VidaNaTela(fonte_padrão, screen, anzol):
    vida_na_tela = fonte_padrão.render(f"Vidas: {anzol.vidas}", True, "red")
    screen.blit(vida_na_tela, (30, 20))


