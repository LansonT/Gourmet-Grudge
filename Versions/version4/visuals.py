import pygame
import important

pygame.init()

w = important.SCREEN_WIDTH
h = important.SCREEN_HEIGHT
screen = important.screen

last_w_animation_time = 0
W_Key = False


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
animated_image = load_and_rotate_image(r"CS50Project\images\player\rattack.jpg", 100)  # Replace 'r"CS50Project\images\player\rattack.jpg"' with the actual path to your animation image.

# Define initial position for the animation
animation_x = (important.SCREEN_WIDTH - animated_image.get_width()) // 2
animation_y = important.SCREEN_HEIGHT  # Start from the bottom

animation_timer = important.current_time #it shouldn't always be current time
animation_active = False #for "W"


def new_arena():
    global last_w_animation_time, W_Key, animation_x, animation_y, animation_timer, animation_active

    # Define animation duration in milliseconds
    animation_duration = 1000  # 1 second

    # Cooldown duration in milliseconds
    cooldown_duration = 500  # 0.5 seconds

    if W_Key and not animation_active and important.current_time - last_w_animation_time >= cooldown_duration:  # Trigger animation on "W" key press
        print("animation_active")
        animation_active = True
        animation_timer = important.current_time
        last_w_animation_time = important.current_time

    image = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Arena.jpg"), (400, 400))
    boxer = pygame.transform.smoothscale(pygame.image.load(r"CS50Project\images\Boxer.jpg"), (100,100))
    screen.blit(image, (0,0))
    screen.blit(boxer, ((w-boxer.get_width())/2,100))

    if animation_active:
        elapsed_time = important.current_time - animation_timer
        
        if elapsed_time < animation_duration:
            animation_y = important.SCREEN_HEIGHT - (elapsed_time / animation_duration) * (important.SCREEN_HEIGHT + animated_image.get_height())
            screen.blit(animated_image, (animation_x, animation_y))
        else:
            W_Key = False
            animation_active = False



    

