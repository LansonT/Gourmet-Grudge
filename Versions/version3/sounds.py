import pygame
import random

pygame.mixer.init()  # Initialize the mixer

#music
menu_music = pygame.mixer.Sound(r"CS50Project\audio\Music\menu.mp3")
music = r"CS50Project\audio\Music\music.mp3" #replaces fight_music (for now maybe)
fight_music = pygame.mixer.Sound(r"CS50Project\audio\Music\music.mp3") 
fight_music.set_volume(0.15)
win = pygame.mixer.Sound(r"CS50Project\audio\Music\win.mp3")
lose = pygame.mixer.Sound(r"CS50Project\audio\Music\lose.wav")

#voice effects
voice_1 = [pygame.mixer.Sound(r"CS50Project\audio\VO\lose1.mp3"), pygame.mixer.Sound(r"CS50Project\audio\VO\lose2.mp3"), pygame.mixer.Sound(r"CS50Project\audio\VO\lose3.mp3")]
defeat = random.choice(voice_1)
stunned = pygame.mixer.Sound(r"CS50Project\audio\VO\stunned.mp3")
hurt = pygame.mixer.Sound(r"CS50Project\audio\VO\hurt1.mp3")

#sound effects
block = pygame.mixer.Sound(r"CS50Project\audio\Effects\block.mp3")
punch = pygame.mixer.Sound(r"CS50Project\audio\Effects\punch1.mp3")