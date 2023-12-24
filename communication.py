

class CommuncationBuffer:

    def __init__(self):
        # all good
        self.good_situation = {}

        # warning
        self.attention = {}
        self.level_attention = {}

        # need support
        self.weak_ship = {}

        # go to help
        self.helper_ship = {}

        # retreat
        self.retreat_ship = {}


    def see_enemy(self, id_ship, numbers_enemy):
        self.attention[id_ship] = [numbers_enemy]

    def need_help(self):
        return False