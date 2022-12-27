import pymongo
import os
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME)-> None:
        try:
            if MongoDBClient.client is None:
                #mondo_db_url = "mongodb+srv://user:Atha786@mongodbuniversity.kpjg8sn.mongodb.net/test"
                MongoDBClient.client = pymongo.MongoClient(os.environ, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
