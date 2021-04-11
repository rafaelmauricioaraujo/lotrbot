from pymongo import MongoClient
from dotenv import load_dotenv
import os

client = MongoClient(os.getenv("DATABASE"))
db = client.dblotrbot

from database import get_heroes, close, get_heroes_attributes

def test_get_heroes():
    cursor = get_heroes()
    
    results = [hero for hero in cursor]
    heroes_list = ''
    
    for result in results:
        heroes_list += result['name'] + '\n'

    print(heroes_list)


def test_get_heroes_attributes(hero):
    
    message = get_heroes_attributes(hero) 
    print(message)


def test_get_heroes_gears(hero):

    cursor = db.heroes.find({"name": hero})
    
    results = [item for item in cursor]
    gears = ""
    
    for result in results['gears']:
        print('result: ', result)
    

# test_get_heroes()
# test_get_heroes_attributes('menelcar')
test_get_heroes_gears('menelcar')