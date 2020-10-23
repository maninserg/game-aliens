import sys

import pygame

def run_game():
    """Initialization game and create screen

    """

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230) #Assingment color of background

    while True:
        """Look events keyboard and mouse

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(bg_color) # For every step refresh screen
            pygame.display.flip()

run_game()

