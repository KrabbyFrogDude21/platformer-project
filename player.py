import pygame
from constants import WIDTH, HEIGHT, camera_x, BLUE, GRAVITY
from shooter import Shooter

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

        if self.rect.left < 0:
            self.rect.x = 0
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

