import pygame

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, colour, speed):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.image.fill(colour)
        self.rect = self.image.get_rect(midleft=(x, y))
        self.speed = speed
        self.vel_x = self.speed * direction #calculate velocity.
        self.active = True

    def update(self, platforms):
        self.rect.x += self.vel_x #use vel_x

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.active = False
                self.kill()  # Remove bullet if it collides with a platform
                break