from dotenv import load_dotenv

load_dotenv()
import os
url=os.environ.get('MONGO_URL')
from pymongo import MongoClient
db_connection = MongoClient(url)
db = db_connection.fastapi
collection = db["cust"]