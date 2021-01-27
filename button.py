import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """ Inizialition attributes of button """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Admin size and properties buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Draw object of button and put to the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message of button create only one time
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Transform msg to rectangle and put text to the center """
        self.msg_image = self.font.render (msg, True, self.text_color,
                                           self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Show clear button and create message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
