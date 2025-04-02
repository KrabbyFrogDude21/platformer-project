import pygame
from player import Player
from enemies.enemy import Enemy
from platforms import Platform
from projectiles.bullet import Bullet
from constants import BLUE, RED, GREEN, WIDTH, HEIGHT


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  

def test_player_init():
    player = Player()
    assert player.rect.x == 80
    assert player.rect.y == HEIGHT - 140
    assert player.image.get_at((0, 0)) == BLUE
    assert player.init_shot_cooldown == 20
    assert player.player_bullet_speed == 7
    assert player.shot_cooldown == 0
    assert player.direction == 1
    assert player.exist == True

def test_enemy_init():
    enemy = Enemy(300, 400)
    assert enemy.rect.x == 280
    assert enemy.rect.y == 360
    assert enemy.image.get_at((0, 0)) == RED
    assert enemy.shoot_timer == 120
    assert enemy.enemy_bullet_speed == 7
    assert enemy.exist == True

def test_platform_init():
    platform = Platform(50, 60, 100, 20)
    assert platform.rect.x == 50
    assert platform.rect.y == 60
    assert platform.rect.width == 100
    assert platform.rect.height == 20
    assert platform.image.get_at((0, 0)) == GREEN

def test_bullet_init():
    bullet = Bullet(10, 20, 1, BLUE, 5)
    assert bullet.rect.midleft == (10, 20)
    assert bullet.image.get_at((0, 0)) == BLUE
    assert bullet.speed == 5
    assert bullet.vel_x == 5
    assert bullet.active == True

