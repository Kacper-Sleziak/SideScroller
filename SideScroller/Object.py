import pygame


class Object(object):
    def __init__(self, x, y, width, height, vel, color, effect):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.effect = effect

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.vel

    def __del__(self):
        print("object destroyed")