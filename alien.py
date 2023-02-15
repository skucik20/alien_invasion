import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class for one alien in enemy army"""

    def __init__(self, ai_game):
        """Initialization 1st alieon and his placement"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # import alien as rect
        self.image = pygame.image.load('images/alion_ship.bmp')
        self.rect = self.image.get_rect()

        # Placement new ship near left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storage x
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move left or right"""

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x