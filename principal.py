#importações
import pygame
from pygame.locals import *
from sys import exit
from codigo.utilitarios.configuracao import *
from codigo.classes.itens import Pamonha, Bandeira
from codigo.classes.jogador import Jogador

#inicialização
pygame.init()


#configurações iniciais
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


#Definição dos estados do jogo
ESTADO_MENU = "MENU"
ESTADO_GAMEPLAY = "GAMEPLAY"
ESTADO_GAME_OVER = "GAME_OVER"
ESTADO_VITORIA = "VITORIA"

estado_atual = ESTADO_MENU


#Criação do grupo e sorteio inicial do item
grupo_itens = pygame.sprite.Group()
item_teste = Pamonha()
grupo_itens.add(item_teste)

#Cria o neymar na classe Jogador
#[Velocidade, Stamina, Posicao]
pos_inicial_x = LARGURA_TELA // 2
pos_inicial_y = ALTURA_TELA // 2
neymar = Jogador(5, 100, (pos_inicial_x, pos_inicial_y), False)

#Variáveis de controle
pamonhas_coletadas = 0
bandeiras_coletadas = 0
tempo_restante = 30

#Variáveis do Gatilho da Bandeira
exibir_alerta = False
texto_alerta = ""
tempo_alerta_inicio = 0
meta_pamonhas = 5

#Variáveis de tempo/Cronômetro
tempo_inicio = 0
segundo_anterior = -1
tempo_bonus_acumulado = 0

#Lógica de Cronômetro (adicionar bônus do colecionável)
def tempo_bonus(bonus):
    global tempo_bonus_acumulado
    tempo_bonus_acumulado += bonus

#Fins de teste de imagem do jogador(Neymar)
imagem_teste = pygame.image.load("recursos/imagens/pixil-frame-0.png")

#Loop do jogo
while True:
    #Atualização do relógio
    relogio.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Controle de estados por teclado:
        if event.type == KEYDOWN:

            #Tecla de fechar o jogo
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            
            #Tecla de iniciar o jogo (Espaço)
            if estado_atual == ESTADO_MENU and event.key == K_SPACE:
                estado_atual = ESTADO_GAMEPLAY
                tempo_inicio = pygame.time.get_ticks()
                tempo_bonus_acumulado = 0
                segundo_anterior = -1
                pamonhas_coletadas = 0
                bandeiras_coletadas = 0
                grupo_itens.empty()
                grupo_itens.add(Pamonha())

            #Tecla de reiniciar o jogo (R)
            elif estado_atual in [ESTADO_GAME_OVER, ESTADO_VITORIA] and event.key == K_r:
                estado_atual = ESTADO_GAMEPLAY
                tempo_inicio = pygame.time.get_ticks()
                tempo_bonus_acumulado = 0
                segundo_anterior = -1
                pamonhas_coletadas = 0
                bandeiras_coletadas = 0
                grupo_itens.empty()
                grupo_itens.add(Pamonha())

    #Lógica da gameplay
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
            if tempo_restante > 0:
                print(f"Tempo restante: {tempo_restante} segundos")
            segundo_anterior = segundos_passados

        #Condição de Fim de Jogo por tempo
        if tempo_restante <= 0:
            estado_atual = ESTADO_GAME_OVER

        #Movimentação do jogador e atualização do grupo de itens
        grupo_itens.update()
        
        #Sistema de andar e regeneração de stamina real
        neymar.posicao = neymar.andando(neymar.posicao)
        neymar.stamina_regen(neymar.correndo)
        
        #Sincronização da posição com rect para colisão
        neymar.rect.topleft = neymar.posicao

        #Física de Colisões e Sistema de Pontuação/Spawn
        itens_coletados = pygame.sprite.spritecollide(neymar, grupo_itens, True, pygame.sprite.collide_mask)
        
        for item in itens_coletados:
            if item.tipo == "pamonha": 
                tempo_bonus_acumulado += 3
                pamonhas_coletadas += 1
                print(f"Pamonha coletada! Total: {pamonhas_coletadas}")
                
                # Gatilhos de libertação das Bandeiras por metas
                if pamonhas_coletadas == 5:
                    grupo_itens.add(Bandeira("Inglaterra"))
                    exibir_alerta = True
                    texto_alerta = "Bandeira da Inglaterra liberada!"
                    tempo_alerta_inicio = pygame.time.get_ticks()
                
                elif pamonhas_coletadas == 10:
                    grupo_itens.add(Bandeira("Alemanha"))
                    exibir_alerta = True
                    texto_alerta = "Bandeira da Alemanha liberada!"
                    tempo_alerta_inicio = pygame.time.get_ticks()
                
                elif pamonhas_coletadas == 15:
                    grupo_itens.add(Bandeira("Argentina"))
                    exibir_alerta = True
                    texto_alerta = "Bandeira da Argentina liberada!"
                    tempo_alerta_inicio = pygame.time.get_ticks()
                
                elif pamonhas_coletadas == 20:
                    grupo_itens.add(Bandeira("Espanha"))
                    exibir_alerta = True
                    texto_alerta = "Bandeira da Espanha liberada!"
                    tempo_alerta_inicio = pygame.time.get_ticks()
                
                elif pamonhas_coletadas == 25:
                    grupo_itens.add(Bandeira("Franca"))
                    exibir_alerta = True
                    texto_alerta = "Bandeira da França liberada!"
                    tempo_alerta_inicio = pygame.time.get_ticks()
                
                else:
                    grupo_itens.add(Pamonha())
                    
            elif item.tipo == "bandeira":
                tempo_bonus_acumulado += 5
                bandeiras_coletadas += 1
                print(f"Bandeira coletada! Total: {bandeiras_coletadas}/5")
                grupo_itens.add(Pamonha())


    #Renderização das telas
    if estado_atual == ESTADO_MENU:
        tela.blit(img_menu, (0, 0))
        
    elif estado_atual == ESTADO_GAMEPLAY:
        tela.blit(img_gameplay, (0, 0)) # Fundo do mapa da develop
        grupo_itens.draw(tela)      
        
        # Desenha o sprite do jogador usando a lógica do Mateus
        tela.blit(imagem_teste, neymar.posicao) 
        
    elif estado_atual == ESTADO_GAME_OVER:
        tela.blit(img_derrota, (0, 0))
        
    elif estado_atual == ESTADO_VITORIA:
        tela.blit(img_vitoria, (0, 0))
    
    pygame.display.flip()
    