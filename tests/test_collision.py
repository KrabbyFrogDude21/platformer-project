
import pygame
from player import Player
from platforms import Platform

def test_player_on_platform():
    pygame.init()
    player = Player()
    platform = Platform(100, 400, 200, 50)

    player.rect.bottom = platform.rect.top + 1
    player.vel_y = 5  

    player.collide_platform([platform])

    assert player.rect.bottom == platform.rect.top
    assert player.on_ground

    pygame.quit()

