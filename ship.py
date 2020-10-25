import pygame

class Ship():
    def __init__(self, screen):
        """Initialition ship in the start position

        """
        self.screen = screen
        #Load image of ship and create rectagle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #A new ship will be created in the down edge of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Draw the ship in the current position

        """
        self.screen.blit(self.image, self.rect)
