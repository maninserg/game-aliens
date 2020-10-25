import sys

import pygame

def check_events():
    """Process touchs of buttom keyboard and mouse

    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, ship):
    """Update screen and create a new screen

    """
    #For every step circle it refresh screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #Show the last screen
    pygame.display.flip()

