import pygame
from enemies.enemy import Enemy  
from projectiles.bossbullet import BossBullet
from constants import PURPLE, RED

class Boss(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.Surface((100, 100))  
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect(midleft=(x, y))
        self.health = 400
        self.speed = 1  
        self.shoot_timer = 120  
        self.exist = True  

    def update(self, player):
        super().update(player)
        self.move_towards_player(player)
        self.shoot_boss_bullet(player)
        if self.rect.colliderect(player.rect):
            player.health -= 100

    def move_towards_player(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

    def shoot_boss_bullet(self, player):
        if self.shoot_timer == 0:
            bullet = BossBullet(self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery, RED, 10)
            self.bullets.add(bullet)
            self.shoot_timer = 120  
        else:
            self.shoot_timer -= 1
