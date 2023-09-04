import pygame
import important
import random
import sounds
import visuals

# pygame setup
pygame.init()
pygame.mixer.init()  # Initialize the mixer
screen = important.screen

#player
def player():
    #stunned
    if important.stunned[0]: #if stunned:
        #for player attempts to take action, nothing happens
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d:
                    sounds.stunned.play()
                    print("Stunned")
        if important.current_time - important.when_stunned[0] < important.stun_timer * 1000: #while stunned:    
            if important.health_stunned[0] > important.player1: #if taken damage (while stunned):
                #lose extra health
                important.player1 -= 1
                print(f"Bonus hit! {important.player1}")
                important.stunned[0] = False

        else:
            #player is no longer stunned
            important.stunned[0] = False

    else:
        #blocking
        #elif player holds "S":
        if pygame.key.get_pressed()[pygame.K_s] and not important.animate[0]:
            #if player also holds *key*:
            if pygame.key.get_pressed()[pygame.K_a]:
                #print("blocking left")
                important.Block = 0
            elif pygame.key.get_pressed()[pygame.K_d]:
                #print("blocking right")
                important.Block = 2
            else:
                #print("blocking middle")
                important.Block = 1

        #attacking
        #if enough time has passed (current time - last time attacked)
        elif important.current_time - important.last_attack[0] >= important.attack_time[0] * 1000 and not important.animate[0]: #for when action is allowed (pygame.event.get())
            important.Attack = 3
            for event in pygame.event.get():
                #if the player tries to attack:
                if event.type == pygame.KEYDOWN:
                    #if the player presses *key*:
                    if event.key == pygame.K_a: #'A'
                        important.Attack = 0
                    elif event.key == pygame.K_w: #'W'
                        important.Attack = 1
                    elif event.key == pygame.K_d: #'D'
                        important.Attack = 2
                
                important.last_attack[0] = important.current_time
        
            if important.Attack < 3:
                important.animate[0] = True
                important.animation_timer[0] = important.current_time
                print("player attacking")

        if important.animate[0]:
            if important.current_time - important.animation_timer[0] < important.animation_duration:
                if important.Bot_Block == important.Attack:
                    important.stunned[0] = True
                    important.when_stunned[0] = important.current_time
                    important.health_stunned[0] = important.player1
                    important.animate[0] = False
                    sounds.block.play()
                    print("BLOCKED!")

            else:
                if not important.stunned[0]:
                    important.player2 -= 1
                    important.last_attack[0] = important.current_time
                    sounds.punch.play()
                    sounds.hurt.play()
                    important.animate[0] = False
                    print(f"Bot: {important.player2}")

    #not blocking
    #elif if not holding "S":
    if not pygame.key.get_pressed()[pygame.K_s]:
        #all blocks = False
        important.Block = 3

#bot
def bot():
    #stunned
    if important.stunned[1]: #if stunned:
        if important.current_time - important.when_stunned[1] < important.stun_timer * 1000: #while stunned:                
            if important.health_stunned[1] > important.player2: #if taken damage (while stunned)
                #lose extra health
                important.player2 -= 1
                print(f"Bonus hit! {important.player2}")
                important.stunned[1] = False

        else:
            #player is no longer stunned
            important.last_attack[1] = important.current_time
            important.stunned[1] = False
    
    else:
        if important.current_time - important.last_attack[1] >= important.attack_time[1] * 1000 and not important.animate[1]:
            r = random.randrange(1, 101) #pick a number from 1 - 100 (numbers below 101)
            important.Bot_Block = 3

        #blocking
            if 1 <= r <= 40:
                n = random.randrange(0, 3)
                important.last_attack[1] = important.current_time
                important.Bot_Block = n
            
        #attacking
            elif 40 < r <= 100:
                    important.Bot_Attack = random.randrange(0, 3)
                    #print(important.Bot_Attack)
                    important.animate[1] = True
                    important.animation_timer[1] = important.current_time
                    print("bot attacking")

            important.attack_time[1] = random.randrange(1, 6)
            
        if important.animate[1]:
            if important.current_time - important.animation_timer[1] < important.animation_duration:
                if important.Block == important.Bot_Attack:
                    important.stunned[1] = True
                    important.when_stunned[1] = important.current_time
                    important.health_stunned[1] = important.player2
                    important.animate[1] = False
                    sounds.block.play()
                    print("BLOCKED THE BOT!")

            else:
                if not important.stunned[1]:
                    important.player1 -= 1
                    important.last_attack[1] = important.current_time
                    sounds.punch.play()
                    sounds.hurt.play()
                    important.animate[1] = False
                    print(f"Player: {important.player1}")