class GameStats():
    """ Tracking the statistics for the game """

    def __init__(self, ai_settings):
        """ Init statistics """
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """ Init statistics that is modifed in the process of the game """
        self.ship_left = self.ai_settings.ship_limit
