import sys
import pygame

from time import sleep
from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from lose_screen import LoseScreen


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

        self.lose = LoseScreen(self)
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        # Start main loop
        while True:
            # Waiting for button press
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                #self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            else:
                print("LOSER")
                self.lose.blitime()

            # print((len(self.bullets)))
            self._update_screen()

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

    def _check_events_keydown_events(self, event):
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

    def _check_events_keyup_events(self, event):
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

    def _update_screen(self):
        """Update pictures on screen, move to now screen"""
        self.screen.fill(self.settings.bg_color)
        if self.stats.game_active == True:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        else:
            self.lose.blitime()
            self.aliens.empty()

        self.aliens.draw(self.screen)
        # Display modified screen
        pygame.display.flip()

    def _fire_bullet(self):
        """Create new bullet and add to bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualization bullet placement, and delete invisible"""

        # Actualization bullet placement
        self.bullets.update()
        # Delete bullets that are out of screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reaction for collision bullets and aliens"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Remove rest of bullets, and make another fleet
            self.bullets.empty()
            self._create_fleet()


    def _create_fleet(self):
        """Make alien army"""
        self.settings.alien_speed += 0.5
        print(self.settings.alien_speed)

        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

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

    def _check_fleet_edges(self):
        """Proper reaction if alien touch edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move fleet down and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update placement of the aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        # Collisions between ship and alien
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship has been hit")
            self._ship_hit()

        # Collisions between ship and bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Reaction for alien-ship collision"""
        # Reduction value stored in ships_left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Delete the contents of the list aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and move ship to the center
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
    def _check_aliens_bottom(self):
        """Check if alien touch the bottom of the screen"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
