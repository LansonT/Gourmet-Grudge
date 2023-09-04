import pygame
import important

w = important.SCREEN_WIDTH
h = important.SCREEN_HEIGHT

font = pygame.font.Font(None, 36)

start = font.render("Start", True, (0, 0, 0))
exit = font.render("Exit", True, (0, 0, 0))

paused = font.render("PAUSED", True, (255, 255, 255))
resume = font.render("Unpause", True, (255, 255, 255))
menu = font.render("Main Menu", True, (255, 255, 255))
quit = font.render("Quit", True, (255, 255, 255))

rematch = font.render("Rematch", True, (255, 255, 255))

def x_min(input):
    min = (w - input.get_width())/2
    return min

def x_max(input):
    max = (w - input.get_width())/2 + input.get_width()
    return max
