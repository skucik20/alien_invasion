class GameStats:
    """Monitoring game stats"""

    def __init__(self, ai_game):
        """Initialiation game stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Run aliens invasion in activ state
        self.game_active = True


    def reset_stats(self):
        """Changeing stats during game"""
        self.ships_left = self.settings.ship_limit
