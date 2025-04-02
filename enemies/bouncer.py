from enemies.enemy import Enemy

class Bouncer(Enemy):
    def __init__(self, x, y, x1, x2):
        super().__init__(x, y)
        self.health = 20
        self.x1 = x1
        self.x2 = x2
        self.vel_x = 7
        self.init_damage_timer = 20
        self.damage_timer = 20

    def update(self, player):
        super().update(player) 
        self.rect.x += self.vel_x  



        # Reverse direction when reaching x1 or x2
        if self.rect.x <= self.x1 or self.rect.x >= self.x2:
            self.vel_x = -self.vel_x  
        

        
        if self.rect.colliderect(player.rect) and self.damage_timer == 0:
            player.health -= 20
            self.damage_timer = self.init_damage_timer
            #print("Player health:",player)
        
        if self.damage_timer > 0:
            self.damage_timer -= 1