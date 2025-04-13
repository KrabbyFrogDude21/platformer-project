import pygame
from constants import WIDTH, HEIGHT, PURPLE, ORANGE


class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        try:
            super().__init__()
            self.radius = 15
            self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  
            self.colour = PURPLE
            pygame.draw.circle(self.image, self.colour , (self.radius, self.radius), self.radius)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.active = True
            self.secret_way = True #Secret ending is active by default
        except Exception as e:
            print("Powerup initialisation error:", e)

    
    def activate(self, player):
        player.init_shot_cooldown = 10
        for bullet in player.bullets:
            bullet.speed = 20
        self.kill()
        player.bullet_speed = 20
