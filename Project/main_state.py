import game_framework
from pico2d import *
import math
import game_state, help_state, option_state

name = "MainState"


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Main.png')
    def draw(self):
        self.image.draw(600, 400)


class MenuBtn:
    MOUSEON = None
    def __init__(self):
        self.Start = load_image('resource/Btn_Main_Start.png')
        self.Help = load_image('resource/Btn_Main_Help.png')
        self.Option = load_image('resource/Btn_Main_Option.png')
        self.Exit = load_image('resource/Btn_Main_Exit.png')
        self.Selected = load_image('resource/Btn_Main_Selected.png')

    def drawStart(self):
        self.Start.draw(600, 400)
    def drawHelp(self):
        self.Start.draw(600, 300)
    def drawOption(self):
        self.Start.draw(600, 200)
    def drawExit(self):
        self.Start.draw(600, 100)

    handle_Btn = [drawStart, drawHelp, drawOption, drawExit]
    def draw(self):



def enter():
    global sx
    global background
    global Button

    background = BackGround()
    sx = 200
    Button = load_image('resource/Button_Main.png')
    pass


def exit():
    pass


def handle_events():
    global sx
    global mx, my

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 799 - event.y
        #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            #if (sx >= 133) & (sx <= 598):
                #sx += 133

    pass


def draw():
    global sx, background

    clear_canvas()
    background.draw()
    Button.clip_draw(0, 75 * 4, 350, 75, 600, 400)
    Button.clip_draw(0, 75 * 3, 350, 75, 600, 300)
    Button.clip_draw(0, 75 * 2, 350, 75, 600, 200)
    Button.clip_draw(0, 75 * 1, 350, 75, 600, 100)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






