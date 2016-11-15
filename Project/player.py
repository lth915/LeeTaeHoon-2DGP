from pico2d import *
import game_state

#mode 0 = none / 1 = build


class Player:
    def __init__(self):
        self.mx, self.my = 0 ,0
        self.stage = 1
        self.life, self.credit, self.mode = 20, 300, 0
        self.font = load_font('Fonts/Myriad.otf')

    def size(self):
        return self.mx, self.my, self.mx, self.my

    def draw(self):
        self.font.draw(1066, 799 - 38, "STAGE %d" % self.stage, (255, 255, 255))
        self.font.draw(1030, 799 - 63, "CREDIT |  %d" % self.credit, (255, 255, 255))
        self.font.draw(1030, 799 - 88, "LIFE        |  %d" % self.life, (255, 255, 255))
    pass