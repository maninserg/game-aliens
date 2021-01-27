import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

from game_stats import GameStats

import game_functions as gf

def run_game():
    """Initialization game and create screen

    """

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create game's statistics
    stats = GameStats(ai_settings)
    #Create ship
    ship = Ship(ai_settings, screen)
    #Create group of bullets
    bullets = Group()
    #Create alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Start main cycle of program
    while True:
        #Look events of keyboard and mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens,
                         bullets)
        #For every step refresh screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

