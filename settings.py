class Settings:
    def __init__(self):
        # Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 193, 37)
        self.ship_speed = 1.5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Value fleet direction 1 is move right, -1 is left
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
