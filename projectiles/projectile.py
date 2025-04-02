import pygame
from constants import WIDTH

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, colour, width=20, height=5):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect(midleft=(x, y))
        self.speed = speed
        self.active = True

    def update(self, camera_x):
        # Remove if out of screen bounds
        if self.rect.x < camera_x or self.rect.x > camera_x + WIDTH:
            self.kill()  

    def collide_platforms(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.active = False
                self.kill()
                break
