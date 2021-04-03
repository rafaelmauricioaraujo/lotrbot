from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE"))
db = client.dblotrbot

def get_heroes():
    return db.heroes.find({})

def get_heroes_attributes(hero):
    return db.heroes.find_one({"name": hero})

def close():
    return client.close()