import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and, create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Planet uriroots🥷")
        
        self.ship = Ship(self)

        # set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            # Redraw the screen during each pass through the loop.           
            # Make the most recently drawn screen visible.
            
    
    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.rect.x += 1
            # Below code by me        
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         # Move the ship to the left
            #         self.ship.rect.x -= 1
                
    
    def _update_screen(self):
        """Update images on the screeb and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # self.screen.fill(self.bg_color)
        pygame.display.flip()
            


# Check indentation
if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
