from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE"))
db = client.dblotrbot

def get_heroes():
    print('find heores called')
    return db.heroes.find({})

def close():
    return client.close()