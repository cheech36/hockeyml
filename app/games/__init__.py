import logging
import json
from requests import get
import datetime

from .. import db

class Games:
    def __init__(self):

        self.conn = db.Connection.connect()
        self.url = 'https://statsapi.web.nhl.com/api/v1/schedule'
        self.table = 'schedule'
        
        # Check to see that the dates stored in the table
        # are the current date
        self.__update__()


    def __update__(self):

        # Calls to python datetime.now() on the server also give
        # utc time so we must subtract 5 hours here as well
        nowEST = datetime.datetime.now() + datetime.timedelta(hours=-5)
        currentDate = nowEST.date()
        cur = self.conn.cursor()
        sql = '''
                 SELECT MAX(gametime) FROM schedule LIMIT 1;
              ''' 
        cur.execute(sql)
        gameTime = cur.fetchone()[0]  # Returns a datetime object

        # If the table is empty
        if( gameTime is None ):
            gameTime = datetime.datetime(1,1,1)
        
        # if the current date is not in the scedule call api
        if ( currentDate > gameTime.date() ):
            logging.debug("Warning Hitting API ...")
            response = get(self.url)
            data = json.loads(response.content)


            ## This is a workaround to avoid hitting api too much
            # import os
            # parDir = os.path.split(__file__)[0]
            # cached_path = os.path.join(parDir,'cached_games.json')
            # with open(cached_path, 'r') as jsonFile:
            #     data = json.load(jsonFile)
            ## end of workaround #
            
            schedule = []
            for game in data['dates'][0]['games']:
                dt = datetime.datetime
                time = game['gameDate']
                time = dt.strptime(game['gameDate'], '%Y-%m-%dT%H:%M:%SZ')
                # Adjust from UTC to EST
                time += datetime.timedelta(hours=-5)
                visitors = game['teams']['away']['team']['name']
                home = game['teams']['home']['team']['name']
                schedule.append([time, home, visitors])



            for game in schedule:
                            
                sql = '''
                      CREATE SEQUENCE IF NOT EXISTS 
                      id_sequence start 1 increment 1;
                      
                      INSERT INTO schedule (id, gametime, home, away)                                           
                      VALUES( nextval('id_sequence'), '{gametime}', 
                              '{home}', '{away}');
                  '''\
                  ''.format(gametime=str(game[0]),
                                 home=str(game[1]),
                                 away=str(game[2]))
                cur.execute(sql)
            self.conn.commit()
        cur.close()

                
    def getGames(self):
        
        sql = '''
                 SELECT DATE_TRUNC('hour', gametime), 
                        home, 
                        away 
                 FROM schedule
                 WHERE date_trunc('day', gametime) =
                 date_trunc('day', (NOW() - interval '5 hour'));
              '''
        cur = self.conn.cursor()
        cur.execute(sql)
        
        # Now get the rows from the table 
        schedule = cur.fetchall()
        
        # Convert the schedule from a tuple of tuples to a list of lists
        schedule = [game for game in map(lambda x: list(x), schedule )]

        # Remove the day information and convert to 12 hour format
        for game in schedule:
            game[0] = game[0].time().strftime("%I:%M %p")

        content = {'games':schedule} 
        return content 
        
