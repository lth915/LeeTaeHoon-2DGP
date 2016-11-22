from pico2d import*
import random


class Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    def __init__(self, kind = 1, location = -50):
        self.x, self.y, self.r = location, 375, 25
        self.hp, self.speed, self.type, self.reward = 300, 0.2, kind, 10
        self.frame, self.total_frames, self.dir = 0, 0, 2
        self.font = load_font('Fonts/Myriad.otf')
        self.wave = False
        if Enemy.image == None:
            self.image = load_image('resource/Enemy Sprite.png')

    def update(self, frame_time):
        if self.wave == True:
            distance = Enemy.RUN_SPEED_PPS * frame_time
            self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
            self.frame = int(self.total_frames) % 8
            self.x += (self.dir * distance)

        #if self.wave == True:
            #self.frame = (self.frame + 1) % 9
            #if (self.x <= 1000) & (self.y == 375):
                #self.dir = 2
                #self.x += self.speed

    def size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 50, self.dir*50, 50, 50, self.x, self.y)
        self.font.draw(self.x - 30, self.y + 25, "[HP:%d]" % self.hp, (255, 0, 0))

    def draw_bb(self):
        draw_rectangle(*self.size())
    pass


def create_wave(enemies, stage):
    for i in range( 1 + (stage*1) ):
        if stage <= 3: t = 1
        elif stage <= 5: t = random.randint(1, 2)
        else: t = random.randint(1, 3)

        enemies.append(Enemy(t, -50 - (i*75) ))
