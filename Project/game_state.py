import game_framework
from pico2d import *
import math
import random
import main_state, function_library

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

class Tower:
    image = None
    def __init__(self):
        self.x, self.y, self.r = 175, 525, 25
        self.range, self.dmg, self.type = 100, 20, 1
        self.target = None
        if self.image == None:
            self.image = load_image('resource/Tower_Laser.png')

    def size(self):
        return (self.x - self.r - self.range), (self.y - self.r - self.range), \
               (self.x + self.r + self.range), (self.y + self.r + self.range)

    def draw(self):
        self.image.draw(self.x, self.y)


class Enemy:
    image = None

    def __init__(self):
        self.x, self.y, self.r = 50, 375, 25
        self.hp, self.speed, self.type, self.reward = 100, 5, 1, 10
        self.frame, self.dir = 0, 2
        if Enemy.image == None:
            self.image = load_image('resource/Enemy Sprite.png')

    def update(self):
        if wave == True:
            self.frame = (self.frame + 1) % 9
            if (self.x < 1000) & (self.y == 375):
                self.dir = 2
                self.x += self.speed

    def size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.dir*50, 50, 50, self.x, self.y)


def enter():
    global background, icon, enemy, enemies, tower
    global wave
    background = BackGround()
    enemy = Enemy()
    tower = Tower()
    icon = Icon()
    wave = False
    pass


def exit():
    pass


def handle_events():
    global wave

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if wave == False:
                wave = True
            else:
                wave = False


def update():
    global wave

    enemy.update()
    delay(0.05)


def draw():
    clear_canvas()
    background.draw()
    icon.drawTower1()
    icon.drawTower2()
    icon.drawTower3()
    icon.drawTower4()
    enemy.draw()
    tower.draw()
    update_canvas()
    pass


def pause():
    pass


def resume():
    pass






