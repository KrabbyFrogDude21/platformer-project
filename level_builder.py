import pygame
from platforms import Platform
from powerup import Powerup
from enemies.bouncer import Bouncer
from enemies.shooter_enemy import ShooterEnemy

class LevelBuilder:
    def __init__(self):
        self.platforms = self.create_platforms()
        self.powerups = self.create_powerups()
        self.original_enemies = self.define_enemies()

    def create_platforms(self):
        platforms = [
            Platform(i * 400, 550, 400, 50) for i in range(11)  # Ground
        ] + [
            Platform(50, 500, 300, 50),
            Platform(200, 450, 100, 100),
            Platform(400, 450, 100, 20),
            Platform(700, 450, 100, 50),
            Platform(1000, 500, 100, 1050),
            Platform(1100, 430, 100, 960),
            Platform(1200, 360, 100, 910),
            Platform(1840, 500, 100, 1050),
            Platform(2200, 450, 100, 1000),
            Platform(1700, 320, 500, 10),
            Platform(2300, 320, 500, 10),
            Platform(1700, 220, 500, 10),
            Platform(2300, 220, 500, 10),
            Platform(2000, 120, 1000, 10),
            Platform(2800, 140, 10, 180),        
            Platform(2800, 480, 100, 1030),
            Platform(2700, 400, 100, 950),
            Platform(3100, 120, 600, 10),
            Platform(3800, 120, 600, 10),
            Platform(3800, 0, 10, 120),
            Platform(3200, 120, 10, 670),
            Platform(3400, 470, 25, 10),
            Platform(3950, 470, 25, 10),
            Platform(3550, 410, 25, 10),
            Platform(3800, 410, 25, 10),
        ]
        return platforms

    def create_powerups(self):
        return [Powerup(3600, 80)]

    def define_enemies(self):
        return [
            ("bouncer", 600, 550, 400, 800),
            ("bouncer", 1420, 550, 1320, 1720),
            ("shooter", 750, 450),
            ("bouncer", 1620, 550, 1320, 1720),
            ("shooter", 2500, 320),
            ("shooter", 2100, 320),
            ("shooter", 2500, 220),
            ("shooter", 2100, 220),
        ]

    def spawn_enemies(self):
        enemy_group = pygame.sprite.Group()
        for e in self.original_enemies:
            if e[0] == "bouncer":
                _, x, y, left, right = e #Refers to its parameters
                enemy_group.add(Bouncer(x, y, left, right))
            elif e[0] == "shooter":
                _, x, y = e 
                enemy_group.add(ShooterEnemy(x, y))
        return enemy_group
