#importações
import pygame
from pygame.locals import *
from sys import exit
from codigo.utilitarios.configuracao import *
from codigo.classes.itens import Pamonha, Bandeira
from codigo.classes.jogador import Jogador

#inicialização
pygame.init()
pygame.mixer.init()  

pygame.display.set_caption(NOME_JOGO)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

#relógio que dá ritmo ao jogo
relogio = pygame.time.Clock()

#Carregamento de imagens
img_menu = pygame.image.load("recursos/cenarios/TELAINICIAL.png")
img_menu = pygame.transform.scale(img_menu, (LARGURA_TELA, ALTURA_TELA))

img_gameplay = pygame.image.load("recursos/cenarios/MAPA.png")
img_gameplay = pygame.transform.scale(img_gameplay, (LARGURA_TELA, ALTURA_TELA))

img_derrota = pygame.image.load("recursos/cenarios/TELADERROTA.png")
img_derrota = pygame.transform.scale(img_derrota, (LARGURA_TELA, ALTURA_TELA))

img_vitoria = pygame.image.load("recursos/cenarios/TELAVITORIA.png")
img_vitoria = pygame.transform.scale(img_vitoria, (LARGURA_TELA, ALTURA_TELA))

# Sons
try:
    som_pamonha = pygame.mixer.Sound(ASSETS["SONS"]["COLETA_PAMONHA"])
    som_bandeira = pygame.mixer.Sound(ASSETS["SONS"]["SPAWN_BANDEIRA"])
    som_game_over = pygame.mixer.Sound(ASSETS["SONS"]["GAME_OVER"])
    som_vitoria = pygame.mixer.Sound(ASSETS["SONS"]["VITORIA"])
    
    pygame.mixer.music.load(ASSETS["SONS"]["MUSICA_FUNDO"])
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f"Aviso ao carregar sons: {e}")

# Fonte
try:
    fonte_ui = pygame.font.Font(ASSETS["FONTES"]["FONTE_PRINCIPAL"], 24)
    fonte_alerta = pygame.font.Font(ASSETS["FONTES"]["FONTE_PRINCIPAL"], 36)
except:
    fonte_ui = pygame.font.SysFont("Arial", 24, bold=True)
    fonte_alerta = pygame.font.SysFont("Arial", 36, bold=True)

#Definição dos estados do jogo
ESTADO_MENU = "MENU"
ESTADO_GAMEPLAY = "GAMEPLAY"
ESTADO_GAME_OVER = "GAME_OVER"
ESTADO_VITORIA = "VITORIA"

estado_atual = ESTADO_MENU

# Inicialização do grupo de sprites e jogador
grupo_itens = pygame.sprite.Group()

pos_inicial_x = LARGURA_TELA // 2
pos_inicial_y = ALTURA_TELA // 2
neymar = Jogador(VELO_NEYMAR, STAMINA_MAX, (pos_inicial_x, pos_inicial_y), False)

#Variáveis de controle
pamonhas_coletadas = 0
bandeiras_coletadas = 0
tempo_restante = TEMPO_INICIAL

exibir_alerta = False
texto_alerta = ""
tempo_alerta_inicio = 0

tempo_inicio = 0
segundo_anterior = -1
tempo_bonus_acumulado = 0

# Função de reset
def resetar_jogo():
    """Reinicializa todas as variáveis do jogo para o estado inicial da gameplay."""
    global estado_atual, tempo_inicio, tempo_bonus_acumulado, segundo_anterior
    global pamonhas_coletadas, bandeiras_coletadas, exibir_alerta
    
    estado_atual = ESTADO_GAMEPLAY
    tempo_inicio = pygame.time.get_ticks()
    tempo_bonus_acumulado = 0
    segundo_anterior = -1
    pamonhas_coletadas = 0
    bandeiras_coletadas = 0
    exibir_alerta = False
    
    # Limpa e reinicia os itens
    grupo_itens.empty()
    grupo_itens.add(Pamonha())
    
    # Reseta o jogador para o centro da tela
    neymar.posicao = (LARGURA_TELA // 2, ALTURA_TELA // 2)
    neymar.rect.topleft = neymar.posicao

# Loop principal
while True:
    relogio.tick(FPS)
    
    # --- EVENTOS ---
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            
            #Tecla de iniciar o jogo (Espaço)
            if estado_atual == ESTADO_MENU and event.key == K_SPACE:
                resetar_jogo()
                # Tecla de reiniciar o jogo (R)
            elif estado_atual in [ESTADO_GAME_OVER, ESTADO_VITORIA] and event.key == K_r:
                resetar_jogo()
                try: 
                    pygame.mixer.music.play(-1)  # Reinicia a música de fundo global
                except: 
                    pass

    #Gameplay
    if estado_atual == ESTADO_GAMEPLAY:

        #Lógica do Cronómetro
        tempo_atual = pygame.time.get_ticks()
        segundos_passados = (tempo_atual - tempo_inicio) // 1000
        tempo_restante = TEMPO_INICIAL - segundos_passados + tempo_bonus_acumulado

        #Teto máximo do tempo
        if tempo_restante > TEMPO_MAX:
            tempo_restante = TEMPO_MAX
            tempo_bonus_acumulado = TEMPO_MAX - (TEMPO_INICIAL - segundos_passados)

        if segundos_passados != segundo_anterior:
            segundo_anterior = segundos_passados

        #Condição de Fim de Jogo por tempo
        if tempo_restante <= 0:
            estado_atual = ESTADO_GAME_OVER
            pygame.mixer.music.stop()
            try: 
                som_game_over.play()
            except: 
                pass

        #Movimentação do jogador e atualização do grupo de itens
        grupo_itens.update()
        neymar.posicao = neymar.andando(neymar.posicao)
        neymar.stamina_regen(neymar.correndo)
        
        #Sincronização da posição com rect para colisão
        neymar.rect.topleft = neymar.posicao

        #Física de Colisões e Sistema de Pontuação/Spawn
        itens_coletados = pygame.sprite.spritecollide(neymar, grupo_itens, True, pygame.sprite.collide_mask)
        
        for item in itens_coletados:
            if item.tipo == "pamonha":
                tempo_bonus_acumulado += 2
                pamonhas_coletadas += 1
                try: 
                    som_pamonha.play()
                except: 
                    pass
                
                # Garante que sempre existirá uma nova pamonha ativa
                grupo_itens.add(Pamonha())
                
                # Gatilhos de liberação das Bandeiras por metas
                bandeira_liberada = None
                if pamonhas_coletadas == 5: bandeira_liberada = "Inglaterra"
                elif pamonhas_coletadas == 10: bandeira_liberada = "Alemanha"
                elif pamonhas_coletadas == 15: bandeira_liberada = "Argentina"
                elif pamonhas_coletadas == 20: bandeira_liberada = "Espanha"
                elif pamonhas_coletadas == 25: bandeira_liberada = "Franca"
                
                if bandeira_liberada:
                    grupo_itens.add(Bandeira(bandeira_liberada))
                    exibir_alerta = True
                    texto_alerta = f"Bandeira da {bandeira_liberada} liberada!"
                    tempo_alerta_inicio = pygame.time.get_ticks()
                    try: 
                        som_bandeira.play()
                    except: 
                        pass
                    
            elif item.tipo == "bandeira":
                tempo_bonus_acumulado += 2
                bandeiras_coletadas += 1
                try: 
                    som_pamonha.play()
                except: 
                    pass
                
                #Condição de vitória 
                if bandeiras_coletadas == 5:
                    estado_atual = ESTADO_VITORIA
                    pygame.mixer.music.stop()
                    try: 
                        som_vitoria.play()
                    except: 
                        pass

    #Renderizar tela
    if estado_atual == ESTADO_MENU:
        tela.blit(img_menu, (0, 0))
        
    elif estado_atual == ESTADO_GAMEPLAY:
        tela.blit(img_gameplay, (0, 0))
        grupo_itens.draw(tela)     
        
        #Desenha o sprite do jogador
        try:
            tela.blit(neymar.image, neymar.posicao)
        except:
            tela.blit(imagem_teste, neymar.posicao)
        
        #Interface 
        txt_tempo = fonte_ui.render(f"Tempo: {tempo_restante}s", True, COR_PRETA)
        txt_pamonhas = fonte_ui.render(f"Pamonhas: {pamonhas_coletadas}", True, COR_PRETA)
        txt_bandeiras = fonte_ui.render(f"Bandeiras: {bandeiras_coletadas}/5", True, COR_PRETA)
        
        tela.blit(txt_tempo, (20, 20))
        tela.blit(txt_pamonhas, (20, 50))
        tela.blit(txt_bandeiras, (LARGURA_TELA - 220, 20))
        
        #Alerta Central temporizado
        if exibir_alerta:
            if pygame.time.get_ticks() - tempo_alerta_inicio < 2000:
                txt_msg = fonte_alerta.render(texto_alerta, True, (255, 223, 0))  # Amarelo Ouro
                rect_msg = txt_msg.get_rect(center=(LARGURA_TELA // 2, 120))
                tela.blit(txt_msg, rect_msg)
            else:
                exibir_alerta = False
        
    elif estado_atual == ESTADO_GAME_OVER:
        tela.blit(img_derrota, (0, 0))
        
    elif estado_atual == ESTADO_VITORIA:
        tela.blit(img_vitoria, (0, 0))
    
    pygame.display.flip()