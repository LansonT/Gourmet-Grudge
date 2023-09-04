import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Get the current time in milliseconds
current_time = pygame.time.get_ticks()

#variables:
#health points
player1 = 20 #player hp
player2 = 20 #bot hp

stunned = [False, False]
when_stunned = [0, 0]
stun_timer = 5 #5 seconds (* 1000 milliseconds in fight.py)

animate = False
bonus = False
attack_time = [1, random.randrange(1, 6)]
last_attack = [1, 0]
Bot_Attack = 3

animation_timer = [0, 0]
animation_duration = 1000

Block = [False, False, False]
Bot_Block = [False, False, False]