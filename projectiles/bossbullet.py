import math
from projectiles.projectile import Projectile
from constants import WIDTH

class BossBullet(Projectile):
    def __init__(self, x, y, target_x, target_y, colour, speed):
        super().__init__(x, y, speed, colour, width=10, height=10)

        dx = target_x - x
        dy = target_y - y
        distance = math.hypot(dx, dy) or 1  #Avoid zero division error
        self.vel_x = (dx / distance) * speed
        self.vel_y = (dy / distance) * speed

    def update(self, platforms, camera_x):
        super().update(camera_x)
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y 

