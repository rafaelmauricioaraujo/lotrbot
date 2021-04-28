from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE"))
db = client.dblotrbot

def get_heroes():

    cursor = db.heroes.find({})
    results = [hero for hero in cursor]
    heroes_list = ''
    for result in results:
        heroes_list += result['name'] + '\n'

    print('retrieving data from database - get heroes')
    return heroes_list


def get_heroes_attributes(hero):

    cursor = db.heroes.find({"name": hero})
    results = [item for item in cursor]
    message = ''

    for result in results:
        message = "the great {} is a hero from {} race and he always have his {} in hands".format(result['name'], result['race'], result['gears'][0]['main_gear']['name'])

    print('retrieving data from database - get heroes attributes')
    return message


def get_heroes_gears(hero):
    
    cursor = db.heroes.find({"name": hero})
    
    results = [item for item in cursor]
    gears = ""
    
    for result in results:
        gears = "His main weapon is a {} with {} damage and {} resistence".format(result['gears'][0]['main_gear']['name'], result['gears'][0]['main_gear']['damage'], result['gears'][0]['main_gear']['resistence'])
    
    print('retrieving data from database - get heroes gears')
    return gears


def close():
    return client.close()