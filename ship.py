import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialition ship in the start position

        """
        self.screen = screen
        self.ai_settings = ai_settings
        #Load image of ship and create rectagle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #A new ship will be created in the down edge of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Save float coordinate center of ship
        self.center = float(self.rect.centerx)
        #Flags moving ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        #Update atribut rect of ship from self.center
        self.rect.centerx = self.center
    def blitme(self):
        """Draw the ship in the current position

        """
        self.screen.blit(self.image, self.rect)
