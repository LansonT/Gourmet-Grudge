print("Importing")
import pygame
import important
import menus

print("setting up")
# pygame setup
screen = important.screen

def main():
    running = True
    print("begin!") 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        menus.menu()
    pygame.quit()

main()