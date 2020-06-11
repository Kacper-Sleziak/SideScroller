import pygame
from Character import Character
from Background import Background
from Arrow import Arrow
from Stats import Stats
from ObjectGroup import ObjectGroup

class Game:
    def __init__(self, WIDTH, HEIGHT, win, difficulty):
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.win = win
        self.difficulty = difficulty
        self.vel = 8 * 0.5 * self.difficulty
        self.bg = Background("OIP.jpg", self.vel)
        self.obj = Character(50, 200)
        self.stats = Stats(5, 5)
        self.group = ObjectGroup(self.win, self.vel, self.WIDTH, self.HEIGHT)
        self.arrows = []
        self.over = True


    def WinUpdate(self):
        self.bg.draw(self.win)
        self.obj.draw(self.win)
        for arrow in self.arrows:
            arrow.draw(self.win)
        self.group.draw(self.win)
        self.stats.draw(self.win, self.obj)
        pygame.display.update()


    def GameUpdate(self):
        self.obj.addScore(self.vel * 0.01)
        self.group.platformWithCharacter(self.obj)
        self.group.itemWithCharacter(self.obj)
        self.group.entityWithCharacter(self.obj)
        self.group.entityWithArrows(self.arrows)
        self.group.arrowsWithCharacter(self.obj)
        self.arrows = self.group.arrowsWithPlatforms(self.arrows)
        self.group.entityShoot()
        self.obj.jump()
        self.obj.crouch()
        self.obj.move()
        self.obj.addMana(0.1)
        self.obj.addStamina(-0.05)
        arrow = self.obj.shoot()
        if type(arrow) == Arrow:
            self.arrows.append(arrow)
        for arrow in self.arrows:
            arrow.move()
            if arrow.x >= self.WIDTH + arrow.width or arrow.x < -arrow.width:
                del self.arrows[self.arrows.index(arrow)]
        self.group.move()
        self.bg.move()
        if self.group.x <= -self.WIDTH:
            del self.group
            self.group = ObjectGroup(self.win, self.vel, self.WIDTH, self.HEIGHT)
        self.vel = 8 * 0.5 * self.difficulty * self.obj.stamina / 60
        self.bg.setVel(self.vel * -1)
        self.group.setVel(self.vel * -1)

