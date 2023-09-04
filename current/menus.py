import important
import pygame
import fight
import sounds
import visuals
import text

# pygame setup
pygame.init()
pygame.mixer.init()  # Initialize the mixer
w = important.SCREEN_WIDTH
h = important.SCREEN_HEIGHT
screen = important.screen

font = pygame.font.Font(None, 36)

def menu():
    running = True
    sounds.menu_music.play()
    while running:
        visuals.draw_menu()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text.x_min(text.start) <= event.pos[0] <= text.x_max(text.start) and (h / 2 + 75) <= event.pos[1] <= (h / 2 + 75) + text.start.get_height():  # Start option clicked
                    sounds.menu_music.stop()
                    match()
                elif text.x_min(text.exit) <= event.pos[0] <= text.x_max(text.exit) and (h / 2 + 125) <= event.pos[1] <= (h / 2 + 125) + text.exit.get_height():  # Exit option clicked
                    running = False

    pygame.quit()

def pause(paused):
    print("paused")
    running = True
    pygame.mixer.music.pause()
    while running:
        screen.fill("red")
        visuals.draw_pause()
        pygame.display.flip()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text.x_min(text.resume) <= event.pos[0] <= text.x_max(text.resume) and 180 <= event.pos[1] <= 180 + text.paused.get_height():  # Start option clicked
                    pygame.mixer.music.unpause()
                    return False
                elif text.x_min(text.menu) <= event.pos[0] <= text.x_max(text.menu) and 230 <= event.pos[1] <= 230 + text.menu.get_height():  # Exit option clicked
                    sounds.fight_music.stop()
                    menu()
                elif text.x_min(text.quit) <= event.pos[0] <= text.x_max(text.quit) and 280 <= event.pos[1] <= 280 + text.quit.get_height():
                    running = False
   
    pygame.quit()

def match():
    print("FIGHT!")
    running = True    
    paused = False
    important.player1 = 20; important.player2 = 20
    pygame.mixer.music.load(sounds.music)
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    while pause(paused) == True:
                        pause(paused)
                    print("unpaused")
        visuals.draw_arena()
        pygame.display.flip()
        important.current_time = pygame.time.get_ticks()
        important.elasped_time = [important.current_time - important.animation_timer[0], important.current_time - important.animation_timer[1]]

        #enable fight controls
        fight.player() #fight controls for player 1
        fight.bot() #fight controls for player 2 (Bot)

        #when user enters anything to text input it closes the game
        if important.player1 <= 0 or important.player2 <= 0:
            pygame.mixer.music.stop()
            sounds.defeat.play()
            sound_time = sounds.defeat.get_length() 
            start_time = important.current_time
            while important.current_time - start_time < sound_time * 1000:
                important.current_time = pygame.time.get_ticks()
                #print(important.current_time)

            #output winner when the other loses all health
            if important.player1 <= 0:
                sounds.lose.play()
                winner = "Player 2 Wins!"
                print("Player 2 wins!")
            elif important.player2 <= 0:
                sounds.win.play()
                winner = "Player 1 Wins!"
                print("Player 1 wins!")
            elif important.player1 <= 0 and important.player2 <= 0:
                sounds.lose.play()
                winner = "Double KO!"
                print("Double KO!")

            gameover(winner)

    pygame.quit()

def gameover(winner):
    print("Match over. Thanks for playing!")
    running = True
    while running:
        screen.fill("red")
        visuals.draw_over(winner)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text.x_min(text.rematch) <= event.pos[0] <= text.x_max(text.rematch) and 180 <= event.pos[1] <= 180 + text.rematch.get_height:  # Start option clicked
                    sounds.win.stop()
                    sounds.lose.stop()
                    match()
                elif text.x_min(text.menu) <= event.pos[0] <= text.x_max(text.menu) and 230 <= event.pos[1] <= 230 + text.menu.get_height:  # Main Menu option clicked
                    sounds.win.stop()
                    sounds.lose.stop()
                    menu()
                elif text.x_min(text.quit) <= event.pos[0] <= text.x_max(text.quit) and 280 <= event.pos[1] <= 280 + text.quit.get_height:  # Exit option clicked
                    running = False

    pygame.quit()
