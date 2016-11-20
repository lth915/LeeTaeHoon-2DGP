import game_framework
from pico2d import *
import math
import random
import main_state

from function_library import *
from icons import *
from map import *
from player import *
from tower import *
from enemy import *

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


def enter():
    global background, player, enemy, enemies, tower, towers, font
    global tower1, tower2, tower3, upgrade, sell, run, stop, accel, option, quit
    global Towersltd, Tssltd, Speedsltd, Setsltd
    global start
    global click, alert_credit, alert_grid, alert_hp
    global tile, tiles

    tower1, tower2, tower3, upgrade, sell, run, stop, accel, option, quit = Tower_Laser(), Tower_Missile(), Tower_Radar()\
        , Tower_Upgrade(), Tower_Sell(), Speed_Run(), Speed_Stop(), Speed_Accelerate(), Option(), Quit()
    Towersltd, Tssltd, Speedsltd, Setsltd = Tower_Selected(), Tsmall_Selected(), Speed_Selected(), Set_Selected()

    click = load_wav('Sounds/Click.wav')
    alert_credit = load_wav('Sounds/NotENF.wav')
    alert_grid = load_wav('Sounds/CantBuild.wav')
    alert_hp = load_wav('Sounds/UnderAttack.wav')
    font = load_font('Fonts/Myriad.otf')

    background= BackGround()
    #tower = Tower()
    player = Player()

    enemy = Enemy()
    enemies = []
    tile = Tile()
    tiles = []
    towers = []

    create_wave(enemies, 1)
    print(enemies)
    map_create(tiles)



    background.music()
    pass


def exit():
    pass


def handle_events(frame_time):
    global wave, player, icon, tile, tiles

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

            if player.mode == 0:
                if collide(player, run):
                    for tower in towers:
                        tower.wave = True
                    for enemy in enemies:
                        enemy.wave = True
                elif collide(player, accel):
                    for enemy in enemies:
                        enemy.speed *= 2
                elif collide(player, stop):
                    for tower in towers:
                        tower.wave = False
                    for enemy in enemies:
                        enemy.wave = False
                # Speed Controller

                if collide(player, tower1):
                    if player.credit >= 100:
                        player.mode = 1
                        player.credit -= 100
                        print("Laser Tower Selected!")
                    else:
                        alert_credit.play(1)
                        print("error!")
                elif collide(player, tower2):
                    if player.credit >= 150:
                        player.mode = 2
                        player.credit -= 150
                        print("Missile Tower Selected!")
                    else:
                        alert_credit.play(1)
                        print("error!")
                elif collide(player, tower3):
                    if player.credit >= 120:
                        player.mode = 3
                        player.credit -= 120
                        print("Radar Tower Selected!")
                    else:
                        alert_credit.play(1)
                        print("error!")
                # Tower Menu

            elif player.mode != 0:
                for tile in tiles:
                    if collide(player, tile):
                        towers.append(Tower(tile.x, tile.y, player.mode))
                        print("Selected Tile Located: %d | %d" % (tile.x, tile.y))
                        print("Current Tower Located: %d | %d" % (towers[-1].x, towers[-1].y))
                        print("==============================")
                player.mode = 0
                pass

            if collide(player, quit): game_framework.push_state(main_state)
            if collide(player, option): pass
    pass


def update(frame_time):
    global wave

    for enemy in enemies:
        for tower in towers:
            if collide(tower, enemy) & tower.wave == True:
                enemy.hp -= tower.dmg
        if enemy.hp <= 0:
            player.credit += enemy.reward
            enemies.remove(enemy)
        enemy.update(frame_time)

    pass


def draw(frame_time):
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
        enemy.draw(frame_time)
        enemy.draw_bb()

    for tower in towers:
        tower.draw()
        tower.draw_bb()

    update_canvas()
    pass


def pause():
    pass


def resume():
    pass






