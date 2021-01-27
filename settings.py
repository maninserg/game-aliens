class Settings():
    """ Class for saving all settings of game

    """
    def __init__(self):
        """ Initialition of settings of game

        """
        #Settings of screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #Settings of ship
        self.ship_limit = 3

        #Settings of bullet
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Settings of aliens
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings which are changed in the game's process """

        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction = 1 is move to the right, -1 is move to the left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed's settings """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


