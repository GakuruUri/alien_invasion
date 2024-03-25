import sys
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    """A class to manage all game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

# Use below code when you dont want full screen
        # self.screen = pygame.display.set_mode(
        #         (self.settings.screen_width, self.settings.screen_height))
        # pygame.display.set_caption("uriroots Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()



    def run_game(self):
        """Start the mmain loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypressess and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position
        self.bullets.update()


        #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
                
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()









# import sys
# import pygame

# from settings import Settings
# from ship import Ship
# from bullet import Bullet


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize game and, create game resources."""
#         pygame.init()

#         self.clock = pygame.time.Clock()
#         self.settings = Settings()

#         ###self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#         ###self.settings.screen_width = self.screen.get_rect().width
#         ###self.settings.screen_height = self.screen.get_rect().height

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#          )
#         ###self.screen = pygame.display.set_mode((1200, 800))

#         pygame.display.set_caption("Planet uriroots🥷")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()

#         # set the background color
#         self.bg_color = (230, 230, 230)

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             # self.bullets.update()
#             self._update_bullets()

#             # # Get rid of bullets that have disappeared.
#             # for bullet in self.bullets.copy():
#             #     if bullet.rect.bottom < 0:
#             #         self.bullets.remove(bullet)

#             ### print(len(self.bullets))

#             self._update_screen()
#             self.clock.tick(60)
#             # Redraw the screen during each pass through the loop.
#             # Make the most recently drawn screen visible.

#     def _check_events(self):
#         # Watch for keyboard and mouse events.
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)

#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True

#         elif event.key == pygame.K_q:
#             sys.exit()

#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#             # Move the ship to the right
#             ###self.ship.rect.x += 1

#     def _fire_bullet(self):
#         """Creat a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet position.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)

#     def _update_screen(self):
#         """Update images on the screeb and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         # self.screen.fill(self.bg_color)
#         pygame.display.flip()


# # Check indentation
# if __name__ == "__main__":
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()
