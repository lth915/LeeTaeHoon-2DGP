import game_framework
from pico2d import *
import math
import random


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.size()
    left_b, bottom_b, right_b, top_b = b.size()

    if left_a >= right_b: return False
    if right_a <= left_b: return False
    if top_a <= bottom_b: return False
    if bottom_a >= top_b: return False

    return True


def buy(wallet, cost):
    if (wallet >= cost):
        wallet -= cost
        return True
    else:
        return False

def create_wave():
    pass