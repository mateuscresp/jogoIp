import pygame

class Jogador:
    def __init__(self, velocidade, stamina, posicao):
        velocidade=5

        self.velocidade=velocidade

        self.stamina=stamina

        self.posicao=posicao
        
    def stamina_regen(self ,correndo):
        
        #Ele só recupera a stamina se nao tiver correndo
        if not correndo:
            self.stamina += 10

        #Corrige pra nao ficar acima de 100
        if self.stamina > 100:
            self.stamina = 100




    def correr(self):
        if self.stamina >= 20:
            return 8, self.stamina - 20
        return 5, self.stamina
    
    def andando(self,posicao_ney):
        x,y = posicao_ney[0], posicao_ney[1]
        velocidade = self.velocidade



    #torre de ifs e elifs dos movimentos (fiz assim pq o movimento ficar mais rapido na diagonal é paia tlgd)
        if pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_d]:
            x += velocidade-2
            y -= velocidade-2

        elif pygame.key.get_pressed()[pygame.K_w] and pygame.key.get_pressed()[pygame.K_a]:
            x -= velocidade-2
            y -= velocidade-2

        elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_d]:
            x += velocidade-2
            y += velocidade-2

        elif pygame.key.get_pressed()[pygame.K_s] and pygame.key.get_pressed()[pygame.K_a]:
            x -= velocidade-2
            y += velocidade-2

        elif pygame.key.get_pressed()[pygame.K_a]:
            x -= velocidade

        elif pygame.key.get_pressed()[pygame.K_d]:
            x += velocidade

        elif pygame.key.get_pressed()[pygame.K_w]:
            y -= velocidade

        elif pygame.key.get_pressed()[pygame.K_s]:
            y += velocidade


        #limita as bordinhas
        if x > 780:
            x = 780

        if x < 0:
            x = 0

        if y > 580:
            y = 580

        if y < 0:
            y = 0


        return (x,y)

        





#=====================================#=====================================#=====================================#========
