import pygame
import Fight

pygame.init()
screen = Fight.screen

w = 400
h = 400

def draw_menu():
    font = pygame.font.Font(None, 36)
    image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\title.png"), (400, 400))
    game_title = font.render("My Sports: Boxing", True, (255, 255, 255))
    start_text = font.render("Start", True, (255, 255, 255))
    exit_text = font.render("Exit", True, (255, 255, 255))
    screen.blit(image, (0,0))
    screen.blit(game_title, ((w - game_title.get_width())/2, 120))
    screen.blit(start_text, (170, 180))
    screen.blit(exit_text, (175, 230))


def draw_pause():
    font = pygame.font.Font(None, 36)
    paused = font.render("PAUSED", True, (255, 255, 255))
    resume_text = font.render("Unpause", True, (255, 255, 255))
    menu_text = font.render("Main Menu", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(paused, ((w - paused.get_width())/2, 120))
    screen.blit(resume_text, ((w - resume_text.get_width())/2, 180))
    screen.blit(menu_text, ((w - menu_text.get_width())/2, 230))
    screen.blit(quit_text, ((w - quit_text.get_width())/2, 280))

def arena():
    image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Arena.jpg"), (400, 400))
    boxer = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Boxer.jpg"), (100,100))
    screen.blit(image, (0,0))
    screen.blit(boxer, ((w-boxer.get_width())/2,100))

def draw_over(winner):
    font = pygame.font.Font(None, 36)
    result = font.render(winner, True, (255, 255, 255))
    rematch_text = font.render("Rematch", True, (255, 255, 255))
    menu_text = font.render("Main Menu", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(result, ((w - result.get_width())/2, 120))
    screen.blit(rematch_text, ((w - rematch_text.get_width())/2, 180))
    screen.blit(menu_text, ((w - menu_text.get_width())/2, 230))
    screen.blit(quit_text, ((w - quit_text.get_width())/2, 280))
