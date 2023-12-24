import json

import numpy as np

# from main import visualize_matrix


class Map:
    def __init__(self, h, w, maps_isl):
        self.map = np.zeros((h*2, w*2))

        self._mark_island(maps_isl)

        self.enemy_ship = []

    def _mark_island(self, maps_isl):
        for map_info in maps_isl:
            x = map_info['start'][0]
            y = map_info['start'][1]

            sectors = map_info['map']
            for delta_y in range(len(sectors)):
                for delta_x in range(len(sectors[0])):
                    if sectors[delta_y][delta_x] != 0:
                        self.map[x+delta_x][y+delta_y] = 1

    def get_vicinity(self, position, radius_watching):
        x, y = position

        min_x = max(0, x - radius_watching)
        max_x = min(len(self.map), x + radius_watching + 1)
        min_y = max(0, y - radius_watching)
        max_y = min(len(self.map[0]), y + radius_watching + 1)

        submatrix = [row[min_y:max_y] for row in self.map[min_x:max_x]]

        for enemy in self.enemy_ship:
            enemy_x, enemy_y = enemy['x'], enemy['y']
            enemy_hp, enemy_max_hp, enemy_size = enemy['hp'], enemy['maxHp'], enemy['size']

            if min_x <= enemy_x < max_x and min_y <= enemy_y < max_y:
                submatrix[enemy_x - min_x][enemy_y - min_y] = (enemy_x, enemy_y, enemy_hp, enemy_max_hp, enemy_size)

        return submatrix


    def add_enemy(self, enemies):
        self.enemy_ship = []
        for enemy in enemies:
            self.enemy_ship.append(
                (enemy['x'], enemy['y'], enemy['hp'], enemy['maxHp'], enemy['size'])
            )

    def reset(self):
        self.enemy_ship = []


# if __name__ == '__main__':
#     with open('map.json', 'r') as file:
#         json_content = file.read()
#         json_map = json.loads(json_content)
#
#     height, width = json_map['height'], json_map['width']
#
#     obj = Map(height, width, json_map['islands'])
    # visualize_matrix(obj.map)
