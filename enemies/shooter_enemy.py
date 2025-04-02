from enemies.enemy import Enemy

class ShooterEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self, player):
        super().update(player) 
        super().shooting_logic(player)