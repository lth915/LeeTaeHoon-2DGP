from pico2d import*


class Enemy:
    image = None

    def __init__(self):
        self.x, self.y, self.r = -50, 375, 25
        self.hp, self.speed, self.type, self.reward = 1000, 0.2, 1, 10
        self.frame, self.dir = 0, 2
        self.font = load_font('Fonts/Myriad.otf')
        self.wave = False
        if Enemy.image == None:
            self.image = load_image('resource/Enemy Sprite.png')

    def update(self, frame_time):
        if self.wave == True:
            self.frame = (self.frame + 1) % 9
            if (self.x <= 1000) & (self.y == 375):
                self.dir = 2
                self.x += self.speed

    def size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 50, self.dir*50, 50, 50, self.x, self.y)
        self.font.draw(self.x - 30, self.y + 25, "[HP:%d]" % self.hp, (255, 0, 0))

    def draw_bb(self):
        draw_rectangle(*self.size())
    pass