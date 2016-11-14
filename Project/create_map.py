from pico2d import *
import json

global i, j


def create_map():
    map = open('data/map.txt', 'w')
    i, j = 0, 0

    matrix = [[{"x":0, "y":0, "data":0} for x in range(20)] for y in range(16)]

    while(i<16):
        j=0
        while(j<20):
            matrix[i][j]["y"] = 799 - (i * 50 + 25)
            matrix[i][j]["x"] = j * 50 + 25
            j = j+1
        i = i+1
        pass

    json.dump(matrix, map, indent=4)

    map.close()
    pass

create_map()