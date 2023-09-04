import pygame
import Fight
import sounds

# pygame setup
pygame.init()
pygame.mixer.init()  # Initialize the mixer
w = 400
h = 400
screen = pygame.display.set_mode((w, h))

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

def menu():
    running = True
    sounds.menu_music.play()
    while running:
        screen.fill((0, 0, 0))
        draw_menu()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 170 <= event.pos[0] <= 230 and 180 <= event.pos[1] <= 210:  # Start option clicked
                    sounds.menu_music.stop()
                    match()
                elif 175 <= event.pos[0] <= 225 and 230 <= event.pos[1] <= 260:  # Exit option clicked
                    running = False

    pygame.quit()

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

def pause(paused):
    print("paused")
    running = True
    pygame.mixer.music.pause()
    while running:
        screen.fill("red")
        draw_pause()
        pygame.display.flip()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 170 <= event.pos[0] <= 230 and 180 <= event.pos[1] <= 210:  # Start option clicked
                    pygame.mixer.music.unpause()
                    return False
                elif 175 <= event.pos[0] <= 225 and 230 <= event.pos[1] <= 260:  # Exit option clicked
                    sounds.fight_music.stop()
                    menu()
                elif 170 <= event.pos[0] <= 230 and 280 <= event.pos[1] <= 310:
                    running = False
   
    pygame.quit()

def arena():
    image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Arena.jpg"), (400, 400))
    boxer = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Boxer.jpg"), (100,100))
    screen.blit(image, (0,0))
    screen.blit(boxer, ((w-boxer.get_width())/2,100))
    pygame.display.flip()

def match():
    print("FIGHT!")
    running = True    
    paused = False
    Fight.player1 = 20; Fight.player2 = 20
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
        arena()
            
        #enable fight controls
        Fight.fight1() #fight controls for player 1
        Fight.bot() #fight controls for player 2 (Bot)

        #when user enters anything to text input it closes the game
        if Fight.player1 <= 0 or Fight.player2 <= 0:
            pygame.mixer.music.stop()
            sounds.defeat.play()
            sound_time = sounds.defeat.get_length()
            current_time = pygame.time.get_ticks() 
            start_time = current_time
            while current_time - start_time < sound_time * 1000:
                current_time = pygame.time.get_ticks() 
                #print(current_time)

            #output winner when the other loses all health
            if Fight.player1 <= 0:
                sounds.lose.play()
                winner = "Player 2 Wins!"
                print("Player 2 wins!")
            elif Fight.player2 <= 0:
                sounds.win.play()
                winner = "Player 1 Wins!"
                print("Player 1 wins!")
            elif Fight.player1 <= 0 and Fight.player2 <= 0:
                sounds.lose.play()
                winner = "Double KO!"
                print("Double KO!")

            gameover(winner)

    pygame.quit()

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


def gameover(winner):
    print("Match over. Thanks for playing!")
    running = True
    while running:
        screen.fill("red")
        draw_over(winner)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 170 <= event.pos[0] <= 230 and 180 <= event.pos[1] <= 210:  # Start option clicked
                    sounds.win.stop()
                    sounds.lose.stop()
                    match()
                elif 175 <= event.pos[0] <= 225 and 230 <= event.pos[1] <= 260:  # Main Menu option clicked
                    sounds.win.stop()
                    sounds.lose.stop()
                    menu()
                elif 175 <= event.pos[0] <= 225 and 280 <= event.pos[1] <= 310:  # Exit option clicked
                    running = False

    pygame.quit()
