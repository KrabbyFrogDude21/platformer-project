import pygame
from constants import WIDTH

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, colour, speed):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.image.fill(colour)
        self.rect = self.image.get_rect(midleft=(x, y))
        self.speed = speed
        self.vel_x = self.speed * direction 
        self.active = True

    def update(self, platforms, camera_x):
        self.rect.x += self.vel_x 
        if self.rect.x < camera_x or self.rect.x > camera_x + WIDTH:
            self.kill() #Ensure bullet doesn't continuously travel


        #Bullet destroyed during platform collision
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.active = False
                self.kill()  
                break