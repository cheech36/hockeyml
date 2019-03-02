import os
import logging
import psycopg2
import configparser

class Connection:
    
    connected = False
    @classmethod
    def connect(cls):
        fileName = 'conn.config'
        parDir = os.path.split(__file__)[0]
        filePath = os.path.join(parDir, fileName)
        config = configparser.ConfigParser()
        config.read(filePath)
        host = config["connection"]["host"]
        dbname = config["connection"]["dbname"]
        user = config["connection"]["user"]
        password = config["connection"]["password"]

        
        
        if not(cls.connected):
            conn = psycopg2.connect(host=host, dbname=dbname,
                                user=user, password=password)

        cls.connected = True
            
        return conn
        
    @classmethod
    def close(cls):
        # call cls.conn.close()
        pass
