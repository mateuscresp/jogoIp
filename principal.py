#importações
import pygame
from pygame.locals import *
from sys import exit
from codigo.utilitarios.configuracao import *


#inicialização
pygame.init()


#configurações iniciais
pygame.display.set_caption(NOME_JOGO)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


#relógio que dá ritmo ao jogo
relogio = pygame.time.Clock()


#Loop do jogo
while True:
    #atualizando relógio
    relogio.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    #pintando e atualizando tela
    tela.fill(COR_VERDE)
    pygame.display.flip()
