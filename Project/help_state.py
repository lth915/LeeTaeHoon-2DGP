import game_framework
from pico2d import *
from utility import *
from ui_help import *
import math
import main_state, menu_state

name = "HelpState"


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Help.png')
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
    pass


class Exit:
    def __init__(self):
        self.x, self.y = 1157, 800 - 771
        self.image = load_image('resource/BtnSelected_Game_Set.png')
        self.collision = False

    def get_size(self):
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def draw(self):
        if self.collision == True:
            self.image.draw(1157, 800 - 771)
        else:
            pass
    pass


def enter():
    global background, mouse, info
    global info, exit, exit_selected
    global tower1, tower2, tower3
    global enemy1, enemy2, enemy3, enemy4

    mouse = Mouse()
    background = BackGround()
    info = Info()
    exit, exit_selected = Exit(), Exit_Selected()
    tower1, tower2, tower3 = Tower1(), Tower2(), Tower3()
    enemy1, enemy2, enemy3, enemy4 = Enemy1(), Enemy2(), Enemy3(), Enemy4()
    pass


def exit():
    pass


def handle_events(frame_time):
    global mouse, info

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state)

        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, 800 - event.y

            if collide(mouse, exit):
                exit.collision = True
            else:
                exit.collision = False

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if collide(mouse, tower1): info.image = load_image('resource/helpinfo_laser.png')
            elif collide(mouse, tower2): info.image = load_image('resource/helpinfo_missile.png')
            elif collide(mouse, tower3): info.image = load_image('resource/helpinfo_radar.png')
            elif collide(mouse, enemy1): info.image = load_image('resource/helpinfo_heli.png')
            elif collide(mouse, enemy2): info.image = load_image('resource/helpinfo_flight.png')
            elif collide(mouse, enemy3): info.image = load_image('resource/helpinfo_stealth.png')
            elif collide(mouse, enemy4): info.image = load_image('resource/helpinfo_boss.png')

            if collide(mouse, exit):
                game_framework.push_state(menu_state)

    pass


def draw(frame_time):
    clear_canvas()

    background.draw()
    exit.draw()
    exit_selected.draw()
    info.draw()

    update_canvas()
    pass


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






