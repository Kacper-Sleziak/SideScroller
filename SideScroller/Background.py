import pygame
from Object import Object


class Background(Object):
    def __init__(self, name, vel):
        self.name = name
        self.bg = pygame.image.load(self.name)
        self.x1 = 0
        self.x2 = self.bg.get_width()
        self.vel = vel

    def draw(self, win):
        win.blit(self.bg, (self.x1, 0))
        win.blit(self.bg, (self.x2, 0))

    def move(self):
        self.x1 += self.vel
        self.x2 += self.vel
        if self.x1 <= self.bg.get_width() * -1:
            self.x1 = self.x2 + self.bg.get_width()
        if self.x2 <= self.bg.get_width() * -1:
            self.x2 = self.x1 + self.bg.get_width()

    def setVel(self, vel):
        self.vel = vel
