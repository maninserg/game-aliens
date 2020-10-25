import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for control bullets

    """
    def __init__(self, ai_settings, screen, ship):
        super().__init__()

        self.screen = screen
        #Create bullet in position (0,0) and assign right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Position of bullet saves in float format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Update position bullet in floar format
        self.y -= self.speed_factor
        #Update position rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        """Output bullet to screen

        """
        pygame.draw.rect(self.screen, self.color, self.rect)
