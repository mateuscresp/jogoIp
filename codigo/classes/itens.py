#Importações de bibliotecas e módulos
import random
import pygame
from codigo.utilitarios.configuracao import LARGURA_TELA, ALTURA_TELA, ASSETS

#Classe mãe dos colecionáveis
class Item(pygame.sprite.Sprite):
    
    def __init__(self, largura_item=30, altura_item=30):
        super().__init__()
        
        #Quadrado amarelo temporário para testes
        self.image = pygame.Surface((largura_item, altura_item), pygame.SRCALPHA)
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        
        #Lógica de Coordenadas Aleatórias (Respeitando os Limites)
        margem = 20 #Sujeita a ajustes pós testes
        
        #Sorteia um X entre a margem esquerda e o limite máximo da direita (largura da tela - tamanho do item - margem)
        self.rect.x = random.randint(margem, LARGURA_TELA - largura_item - margem)
        
        #Sorteia um Y entre a margem superior e o limite máximo de baixo (altura da tela - tamanho do item - margem)
        self.rect.y = random.randint(margem, ALTURA_TELA - altura_item - margem)

        self.mask = pygame.mask.from_surface(self.image)

#Pamonha (Herda do Item)
class Pamonha(Item):
    def __init__(self):
        super().__init__(largura_item=90, altura_item=90) #Roda o código da classe mãe
        self.tipo = "pamonha"
        try:
            original_image = pygame.image.load(ASSETS["IMAGENS"]["PAMONHA1"]).convert_alpha()
            self.image = pygame.transform.scale(original_image, (90, 90))
            print("Pamonha carregada com sucesso")

        except FileNotFoundError:
            print("Aviso: Arquivo recursos/imagens/Pamonha1.png não encontrado. Usando backup.")
            self.image.fill((255, 215, 0)) #Amarelo backup

        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

#Bandeira (Herda do Item)
class Bandeira(Item):

    def __init__(self, pais):
        super().__init__(largura_item=110, altura_item=110) #Roda o código da classe mãe
        self.tipo = "bandeira"
        self.pais = pais #Guarda qual país é essa bandeira
        try:
            chave = f"BANDEIRA_{pais.upper()}"
            original_image = pygame.image.load(ASSETS["IMAGENS"][chave]).convert_alpha()
            self.image = pygame.transform.scale(original_image, (110, 110))
        except (FileNotFoundError, KeyError):
            self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

#Taça da Copa do Mundo (Herda do Item)
class Taca(Item):
    def __init__(self):
        super().__init__(largura_item=120, altura_item=120) #Taça um pouco maior que os outros itens
        self.tipo = "taca"
        try:
            original_image = pygame.image.load(ASSETS["IMAGENS"]["TACA"]).convert_alpha()
            self.image = pygame.transform.scale(original_image, (120, 120))
        except FileNotFoundError:
            print("Aviso: Arquivo recursos/imagens/Taca.png não encontrado. Usando backup.")
            self.image.fill((218, 165, 32)) #Cor dourado
        
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)