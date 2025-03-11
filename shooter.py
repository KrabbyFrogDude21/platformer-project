import pygame
pygame.init()
from bullet import Bullet
from constants import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y, colour):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(colour)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.bullets = pygame.sprite.Group()


    def shoot(self, direction, colour):
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction, colour)
            self.bullets.add(bullet)


    def update_bullets(self, platforms):
        """Update and draw bullets"""
        self.bullets.update(platforms)
        for bullet in self.bullets:
            screen.blit(bullet.image, (bullet.rect.x + camera_x, bullet.rect.y))
