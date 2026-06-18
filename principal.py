#importações
import pygame
from pygame.locals import *
from sys import exit
from codigo.utilitarios.configuracao import *
from codigo.classes.itens import ItemColetavel 

#inicialização
pygame.init()
#Música de fundo
pygame.mixer.init()
pygame.mixer.music.load(ASSETS["SONS"]["MUSICA_FUNDO"])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#configurações iniciais
pygame.display.set_caption(NOME_JOGO)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


#relógio que dá ritmo ao jogo
relogio = pygame.time.Clock()


#Criação do grupo e sorteio inicial do item
grupo_itens = pygame.sprite.Group()
item_teste = ItemColetavel()
grupo_itens.add(item_teste)


#Variáveis de tempo/Cronômetro
tempo_inicio = pygame.time.get_ticks()
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
        #Futuro estado de encerramento do jogo ou reinicio (a ser implementado)
        print("Tempo esgotado! Fim de jogo.")
        pygame.quit()
        exit()


    #Lógica dos itens (útil para o futuro)
    grupo_itens.update()
    
    #pintando e atualizando tela
    tela.fill(COR_VERDE)
    
    #Desenho do item
    grupo_itens.draw(tela)
    
    pygame.display.flip()
    