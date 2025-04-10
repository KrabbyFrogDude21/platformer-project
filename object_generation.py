class ObjectGenerate:
    def __init__(self):
        self.platforms = [
            Platform(i * 400, GROUND_HEIGHT, 400, 50) for i in range(11)  # Ground
        ] + [
            Platform(50, 500, 300, 50),
            Platform(200, 450, 100, 100),
            Platform(400, 450, 100, 20),
            Platform(700, 450, 100, 50),
            Platform(1000, 500, 100, 500 + GROUND_HEIGHT),
            Platform(1100, 430, 100, 430 + GROUND_HEIGHT),
            Platform(1200, 360, 100, 360 + GROUND_HEIGHT),
            Platform(1840, 500, 100, 500 + GROUND_HEIGHT),
            Platform(1840, 500, 100, 500 + GROUND_HEIGHT), 
            Platform(2200, 450, 100, 450 + GROUND_HEIGHT), #Block
            Platform(1700, 320, 500, 10),
            Platform(2300, 320, 500, 10),
            Platform(1700, 220, 500, 10),
            Platform(2300, 220, 500, 10),
            Platform(2000, 120, 1000, 10),
            Platform(2800, 140, 10, 180),        
            Platform(2800, 480, 100, 480 + GROUND_HEIGHT),
            Platform(2700, 400, 100, 400 + GROUND_HEIGHT),
            Platform(3100, 120, 600, 10),
            Platform(3800, 120, 600, 10),
            Platform(3800, 0, 10, 120),
            Platform(3200, 120, 10, 120 + GROUND_HEIGHT),
            Platform(3400, 470, 25, 10), #boss platform
            Platform(3950, 470, 25, 10), #boss platform
            Platform(3550, 410, 25, 10), #boss platform
            Platform(3800, 410, 25, 10) #boss platform
        ]
        self.original_enemies = [
            ("bouncer", 600, HEIGHT - 50, 400, 800),
            ("bouncer", 500 + 920, HEIGHT - 50, 400 + 920, 800 + 920),
            ("shooter", 750, 450),
            ("bouncer", 700 + 920, HEIGHT - 50, 400 + 920, 800 + 920),
            ("shooter", 2500, 320),
            ("shooter", 2100, 320),
            ("shooter", 2500, 220),
            ("shooter", 2100, 220),
        ]
