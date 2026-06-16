import random
import pygame

# Importando a largura e altura definidas no seu arquivo de configuração
from codigo.utilitarios.configuracao import LARGURA_TELA, ALTURA_TELA

class ItemColetavel(pygame.sprite.Sprite):
    """Classe mãe para todos os itens coletáveis do jogo."""
    
    def __init__(self, largura_item=30, altura_item=30):
        super().__init__()
        
        # Criando um quadrado amarelo temporário para testes
        self.image = pygame.Surface((largura_item, altura_item))
        self.image.fill((255, 215, 0)) # Cor dourada
        
        self.rect = self.image.get_rect()
        
        # --- LÓGICA DE COORDENADAS ALEATÓRIAS (RESPEITANDO OS LIMITES) ---
        margem = 20 # Distância mínima que o item deve ficar da borda da tela
        
        # Sorteia um X entre a margem esquerda e o limite máximo da direita (largura da tela - tamanho do item - margem)
        self.rect.x = random.randint(margem, LARGURA_TELA - largura_item - margem)
        
        # Sorteia um Y entre a margem superior e o limite máximo de baixo (altura da tela - tamanho do item - margem)
        self.rect.y = random.randint(margem, ALTURA_TELA - altura_item - margem)