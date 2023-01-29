import pygame


class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Import ship image
        self.image = pygame.image.load('images/ship_1.bmp')
        self.rect = self.image.get_rect()

        # Every new shim appires at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #
        self.x = float(self.rect.x)

        # default motion of ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating position of the ship"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object based on self.x value
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
