from constants import *
from shooter import Shooter

# Enemy Class (Shoots Every 3 Seconds)
class Enemy(Shooter):
    def __init__(self, x, y):
        super().__init__(x, y, RED)
        self.shoot_timer = 180  # 3 seconds at 60 FPS
        self.exist = True

    def update(self, platforms, player):
        if self.exist:
            if self.shoot_timer == 0:
                if self.rect.x > player.rect.x:
                    self.shoot(-1, RED)  
                    self.shoot_timer = 180
                else:
                    self.shoot(1, RED)  
                    self.shoot_timer = 180
            else:
                self.shoot_timer -= 1

            for bullet in player.bullets:
                if self.rect.colliderect(bullet.rect):
                    print("colldiede")
                    self.exist = False
                    self.kill()
                    bullet.kill()  # Remove the bullet
                    break   

        