import pygame


class Buttons:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont("comicsans", 15)
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (200, 200, 255), self.button)
        win.blit(self.font.render(self.text, 1, (0, 0, 0)), (self.x + 5, self.y + 5))

