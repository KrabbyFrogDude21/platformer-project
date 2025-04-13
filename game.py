import pygame
from constants import *
from player import Player

from enemies.boss import Boss

from level_builder import LevelBuilder

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.game_finished = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("cool game")
        self.clock = pygame.time.Clock()
        self.camera_x = 0
        self.player = Player()

        self.builder = LevelBuilder()
        self.platforms = self.builder.platforms
        self.powerup_group = pygame.sprite.Group(self.builder.powerups)
        self.original_enemies = self.builder.original_enemies
        self.enemy_group = self.builder.spawn_enemies()

        self.boss_spawned = False

    def spawn_enemies(self):
        self.enemy_group = self.builder.spawn_enemies()

    def update_camera(self):
        if self.player.rect.y > 200 and self.player.rect.x >= 3320: #Boss Arena
            self.camera_x = 3320  

        elif self.player.rect.centerx > WIDTH // 2:
            self.camera_x = self.player.rect.centerx - (WIDTH // 2)

    # Draws everything with the camera offset for scrolling camera
    def draw(self, x, y, image):
        self.screen.blit(image, (x - self.camera_x, y))

    def handle_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        return keys
    
    def check_game_end(self):
        if self.player.rect.y > 150 and self.player.rect.x >= 3320 and not self.boss_spawned:
            self.boss = Boss(3900, GROUND_HEIGHT - 50)
            self.enemy_group.add(self.boss)
            self.boss_spawned = True
            self.camera_x = 3320  
        elif self.boss_spawned:
           if self.boss.exist == False:
                self.game_finished = True
        elif self.player.secret_powerup:
                self.game_finished = True
        
    def update(self, keys):
        if self.player.health <= 0:
            if self.player.powerup:
                self.player.rect.midbottom = (3600,100)
                self.boss.kill()
                self.boss_spawned = False
            else:
                self.player.rect.midbottom = (100, 500)
                self.camera_x = 0 
                self.spawn_enemies()
            self.player.health = 20


        self.update_camera()
        self.check_game_end()

        self.player.update(self.enemy_group, keys, self.platforms, self.powerup_group)

        for enemy in self.enemy_group:
            enemy.update(self.player) 
            enemy.bullets.update(self.platforms, self.camera_x)

        self.player.bullets.update(self.platforms, self.camera_x)



    def render_game(self):
        self.screen.fill(WHITE)

        for platform in self.platforms:
            self.draw(platform.rect.x, platform.rect.y, platform.image)

        self.draw(self.player.rect.x, self.player.rect.y, self.player.image)

        for enemy in self.enemy_group:
            self.draw(enemy.rect.x, enemy.rect.y, enemy.image)
        for bullet in self.player.bullets:
            self.draw(bullet.rect.x, bullet.rect.y, bullet.image)

        # Draw enemy bullets, only if they have bullets
        for enemy in self.enemy_group:
            if hasattr(enemy, "bullets"):
                for bullet in enemy.bullets:
                    self.draw(bullet.rect.x, bullet.rect.y, bullet.image)

        for powerup in self.powerup_group:
            self.draw(powerup.rect.x, powerup.rect.y, powerup.image)

        pygame.display.update()

    def display_finish_screen(self):
        font = pygame.font.Font(None, 50)
        if self.player.secret_powerup:
            text = font.render("Secret Ending", True, (0, 255, 255))
        else:
            text = font.render("You Win!", True, (255, 255, 255))
        self.screen.fill(BLACK)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()


    def run(self):
        while self.running:
            try:
                self.clock.tick(60)
                keys = self.handle_events()
                if not self.game_finished:
                    self.update(keys)
                    self.render_game()
                else:
                    self.display_finish_screen()

            except Exception as e:
                print("Error occured:", e)
                pygame.quit()
