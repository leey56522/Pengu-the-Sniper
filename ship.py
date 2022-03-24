import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/penguin2.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's x value, not the rect
        #print("OK WE ARE INSIDE UPDATE FUNCTION")
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #print("inside update right")
            #print("starting right x", self.rect.x)
            #print("change in right x", self.settings.ship_speed)
            self.x += self.settings.ship_speed
            #print("AFTER CHANGE ADDED", self.rect.x)
        if self.moving_left and self.rect.left > 0:
            #print("inside update left")
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        #print("CHANGE X", self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)