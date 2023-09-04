import pygame
import important

pygame.init()

w = important.SCREEN_WIDTH
h = important.SCREEN_HEIGHT
screen = important.screen

font = pygame.font.Font(None, 36)

Lx = (important.SCREEN_WIDTH - 100) // 2 - 100
Mx = (important.SCREEN_WIDTH - 100) // 2
Rx = (important.SCREEN_WIDTH - 100) // 2 + 100

X = [Lx, Mx, Rx]
Y = [important.SCREEN_HEIGHT, 100] #Y value for [Player, and Bot] in that order

def draw_menu():
    menu_image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\title.png"), (w, h))
    title = font.render("My Sports: Boxing", True, (255, 255, 255))
    start = font.render("Start", True, (255, 255, 255))
    exit = font.render("Exit", True, (255, 255, 255))
    screen.blit(menu_image, (0,0))
    screen.blit(title, ((w - title.get_width())/2, 120))
    screen.blit(start, ((w - start.get_width())/2, 180))
    screen.blit(exit, ((w - exit.get_width())/2, 230))

def draw_pause():
    paused = font.render("PAUSED", True, (255, 255, 255))
    resume = font.render("Unpause", True, (255, 255, 255))
    menu = font.render("Main Menu", True, (255, 255, 255))
    quit = font.render("Quit", True, (255, 255, 255))
    screen.blit(paused, ((w - paused.get_width())/2, 120))
    screen.blit(resume, ((w - resume.get_width())/2, 180))
    screen.blit(menu, ((w - menu.get_width())/2, 230))
    screen.blit(quit, ((w - quit.get_width())/2, 280))

def draw_arena():
    ring = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Arena.jpg"), (400, 400))
    boxer = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\PixelDoug.png"), (100,100))
    screen.blit(ring, (0,0))
    screen.blit(boxer, ((w - boxer.get_width())/2,100))

    if important.Attack < 3 and important.elasped_time[0] < important.animation_duration:
        if important.Attack == 0:
            image = important.p_lattack
        else:
            image = important.p_rattack

        Y[0] = important.SCREEN_HEIGHT - (important.elasped_time[0] / important.animation_duration) * (important.SCREEN_HEIGHT + 100)
        screen.blit(image, (X[important.Attack], Y[0]))

    if important.Bot_Attack < 3 and important.elasped_time[1] < important.animation_duration:
        if important.Bot_Attack == 0:
            image = important.b_lattack
        else:
            image = important.b_rattack

        Y[1] = -100 + (important.elasped_time[1] / important.animation_duration) * (important.SCREEN_HEIGHT + 100)
        screen.blit(image, (X[important.Bot_Attack], Y[1]))

    if important.Block < 3:
        if important.Block == 2:
            image = important.p_rblock
        else:
            image = important.p_lblock

        screen.blit(image, ((X[important.Block], important.SCREEN_HEIGHT - 100 - 50)))

    if important.Bot_Block < 3:
        if important.Bot_Block == 2:
            image = important.b_rblock
        else:
            image = important.b_lblock

        screen.blit(image, ((X[important.Bot_Block], 100 - 50)))

    health1 = font.render(f"player 1: {important.player1}", True, (255,255,255))
    health2 = font.render(f"player 2: {important.player2}", True, (255,255,255))
    screen.blit(health1, (20,20))
    screen.blit(health2, ((important.SCREEN_WIDTH - health2.get_width() - 20),20))


def draw_over(winner):
    result = font.render(winner, True, (255, 255, 255))
    rematch = font.render("Rematch", True, (255, 255, 255))
    menu = font.render("Main Menu", True, (255, 255, 255))
    quit = font.render("Quit", True, (255, 255, 255))
    screen.blit(result, ((w - result.get_width())/2, 120))
    screen.blit(rematch, ((w - rematch.get_width())/2, 180))
    screen.blit(menu, ((w - menu.get_width())/2, 230))
    screen.blit(quit, ((w - quit.get_width())/2, 280))