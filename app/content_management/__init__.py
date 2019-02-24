import logging
logging.basicConfig(level=logging.DEBUG)

from .. import games

class CMS:
    def __init__(self):
        pass
    def load(self):
        games_today = games.Games()
        return games_today.getGames()
    
