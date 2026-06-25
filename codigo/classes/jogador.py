import pygame


#Classe do jogador
class Jogador:
    def __init__(self, velocidade, stamina, posicao, correndo, movimento, contador_sprites):
        velocidade=5

        self.velocidade=velocidade
        self.stamina=stamina
        self.posicao=posicao
        self.correndo=correndo
        self.movimento=movimento
        self.contador_sprites=contador_sprites

        #Carrega a imagem base para o jogador conseguir colidir
        self.image = pygame.image.load("recursos/imagens/pixil-frame-0.png")
        
        #Cria a caixa de colisão baseada no tamanho da imagem
        self.rect = self.image.get_rect()
        
        #Define a posição inicial do rect
        self.rect.topleft = self.posicao
        
        #Cria a máscara para colisão pixel-perfect (sugestão do Claude)
        self.mask = pygame.mask.from_surface(self.image)
        
    def stamina_regen(self ,correndo):
        
        #Ele só recupera a stamina se nao tiver correndo
        if not correndo:
            self.stamina += 10/60

        #Corrige pra nao ficar acima de 100
        if self.stamina > 100:
            self.stamina = 100




    def correr(self):
        if self.stamina >10/60 and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            return 8, self.stamina - 20/60 ,True
        return 5, self.stamina , False
    


    def andando(self,posicao_ney):
        x,y = posicao_ney[0], posicao_ney[1]
        velocidade,self.stamina,self.correndo = self.correr()



    #torre de ifs e elifs dos movimentos (fiz assim pq o movimento ficar mais rapido na diagonal é paia tlgd)
        if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
            x += velocidade-2
            y -= velocidade-2
            self.movimento="DIREITA"
            self.movimento_anterior="DIREITA"

        elif pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
            x -= velocidade-2
            y -= velocidade-2
            self.movimento="ESQUERDA"
            self.movimento_anterior="ESQUERDA"


        elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_d]:
            x += velocidade-2
            y += velocidade-2
            self.movimento="DIREITA"
            self.movimento_anterior="DIREITA"


        elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
            x -= velocidade-2
            y += velocidade-2
            self.movimento="ESQUERDA"
            self.movimento_anterior="ESQUERDA"

        elif pygame.key.get_pressed()[pygame.K_a]:
            x -= velocidade
            self.movimento="ESQUERDA"
            self.movimento_anterior="ESQUERDA"

        elif pygame.key.get_pressed()[pygame.K_d]:
            x += velocidade
            self.movimento="DIREITA"
            self.movimento_anterior="DIREITA"

            

        elif pygame.key.get_pressed()[pygame.K_w]:
            y -= velocidade
            self.movimento = self.movimento_anterior
            

        elif pygame.key.get_pressed()[pygame.K_s]:
            y += velocidade
            self.movimento = self.movimento_anterior
            
        
        else:
            self.movimento="PARADO"


        #limita as bordinhas
        if x > 700:
            x = 700

        if x < 0:
            x = 0

        if y > 500:
            y = 500

        if y < 0:
            y = 0



        return (x,y)






    def escolha_sprite(self):
        
        #ESCOLHA DE SPRITES
        #contador é baseado nos frames

        
        if self.movimento == "ESQUERDA" and self.contador_sprites>15 and self.correndo:
            if self.contador_sprites>30:
                self.contador_sprites=0
            self.contador_sprites+=1
            return pygame.transform.flip(pygame.image.load("recursos/imagens/NEYCORRENDO1.png") , True, False)
        
        elif self.movimento == "ESQUERDA" and self.correndo:
            self.contador_sprites+=1
            return pygame.transform.flip(pygame.image.load("recursos/imagens/NEYCORRENDO2.png") , True, False)
        
        elif self.movimento == "ESQUERDA" and self.contador_sprites>15:
            if self.contador_sprites>30:
                self.contador_sprites=0
            self.contador_sprites+=1
            return pygame.transform.flip(pygame.image.load("recursos/imagens/NEYANDANDO1.png") , True, False)        

        
        elif self.movimento == "ESQUERDA":
            self.contador_sprites+=1
            return pygame.transform.flip(pygame.image.load("recursos/imagens/NEYANDANDO2.png") , True, False)
    
        
        elif self.movimento == "DIREITA" and self.contador_sprites>15 and self.correndo:
            if self.contador_sprites>30:
                self.contador_sprites=0
            self.contador_sprites+=1
            return pygame.image.load("recursos/imagens/NEYCORRENDO1.png")

        
        elif self.movimento == "DIREITA" and self.correndo:
            self.contador_sprites+=1
            return pygame.image.load("recursos/imagens/NEYCORRENDO2.png")
        
        
        elif self.movimento == "DIREITA" and self.contador_sprites>15:
            if self.contador_sprites>30:
                self.contador_sprites=0
            self.contador_sprites+=1
            return pygame.image.load("recursos/imagens/NEYANDANDO1.png")
        
        
        elif self.movimento == "DIREITA":
            self.contador_sprites+=1
            return pygame.image.load("recursos/imagens/NEYANDANDO2.png")
        
        elif self.movimento == "PARADO":
            self.contador_sprites=0
            return pygame.image.load("recursos/imagens/NEYPARADO.png")







#=====================================#=====================================#====================================
