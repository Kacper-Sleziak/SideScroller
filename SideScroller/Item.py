from Object import Object

class Item(Object):
    def __init__(self, x, y, vel, effect):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.vel = vel
        self.effect = effect
        if self.effect == 1:
            self.color = (0, 255, 0)
        elif self.effect == 2:
            self.color = (0, 0, 255)
        elif self.effect == 3:
            self.color = (255, 0, 0)
