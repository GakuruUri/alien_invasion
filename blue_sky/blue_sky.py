"""
12-1. Blue Sky: Make a Pygame window with a blue background.

"""
import sys
import pygame

from settings import Settings


class Blue_Sky:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Blue Sky Game")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Redraw the screeen during each pass through
            self.screen.fill(self.settings.bg_color)
            
            
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    # Make an instance and run the game
    bsg = Blue_Sky()
    bsg.run_game()
        
        