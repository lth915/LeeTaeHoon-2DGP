import game_framework
from pico2d import *
import math
import game_state, help_state, option_state

name = "MainState"


class BackGround:
    def __init__(self):
        self.image = load_image('resource/BackGround_Main.png')
        self.bgm = load_music('Sounds/Background_Main.mp3')
        self.bgm.set_volume(50)

    def draw(self):
        self.image.draw(600, 400)

    def music(self):
        self.bgm.repeat_play()

    def music_off(self):
        self.bgm.stop()


class MenuBtn:
    def __init__(self):
        self.Start = load_image('resource/Btn_Main_Start.png')
        self.Help = load_image('resource/Btn_Main_Help.png')
        self.Option = load_image('resource/Btn_Main_Option.png')
        self.Exit = load_image('resource/Btn_Main_Exit.png')
        self.Selected = load_image('resource/Btn_Main_Selected.png')
        self.width, self.height = 350, 75

    def drawStart(self):
        self.Start.draw(600, 400)
    def drawHelp(self):
        self.Help.draw(600, 300)
    def drawOption(self):
        self.Option.draw(600, 200)
    def drawExit(self):
        self.Exit.draw(600, 100)


class BtnSelected:
    def __init__(self):
        self.x, self.y = 600, -100
        self.image = load_image('resource/Btn_Main_Selected.png')

    def draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global BG
    global Btn, Selected
    global mx, my

    BG = BackGround()
    Btn = MenuBtn()
    Selected = BtnSelected()
    mx, my = None, None
    BG.music()
    pass


def exit():
    pass


def handle_events():
    global mx, my, Btn, Selected

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 799 - event.y
            if (mx > 600 - Btn.width / 2) & (mx < 600 + Btn.width / 2) & (my > 400 - Btn.height / 2) & (my < 400 + Btn.height / 2):
                Selected.y = 400
            elif (mx > 600 - Btn.width / 2) & (mx < 600 + Btn.width / 2) & (my > 300 - Btn.height / 2) & (my < 300 + Btn.height / 2):
                Selected.y = 300
            elif (mx > 600 - Btn.width / 2) & (mx < 600 + Btn.width / 2) & (my > 200 - Btn.height / 2) & (my < 200 + Btn.height / 2):
                Selected.y = 200
            elif (mx > 600 - Btn.width / 2) & (mx < 600 + Btn.width / 2) & (my > 100 - Btn.height / 2) & (my < 100 + Btn.height / 2):
                Selected.y = 100
            else:
                Selected.y = -100
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if Selected.y == 400:
                BG.music_off()
                game_framework.push_state(game_state)
            if Selected.y == 300:
                BG.music_off()
                game_framework.push_state(help_state)
            if Selected.y == 200:
                BG.music_off()
                game_framework.push_state(option_state)
            if Selected.y == 100:
                BG.music_off()
                game_framework.quit()
    pass


def draw():
    global BG, Btn, Selected

    clear_canvas()
    BG.draw()
    Selected.draw()
    Btn.drawStart()
    Btn.drawHelp()
    Btn.drawOption()
    Btn.drawExit()
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






