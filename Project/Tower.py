from pico2d import*
import main_state
from utility import *

class Tower:
    image = None
    range = None
    credit = None
    dmg = None

    def __init__(self, tile_x, tile_y, type):
        self.x, self.y, self.r = tile_x, tile_y, 25
        self.target = None
        self.wave = False

        if type == 1:
            self.image = load_image('resource/Tower_Laser.png')
            self.credit, self.range, self.dmg = 100, 150, 1
        elif type == 2:
            self.image = load_image('resource/Tower_Missile.png')
            self.credit, self.range, self.dmg = 150, 150, 1
        else:
            self.image = load_image('resource/Tower_Radar.png')
            self.credit, self.range, self.dmg = 120, 150, 1

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, enemy):
        if collide(self, enemy):
            self.target = enemy
            targeted = True
            pass

    def draw_bb(self):
        draw_rectangle(*self.size())
    pass


def add_tower():
    pass