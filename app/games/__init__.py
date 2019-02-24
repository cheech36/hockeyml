import logging
import json
from requests import get
import datetime


class Games:
    def __init__(self):
        self.url = 'https://statsapi.web.nhl.com/api/v1/schedule'

    def getGames(self):
        
        response = get(self.url)
        data = json.loads(response.content)

        gameContent = []
        for game in data['dates'][0]['games']:
            dt = datetime.datetime
            
            time = dt.strptime(game['gameDate'], '%Y-%m-%dT%H:%M:%SZ')
            # Adjust from UTC to EST
            time += datetime.timedelta(hours=-5)
            time = time.strftime("%I:%M %p")
            visitors = game['teams']['away']['team']['name']
            home = game['teams']['home']['team']['name']
            gameContent.append([time, visitors, home])
        
        content = {'games':gameContent} 
        return content 
        
