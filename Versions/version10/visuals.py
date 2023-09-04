import pygame
import important
import text

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
    menu_image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\title.jpg"), (w, h))
    screen.blit(menu_image, (0,0))
    screen.blit(text.start, ((w - text.start.get_width())/2, (h / 2 + 75)))
    screen.blit(text.exit, ((w - text.exit.get_width())/2, (h / 2 + 125)))

def draw_pause():
    screen.blit(text.paused, ((w - text.paused.get_width())/2, 120))
    screen.blit(text.resume, ((w - text.resume.get_width())/2, 180))
    screen.blit(text.menu, ((w - text.menu.get_width())/2, 230))
    screen.blit(text.quit, ((w - text.quit.get_width())/2, 280))

def draw_arena():
#    ring = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\classroom.jpg"), (w, h))
#    boxer = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\PixelDoug.png"), (100,100))
    screen.blit(important.ring, (0,0))
    screen.blit(important.fighter, ((w - important.fighter.get_width())/2,100))

    if important.Attack < 3 and important.elasped_time[0] < important.animation_duration:
        
        if important.Attack == 0:
            image = important.fork
        elif important.Attack == 1:
            image = important.spoon
        else:
            image = important.knife

        Y[0] = important.SCREEN_HEIGHT - (important.elasped_time[0] / important.animation_duration) * (important.SCREEN_HEIGHT - 200) #starting location (at the bottom of the screen) - the time it has travelled so far (subtracts as the values increase from top to bottom rather than bottom to top like in a graph)
        screen.blit(image, (X[important.Attack], Y[0]))

    if important.Bot_Attack < 3 and important.elasped_time[1] < important.animation_duration:
        if important.Bot_Attack == 0:
            image = important.b_lattack
        else:
            image = important.b_rattack

        Y[1] = 100 + (important.elasped_time[1] / important.animation_duration) * (important.SCREEN_HEIGHT) #starting location (100) + the time it has travelled so far
        screen.blit(image, (X[important.Bot_Attack], Y[1]))

    if important.Block < 3:
        image = important.block

        screen.blit(image, ((X[important.Block], important.SCREEN_HEIGHT - 100 - 50)))

    if important.Bot_Block < 3:
        image = important.block

        screen.blit(image, ((X[important.Bot_Block], 200)))

    health1 = font.render(f"player 1: {important.player1}", True, (255,255,255))
    health2 = font.render(f"player 2: {important.player2}", True, (255,255,255))
    screen.blit(health1, (20,20))
    screen.blit(health2, ((important.SCREEN_WIDTH - health2.get_width() - 20),20))


def draw_over(winner):
    result = font.render(winner, True, (255, 255, 255))
    screen.blit(result, ((w - result.get_width())/2, 120))
    screen.blit(text.rematch, ((w - text.rematch.get_width())/2, 180))
    screen.blit(text.menu, ((w - text.menu.get_width())/2, 230))
    screen.blit(text.quit, ((w - text.quit.get_width())/2, 280))