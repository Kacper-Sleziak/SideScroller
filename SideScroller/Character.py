from Entity import Entity
from Arrow import Arrow


class Character(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.standHeight = 50
        self.crouchHeight = 25
        self.width = 20
        self.color = (100, 100, 100)
        self.vel = 0
        self.mana = 100
        self.stamina = 100
        self.health = 100
        self.score = 0
        self.isJumping = False
        self.isCrouching = False
        self.isShooting = False
        self.canFall = False
        self.jumpCount = 3
        self.crouchCount = 16
        self.shootTime = 0
        self.gravity = 3

    def move(self):
        if self.canFall and not self.isJumping:
            self.y += self.vel
            self.vel += self.gravity
        elif not self.canFall:
            self.vel = 0

    def jump(self):
        if self.jumpCount >= 0 and self.isJumping and not self.isCrouching:
            self.y -= (self.jumpCount ** 2) * 0.5
            self.jumpCount -= 1
        else:
            self.isJumping = False
            self.jumpCount = 8

    def crouch(self):
        if self.crouchCount >= 0 and not self.isJumping and self.isCrouching == True:
            if self.crouchCount == 16:
                self.height = self.crouchHeight
                self.y += self.crouchHeight
            self.crouchCount -= 1
        elif self.crouchCount < 0:
            self.isCrouching = False
            self.height = self.standHeight
            self.y -= self.crouchHeight
            self.crouchCount = 16

    def shoot(self):
        if self.isShooting and self.shootTime == 0:
            if self.mana >= 20:
                self.isShooting = True
                self.shootTime = 10
                arrow = Arrow(self.x + self.width, self.y + self.height * 0.5, (0, 0, 255), 8)
                self.mana -= 20
                return arrow
        elif self.shootTime > 0:
            self.shootTime -= 1
            if self.shootTime == 0:
                self.isShooting = False


    def addMana(self, amount):
        if 100 > self.mana + amount > 0:
            self.mana += amount
        elif self.mana + amount < 0:
            self.mana = 0
        elif self.mana + amount > 100:
            self.mana = 100

    def addStamina(self, amount):
        if 100 > self.stamina + amount > 0:
            self.stamina += amount
        elif self.stamina + amount < 0:
            self.stamina = 0
        elif self.stamina + amount > 100:
            self.stamina = 100

    def addScore(self, amount):
        self.score += amount