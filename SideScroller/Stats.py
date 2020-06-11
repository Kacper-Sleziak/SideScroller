import pygame


class Stats():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("comicsansms", 10)

    def draw(self, win, character):
        win.blit(self.font.render("Score: " + str(int(character.score)), 1, (0, 0, 0)), (self.x, self.y))
        win.blit(self.font.render("Health:" + str(int(character.health)), 1, (0, 0, 0)), (self.x, self.y + 15))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y + 30, character.health, 10))
        win.blit(self.font.render("Stamina:" + str(int(character.stamina)), 1, (0, 0, 0)), (self.x, self.y + 45))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y + 60, character.stamina, 10))
        win.blit(self.font.render("Mana :" + str(int(character.mana)), 1, (0, 0, 0)), (self.x, self.y + 75))
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y + 90, character.mana, 10))
