import logging
logging.basicConfig(level=logging.DEBUG)

from .. import games
# from .. import game_prediction

class CMS:
    def __init__(self):
        pass
    
    def load(self):

        # content dict passed to homepage
        content = dict()

        # populate content with game schedule
        gm = games.Games()
        games_today = gm.getGames()

        # predictions
        # game_predictions = []
        # gm_pred = game_prediction.GamePrediction()
        # for game in games_today:
        #     teamHome = games_today[0]
        #     teamAway = games_today[1]
        #     prediction = gm_pred.predict(teamHome, teamAway)
        #     game.append(prediction)
        #     game_predictions.append(game)
        
        
        #logging.debug(type(games_today))
        game_predictions = games_today['games']  # temp code
        content['game_predictions'] = game_predictions
        
        # populate content with other fields to be displayed
        # on the hompage
        # foos_today = foo.Foos()
        # content.update( foos_today)

        content.update(games_today)
        return content
    
