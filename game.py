import pygame
from constants import *
from player import Player
from enemies.bouncer import Bouncer
from enemies.shooter_enemy import ShooterEnemy
from enemies.boss import Boss
from platforms import Platform
from powerup import Powerup

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
        self.enemy_group = pygame.sprite.Group()
        self.boss_spawned = False
        self.powerup_group = pygame.sprite.Group()
        self.powerup1 = Powerup(3600, 80)
        self.powerup_group.add(self.powerup1)
        # Add enemies


        self.platforms = [
            Platform(i * 400, GROUND_HEIGHT, 400, 50) for i in range(11)  # Ground
        ] + [
            Platform(50, 500, 300, 50),
            Platform(200, 450, 100, 100),
            Platform(400, 450, 100, 20),
            Platform(700, 450, 100, 50),
            Platform(1000, 500, 100, 500 + GROUND_HEIGHT),
            Platform(1100, 430, 100, 430 + GROUND_HEIGHT),
            Platform(1200, 360, 100, 360 + GROUND_HEIGHT),
            Platform(1840, 500, 100, 500 + GROUND_HEIGHT),
            Platform(1840, 500, 100, 500 + GROUND_HEIGHT), 
            Platform(2200, 450, 100, 450 + GROUND_HEIGHT), #Block
            Platform(1700, 320, 500, 10),
            Platform(2300, 320, 500, 10),
            Platform(1700, 220, 500, 10),
            Platform(2300, 220, 500, 10),
            Platform(2000, 120, 1000, 10),
            Platform(2800, 140, 10, 180),        
            Platform(2800, 480, 100, 480 + GROUND_HEIGHT),
            Platform(2700, 400, 100, 400 + GROUND_HEIGHT),
            Platform(3100, 120, 600, 10),
            Platform(3800, 120, 600, 10),
            Platform(3800, 0, 10, 120),
            Platform(3200, 120, 10, 120 + GROUND_HEIGHT),
            Platform(3400, 470, 25, 10), #boss platform
            Platform(3950, 470, 25, 10), #boss platform
            Platform(3550, 410, 25, 10), #boss platform
            Platform(3800, 410, 25, 10) #boss platform
        ]
        self.original_enemies = [
            ("bouncer", 600, HEIGHT - 50, 400, 800),
            ("bouncer", 500 + 920, HEIGHT - 50, 400 + 920, 800 + 920),
            ("shooter", 750, 450),
            ("bouncer", 700 + 920, HEIGHT - 50, 400 + 920, 800 + 920),
            ("shooter", 2500, 320),
            ("shooter", 2100, 320),
            ("shooter", 2500, 220),
            ("shooter", 2100, 220),
        ]

        self.spawn_enemies()
        
    def spawn_enemies(self):
        self.enemy_group.empty()  # Clear current enemies
        for e in self.original_enemies:
            if e[0] == "bouncer":
                _, x, y, left, right = e
                self.enemy_group.add(Bouncer(x, y, left, right))
            elif e[0] == "shooter":
                _, x, y = e
                self.enemy_group.add(ShooterEnemy(x, y))

    def update_camera(self):
        if self.player.rect.y > 200 and self.player.rect.x >= 3320: #Enter boss arena
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
        if self.player.rect.y > 150 and self.player.rect.x >= 3320 and not self.boss_spawned:
            self.boss = Boss(3900, GROUND_HEIGHT - 50)
            self.enemy_group.add(self.boss)
            self.boss_spawned = True
            self.camera_x = 3320  # Lock the camera
        elif self.boss_spawned:
           if self.boss.exist == False:
                self.game_finished = True
        elif self.player.secret_powerup:
                self.game_finished = True


        self.player.update(self.enemy_group, keys, self.platforms, self.powerup_group)
        if keys[pygame.K_t]: 
            self.player.teleport(3300, 110, self.camera_x)
  
        for enemy in self.enemy_group:
            enemy.update(self.player) 
            enemy.bullets.update(self.platforms, self.camera_x)

        self.player.bullets.update(self.platforms, self.camera_x)
        mouse_x, mouse_y = pygame.mouse.get_pos()



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
