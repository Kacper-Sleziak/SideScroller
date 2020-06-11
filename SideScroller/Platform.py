from Object import Object


class Platform(Object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.vel = vel
        self.color = (154, 96, 36)
        self.effect = 6