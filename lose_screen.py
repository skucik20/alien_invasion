import pygame

class LoseScreen:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Import ship image
        self.image = pygame.image.load('images/game_over.bmp')
        self.rect = self.image.get_rect()

        # Every new shim appires at the bottom of the screen
        self.rect.midbottom = self.screen_rect.center

    def blitime(self):
        self.screen.blit(self.image, self.rect)