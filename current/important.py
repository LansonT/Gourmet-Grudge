import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Get the current time in milliseconds
current_time = pygame.time.get_ticks()

#variables:
#health points
player1 = 20 #player hp
player2 = 20 #bot hp

stunned = [False, False]
when_stunned = [0, 0]
health_stunned = [20, 20]
stun_timer = 5 #5 seconds (* 1000 milliseconds in fight.py)

animate = [False, False]
attack_time = [1, 1]
last_attack = [1, 0]
Attack = 3
Bot_Attack = 3

animation_timer = [0, 0]
animation_duration = 1000
elasped_time = [0, 0]

Block = 3
Bot_Block = 3

def image_loading(path):
    image = pygame.image.load(path)
    scaled_width = 100
    scaled_height = int(scaled_width * image.get_width() / image.get_height())
    image = pygame.transform.scale(image, (scaled_width, scaled_height))
    return image

knife = image_loading(r"CS50Project/images/player/knife.png")
fork = image_loading(r"CS50Project/images/player/fork.png")
spoon = image_loading(r"CS50Project/images/player/spoon.png")

pepper = image_loading(r"CS50Project/images/bot/PixelDoug.png")
oo = image_loading(r"CS50Project/images/bot/juice.png")
classroom = pygame.transform.smoothscale(pygame.image.load(r"CS50Project/images/classroom.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

taco = image_loading(r"CS50Project/images/bot/SpaghettiTaco.png")
ball = image_loading(r"CS50Project/images/bot/meatball.png")
kitchen = pygame.transform.smoothscale(pygame.image.load(r"CS50Project/images/kitchen.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

if random.randrange(1,101) <= 30:
    fighter = pepper
    b_lattack = oo
    b_rattack = oo
    ring = classroom
else:
    fighter = taco
    b_lattack = ball
    b_rattack = ball
    ring = kitchen


#b_lattack = image_loading(r"CS50Project/images/bot/lattack.png")
#b_rattack = image_loading(r"CS50Project/images/bot/rattack.png")

#p_lblock = image_loading(r"CS50Project/images/player/lblock.jpg")
#p_rblock = image_loading(r"CS50Project/images/player/rblock.jpg")
#b_lblock = image_loading(r"CS50Project/images/bot/lblock.jpg")
#b_rblock = image_loading(r"CS50Project/images/bot/rblock.jpg")

block = image_loading(r"CS50Project/images/block.png")
