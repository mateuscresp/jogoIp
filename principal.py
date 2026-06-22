#importações
import pygame
from pygame.locals import *
from sys import exit
from codigo.utilitarios.configuracao import *
from codigo.classes.itens import ItemColetavel 

#inicialização
pygame.init()


#configurações iniciais
pygame.display.set_caption(NOME_JOGO)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


#relógio que dá ritmo ao jogo
relogio = pygame.time.Clock()


#Carregamento de imagens
img_menu = pygame.image.load("recursos/cenarios/TELAINICIAL.png")
img_gameplay = pygame.image.load("recursos/cenarios/MAPA.png")
img_derrota = pygame.image.load("recursos/cenarios/TELADERROTA.png")
img_vitoria = pygame.image.load("recursos/cenarios/TELAVITORIA.png")


#Definição dos estados do jogo
ESTADO_MENU = "MENU"
ESTADO_GAMEPLAY = "GAMEPLAY"
ESTADO_GAME_OVER = "GAME_OVER"
ESTADO_VITORIA = "VITORIA"

estado_atual = ESTADO_MENU


#Criação do grupo e sorteio inicial do item
grupo_itens = pygame.sprite.Group()
item_teste = ItemColetavel()
grupo_itens.add(item_teste)


#Variáveis de tempo/Cronômetro
tempo_inicio = 0
segundo_anterior = -1
tempo_bonus_acumulado = 0

#Lógica de Cronômetro (adicionar bônus do colecionável)
def tempo_bonus(bonus):
    global tempo_bonus_acumulado
    tempo_bonus_acumulado += bonus


#Loop do jogo
while True:
    #atualizando relógio
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
            
            #Tecla de iniciar o jogo
            if estado_atual == ESTADO_MENU and event.key == K_SPACE:
                estado_atual = ESTADO_GAMEPLAY
                tempo_inicio = pygame.time.get_ticks()
                tempo_bonus_acumulado = 0
                segundo_anterior = -1
                grupo_itens.empty()
                grupo_itens.add(ItemColetavel())
            
            #Tecla de reiniciar o jogo:
            elif estado_atual in [ESTADO_GAME_OVER, ESTADO_VITORIA] and event.key == K_r:
                estado_atual = ESTADO_GAMEPLAY
                tempo_inicio = pygame.time.get_ticks()
                tempo_bonus_acumulado = 0
                segundo_anterior = -1
                grupo_itens.empty()
                grupo_itens.add(ItemColetavel())

    if estado_atual == ESTADO_GAMEPLAY:

        #Lógica de Cronômetro (cálculo)
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

        #Condição de fim de jogo
        if tempo_restante <= 0:
            estado_atual = ESTADO_GAME_OVER


        #Lógica dos itens (útil para o futuro)
        grupo_itens.update()
    
    #Desenho dinâmico baseado no estado atual
    if estado_atual == ESTADO_MENU:
        tela.blit(img_menu, (0, 0))
        
    elif estado_atual == ESTADO_GAMEPLAY:
        tela.blit(img_gameplay, (0, 0))
        grupo_itens.draw(tela)
        
    elif estado_atual == ESTADO_GAME_OVER:
        tela.blit(img_derrota, (0, 0))
        
    elif estado_atual == ESTADO_VITORIA:
        tela.blit(img_vitoria, (0, 0))
    
    pygame.display.flip()