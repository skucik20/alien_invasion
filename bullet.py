import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class that represent managment of bullets"""

    def __init__(self, ai_game):
        """Build bullet object in place where ship actually is"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # making rectangle in 0,0 pont and then define proper place
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):

        # actualization bullet place
        self.y -= self.settings.bullet_speed
        # actualization bullet speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
