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
        self.type = type

        if type == 'Laser Tower':
            self.image = load_image('resource/Tower_Laser.png')
            self.credit, self.range, self.dmg = 100, 150, 1
        elif type == 'Missile Tower':
            self.image = load_image('resource/Tower_Missile.png')
            self.credit, self.range, self.dmg = 150, 150, 1
        elif type == 'Radar Tower':
            self.image = load_image('resource/Tower_Radar.png')
            self.credit, self.range, self.dmg = 120, 150, 1

    def get_size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)

    def attack(self, enemy):
        if collide(self, enemy):
            enemy.hp -= self.dmg

    def draw_bb(self):
        draw_rectangle(*self.get_size())
    pass


def add_tower():
    pass