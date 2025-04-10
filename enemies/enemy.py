from constants import *
from shooter import Shooter

# Enemy Class (Shoots Every 3 Seconds)
class Enemy(Shooter):
    def __init__(self, x, y):
        super().__init__(x, y, RED)
        self.init_shooter_timer = 120
        self.shoot_timer = self.init_shooter_timer
        self.bullet_speed = 10
        self.health = 40
        self.damage_take = 20
        self.exist = True

    def update(self, player):
        self.take_damage(player)

    def take_damage(self, player):
        for bullet in player.bullets:
            if self.rect.colliderect(bullet.rect):
                self.health -= self.damage_take
                print(self.health)
                bullet.kill()
                if self.health <= 0:
                    print("Fast Enemy Defeated!")
                    self.kill()

    def shooting_logic(self,player):
        if self.exist:
            if self.shoot_timer == 0:
                if self.rect.x > player.rect.x:
                    self.shoot(-1, RED, self.bullet_speed)  
                    self.shoot_timer = self.init_shooter_timer
                else: #Including if player.x = enemy.x
                    self.shoot(1, RED, self.bullet_speed)  
                    self.shoot_timer = self.init_shooter_timer
            else:
                self.shoot_timer -= 1
