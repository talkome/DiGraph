import math

BLACK = 1
WHITE = 0
INFINITY = math.inf


class node_data:

    def __init__(self, key, pos=(0, 0, 0)):
        self.key = key
        self.weight = INFINITY
        self.tag = WHITE
        self.pos = pos
        self.info = ""

    def get_key(self):
        return self.key

    def get_tag(self):
        return self.tag

    def get_weight(self):
        return self.weight

    def get_info(self):
        return self.info

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def set_info(self, info):
        self.info = info

    def set_key(self, key):
        self.key = key

    def set_weight(self, weight):
        self.weight = weight

    def set_tag(self, tag):
        self.tag = tag

    def __str__(self):
        if self.info == '':
            return f"V{self.key}(w:{self.weight}, t:{self.tag}, p:{self.pos})"
        else:
            return f"V{self.key}(w:{self.weight}, t:{self.tag}, p:{self.pos}, i:{self.info})"

    def __repr__(self):
        if self.info == '':
            return f"V{self.key}(w:{self.weight}, t:{self.tag}, p:{self.pos})"
        else:
            return f"V{self.key}(w:{self.weight}, t:{self.tag}, p:{self.pos}, i:{self.info})"

    def __lt__(self, other):
        return self.weight < other.weight
