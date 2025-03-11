import pygame, time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRAVITY = 1.5

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Platformer")
clock = pygame.time.Clock()

# Camera offset
camera_x = 0


# Shooter Base Class
class Shooter(pygame.sprite.Sprite):
    def __init__(self, x, y, colour):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(colour)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.bullets = pygame.sprite.Group()


    def shoot(self, direction, colour):
            bullet = Bullet(self.rect.centerx, self.rect.centery, direction, colour)
            self.bullets.add(bullet)


    def update_bullets(self, platforms):
        """Update and draw bullets"""
        self.bullets.update(platforms)
        for bullet in self.bullets:
            screen.blit(bullet.image, (bullet.rect.x + camera_x, bullet.rect.y))


# Player Class
class Player(Shooter):
    def __init__(self):
        super().__init__(100, HEIGHT - 100, BLUE)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.last_pressed = True  # Right is true, left is false
        self.shot_cooldown = 0
        self.direction = 1

    def move(self, keys):
        global camera_x
        self.vel_x = 0
        self.vel_y += GRAVITY

        if keys[pygame.K_a]:
            self.vel_x = -5
            self.last_pressed = False
        if keys[pygame.K_d]:
            self.vel_x = 5
            self.last_pressed = True
        if keys[pygame.K_w] and self.on_ground:
            self.vel_y = -20
            self.on_ground = False
        if keys[pygame.K_SPACE]:
            if self.last_pressed:
                self.direction = 1
            else: 
                self.direction = -1
        
            if self.shot_cooldown == 0:    
                self.shoot(self.direction, BLUE)
                self.shot_cooldown = 20
            else:
                self.shot_cooldown -= 1

    def update(self, platforms):
        global camera_x
        self.rect.x += self.vel_x
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                    self.vel_x = 0
                if self.vel_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
                    self.vel_x = 0

        # Move vertically
        self.rect.y += self.vel_y
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  # Falling down
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.vel_y = 0
                elif self.vel_y < 0:  # Hitting head    
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
                break
    

        # Camera movement
        if self.rect.centerx > WIDTH // 2 and self.vel_x != 0:
            camera_x -= self.vel_x

        self.update_bullets(platforms)


# Enemy Class (Shoots Every Second)
# Enemy Class (Shoots Every 3 Seconds)
class Enemy(Shooter):
    def __init__(self, x, y):
        super().__init__(x, y, RED)
        self.shoot_timer = 180  # 3 seconds at 60 FPS

    def update(self, platforms, player, bullets):
        """Enemy shoots every 180 frames (~3 seconds)"""
        if self.shoot_timer == 0:
            if self.rect.x > player.rect.x:
                self.shoot(-1, RED)  
                self.shoot_timer = 180
            else:
                self.shoot(1, RED)  
                self.shoot_timer = 180
        else:
            self.shoot_timer -= 1

        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                self.kill()  # Kill the enemy
                bullet.kill()  # Remove the bullet
                break

        self.update_bullets(platforms)

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


# Platform Class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))


# Platforms
class Game:
    def __init__(self):
        self.running = True
        self.screen = screen
        self.clock = clock
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
        """Main game loop"""
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
