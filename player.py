import pygame
from constants import WIDTH, HEIGHT, camera_x, BLUE, GRAVITY, BLACK
from shooter import Shooter

class Player(Shooter):
    def __init__(self):
        super().__init__(100, HEIGHT - 100, BLUE)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.last_pressed = True  # Right is true, left is false
        self.health = 20
        self.init_shot_cooldown = 20
        self.bullet_speed = 7
        self.shot_cooldown = 0
        self.direction = 1
        self.powerup = False


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
                self.shoot(self.direction, BLUE, self.bullet_speed)
                self.shot_cooldown = self.init_shot_cooldown
        if self.shot_cooldown > 0:
            self.shot_cooldown -= 1

    def collide_platform(self, platforms):
        global camera_x
        self.rect.x += self.vel_x

        #Horizontal collision
        if self.rect.left < 0:
            self.rect.x = 0
        elif 3300 <= self.rect.x <= 3320 and self.rect.y > 150:
            self.rect.x = 3320
        elif 4080 <= self.rect.x and self.rect.y > 150:
            self.rect.x = 4080
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:  
                    self.rect.right = platform.rect.left
                    self.vel_x = 0
                if self.vel_x < 0:  
                    self.rect.left = platform.rect.right
                    self.vel_x = 0

        self.rect.y += self.vel_y
        self.on_ground = False

        #Vertical collision
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:  
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.vel_y = 0
                elif self.vel_y < 0:      
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
                break
    
        if self.rect.centerx > WIDTH // 2 and self.vel_x != 0:
            camera_x -= self.vel_x

    def collide_bullet(self, enemy_group):
        for enemy in enemy_group:
            for bullet in enemy.bullets:
                if self.rect.colliderect(bullet.rect):
                    bullet.kill()
                    self.health -= 20
                    print("Player health:",self.health)


    def teleport(self, new_x, new_y, camera_x):
        """
        Teleports the player to a new position, considering camera_x
        """
        # Adjust the teleport location by taking the camera_x into account
        self.rect.x = new_x - camera_x
        self.rect.y = new_y

    def collide_powerup(self, powerup_group):
        for powerup in powerup_group:
            if self.rect.colliderect(powerup.rect):
                powerup.activate(self)
                powerup.kill()
                self.powerup = True


    
    #Combined all player functions into 1 for code readability
    def update(self, enemy_group, keys, platforms, powerup_group):
        self.move(keys)
        self.collide_bullet(enemy_group)
        self.collide_platform(platforms)
        self.collide_powerup(powerup_group)

