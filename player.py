import pygame
from constants import *
from shooter import Shooter

class Player(Shooter):
    def __init__(self):
        try:
            super().__init__(100, HEIGHT - 100, BLUE)
            self.vel_x = 0
            self.vel_y = 0
            self.on_ground = False
            self.last_pressed = True
            self.health = 20
            self.init_shot_cooldown = 20
            self.bullet_speed = 10
            self.shot_cooldown = 0
            self.direction = 1
            self.powerup = False
            self.secret_powerup = False
        except Exception as e:
            print("Player initialization error:", e)

    def move(self, keys, powerup_group):
        global camera_x
        try:
            self.vel_x = 0
            self.vel_y += GRAVITY

            if keys[pygame.K_a]:
                self.vel_x = -5
                self.last_pressed = False

            if keys[pygame.K_d]:
                self.vel_x = 5
                self.last_pressed = True

            if keys[pygame.K_w] and self.on_ground:
                self.vel_y = -23
                self.on_ground = False

            if keys[pygame.K_SPACE]:
                self.direction = 1 if self.last_pressed else -1
                if self.shot_cooldown == 0:
                    self.shoot(self.direction, BLUE, self.bullet_speed)
                    self.shot_cooldown = self.init_shot_cooldown
            
                for powerup in powerup_group:
                    powerup.image.fill(ORANGE)
                    powerup.secret_way = False

            if self.shot_cooldown > 0:
                self.shot_cooldown -= 1
        except Exception as e:
            print("Player move error:", e)

    def collide_platform(self, platforms):
        global camera_x
        try:
            self.rect.x += self.vel_x

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
        except Exception as e:
            print("Player platform collision error:", e)

    def collide_bullet(self, enemy_group):
        try:
            if not enemy_group:
                return 
            
            for enemy in enemy_group:
                for bullet in enemy.bullets:
                    if self.rect.colliderect(bullet.rect):
                        bullet.kill()
                        self.health -= 20
                        print("Player health:", self.health)
            
        except Exception as e:
            print("Player bullet collision error:", e)

    def teleport(self, new_x, new_y, camera_x):
        try:
            self.rect.x = new_x - camera_x
            self.rect.y = new_y
        except Exception as e:
            print("Player teleport error:", e)

    def collide_powerup(self, powerup_group):
        try:
            for powerup in powerup_group:
                if self.rect.colliderect(powerup.rect):
                    if powerup.secret_way:
                        self.secret_powerup = True
                    else:
                        powerup.activate(self)
                        powerup.kill()
                        self.powerup = True
        except Exception as e:
            print("Player powerup collision error:", e)

    def update(self, enemy_group, keys, platforms, powerup_group):
        try:
            self.move(keys, powerup_group)
            self.collide_bullet(enemy_group)
            self.collide_platform(platforms)
            self.collide_powerup(powerup_group)
        except Exception as e:
            print("Player update error:", e)
