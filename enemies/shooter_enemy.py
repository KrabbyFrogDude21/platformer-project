from enemies.enemy import Enemy
from constants import ORANGE
class ShooterEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self, player):
        super().update(player) 
        super().shooting_logic(player) 

    #Altered version of inherited take_damage
    def take_damage(self, player):
        for bullet in player.bullets:
            if self.rect.colliderect(bullet.rect):
                self.health -= self.damage_take
                #print(self.health)
                bullet.kill()
                self.image.fill(ORANGE)  # Orange flash on damage
                if self.health <= 0:
                    #print("shooter enemy died!")
                    self.kill()
