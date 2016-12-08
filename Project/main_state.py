import game_framework
from pico2d import *
import math
import random
import menu_state

from utility import *
from ui import *
from map import *
from player import *
from tower import *
from enemy import *

name = "MainState"


def towers_attack(frame_time):
    for enemy in enemies:
        for tower in towers:
            if collide(tower, enemy):

                enemy.hp -= tower.dmg

def towerss_attack():

    for enemy in enemies:
        for tower in towers:
            if collide(tower, enemy):
                enemy.hp -= tower.dmg

    timer = threading.Timer(1, towerss_attack)
    timer.start()



def enemies_move(frame_time):
    for enemy in enemies:
        if enemy.hp <= 0:
            player.credit += enemy.reward
            enemies.remove(enemy)
        enemy.update(frame_time)

def check_stage():
    global activation

    if enemies == []:
        activation = False
        player.stage += 1
        print("Stage %d Clear! Start Stage %d" % (player.stage-1, player.stage))
        create_enemies(player.stage)
        return True

def create_enemies(stage):
    for i in range( 1 + (stage*1) ):
        if stage <= 3: enemy_type = 1
        elif stage <= 5: enemy_type = random.randint(1, 2)
        else: enemy_type = random.randint(1, 3)

        enemies.append(Enemy(enemy_type, -50 - (i*75) ))


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Ingame.png')
        self.bgm_main = load_music('Sounds/Background_game.mp3')
        self.bgm_opening = load_wav('Sounds/Opening.wav')

    def draw(self):
        self.image.draw(600, 400)

    def music(self):
        self.bgm_opening.play(1)
        self.bgm_main.repeat_play()

    def music_off(self):
        self.bgm_main.stop()
    pass


class Mouse:
    def __init__(self):
        self.x, self.y = None, None
        self.selection = None

    def get_size(self):
        return self.x, self.y, self.x, self.y




def enter():
    global background, player, font, mouse
    global enemies, towers, tiles
    global activation, timer

    global tower1, tower2, tower3, upgrade, sell, run, stop, accel, option, quit
    global Tower_overlay, Ts_overlay, Speed_overlay, Set_overlay
    global click, alert_credit, alert_grid, alert_hp

    tower1, tower2, tower3 = Tower_Laser(), Tower_Missile(), Tower_Radar()
    upgrade, sell = Tower_Upgrade(), Tower_Sell()
    run, stop, accel = Speed_Run(), Speed_Stop(), Speed_Accelerate()
    option, quit = Option(), Quit()
    Tower_overlay, Ts_overlay, Speed_overlay, Set_overlay = Tower_Selected(), Tsmall_Selected(), Speed_Selected(), Set_Selected()

    click = load_wav('Sounds/Click.wav')
    alert_credit = load_wav('Sounds/NotENF.wav')
    alert_grid = load_wav('Sounds/CantBuild.wav')
    alert_hp = load_wav('Sounds/UnderAttack.wav')
    font = load_font('Fonts/Myriad.otf')
    background= BackGround()
    player = Player()
    mouse = Mouse()
    activation = False

    enemies = []
    tiles = []
    towers = []

    create_enemies(1)
    print(enemies)
    map_create(tiles)

    background.music()
    pass


def exit():
    pass


def handle_events(frame_time):
    global player, tile, tiles, activation

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            if not mouse.selection == None:
                if mouse.selection == 'Laser Tower': player.credit += 100
                if mouse.selection == 'Missile Tower': player.credit += 150
                if mouse.selection == 'Radar Tower': player.credit += 120
                mouse.selection = None
                print("Cancled!")

        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, 799 - event.y

            if collide(mouse, tower1): Tower_overlay.x = tower1.x
            elif collide(mouse, tower2): Tower_overlay.x = tower2.x
            elif collide(mouse, tower3): Tower_overlay.x = tower3.x
            else: Tower_overlay.x = 1400

            if collide(mouse, upgrade): Ts_overlay.y = upgrade.y
            elif collide(mouse, sell): Ts_overlay.y = sell.y
            else: Ts_overlay.y = 900

            if collide(mouse, run): Speed_overlay.x = run.x
            elif collide(mouse, accel): Speed_overlay.x = accel.x
            elif collide(mouse, stop): Speed_overlay.x = stop.x
            else: Speed_overlay.x = 1400

            if collide(mouse, option): Set_overlay.x = option.x
            elif collide(mouse, quit): Set_overlay.x = quit.x
            else: Set_overlay.x = 1400

        elif event.type == SDL_MOUSEBUTTONDOWN:
            click.play()

            if mouse.selection == None:
                if collide(mouse, run):
                    activation = True
                elif collide(mouse, accel):
                    for enemy in enemies:
                        enemy.speed *= 2
                elif collide(mouse, stop):
                    activation = False
                # Speed Controller

                if collide(mouse, tower1):
                    if player.credit >= 100:
                        mouse.selection = 'Laser Tower'
                        player.credit -= 100
                        print("Laser Tower Selected!")
                    else:
                        alert_credit.play(1)
                        print("error!")
                elif collide(mouse, tower2):
                    if player.credit >= 150:
                        mouse.selection = 'Missile Tower'
                        player.credit -= 150
                        print("Missile Tower Selected!")
                    else:
                        alert_credit.play(1)
                        print("error!")
                elif collide(mouse, tower3):
                    if player.credit >= 120:
                        mouse.selection = 'Radar Tower'
                        player.credit -= 120
                        print("Radar Tower Selected!")
                    else:
                        alert_credit.play(1)
                        print("error!")
                # Tower Menu

            elif not mouse.selection == None:
                for tile in tiles:
                    if collide(mouse, tile):
                        if tile.buildable == True:
                            towers.append(Tower(tile.x, tile.y, mouse.selection))
                            mouse.selection = None
                            tile.buildable = False
                            print("Selected Tile Located: %d | %d" % (tile.x, tile.y))
                            print("Current Tower Located: %d | %d" % (towers[-1].x, towers[-1].y))
                            print("==============================")
                        else:
                            alert_grid.play(1)
                            print("error!")
                pass

            if collide(mouse, quit): game_framework.push_state(menu_state)
            if collide(mouse, option): pass
    pass


def update(frame_time):
    if activation == True:
        enemies_move(frame_time)
        towers_attack(frame_time)
    check_stage()
    pass


def draw(frame_time):
    clear_canvas()
    background.draw()
    player.draw()

    Speed_overlay.draw()

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


    Tower_overlay.draw()
    Ts_overlay.draw()
    Set_overlay.draw()

    for enemy in enemies:
        enemy.draw(frame_time)
        #enemy.draw_bb()

    for tower in towers:
        tower.draw()
        tower.draw_bb()

    update_canvas()
    pass


def pause():
    pass


def resume():
    pass
