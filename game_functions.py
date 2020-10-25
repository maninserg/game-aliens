import sys

import pygame

def check_keydown_events(event, ship):
    """Respond for key downs

    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond for key ups """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Process touchs of buttom keyboard and mouse

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """Update screen and create a new screen

    """
    #For every step circle it refresh screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #Show the last screen
    pygame.display.flip()

