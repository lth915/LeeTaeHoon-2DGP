import game_framework
from pico2d import *
import math
import random
import main_state, function_library

from function_library import collide

name = "MainState"


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Ingame2.png')
        self.bgm = load_music('Sounds/Background_game.mp3')

    def draw(self):
        self.image.draw(600, 400)

    def music(self):
        self.bgm.repeat_play()

    def music_off(self):
        self.bgm.stop()

class Icon:
    def __init__(self):
        self.Tower1 = load_image('resource/Icon_LaserTower.png')
        self.Tower2 = load_image('resource/Icon_MissileTower.png')
        self.Tower3 = load_image('resource/Icon_RadarTower.png')

    def drawTower1(self):
        self.Tower1.draw(1049, 489)
    def drawTower2(self):
        self.Tower2.draw(1099, 489)
    def drawTower3(self):
        self.Tower3.draw(1149, 489)

class Player:
    def __init__(self):
        self.mx, self.my = 0 ,0
        self.life, self.credit, self.mode = 20, 0, 0

class Tower:
    image = None
    def __init__(self):
        self.x, self.y, self.r = 175, 525, 25
        self.range, self.dmg, self.type = 150, 1, 1
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
        self.hp, self.speed, self.type, self.reward = 10000, 0.2, 1, 10
        self.frame, self.dir = 0, 2
        if Enemy.image == None:
            self.image = load_image('resource/Enemy Sprite.png')

    def update(self):
        if wave == True:
            self.frame = (self.frame + 1) % 9
            if (self.x <= 1000) & (self.y == 375):
                self.dir = 2
                self.x += self.speed

    def size(self):
        return (self.x - self.r), (self.y - self.r), (self.x + self.r), (self.y + self.r)

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.dir*50, 50, 50, self.x, self.y)
        font.draw(self.x - 30, self.y + 25, "[HP:%d]" % self.hp, (255, 0, 0))


def enter():
    global background, icon, enemy, enemies, tower, font
    global wave
    global start
    background, tower, icon = BackGround(), Tower(), Icon()
    enemy, enemies = Enemy(), [Enemy() for i in range(20)]
    font = load_font('Fonts/Myriad.otf')
    wave = False
    start = 50

    background.music()
    for i in range(20):
        enemies[i].x -= start
        start += 75


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

    for enemy in enemies:
        if collide(tower, enemy):
            enemy.hp -= tower.dmg
        if enemy.hp <= 0:
            enemies.remove(enemy)
        enemy.update()


def draw():
    clear_canvas()
    background.draw()
    icon.drawTower1()
    icon.drawTower2()
    icon.drawTower3()
    for enemy in enemies:
        enemy.draw()
    tower.draw()
    update_canvas()
    pass


def pause():
    pass


def resume():
    pass






