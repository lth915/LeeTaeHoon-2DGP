import game_framework
from pico2d import *
import math
import random

import main_state

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.size()
    left_b, bottom_b, right_b, top_b = b.size()

    if left_a >= right_b: return False
    if right_a <= left_b: return False
    if top_a <= bottom_b: return False
    if bottom_a >= top_b: return False

    return True