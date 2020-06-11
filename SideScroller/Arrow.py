from Object import Object


class Arrow(Object):
    def __init__(self, x, y, color, vel):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.vel = vel
        self.color = color
        self.effect = 5
