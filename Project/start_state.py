import game_framework
from pico2d import *
import main_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1200, 800)
    #800, 600
    #400, 300
    image = load_image('resource/start.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()
    pass


def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(main_state)
    delay(0.01)
    logo_time += 0.01
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass

