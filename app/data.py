from os import getenv
from typing import Dict, Optional

from pymongo import MongoClient
from pandas import DataFrame
from dotenv import load_dotenv


class MongoDB:
    load_dotenv()
    url = getenv("MONGO_URL")
    database = getenv("DATABASE")
    collection = getenv("COLLECTION")

    def connect(self):
        return MongoClient(self.url)[self.database][self.collection]

    def dataframe(self, query: Optional[Dict] = None):
        return DataFrame(self.connect().find(
            filter=query,
            projection={"_id": False},
            limit=1000,
        ))
