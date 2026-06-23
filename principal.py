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
        self.image = pygame.Surface((50, 50)) 
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

    def update(self):
        #Faz o quadrado seguir o mouse para facilitar o teste de colisão
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

        #Atualização dos Elementos do Jogo
        grupo_itens.update()
        neymar.update() 

        #Física de Colisões e Sistema de Pontuação/Spawn
        itens_coletados = pygame.sprite.spritecollide(neymar, grupo_itens, True)
        
        for item in itens_coletados:
            
            if item.tipo == "pamonha": 
                tempo_bonus_acumulado += 3
                pamonhas_coletadas += 1
                print(f"Pamonha coletada! Total: {pamonhas_coletadas}")
                
                #Gatilhos de libertação das Bandeiras por metas
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
        
    #Renderização
    if estado_atual == ESTADO_MENU:
        tela.blit(img_menu, (0, 0))
        
    elif estado_atual == ESTADO_GAMEPLAY:
        tela.blit(img_gameplay, (0, 0))
        grupo_itens.draw(tela)      
        tela.blit(neymar.image, neymar.rect) 
        
    elif estado_atual == ESTADO_GAME_OVER:
        tela.blit(img_derrota, (0, 0))
        
    elif estado_atual == ESTADO_VITORIA:
        tela.blit(img_vitoria, (0, 0))
    
    pygame.display.flip()