import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    # General class to manage game
    def __init__(self):
        # Game initialization
        pygame.init()

        self.settings = Settings()

        # Open app in small window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Open app in full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # Start main loop
        while True:
            # Waiting for button press
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Delate bullets that are out of screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print((len(self.bullets)))
            self._updatae_screen()


    def _check_events(self):
        """Reaction for mouse/keyboard click"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Moving to right
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_events_keyup_events(event)

    def _check_events_keydown_events(self,event):
        """Reaction for click button"""
        if event.key == pygame.K_RIGHT:
            # Move ship to right
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            # Move ship to left
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_events_keyup_events(self,event):
        """Reaction for unclick button"""
        if event.key == pygame.K_RIGHT:
            # Stop move right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop move left
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _updatae_screen(self):
        """Update pictures on screen, move to now screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Display modified screen
        pygame.display.flip()

    def _fire_bullet(self):
        """Create new bullet and add to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
