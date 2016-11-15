from pico2d import *
from game_state import *
from player import *
from tower import *

class Tile:
    def __init__(self):
        self.x, self.y = 500 ,500
        self.data = 0
        self.width, self.height = 24, 24
        self.slot = None

    def update(self):
        pass

    def draw(self):
        pass

    def size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


def map_create(matrix):
    i, j = 0, 0

    for j in range(16):
        for i in range(20):
            matrix.x = (i * 50) + 25
            matrix.y = 799 - (j * 50 + 25)
            print("%d:%d|%d:%d|%d" % (i, matrix.x, j, matrix.y, matrix.data))



    pass


def build_check(matrix, player):
    i, j = 0, 0

    #for j in range(16):
        #for i in range(20):

    pass
