import game_framework
from pico2d import *
import math
import game_state, help_state, option_state

name = "MainState"
image = None


def enter():
    global image
    global btstart, btoption, bthelp, btexit, btselect
    global sx
    image = load_image('resource/title.png')
    btstart = load_image('resource/btstart.png')
    btoption = load_image('resource/btoption.png')
    bthelp = load_image('resource/bthelp.png')
    btexit = load_image('resource/btexit.png')
    btselect = load_image('resource/btselect.png')
    sx = 200
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    global sx

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if (sx >= 133) & (sx <= 598):
                sx += 133
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if (sx >= 201) & (sx <= 599):
                sx -= 133
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if sx == 200:
                game_framework.change_state(game_state)
            elif sx == 333:
                game_framework.change_state(option_state)
            elif sx == 466:
                game_framework.change_state(help_state)
            elif sx == 599:
                game_framework.quit()
    pass


def draw():
    global sx

    clear_canvas()
    image.draw(400, 300)
    btstart.draw(200, 150)
    btoption.draw(333, 150)
    bthelp.draw(466, 150)
    btexit.draw(599, 150)
    btselect.draw(sx, 150)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






