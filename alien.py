import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for one alien in enemy army"""

    def __init__(self, ai_game):
        """Initialization 1st alieon and his placement"""
        super().__init__()
        self.screen = ai_game.screen

        # import alien as rect
        self.image = pygame.image.load('images/alion_ship.bmp')
        self.rect = self.image.get_rect()

        # Placement new ship near left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storage x
        self.x = float(self.rect.x)