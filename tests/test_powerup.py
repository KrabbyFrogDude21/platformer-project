from player import Player
from powerup import Powerup

def test_powerup_activation():
    player = Player()
    powerup = Powerup(200, 300)

    original_speed = player.bullet_speed


    powerup.activate(player)

    assert player.bullet_speed > original_speed
