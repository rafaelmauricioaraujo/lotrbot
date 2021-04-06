# import sys
# sys.path.append('.')

from database import get_heroes, close, get_heroes_attributes

def test_get_heroes():
    cursor = get_heroes()
    
    results = [hero for hero in cursor]
    heroes_list = ''
    
    for result in results:
        heroes_list += result['name'] + '\n'

    print(heroes_list)


def test_get_heroes_attributes(hero):
    
    cursor = get_heroes_attributes(hero)
    results = [item for item in cursor]
    # print('results: ', results)
    message = ''
    for result in results:
        # print('result: ', result['gears'][0]['main_gear']['name'])
        message = 'the great {} is a hero from {} race and he always have his {} in hands'.format(result['name'], result['race'], result['gears'][0]['main_gear']['name'])
    
    print(message)

# test_get_heroes()
test_get_heroes_attributes('menelcar')