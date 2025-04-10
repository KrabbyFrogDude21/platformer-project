import pygame
from constants import WHITE  

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 100))  
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
