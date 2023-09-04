import pygame
import important

pygame.init()

w = important.SCREEN_WIDTH
h = important.SCREEN_HEIGHT
screen = important.screen

Attack_Keys = [False, False, False] #player's l, m, r
Bot_Attack = [False, False, False]

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

def draw_arena():
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

# Function to load and rotate images
def load_and_rotate_image(image_path, desired_width):
    image = pygame.image.load(image_path)
    aspect_ratio = image.get_width() / image.get_height()
    new_image_width = desired_width
    new_image_height = int(new_image_width / aspect_ratio)
    image = pygame.transform.scale(image, (new_image_width, new_image_height))
    return pygame.transform.rotate(image, -90)  # Rotate counter-clockwise by 90 degrees

# Load the image for the animation
left_animated_image = load_and_rotate_image(r"CS50Project\images\player\lattack.jpg", 100)  # Replace 'r"CS50Project\images\player\lattack.jpg"' with the actual path to the left animation image.
right_animated_image = load_and_rotate_image(r"CS50Project\images\player\rattack.jpg", 100)  # Replace 'r"CS50Project\images\player\rattack.jpg"' with the actual path to your animation image.
left_block = load_and_rotate_image(r"CS50Project\images\player\lblock.jpg", 100)
right_block = load_and_rotate_image(r"CS50Project\images\player\rblock.jpg", 100)

bot_punch_left = load_and_rotate_image(r"CS50Project\images\bot\lattack.jpg", 100)
bot_punch_right = load_and_rotate_image(r"CS50Project\images\bot\rattack.jpg", 100)
bot_block_left = load_and_rotate_image(r"CS50Project\images\bot\lblock.jpg", 100)
bot_block_right = load_and_rotate_image(r"CS50Project\images\bot\rblock.jpg", 100)

# Define initial position for the middle animation (W)
W_x = (important.SCREEN_WIDTH - right_animated_image.get_width()) // 2
W_y = important.SCREEN_HEIGHT  # Start from the bottom

W_timer = important.current_time #it shouldn't always be current time
W_active = False #for "W"

# Define initial position for the left animation (A)
A_x = (important.SCREEN_WIDTH - left_animated_image.get_width()) // 2 - 100  # Move left by 100 pixels
A_y = important.SCREEN_HEIGHT  # Start from the bottom

A_timer = 0
A_active = False

# Define initial position for the left animation (A)
D_x = (important.SCREEN_WIDTH - right_animated_image.get_width()) // 2 + 100  # Move right by 100 pixels
D_y = important.SCREEN_HEIGHT  # Start from the bottom

D_timer = 0
D_active = False

Block_Keys = [False, False, False] #player's AS, S, SD
Bot_Block = [False, False, False]

L_x = (important.SCREEN_WIDTH - right_animated_image.get_width()) // 2 - 100
L_y = 0

L_active = False
L_timer = 0

M_x = (important.SCREEN_WIDTH - right_animated_image.get_width()) // 2
M_y = 0

M_active = False
M_timer = 0

R_x = (important.SCREEN_WIDTH - right_animated_image.get_width()) // 2 + 100
R_y = 0

R_active = False
R_timer = 0

def new_arena():
    global W_x, W_y, W_timer, W_active
    global A_x, A_y, A_timer, A_active
    global D_x, D_y, D_timer, D_active
    global L_x, L_y, L_timer, L_active
    global M_x, M_y, M_timer, M_active
    global R_x, R_y, R_timer, R_active

    # Define animation duration in milliseconds
    animation_duration = 1000  # 1 second

    if Attack_Keys[1] and not W_active:  # Trigger animation on "W" key press
        print("animation_active")
        W_active = True
        W_timer = important.current_time
    elif Attack_Keys[0] and not A_active:  # Trigger animation on "A" key press
        print("A active")
        A_active = True
        A_timer = important.current_time
    elif Attack_Keys[2] and not D_active:  # Trigger animation on "D" key press
        print("D active")
        D_active = True
        D_timer = important.current_time

    if Bot_Attack[0] and not L_active:
        L_active = True
        L_timer = important.current_time

    if Bot_Attack[1] and not M_active:
        M_active = True
        M_timer = important.current_time
    
    if Bot_Attack[2] and not R_active:
        R_active = True
        R_timer = important.current_time

    image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Arena.jpg"), (400, 400))
    boxer = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Boxer.jpg"), (100,100))
    screen.blit(image, (0,0))
    screen.blit(boxer, ((w-boxer.get_width())/2,100))

    if W_active:
        elapsed_time = important.current_time - W_timer

        if elapsed_time < animation_duration:
            W_y = important.SCREEN_HEIGHT - (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + right_animated_image.get_height())
            screen.blit(right_animated_image, (W_x, W_y))
        else:
            Attack_Keys[1] = False
            W_active = False

    if A_active:
        elapsed_time = important.current_time - A_timer
        
        if elapsed_time < animation_duration:
            A_y = important.SCREEN_HEIGHT - (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + left_animated_image.get_height())
            screen.blit(left_animated_image, (A_x, A_y))
        else:
            Attack_Keys[0] = False
            A_active = False

    if D_active:
        elapsed_time = important.current_time - D_timer

        if elapsed_time < animation_duration:
            D_y = important.SCREEN_HEIGHT - (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + right_animated_image.get_height())
            screen.blit(right_animated_image, (D_x, D_y))
        else:
            Attack_Keys[2] = False
            D_active = False

    if L_active:
        elapsed_time = important.current_time - L_timer

        if elapsed_time < animation_duration:
            L_y = 0 + (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + bot_punch_left.get_height())
            screen.blit(bot_punch_left, (L_x, L_y))
        else:
            Bot_Attack[0] = False
            L_active = False

    if M_active:
        elapsed_time = important.current_time - M_timer

        if elapsed_time < animation_duration:
            M_y = 0 + (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + bot_punch_left.get_height())
            screen.blit(bot_punch_left, (M_x, M_y))
        else:
            Bot_Attack[1] = False
            M_active = False
    
    if R_active:
        elapsed_time = important.current_time - R_timer

        if elapsed_time < animation_duration:
            R_y = 0 + (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + bot_punch_right.get_height())
            screen.blit(bot_punch_right, (R_x, R_y))
        else:
            Bot_Attack[2] = False
            R_active = False


    if Block_Keys[1]:
        screen.blit(left_block, ((important.SCREEN_WIDTH - left_block.get_width()) // 2, important.SCREEN_HEIGHT - left_block.get_height() - 50))  # Display 100 pixels above the bottom
    
    elif Block_Keys[2]:
        screen.blit(right_block, ((important.SCREEN_WIDTH - right_block.get_width()) // 2 + 100, important.SCREEN_HEIGHT - right_block.get_height() - 50))  # Display 100 pixels above the bottom

    elif Block_Keys[0]:
        screen.blit(left_block, ((important.SCREEN_WIDTH - left_block.get_width()) // 2 - 100, important.SCREEN_HEIGHT - left_block.get_height() - 50))  # Display 100 pixels above the bottom

    if Bot_Block[0]:
        screen.blit(bot_block_left, ((important.SCREEN_WIDTH - bot_block_left.get_width()) // 2 - 100, bot_block_left.get_height() - 50))

    elif Bot_Block[1]:
        screen.blit(bot_block_right, ((important.SCREEN_WIDTH - bot_block_right.get_width()) // 2, bot_block_right.get_height() - 50))

    elif Bot_Block[2]:
        screen.blit(bot_block_right, ((important.SCREEN_WIDTH - bot_block_right.get_width()) // 2 + 100, bot_block_right.get_height() - 50))
    
    font = pygame.font.Font(None, 36)
    health1 = font.render(f"player 1: {important.player1}", True, (255,255,255))
    health2 = font.render(f"player 2: {important.player2}", True, (255,255,255))
    screen.blit(health1, (20,20))
    screen.blit(health2, ((important.SCREEN_WIDTH - health2.get_width() - 20),20))
    
