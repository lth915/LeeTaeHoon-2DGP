from pico2d import*


####################################################################################################
####################################################################################################
#   Tower

class Tower_Laser:
    image = None

    def __init__(self):
        self.x, self.y = 1049 ,489
        self.width, self.height = 24, 37
        if self.image == None:
            self.image = load_image('resource/Btn_Game_TLaser.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x ,self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Tower_Missile:
    image = None

    def __init__(self):
        self.x, self.y = 1099, 489
        self.width, self.height = 24, 37
        if self.image == None:
            self.image = load_image('resource/Btn_Game_TMissile.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Tower_Radar:
    image = None

    def __init__(self):
        self.x, self.y = 1149, 489
        self.width, self.height = 24, 37
        if self.image == None:
            self.image = load_image('resource/Btn_Game_TRadar.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Tower_Upgrade:
    image = None

    def __init__(self):
        self.x, self.y = 1152, 799 - 213
        self.width, self.height = 17, 10
        if self.image == None:
            self.image = load_image('resource/Btn_Game_Tup.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Tower_Sell:
    image = None

    def __init__(self):
        self.x, self.y = 1152, 799 - 236
        self.width, self.height = 0, 0
        if self.image == None:
            self.image = load_image('resource/Btn_Game_Tsell.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Tower_Selected:
    image = None

    def __init__(self):
        self.x, self.y = 1400, 489
        self.print = False
        if self.image == None:
            self.image = load_image('resource/BtnSelected_Game_Tower.png')

    def draw(self):
        self.image.draw(self.x ,self.y)
    pass


class Tsmall_Selected:
    image = None

    def __init__(self):
        self.x, self.y = 1152 ,900
        self.print = False
        if self.image == None:
            self.image = load_image('resource/BtnSelected_Game_Tsmall.png')

    def draw(self):
        self.image.draw(self.x ,self.y)
    pass


####################################################################################################
####################################################################################################
#   Speed Controler

class Speed_Run:
    image = None

    def __init__(self):
        self.x, self.y = 1100, 799 - 424
        self.width, self.height = 24, 24
        if self.image == None:
            self.image = load_image('resource/Btn_Game_SRun.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height


class Speed_Accelerate:
    image = None

    def __init__(self):
        self.x, self.y = 1049, 799 - 424
        self.width, self.height = 24, 24
        if self.image == None:
            self.image = load_image('resource/Btn_Game_SAccel.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height


class Speed_Stop:
    image = None

    def __init__(self):
        self.x, self.y = 1151, 799 - 424
        self.width, self.height = 24, 24
        if self.image == None:
            self.image = load_image('resource/Btn_Game_SStop.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Speed_Selected:
    image = None

    def __init__(self):
        self.x, self.y = 1400, 799 - 424
        self.print = False
        if self.image == None:
            self.image = load_image('resource/BtnSelected_Game_Speed.png')

    def draw(self):
        self.image.draw(self.x ,self.y)
    pass


####################################################################################################
####################################################################################################
#   Setting

class Option:
    image = None

    def __init__(self):
        self.x, self.y = 1063, 799 - 755
        self.width, self.height = 30, 20
        if self.image == None:
            self.image = load_image('resource/Btn_Game_Option.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Quit:
    image = None

    def __init__(self):
        self.x, self.y = 1137, 799 - 755
        self.width, self.height = 30, 20
        if self.image == None:
            self.image = load_image('resource/Btn_Game_Exit.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_size(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height
    pass


class Set_Selected:
    image = None

    def __init__(self):
        self.x, self.y = 1400, 799 - 755
        self.print = False
        if self.image == None:
            self.image = load_image('resource/BtnSelected_Game_Set.png')

    def draw(self):
        self.image.draw(self.x ,self.y)
    pass