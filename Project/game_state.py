import game_framework
from pico2d import *
import math
import random
import main_state

from function_library import *
from icons import *

name = "MainState"


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Ingame2.png')
        self.bgm = load_music('Sounds/Background_game.mp3')
        self.open = load_wav('Sounds/WelcomeBack.wav')

    def draw(self):
        self.image.draw(600, 400)

    def music(self):
        self.open.play(1)
        self.bgm.repeat_play()

    def music_off(self):
        self.bgm.stop()
    pass

class Player:
    def __init__(self):
        self.mx, self.my = 0 ,0
        self.stage = 1
        self.life, self.credit, self.mode = 20, 300, 0
        self.selected = 0

    def size(self):
        return self.mx, self.my, self.mx, self.my

    def draw(self):
        font.draw(1066, 799 - 38, "STAGE %d" % self.stage, (255, 255, 255))
        font.draw(1030, 799 - 63, "CREDIT |  %d" % self.credit, (255, 255, 255))
        font.draw(1030, 799 - 88, "LIFE        |  %d" % self.life, (255, 255, 255))
    pass

class Tower:
    image = None
    def __init__(self):
        self.x, self.y, self.r = 225, 525, 25
        self.range, self.dmg, self.type = 150, 1, 1
        self.credit = 100
        self.target = None
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


class Enemy:
    image = None

    def __init__(self):
        self.x, self.y, self.r = -50, 375, 25
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

    def draw_bb(self):
        draw_rectangle(*self.size())
    pass


def enter():
    global background, player, enemy, enemies, tower, font
    global tower1, tower2, tower3, upgrade, sell, run, stop, accel, option, quit
    global Towersltd, Tssltd, Speedsltd, Setsltd
    global wave
    global start
    global click, alert_credit, alert_grid, alert_hp
    tower1, tower2, tower3, upgrade, sell, run, stop, accel, option, quit = Tower_Laser(), Tower_Missile(), Tower_Radar()\
        , Tower_Upgrade(), Tower_Sell(), Speed_Run(), Speed_Stop(), Speed_Accelerate(), Option(), Quit()

    Towersltd, Tssltd, Speedsltd, Setsltd = Tower_Selected(), Tsmall_Selected(), Speed_Selected(), Set_Selected()
    click = load_wav('Sounds/Click.wav')
    alert_credit = load_wav('Sounds/NotENF.wav')
    alert_grid = load_wav('Sounds/CantBuild.wav')
    alert_hp = load_wav('Sounds/UnderAttack.wav')

    background, tower= BackGround(), Tower()
    player = Player()
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
    global wave, player, icon

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            player.mx, player.my = event.x, 799 - event.y

            if collide(player, tower1): Towersltd.x = tower1.x
            elif collide(player, tower2): Towersltd.x = tower2.x
            elif collide(player, tower3): Towersltd.x = tower3.x
            else: Towersltd.x = 1400

            if collide(player, upgrade): Tssltd.y = upgrade.y
            elif collide(player, sell): Tssltd.y = sell.y
            else: Tssltd.y = 900

            if collide(player, run): Speedsltd.x = run.x
            elif collide(player, accel): Speedsltd.x = accel.x
            elif collide(player, stop): Speedsltd.x = stop.x
            else: Speedsltd.x = 1400

            if collide(player, option): Setsltd.x = option.x
            elif collide(player, quit): Setsltd.x = quit.x
            else: Setsltd.x = 1400

        elif event.type == SDL_MOUSEBUTTONDOWN:
            click.play()
            if collide(player, run): wave = True
            elif collide(player, accel):
                for enemy in enemies:
                    enemy.speed *= 2
            elif collide(player, stop): wave = False
            elif collide(player, quit): game_framework.push_state(main_state)

            if collide(player, tower1):
                if player.credit >= tower.credit:
                    player.mode = 1
                    player.credit -= tower.credit
                else:
                    alert_credit.play(1)
            elif collide(player, tower2):
                if player.credit >= tower.credit:
                    player.mode = 1
                    player.credit -= tower.credit
                else:
                    alert_credit.play(1)
            elif collide(player, tower3):
                if player.credit >= tower.credit:
                    player.mode = 1
                    player.credit -= tower.credit
                else:
                    alert_credit.play(1)
    pass


def update():
    global wave

    for enemy in enemies:
        if collide(tower, enemy):
            enemy.hp -= tower.dmg
        if enemy.hp <= 0:
            enemies.remove(enemy)
        enemy.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    player.draw()

    Speedsltd.draw()

    tower1.draw()
    tower2.draw()
    tower3.draw()
    upgrade.draw()
    sell.draw()
    run.draw()
    accel.draw()
    stop.draw()
    option.draw()
    quit.draw()


    Towersltd.draw()
    Tssltd.draw()
    Setsltd.draw()

    for enemy in enemies:
        enemy.draw()
        enemy.draw_bb()
    tower.draw()

    tower.draw_bb()

    update_canvas()
    pass


def pause():
    pass


def resume():
    pass






