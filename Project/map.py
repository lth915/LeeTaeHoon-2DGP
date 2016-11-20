from pico2d import *
from game_state import *
from player import *
from tower import *

class Tile:
    def __init__(self, x = 500, y = 500):
        self.x, self.y = x, y
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

    for j in range(16):
        for i in range(20):
            matrix.append(Tile((i * 50) + 25, 799 - (j * 50 + 25)))
            print("%d:%d|%d:%d|%d" % (i, matrix[-1].x, j, matrix[-1].y, matrix[-1].data))

            #matrix.x = (i * 50) + 25
            #matrix.y = 799 - (j * 50 + 25)
            #print("%d:%d|%d:%d|%d" % (i, matrix.x, j, matrix.y, matrix.data))



    pass


def build_check(matrix, player):
    i, j = 0, 0

    #for j in range(16):
        #for i in range(20):

    pass
