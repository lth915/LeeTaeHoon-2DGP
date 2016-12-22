from pico2d import*


class Info:
    def __init__(self):
        self.x, self.y = 854, 800 - 418
        self.width, self.height = 185, 125
        self.image = None

    def draw(self):
        if not self.image == None:
            self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Tower1:
    def __init__(self):
        self.x, self.y = 854, 800 - 225
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Tower2:
    def __init__(self):
        self.x, self.y = 904, 800 - 225
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Tower3:
    def __init__(self):
        self.x, self.y = 959, 800 - 225
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Enemy1:
    def __init__(self):
        self.x, self.y = 849, 800 - 280
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Enemy2:
    def __init__(self):
        self.x, self.y = 904, 800 - 280
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Enemy3:
    def __init__(self):
        self.x, self.y = 959, 800 - 280
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Enemy4:
    def __init__(self):
        self.x, self.y = 1014, 800 - 280
        self.width, self.height = 25, 25

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass

class Exit:
    image = None

    def __init__(self):
        self.x, self.y = 1157, 800 - 771
        self.width, self.height = 30, 20
        if self.image == None:
            self.image = load_image('resource/Btn_Game_Exit.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Exit_Selected:
    image = None

    def __init__(self):
        self.x, self.y = 1157, 800 - 771
        if self.image == None:
            self.image = load_image('resource/BtnSelected_Game_Set.png')

    def draw(self):
        self.image.draw(self.x ,self.y)
    pass