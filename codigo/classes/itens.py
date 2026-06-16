#Importações de bibliotecas e módulos
import random
import pygame
from codigo.utilitarios.configuracao import LARGURA_TELA, ALTURA_TELA

#Classe mãe dos colecionáveis
class ItemColetavel(pygame.sprite.Sprite):
    
    def __init__(self, largura_item=30, altura_item=30):
        super().__init__()
        
        #Quadrado amarelo temporário para testes
        self.image = pygame.Surface((largura_item, altura_item))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        
        #Lógica de Coordenadas Aleatórias (Respeitando os Limites)
        margem = 20 #Sujeita a ajustes pós testes
        
        #Sorteia um X entre a margem esquerda e o limite máximo da direita (largura da tela - tamanho do item - margem)
        self.rect.x = random.randint(margem, LARGURA_TELA - largura_item - margem)
        
        #Sorteia um Y entre a margem superior e o limite máximo de baixo (altura da tela - tamanho do item - margem)
        self.rect.y = random.randint(margem, ALTURA_TELA - altura_item - margem)