from Platform import Platform
from Object import Object
from Item import Item
from Effects import Effect
from Entity import Entity
from Arrow import Arrow
import random


class ObjectGroup:
    def __init__(self, win, vel, width, height):
        self.win = win
        self.vel = vel
        self.width = width
        self.x = self.width
        self.height = height - 45
        self.platformPattern = random.randint(0, 3)
        self.platformList = [Object(0, self.height, self.width, 100, 0, (0, 255, 0), 6)]
        self.itemList = []
        self.entityList = []
        self.arrowList = []
        if self.platformPattern == 0:
            self.platformList.append(Platform(self.width, self.height - 49, self.vel))
            self.platformList.append(Platform(self.width + 100, self.height - 98, self.vel))
            self.itemList.append(Item(self.width + 30, self.height - 70, self.vel, 1))
            self.itemList.append(Item(self.width + 150, self.height - 120, self.vel, 2))
            self.entityList.append(Entity(self.width + 150, self.height - 50, self.vel))
        if self.platformPattern == 1:
            self.platformList.append(Platform(self.width, self.height - 30, self.vel))
            self.itemList.append(Item(self.width + 50, self.height - 50, self.vel, 3))
            self.entityList.append(Entity(self.width + 150, self.height - 50, self.vel))
        if self.platformPattern == 2:
            self.platformList.append(Platform(self.width, self.height - 49, self.vel))
            self.platformList.append(Platform(self.width + 150, self.height - 98, self.vel))
            self.platformList.append(Platform(self.width + 300, self.height - 147, self.vel))
            self.itemList.append(Item(self.width + 30, self.height - 70, self.vel, 2))
            self.itemList.append(Item(self.width + 320, self.height - 170, self.vel, 3))
            self.itemList.append(Item(self.width + 370, self.height - 170, self.vel, 1))
            self.entityList.append(Entity(self.width + 180, self.height - 148, self.vel))
        if self.platformPattern == 3:
            self.platformList.append(Platform(self.width, self.height - 49, self.vel))
            self.platformList.append(Platform(self.width + 100, self.height - 98, self.vel))
            self.itemList.append(Item(self.width + 50, self.height - 20, self.vel, 2))
            self.entityList.append(Entity(self.width + 170, self.height - 148, self.vel))

    def draw(self, win):
        for platform in self.platformList:
            platform.draw(win)
        for item in self.itemList:
            item.draw(win)
        for entity in self.entityList:
            entity.draw(win)
        for arrow in self.arrowList:
            arrow.draw(win)

    def move(self):
        for platform in self.platformList:
            platform.move()
        for item in self.itemList:
            item.move()
        for entity in self.entityList:
            entity.move()
        for arrow in self.arrowList:
            arrow.move()
        self.x += self.vel

    def setVel(self, vel):
        self.vel = vel
        for platform in self.platformList[1:]:
            platform.vel = vel
        for item in self.itemList:
            item.vel = vel
        for entity in self.entityList:
            entity.vel = vel

    def entityShoot(self):
        for entity in self.entityList:
            arrow = entity.shoot()
            if type(arrow) == Arrow:
                self.arrowList.append(arrow)

    def platformWithCharacter(self, character):
        character.canFall = True
        x1, x2, y1, y2 = character.x, character.x + character.width, character.y, character.y + character.height
        for platform in self.platformList:
            px1, px2, py1, py2 = platform.x, platform.x + platform.width, platform.y, platform.y + platform.height
            if platform.x < character.x < platform.x + platform.width \
                    or platform.x < character.x + character.width < platform.x + platform.width:
                if platform.y <= character.y + character.height <= platform.y + platform.height:
                    character.canFall = False
                    character.y = platform.y - character.height
                elif platform.y <= character.y <= platform.y + platform.height:
                    character.isJumping = False
                    character.canFall = True
                    character.y = platform.y + platform.height
                else:
                    if px1 > x2 or px2 < x1 or py1 > y2 or py2 < y1:
                        pass
                    else:
                        Effect(character, platform.effect)

    def itemWithCharacter(self, character):
        x1, x2, y1, y2 = character.x, character.x + character.width, character.y, character.y + character.height
        for item in self.itemList:
            ix1, ix2, iy1, iy2 = item.x, item.x + item.width, item.y, item.y + item.height
            if ix1 > x2 or ix2 < x1 or iy1 > y2 or iy2 < y1:
                pass
            else:
                Effect(character, item.effect)
                del self.itemList[self.itemList.index(item)]

    def entityWithCharacter(self, character):
        x1, x2, y1, y2 = character.x, character.x + character.width, character.y, character.y + character.height
        for entity in self.entityList:
            ex1, ex2, ey1, ey2 = entity.x, entity.x + entity.width, entity.y, entity.y + entity.height
            if ex1 > x2 or ex2 < x1 or ey1 > y2 or ey2 < y1:
                pass
            else:
                Effect(character, entity.effect)
                del self.entityList[self.entityList.index(entity)]

    def arrowsWithCharacter(self, character):
        x1, x2, y1, y2 = character.x, character.x + character.width, character.y, character.y + character.height
        for arrow in self.arrowList:
            ax1, ax2, ay1, ay2 = arrow.x, arrow.x + arrow.width, arrow.y, arrow.y + arrow.height
            if ax1 > x2 or ax2 < x1 or ay1 > y2 or ay2 < y1:
                pass
            else:
                Effect(character, arrow.effect)
                del self.arrowList[self.arrowList.index(arrow)]

    def arrowsWithPlatforms(self, arrows):
        for arrow in arrows:
            for platform in self.platformList:
                ax1, ax2, ay1, ay2 = arrow.x, arrow.x + arrow.width, arrow.y, arrow.y + arrow.height
                px1, px2, py1, py2 = platform.x, platform.x + platform.width, platform.y, platform.y + platform.height
                if ax1 > px2 or ax2 < px1 or ay1 > py2 or ay2 < py1:
                    pass
                else:
                    del arrows[arrows.index(arrow)]
        return arrows

    def entityWithArrows(self, arrows):
        for arrow in arrows:
            x1, x2, y1, y2 = arrow.x, arrow.x + arrow.width, arrow.y, arrow.y + arrow.height
            for entity in self.entityList:
                ex1, ex2, ey1, ey2 = entity.x, entity.x + entity.width, entity.y, entity.y + entity.height
                if ex1 > x2 or ex2 < x1 or ey1 > y2 or ey2 < y1:
                    pass
                else:
                    Effect(entity, arrow.effect)
                    del self.entityList[self.entityList.index(entity)]
                    del arrows[arrows.index(arrow)]

    def __del__(self):
        print("group destroyed")
