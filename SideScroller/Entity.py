from Object import Object
from Arrow import Arrow


class Entity(Object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 50
        self.vel = vel
        self.health = 50
        self.color = (255, 100, 100)
        self.shootTime = 30
        self.effect = 5

    def shoot(self):
        if self.shootTime == 0:
            self.shootTime = 30
            arrow = Arrow(self.x, self.y + self.height * 0.5, (255, 0, 0), -20)
            return arrow
        elif self.shootTime > 0:
            self.shootTime -= 1

    def addHealth(self, amount):
        if 100 >= self.health + amount >= 0:
            self.health += amount
        elif self.health + amount < 0:
            self.health = 0
        elif self.health + amount > 100:
            self.health = 100
