from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE"))
db = client.dblotrbot

def get_heroes():
    print('heores')
    return db.heroes.find({})

def get_heroes_attributes(hero):
    print('heroes attributes')
    return db.heroes.find({"name":hero})

def close():
    return client.close()