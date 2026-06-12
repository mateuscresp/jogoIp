#importação
import pygame


#classe mãe
class ElementoJogo(pygame.sprite.Sprite):
    def __init__(self, caminho_imagem, coord_x, coord_y):
        super().__init__()
        
        try:
            self.image = pygame.image.load(caminho_imagem).convert_alpha()
        except(pygame.error, FileNotFoundError):
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y