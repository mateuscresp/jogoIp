import pygame


#extremamente

class Jogador:
    def __init__(self, velocidade, stamina, posicao, correndo):
        velocidade=5

        self.velocidade=velocidade
        self.stamina=stamina
        self.posicao=posicao
        self.correndo=correndo
        
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
        if x > 700:
            x = 700

        if x < 0:
            x = 0

        if y > 500:
            y = 500

        if y < 0:
            y = 0



        return (x,y)

        





#=====================================#=====================================#====================================
