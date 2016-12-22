from pico2d import*
import random


class Enemy:
    PIXEL_PER_METER = (20.0 / 100)
    RUN_SPEED_KMPH = 2000.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    type = None

    #Earth 40000km : Game 12Km = 3333 : 1


    def __init__(self, type = 1, start_x = -50, start_y = 800 - 225):
        self.x, self.y, self.r = start_x, start_y, 25
        self.frame, self.total_frames, self.direction = 0, 0, 2
        self.font = load_font('Fonts/Myriad.otf')
        self.type = type
        self.attackedable = True
        self.state = 0

        if type == 1:
            self.image = load_image('resource/Enemy_Heli.png')
            self.hp, self.speed, self.reward = 100, 1, 10
        if type == 2:
            self.image = load_image('resource/Enemy_Flight.png')
            self.hp, self.speed, self.reward = 150, 1, 20
        if type == 3:
            self.image = load_image('resource/Enemy_Stealth.png')
            self.hp, self.speed, self.reward = 100, 1, 15
            self.attackedable = False
        if type == 4:
            pass

    def update(self, frame_time):
        distance = self.speed * Enemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if (self.state == 0) & (self.x <= 274):
            self.x += distance
            self.direction = 2
            if self.x >= 274:
                self.state = 1
        if (self.state == 1) & (self.y >= 800-575):
            self.y -= distance
            self.direction = 1
            if self.y <= 800-575:
                self.state = 2
        if (self.state == 2) & (self.y <= 800-575):
            self.x += distance
            self.direction = 2
            if self.x >= 475:
                self.state = 3
        if (self.state == 3) & (self.x >= 475):
            self.y += distance
            self.direction = 3
            if self.y >= 800-125:
                self.state = 4
        if (self.state == 4) & (self.y >= 800-125):
            self.x += distance
            self.direction = 2
            if self.x >= 875:
                self.state = 5
        if (self.state == 5) & (self.x >= 875):
            self.y -= distance
            self.direction = 1
            if self.y <= 800-275:
                self.state = 6
        if (self.state == 6) & (self.y <= 800-275):
            self.x -= distance
            self.direction = 0
            if self.x <= 625:
                self.state = 7
        if (self.state == 7) & (self.x <= 625):
            self.y -= distance
            self.direction = 1
            if self.y <= 800-425:
                self.state = 8
        if (self.state == 8) & (self.y <= 800-425):
            self.x += distance
            self.direction = 2
            if self.x >= 875:
                self.state = 9
        if (self.state == 9) & (self.x >= 875):
            self.y -= distance
            self.direction = 1
            if self.y <= 0:
                self.state = 10


    def get_size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 50, self.direction * 50, 50, 50, self.x, self.y)
        self.font.draw(self.x - 30, self.y + 25, "[HP:%d]" % self.hp, (255, 0, 0))

    def draw_bb(self):
        draw_rectangle(*self.get_size())
    pass
