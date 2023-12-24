import logging
import random


class Ship:
    def __init__(self, id, position, size, size_max_hp, current_hp, speed, mspeed,
                 min_speed, delta, timeout, wait, r, scan_radius, comfort_distance=30):
        self.id = id
        self.position = position
        self.size = size
        self.max_hp = size_max_hp
        self.hp = current_hp

        self.speed = speed
        self.maxSpeed = mspeed
        self.minSpeed = min_speed
        self.delta_speed = delta

        # Canon
        self.timeout = timeout
        self.wait = wait
        self.r = r
        self.scan_radius = scan_radius

        # Comfort
        self.comfort_dist = comfort_distance

    def watch_enviroment(self):
        ...

    def _have_enemy(self, submatrix):
        for i in range(len(submatrix)):
            for j in range(len(submatrix[0])):
                cell = submatrix[i][j]
                if isinstance(cell, tuple) and len(cell) == 5:
                    enemy_x, enemy_y, enemy_hp, enemy_max_hp, enemy_size = cell
                    return True  # Found an enemy

        return False

    def retreat(self):
        ...

    def atack(self):
        ...

    def update_condition(self, new_info):
        x = new_info.get('x')
        y = new_info.get('y')
        self.position = (x, y)

        self.size = new_info.get('size', self.size)
        self.hp = new_info.get('hp', self.hp)
        self.max_hp = new_info.get('maxHp', self.max_hp)
        self.speed = new_info.get('speed', self.speed)
        self.maxSpeed = new_info.get('maxSpeed', self.maxSpeed)
        self.minSpeed = new_info.get('minSpeed', self.minSpeed)
        self.delta_speed = new_info.get('maxChangeSpeed', self.delta_speed)
        self.timeout = new_info.get('cannonCooldown', self.timeout)
        self.wait = new_info.get('cannonCooldownLeft', self.wait)
        self.r = new_info.get('cannonRadius', self.r)
        self.scan_radius = new_info.get('scanRadius', self.scan_radius)


    def distance_watcher(self, vicinity):
        for i in range(len(vicinity)):
            for j in range(len(vicinity)):
                ...


    def find_scatter_path(self):
        ...

    def do(self, map):
        global forum

        vicinity = map.get_vicinity(self.position, self.scan_radius)
        if self._have_enemy(vicinity):
            # finding path to retreat
            change_speed = random.randint(-5, 5)
            rotate = random.choice([-90, 0, 90])
            cannon_shoot = {"x": random.randint(1, 100), "y": random.randint(1, 100)}

            logging.warning('i see the enemy')
        elif forum.need_help():
            # go to help
            change_speed = random.randint(-5, 5)
            rotate = random.choice([-90, 0, 90])
            cannon_shoot = {"x": random.randint(1, 100), "y": random.randint(1, 100)}

            logging.warning('go to help')
        else:
            # use vicinity map to finding path to not scatter with island
            change_speed = random.randint(-5, 5)
            rotate = random.choice([-90, 0, 90])
            cannon_shoot = {"x": random.randint(1, 100), "y": random.randint(1, 100)}

        if cannon_shoot is not None:
            command = {
                "ships": [
                    {
                        "id": self.id,
                        "changeSpeed": change_speed,
                        "rotate": rotate,
                        "cannonShoot": cannon_shoot
                    }
                ]
            }
            logging.warning('I start moving, and shouting')
        else:
            command = {
                "ships": [
                    {
                        "id": self.id,
                        "changeSpeed": change_speed,
                        "rotate": rotate,
                    }
                ]
            }
            logging.warning('swim...')

        return command