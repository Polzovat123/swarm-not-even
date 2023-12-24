import logging
import time

import requests

from communication import CommuncationBuffer
from map import Map
from requestAdapter import DatsteamAPI
from ship import Ship

api = DatsteamAPI()
map_result = api.get_map()
map_world_url = map_result['mapUrl']
response = requests.get(map_world_url)
json_content = response.json()
map_world = Map(json_content['height'], json_content['width'], json_content['islands'])

id_our_ship = [1436]# input('write script ship: ')

scan = api.scan()['scan']

my_ships = scan['myShips']
enemy = scan['enemyShips']
tick = scan['tick']

fleet = []
for ship in my_ships:
    fleet.append(Ship(
        id=ship['id'],
        position=(ship['x'], ship['y']),
        size=ship['size'],
        size_max_hp=ship['maxHp'],
        current_hp=ship['hp'],
        speed=ship['speed'],
        mspeed=ship['maxChangeSpeed'],
        min_speed=ship['minSpeed'],
        delta=ship['maxChangeSpeed'],
        timeout=ship['cannonCooldown'],
        wait=ship['cannonCooldownLeft'],
        r=ship['cannonRadius'],
        scan_radius=ship['scanRadius'],
    ))

forum = CommuncationBuffer()

while True:
    scan = api.scan()['scan']

    my_ships = scan['myShips']
    enemy = scan['enemyShips']
    tick = scan['tick']

    map_world.add_enemy(enemy)
    logging.warning(f'{tick} Ship thing:')
    for ship in fleet:
        for info in my_ships:
            _id = info['id']
            if ship.id == _id :#and _id in id_our_ship:
                print(ship.id)
                ship.update_condition(
                    info
                )
                command = ship.do(
                    map_world
                )
                api.send_ship_commands(
                    command
                )
                break
    map_world.reset()
    time.sleep(3)