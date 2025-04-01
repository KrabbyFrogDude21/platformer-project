from enemies.enemy import Enemy

class Bouncer(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vel_x = 10  

    def update(self, player, platforms):
        super().update(player) 
        self.rect.x += self.vel_x  

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.vel_x = -self.vel_x  
                self.rect.x += self.vel_x  
                break  
        