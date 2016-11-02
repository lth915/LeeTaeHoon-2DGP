import game_framework
from pico2d import *
import math
import random
import main_state

name = "MainState"


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Ingame.png')

    def draw(self):
        self.image.draw(600, 400)

class Icon:
    def __init__(self):
        self.Tower1 = load_image('resource/Icon_LaserTower.png')
        self.Tower2 = load_image('resource/Icon_MissileTower.png')
        self.Tower3 = load_image('resource/Icon_RadarTower.png')
        self.Tower4 = load_image('resource/Icon_AntiTower.png')

    def drawTower1(self):
        self.Tower1.draw(1050, 750)
    def drawTower2(self):
        self.Tower2.draw(1150, 750)
    def drawTower3(self):
        self.Tower3.draw(1050, 650)
    def drawTower4(self):
        self.Tower4.draw(1150, 650)


class Enemy1:
    image = None

    def __init__(self):
        self.x, self.y = -50, 425
        self.speed = 0
        self.frame = 1
        if Enemy1.image == None:
            self.image = load_image('resource/enemy1.png')

    def update(self):
        if (self.x < 225) & (self.y == 425):
            self.frame = 1
            self.x += self.speed
        elif (self.x == 225) & (self.y <= 425) & (self.y > 225):
            self.frame = 2
            self.y -= self.speed
        elif (self.x >= 225) & (self.x < 425) & (self.y == 225):
            self.frame = 1
            self.x += self.speed
        elif (self.x == 425) & (self.y >= 225) & (self.y < 475):
            self.frame = 0
            self.y += self.speed
        elif (self.x >= 425) & (self.x < 575) & (self.y == 475):
            self.frame = 1
            self.x += self.speed
        elif (self.x == 575) & (self.y <= 475) & (self.y > 325):
            self.frame = 2
            self.y -= self.speed
        elif (self.x >= 575) & (self.x <= 850) & (self.y == 325):
            self.frame = 1
            self.x += self.speed
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 60, 0, 60, 60, self.x, self.y)


def enter():
    global background
    global wave
    global sx, frame
    global enemy, enemies
    global gbtselect
    global icon
    sx = 325
    background = BackGround()
    enemy = Enemy1()
    icon = Icon()
    wave = False
    gbtselect = load_image('resource/gbtselect.png')
    pass


def exit():
    global background
    del(background)
    pass


def handle_events():
    global sx, wave, enemy

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
    pass


def update():
    enemy.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    icon.drawTower1()
    icon.drawTower2()
    icon.drawTower3()
    icon.drawTower4()
    enemy.draw()
    gbtselect.draw(sx, 75)
    update_canvas()
    pass


def pause():
    pass


def resume():
    pass






