from game import Game

def test_player_reset_on_death():
    game = Game()
    game.player.health = 0
    game.player.powerup = False
    game.update(None)  
    assert game.player.health == 20
    assert game.player.rect.midbottom == (100, 500)
