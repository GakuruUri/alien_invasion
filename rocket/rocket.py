import pygame

class Rocket:
    """A class to manage the rocket."""
    
    def __init__(self, ai_game):
        """Initialize the rocket and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()
        
        # Start rocket center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
   
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the rocket's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed


        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)