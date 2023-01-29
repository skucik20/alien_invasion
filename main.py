import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        # Start main loop
        while True:
            # Waiting for button press
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            #print((len(self.bullets)))
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

        self.aliens.draw(self.screen)
        # Display modified screen
        pygame.display.flip()

    def _fire_bullet(self):
        """Create new bullet and add to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualization bullet placement, and delate invisible"""

        # Actualiztion bullet placement
        self.bullets.update()
        # Delate bullets that are out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Make alien army"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        # How much rows in screen?
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

        num_rows = available_space_y // (2 * alien_height)

        # Make row of aliens
        for row_number in range(num_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
