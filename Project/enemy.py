from pico2d import*
import random


class Enemy:
    PIXEL_PER_METER = (10.0 / 100)
    RUN_SPEED_KMPH = 2000.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None

    #Earth 40000km : Game 12Km = 3333 : 1


    def __init__(self, type = 1, start_x = -50, start_y = 375):
        self.x, self.y, self.r = start_x, start_y, 25
        self.frame, self.total_frames, self.dir = 0, 0, 2
        self.font = load_font('Fonts/Myriad.otf')
        self.activation = False

        if type == 1:
            self.image = load_image('resource/Enemy Sprite.png')
            self.hp, self.speed, self.reward = 100, 1, 10
        if type == 2:
            self.image = load_image('resource/Enemy Sprite.png')
            self.hp, self.speed, self.reward = 150, 1.5, 10
        if type == 3:
            self.image = load_image('resource/Enemy Sprite.png')
            self.hp, self.speed, self.reward = 100, 1.2, 10

    def update(self, frame_time):
        if self.activation == True:
            distance = self.speed * Enemy.RUN_SPEED_PPS * frame_time
            self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
            self.frame = int(self.total_frames) % 8
            self.x += (self.dir * distance)

    def get_size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 50, self.dir*50, 50, 50, self.x, self.y)
        self.font.draw(self.x - 30, self.y + 25, "[HP:%d]" % self.hp, (255, 0, 0))

    def draw_bb(self):
        draw_rectangle(*self.get_size())
    pass
