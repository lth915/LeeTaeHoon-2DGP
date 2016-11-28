from pico2d import *
import main_state

#mode 0 = none / 1 = build


class Player:
    def __init__(self):
        self.stage = 1
        self.life, self.credit= 20, 300
        self.font = load_font('Fonts/Myriad.otf')

    def draw(self):
        self.font.draw(1066, 799 - 38, "STAGE %d" % self.stage, (255, 255, 255))
        self.font.draw(1030, 799 - 63, "CREDIT |  %d" % self.credit, (255, 255, 255))
        self.font.draw(1030, 799 - 88, "LIFE        |  %d" % self.life, (255, 255, 255))
    pass