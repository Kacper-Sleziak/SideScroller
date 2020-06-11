import pygame
import sys
from Buttons import Buttons
from Game import Game


class Menus:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 300
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.difficulty = 2
        self.menuButtonList = [Buttons(50, 50, 100, 20, "Play"),
                               Buttons(50, 80, 100, 20, "Easy"),
                               Buttons(50, 110, 100, 20, "Normal"),
                               Buttons(50, 140, 100, 20, "Hard"),
                               Buttons(50, 180, 100, 20, "Reset High Score"),
                               Buttons(50, 210, 100, 20, "Quit")]
        self.endScreenButtonList = [Buttons(50, 200, 100, 20, "Main Menu"),
                                    Buttons(650, 200, 100, 20, "Quit")]
        self.chosen = [self.menuButtonList[self.difficulty].x, self.menuButtonList[self.difficulty].y]
        f = open("HighScore.txt", "r")
        self.highScore = int(f.read())
        f.close()
        self.run = True
        self.click = False

    def main_menu(self):
        while self.run:
            self.win.fill((0, 0, 0))
            for button in self.menuButtonList:
                button.draw(self.win)
            pygame.draw.line(self.win, (255, 0, 0), (self.chosen[0], self.chosen[1]),
                             (self.chosen[0] + 100, self.chosen[1]), 3)
            pygame.draw.line(self.win, (255, 0, 0), (self.chosen[0] + 100, self.chosen[1]),
                             (self.chosen[0] + 100, self.chosen[1] + 20), 3)
            pygame.draw.line(self.win, (255, 0, 0), (self.chosen[0] + 100, self.chosen[1] + 20),
                             (self.chosen[0], self.chosen[1] + 20), 3)
            pygame.draw.line(self.win, (255, 0, 0), (self.chosen[0], self.chosen[1] + 20),
                             (self.chosen[0], self.chosen[1]), 3)
            mousex, mousey = pygame.mouse.get_pos()

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            for button in self.menuButtonList:
                if button.button.collidepoint((mousex, mousey)):
                    if self.click:
                        if self.menuButtonList.index(button) == 0:
                            self.game()
                        elif self.menuButtonList.index(button) == 1:
                            self.changeDiff(1)
                        elif self.menuButtonList.index(button) == 2:
                            self.changeDiff(2)
                        elif self.menuButtonList.index(button) == 3:
                            self.changeDiff(3)
                        elif self.menuButtonList.index(button) == 4:
                            self.resetHS()
                        elif self.menuButtonList.index(button) == 5:
                            self.Quit()
            pygame.display.update()

    def end_menu(self, score):
        while self.run:
            self.win.fill((0, 0, 0))
            for button in self.endScreenButtonList:
                button.draw(self.win)

            mousex, mousey = pygame.mouse.get_pos()

            for button in self.endScreenButtonList:
                if button.button.collidepoint((mousex, mousey)):
                    if self.click:
                        if self.endScreenButtonList.index(button) == 0:
                            self.main_menu()
                        elif self.endScreenButtonList.index(button) == 1:
                            self.Quit()

            if score > self.highScore:
                self.highScore = score
                f = open("HighScore.txt", "w")
                f.write(str(int(score)))
                f.close()

            font = pygame.font.SysFont("comicsansms", 30)
            self.win.blit(font.render("Game Over!", 1, (255, 255, 255)), (300, 50))
            self.win.blit(font.render("Your Score: " + str(int(score)), 1, (255, 255, 255)),
                          (300, 110))
            self.win.blit(font.render("High Score: " + str(int(self.highScore)), 1, (255, 255, 255)),
                          (300, 170))

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()

    def changeDiff(self, diff):
        self.difficulty = diff
        self.chosen = [self.menuButtonList[self.difficulty].x, self.menuButtonList[self.difficulty].y]

    def resetHS(self):
        self.highScore = 0
        f = open("HighScore.txt", "w")
        f.write("0")
        f.close()

    def Quit(self):
        pygame.quit()
        sys.exit()

    def game(self):
        game = Game(self.WIDTH, self.HEIGHT, self.win, self.difficulty)
        while game.obj.health != 0 and game.obj.stamina != 0:
            pygame.time.delay(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and not game.obj.isJumping and not game.obj.canFall:
                game.obj.isCrouching = True
            if keys[pygame.K_UP] and not game.obj.isJumping and not game.obj.isCrouching and not game.obj.canFall:
                game.obj.isJumping = True
            if keys[pygame.K_SPACE]:
                game.obj.isShooting = True
            game.GameUpdate()
            game.WinUpdate()
        score = game.obj.score
        del game
        self.end_menu(score)
