print("Importing")
import pygame
import menus

print("setting up")
# pygame setup
screen = menus.screen

def main():
    running = True
    print("begin!") 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        menus.menu()

main()