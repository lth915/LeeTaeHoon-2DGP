import game_framework
from pico2d import *
import math
import main_state, menu_state

name = "OptionState"


def enter():
    pass


def exit():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(menu_state)
    pass


def draw(frame_time):
    clear_canvas()
    pass


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






