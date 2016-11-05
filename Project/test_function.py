from pico2d import *

class Enemy:
    def __init__(self):
        self.x, self.y = 100, 100
        self.width, self.height = 50, 50
        self.hp, self.speed, self.type = 100, 50, 1
    def size(self):
        return (self.x - self.width), (self.y - self.height), (self.x + self.width), (self.y + self.height)

class Tower:
    def __init__(self):
        self.x, self.y = 500, 100
        self.width, self.height = 50, 50
        self.range, self.dmg, self.type = 100, 70, 1
    def size(self):
        return (self.x - self.width - self.range), (self.y - self.height - self.range), \
               (self.x + self.width + self.range), (self.y + self.height + self.range)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.size()
    left_b, bottom_b, right_b, top_b = b.size()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

enemy = Enemy()
tower = Tower()

while(1):
    print('Enemy is located | X:%4d | Y:%4d | HP:%4d |' % (enemy.x, enemy.y, enemy.hp))

    if collide(enemy, tower) == True:
        print('  -Enemy is Attacked! | HP:%4d |' % enemy.hp)
        enemy.hp -= tower.dmg
        if enemy.hp <= 0:
            print('  -Enemy Down! | HP:%4d |' % enemy.hp)
            break

    enemy.x += enemy.speed

    delay(0.5)