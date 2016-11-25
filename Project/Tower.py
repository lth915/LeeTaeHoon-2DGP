from pico2d import*
import main_state
from utility import *

class Tower:
    image = None
    range = None
    credit = None
    dmg = None

    def __init__(self, x, y, type):
        self.x, self.y, self.r = x, y, 25
        self.target = None
        self.activation = False

        if type == 1:
            self.image = load_image('resource/Tower_Laser.png')
            self.credit, self.range, self.dmg = 100, 150, 1
        elif type == 2:
            self.image = load_image('resource/Tower_Missile.png')
            self.credit, self.range, self.dmg = 150, 150, 1
        elif type == 3:
            self.image = load_image('resource/Tower_Radar.png')
            self.credit, self.range, self.dmg = 120, 150, 1

    def get_size(self):
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
        draw_rectangle(*self.get_size())
    pass


def add_tower():
    pass