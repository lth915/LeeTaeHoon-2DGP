from pico2d import*
import game_state


class Tower:
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 25
        self.range, self.dmg, self.type = 150, 1, 1
        self.credit = 100
        self.target = None
        self.wave = False
        if self.image == None:
            self.image = load_image('resource/Tower_Laser.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.size())
    pass


class LaserTower(Tower):
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 1, 20, 125
        self.credit = 120
        self.target = None
        self.wave = False
        if self.image == None:
            self.image = load_image('resource/Tower_Laser.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


class MissileTower(Tower):
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 2, 30, 150
        self.credit = 0
        self.target = None
        self.wave = False
        if self.image == None:
            self.image = load_image('resource/Tower_Missile.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


class RadarTower(Tower):
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 3, 0, 150
        self.credit = 0
        self.target = None
        self.wave = False
        if self.image == None:
            self.image = load_image('resource/Tower_Radar.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


def add_tower():
    pass