import pygame
from constants import WIDTH, HEIGHT, WHITE, BLACK
from player import Player
from enemy import Enemy
from platforms import Platform
from powerup import Powerup

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("cool game")
        self.clock = pygame.time.Clock()
        self.camera_x = 0
        self.player = Player()
        self.enemy_group = pygame.sprite.Group()
        self.enemy = Enemy(600, HEIGHT - 50)
        self.enemy_group.add(self.enemy)
        self.platforms = [
            Platform(i * 400, HEIGHT - 50, 400, 50) for i in range(10)
        ] + [
            Platform(400, 450, 100, 20),
            Platform(700, 450, 100, 50),
            Platform(1000, 500, 100, 50),
            Platform(1400, 500, 150, 50),
            Platform(1800, 0, 10, 1000)
        ]

    def update_camera(self):
        if self.player.rect.centerx > WIDTH // 2:
            self.camera_x = self.player.rect.centerx - (WIDTH // 2)

    def draw(self, x, y, image):
        self.screen.blit(image, (x - self.camera_x, y))

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        return keys

    def update_game_state(self, keys):
        self.player.update(self.enemy_group, keys, self.platforms)
        self.enemy.update(self.player)
        self.player.bullets.update(self.platforms)
        for enemy in self.enemy_group:
            enemy.bullets.update(self.platforms)
        self.update_camera()

    def render_game(self):
        self.screen.fill(WHITE)
        for platform in self.platforms:
            self.draw(platform.rect.x, platform.rect.y, platform.image)
        self.draw(self.player.rect.x, self.player.rect.y, self.player.image)
        for enemy in self.enemy_group:
            self.draw(enemy.rect.x, enemy.rect.y, enemy.image)
        for bullet in self.player.bullets:
            self.draw(bullet.rect.x, bullet.rect.y, bullet.image)
        for enemy in self.enemy_group:
            for bullet in enemy.bullets:
                self.draw(bullet.rect.x, bullet.rect.y, bullet.image)
        pygame.display.update()

    def run(self):
        while self.running:
            keys = self.handle_events()
            self.update_game_state(keys)
            self.render_game()
            self.clock.tick(60)
        pygame.quit()