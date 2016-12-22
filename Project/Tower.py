from pico2d import*
import main_state
import threading
from utility import *

class Tower:
    image = None
    range = None
    credit = None
    dmg = None
    timer = None
    sound = None

    PIXEL_PER_METER = (20 / 100)
    RUN_SPEED_KMPH = 2000.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1

    def __init__(self, x, y, type):
        self.x, self.y, self.r = x, y, 25
        self.target = None
        self.frame, self.total_frames, self.direction = 0, 0, 0
        self.type = type
        self.speed = 1
        self.delete = False
        self.selected = False
        self.image = load_image('resource/Tower_Laser.png')

        if type == 'Laser Tower':
            self.image = load_image('resource/Tower_Laser.png')
            self.sound = load_wav('Sounds/Laser.wav')
            self.credit, self.range, self.dmg = 100, 100, 0.05
        elif type == 'Missile Tower':
            self.image = load_image('resource/Tower_Missile.png')
            self.sound = load_wav('Sounds/Missile.wav')
            self.credit, self.range, self.dmg = 150, 150, 0.07
        elif type == 'Radar Tower':
            self.image = load_image('resource/Tower_Radar.png')
            self.credit, self.range, self.dmg = 120, 150, 0

    def get_size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def get_range(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def update(self, frame_time):
        self.total_frames += Tower.FRAMES_PER_ACTION * Tower.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if not self.target == None:
            if not collide_range(self, self.target):
                self.target = None

        if not self.target == None:
            if self.target.hp <= 0:
                self.target = None


        if not self.target == None:
            if direction_check(self, self.target) == 'TOP': self.direction = 0
            if direction_check(self, self.target) == 'TOP-RIGHT': self.direction = 1
            if direction_check(self, self.target) == 'RIGHT': self.direction = 2
            if direction_check(self, self.target) == 'RIGHT-BOTTOM': self.direction = 3
            if direction_check(self, self.target) == 'BOTTOM': self.direction = 4
            if direction_check(self, self.target) == 'BOTTOM-LEFT': self.direction = 5
            if direction_check(self, self.target) == 'LEFT': self.direction = 6
            if direction_check(self, self.target) == 'LEFT-TOP': self.direction = 7

    def draw(self):
        if self.type == 'Radar Tower':
            self.image.clip_draw(self.frame * 50, self.direction * 0, 50, 50, self.x, self.y)
        else:
            self.image.clip_draw(self.direction * 50, 0, 50, 50, self.x, self.y)
        if self.selected == True:
            draw_rectangle(*self.get_size())
            draw_rectangle(*self.get_range())

    def attack(self):
        if self.type == "Laser Tower":
            if self.target.type == 2: self.target.hp -= (self.dmg * 1.2 * self.speed)
            else: self.target.hp -= (self.dmg * self.speed)
        elif self.type == 'Missile Tower':
            if self.target.type == 1: self.target.hp -= (self.dmg * 1.2 * self.speed)
            else: self.target.hp -= (self.dmg * self.speed)

        if not self.type == 'Radar Tower':
            self.sound.play()

        print("attack")


    def draw_bb(self):
        draw_rectangle(*self.get_range())
    pass