from pico2d import*
import main_state
from utility import *

class Tower:
    image = None
    range = None
    credit = None
    dmg = None

    PIXEL_PER_METER = (10.0 / 100)
    RUN_SPEED_KMPH = 2000.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

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
            self.credit, self.range, self.dmg = 150, 200, 1
        elif type == 'Radar Tower':
            self.image = load_image('resource/Tower_Radar.png')
            self.credit, self.range, self.dmg = 120, 200, 1

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