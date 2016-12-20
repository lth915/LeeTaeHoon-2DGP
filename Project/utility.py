import game_framework
from pico2d import *
import math
import random

import main_state

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_size()
    left_b, bottom_b, right_b, top_b = b.get_size()

    if left_a >= right_b: return False
    if right_a <= left_b: return False
    if top_a <= bottom_b: return False
    if bottom_a >= top_b: return False

    return True


def collide_range(a, b):
    left_a, bottom_a, right_a, top_a = a.get_range()
    left_b, bottom_b, right_b, top_b = b.get_size()

    if left_a >= right_b: return False
    if right_a <= left_b: return False
    if top_a <= bottom_b: return False
    if bottom_a >= top_b: return False

    return True


def direction_check(a, b):

    if (a.y < b.y) & (a.x - (a.r * 5) < b.x) & (a.x + (a.r * 5) > b.x): return 'TOP'
    if (a.x + (a.r * 5) < b.x) & (a.y + (a.r * 5) < b.y): return 'TOP-RIGHT'
    if (a.y + (a.r * 5) > b.y) & (a.y - (a.r * 5) < b.y) & (a.x < b.x): return 'RIGHT'
    if (a.y - (a.r * 5) > b.y) & (a.x + (a.r * 5) < b.x): return 'RIGHT-BOTTOM'
    if (a.y > b.y) & (a.x - (a.r * 5) < b.x) & (a.x + (a.r * 5) > b.x): return 'BOTTOM'
    if (a.x - (a.r * 5) > b.x) & (a.y - (a.r * 5) > b.y): return 'BOTTOM-LEFT'
    if (a.y + (a.r * 5) > b.y) & (a.y - (a.r * 5) < b.y) & (a.x > b.x): return 'LEFT'
    if (a.y + (a.r * 5) < b.y) & (a.x - (a.r * 5) > b.x): return 'LEFT-TOP'

    return 'ERROR'