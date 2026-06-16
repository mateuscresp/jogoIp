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


#Criação do grupo e sorteio inicial do item
grupo_itens = pygame.sprite.Group()
item_teste = ItemColetavel()
grupo_itens.add(item_teste)



#Loop do jogo
while True:
    #atualizando relógio
    relogio.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Lógica dos itens (útil para o futuro)
    grupo_itens.update()
    
    #pintando e atualizando tela
    tela.fill(COR_VERDE)
    
    #Desenho do item
    grupo_itens.draw(tela)
    
    pygame.display.flip()