import pygame
from constants import WIDTH, HEIGHT, WHITE, camera_x
from player import Player
from enemy import Enemy
from platforms import Platform
 
class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemy = Enemy(600, HEIGHT - 50)
        self.platforms = [
            Platform(i * 400, HEIGHT - 50, 400, 50) for i in range(10)
        ] + [
            Platform(400, 450, 100, 100),
            Platform(700, 450, 100, 50),
            Platform(1000, 500, 100, 50),
            Platform(1400, 300, 150, 50),
            Platform(1800, 500, 250, 50)
        ]

    def run(self):
        while self.running:
            self.screen.fill(WHITE)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.move(keys)
            self.player.update(self.platforms)
            self.enemy.update(self.platforms, self.player, self.player.bullets)

            # Draw everything
            for platform in self.platforms:
                self.screen.blit(platform.image, (platform.rect.x + camera_x, platform.rect.y))

            self.screen.blit(self.player.image, (self.player.rect.x + camera_x, self.player.rect.y))
            self.screen.blit(self.enemy.image, (self.enemy.rect.x + camera_x, self.enemy.rect.y))

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()