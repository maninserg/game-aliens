import sys

import pygame

from settings import Settings

from ship import Ship

def run_game():
    """Initialization game and create screen

    """

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create ship
    ship = Ship(screen)

    # Start main cycle of program
    while True:
        #Look events of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(ai_settings.bg_color) # For every step refresh screen
            ship.blitme()
            pygame.display.flip()

run_game()

