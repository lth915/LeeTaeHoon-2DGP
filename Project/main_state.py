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
    global attack_cycle


    for enemy in enemies:
        for tower in towers:
            tower.update(frame_time)

            if (tower.type == 'Radar Tower') & (enemy.type == 3):
                if collide_range(tower, enemy): enemy.attackedable = True
                else: enemy.attackedable = False

            if enemy.attackedable == True:
                if collide_range(tower, enemy):
                    if tower.target == None:
                        tower.target = enemy
                        print("Lockon")
                        tower.attack()
                    else:
                        tower.attack()

    pass

def enemies_move(frame_time):
    for enemy in enemies:
        if enemy.hp <= 0:
            player.credit += enemy.reward
            enemies.remove(enemy)
        if (enemy.state == 10) & (enemy.y <= 0):
            player.life -= 1
            #alert_hp.play()
            enemies.remove(enemy)
        enemy.update(frame_time)
    pass

def check_stage():
    global activation

    if enemies == []:
        activation = False
        player.stage += 1
        print("Stage %d Clear! Start Stage %d" % (player.stage-1, player.stage))
        create_enemies(player.stage)
        clear.drawing = True
        sound_victory.play()

    if player.life == 0:
        defeated.drawing = True
        sound_defeated.play()
        return True
    pass

def create_enemies(stage):
    for i in range( 10 + (stage*2) ):
        if stage <= 1: enemy_type = 1
        elif stage <= 2: enemy_type = random.randint(1, 2)
        else: enemy_type = random.randint(1, 3)

        enemies.append(Enemy(enemy_type, -50 - (i*100) ))
    pass # ============================================================================================================


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Ingame3.png')
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
        self.selected = None

    def get_size(self):
        return self.x, self.y, self.x, self.y
    pass # ============================================================================================================


def enter():
    global background, player, font, mouse
    global enemies, towers
    global activation
    global timer
    global attack_cycle

    global tower1, tower2, tower3, upgrade, sell, run, stop, accel, option, quit
    global Tower_overlay, Ts_overlay, Speed_overlay, Set_overlay, clear, defeated
    global click, alert_credit, alert_grid, alert_hp, sound_victory, sound_defeated

    tower1, tower2, tower3 = Tower_Laser(), Tower_Missile(), Tower_Radar()
    upgrade, sell = Tower_Upgrade(), Tower_Sell()
    clear, defeated = Stage_Clear(), Stage_Defeated()
    run, stop, accel = Speed_Run(), Speed_Stop(), Speed_Accelerate()
    option, quit = Option(), Quit()
    Tower_overlay, Ts_overlay, Speed_overlay, Set_overlay = Tower_Selected(), Tsmall_Selected(), Speed_Selected(), Set_Selected()

    click = load_wav('Sounds/Click.wav')
    alert_credit = load_wav('Sounds/NotENF.wav')
    alert_grid = load_wav('Sounds/CantBuild.wav')
    alert_hp = load_wav('Sounds/UnderAttack.wav')
    sound_victory = load_wav('Sounds/Victory.wav')
    sound_defeated = load_wav('Sounds/Defeated.wav')
    font = load_font('Fonts/Myriad.otf')
    background= BackGround()
    player = Player()
    mouse = Mouse()

    timer = 0
    attack_cycle = 200
    activation = False

    enemies = []
    towers = []

    create_enemies(1)
    print(enemies)

    background.music()
    pass # ============================================================================================================


def exit():
    pass # ============================================================================================================


def handle_events(frame_time):
    global player, activation, towers, attack_cycle

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
                mouse.selected = None
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

            if clear.drawing == True:
                clear.drawing = False
                if player.stage == 11:
                    game_framework.push_state(menu_state)
            if defeated.drawing == True:
                defeated.drawing = False
                game_framework.push_state(menu_state)

            if mouse.selection == None:
                if collide(mouse, run):
                    activation = True
                elif collide(mouse, accel):
                    for enemy in enemies:
                        if enemy.speed == 1:
                            enemy.speed = 2
                        elif enemy.speed == 2:
                            enemy.speed = 3
                        elif enemy.speed == 3:
                            enemy.speed = 1
                    for tower in towers:
                        if tower.speed == 1:
                            tower.speed = 2
                        if tower.speed == 2:
                            tower.speed = 3
                        if tower.speed == 3:
                            tower.speed = 1
                elif collide(mouse, stop):
                    activation = False
                elif mouse.x < 1000:
                    for tower in towers:
                        if collide(mouse, tower):
                            mouse.selection = 'Tower Selected'
                            mouse.selected = tower
                            tower.selected = True
                            print("Tower Selected, Now Can Upgrade or Demolish")

                # Speed Controller & Tower Select

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

            elif mouse.selection == 'Tower Selected':
                if collide(mouse, upgrade):
                    if player.credit >= int(mouse.selected.credit/2):
                        player.credit -= int(mouse.selected.credit/2)
                        mouse.selected.credit += int(mouse.selected.credit/2)
                        mouse.selected.range += 25
                        mouse.selected.dmg += (mouse.selected.dmg*0.2)
                    else:
                        alert_credit.play(1)
                        print("error!")

                elif collide(mouse, sell):
                    player.credit += int(mouse.selected.credit/2)
                    mouse.selected.delete = True
                    mouse.selected = None

                    for tower in towers:
                        if tower.selected == True: tower.selected = False
                        if tower.delete == True:
                            towers.remove(tower)

                    mouse.selection = None
                else:
                    cancel = True

                    for tower in towers:
                        tower.selected = False

                        if collide(mouse, tower):
                            mouse.selected = tower
                            tower.selected = True
                            cancel = False
                            print("Tower Selected, Now Can Upgrade or Demolish")

                    if cancel == True:
                        mouse.selection = None
                        mouse.selected = None
                        print("Tower Canceled")

            else:
                build = True

                for tower in towers:
                    if collide(mouse, tower): build = False

                if build == True:
                    towers.append(Tower((int(mouse.x / 50) * 50) + 25, (int(mouse.y / 50) * 50) + 25, mouse.selection))
                    mouse.selection = None
                    print("Current Tower Located: %d | %d" % (towers[-1].x, towers[-1].y))
                    print("==============================")
                else:
                    alert_grid.play(1)
                    print("error!")


            if collide(mouse, quit): game_framework.push_state(menu_state)
            if collide(mouse, option): pass
    pass # ============================================================================================================


def update(frame_time):

    if activation == True:
        if player.life <= 0:
            defeated.drawing = True

        enemies_move(frame_time)
        towers_attack(frame_time)

    check_stage()
    pass # ============================================================================================================


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

    for tower in towers:
        tower.draw()

    if not defeated.drawing == True:
        clear.draw()
    defeated.draw()

    if not mouse.selected == None:
        font.draw(1035, 799 - 170, "%s" % mouse.selected.type, (255, 255, 255))
        font.draw(1035, 799 - 210, "DMG   |  %d" % (mouse.selected.dmg*100), (255, 255, 255))
        font.draw(1035, 799 - 230, "RANG |  %d" % (mouse.selected.range), (255, 255, 255))

    update_canvas()
    pass # ============================================================================================================


def pause():
    pass # ============================================================================================================


def resume():
    pass # ============================================================================================================
