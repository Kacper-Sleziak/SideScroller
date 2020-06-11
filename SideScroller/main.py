import pygame
from Menus import Menus

WIDTH, HEIGHT = 800, 300
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side Scroller")
menu = Menus()
menu.main_menu()
