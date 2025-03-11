import pygame

# Bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, colour):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.image.fill(colour)
        self.rect = self.image.get_rect(midleft=(x, y))
        self.speed = 7 * direction
        self.active = True

    def update(self, platforms):
        self.rect.x += self.speed

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.active = False
                self.kill()  # Remove bullet if it collides with a platform
                break
