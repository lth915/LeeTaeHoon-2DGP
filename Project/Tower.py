from pico2d import*


class Tower:
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 0, 0, 0
        self.credit = 0
        self.target = None
        if self.image == None:
            self.image = load_image('resource/Tower_Radar.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


class Tower_Laser(Tower):
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 1, 20, 125
        self.credit = 120
        self.target = None
        if self.image == None:
            self.image = load_image('resource/Tower_Laser.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


class Tower_Missile(Tower):
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 2, 30, 150
        self.credit = 0
        self.target = None
        if self.image == None:
            self.image = load_image('resource/Tower_Missile.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass


class Tower_Radar(Tower):
    image = None
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 0
        self.type, self.dmg, self.range = 3, 0, 150
        self.credit = 0
        self.target = None
        if self.image == None:
            self.image = load_image('resource/Tower_Radar.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)
    pass