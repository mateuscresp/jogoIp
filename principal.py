#importações
import pygame
from pygame.locals import *
from sys import exit
from codigo.utilitarios.configuracao import *
from codigo.classes.itens import Pamonha, Bandeira

#NEYMAR TEMPORÁRIO PARA TESTES
class JogadorTemporario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50)) # Um quadrado 50x50
        self.image.fill((255, 255, 0))        # Cor amarela
        self.rect = self.image.get_rect()

    def update(self):
        # Faz o quadrado seguir o mouse para facilitar o teste de colisão
        self.rect.center = pygame.mouse.get_pos()

#inicialização
pygame.init()


#configurações iniciais
pygame.display.set_caption(NOME_JOGO)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))


#relógio que dá ritmo ao jogo
relogio = pygame.time.Clock()

#CRIANDO A VARIÁVEL DO NEYMAR
neymar = JogadorTemporario()


#Criação do grupo e sorteio inicial do item
grupo_itens = pygame.sprite.Group()
item_teste = Pamonha()
grupo_itens.add(item_teste)

#Variáveis de controle
pamonhas_coletadas = 0
bandeiras_coletadas = 0
tempo_restante = 30  # Tempo inicial em segundos

#Variáveis do Gatilho da Bandeira
exibir_alerta = False
texto_alerta = ""
tempo_alerta_inicio = 0
meta_pamonhas = 5  # Quantidade para nascer uma bandeira



#Loop do jogo
while True:
    #atualizando relógio
    relogio.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Lógica dos itens
    grupo_itens.update()

    #FAZENDO NEYMAR SEGUIR O MOUSE
    neymar.update()

    
    # Colisão do Neymar com os itens do grupo
    # OBS: Aqui estou usando um 'neymar' hipotético. 
    itens_coletados = pygame.sprite.spritecollide(neymar, grupo_itens, True)
    
    for item in itens_coletados:
        # Verifica se o item coletado foi Pamonha
        if item.tipo == "pamonha": 
            tempo_restante += 3
            pamonhas_coletadas += 1
            print(f"Pamonha coletada! Tempo: {tempo_restante}s | Pamonhas: {pamonhas_coletadas}")
            
            #Bateu a meta para a bandeira nascer
            if pamonhas_coletadas == 5:
                nova_bandeira = Bandeira("Inglaterra")
                grupo_itens.add(nova_bandeira)
                exibir_alerta = True
                print("Bandeira da Inglaterra liberada!")
                
            elif pamonhas_coletadas == 10:
                nova_bandeira = Bandeira("Alemanha")
                grupo_itens.add(nova_bandeira)
                exibir_alerta = True
                print("Bandeira da Alemanha liberada!")
                
            elif pamonhas_coletadas == 15:
                nova_bandeira = Bandeira("Argentina")
                grupo_itens.add(nova_bandeira)
                exibir_alerta = True
                print("Bandeira da Argentina liberada!")
                
            elif pamonhas_coletadas == 20:
                nova_bandeira = Bandeira("Espanha")
                grupo_itens.add(nova_bandeira)
                exibir_alerta = True
                print("Bandeira da Espanha liberada!")
                
            elif pamonhas_coletadas == 25:
                nova_bandeira = Bandeira("Franca")
                grupo_itens.add(nova_bandeira)
                exibir_alerta = True
                print("Bandeira da França liberada!")
                
            else:
                #Se não bateu nenhum desses números redondos, nasce pamonha normal
                nova_pamonha = Pamonha()
                grupo_itens.add(nova_pamonha)
                
        #Verifica se o item coletado foi Bandeira
        elif item.tipo == "bandeira":
            tempo_restante += 5
            bandeiras_coletadas += 1
            print(f"Bandeira coletada! Tempo: {tempo_restante}s | Bandeiras: {bandeiras_coletadas}/5")
            #Faz a pamonha voltar depois de pegar a bandeira!
            nova_pamonha = Pamonha()
            grupo_itens.add(nova_pamonha)

    
    #pintando e atualizando tela
    tela.fill(COR_VERDE)
    
    #Desenho do item
    grupo_itens.draw(tela)

    #DESENHANDO O NEYMAR NA TELA
    tela.blit(neymar.image, neymar.rect)
    
    pygame.display.flip()