from projectiles.projectile import Projectile

class Bullet(Projectile):
    def __init__(self, x, y, direction, colour, speed):
        super().__init__(x, y, speed * direction, colour)
    def update(self, platforms, camera_x):
        super().update(camera_x)
        super().collide_platforms(platforms)
        self.rect.x += self.speed  
