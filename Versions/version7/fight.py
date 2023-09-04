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
        health = important.player1 #health recorded for bonus damage
        while important.current_time - important.when_stunned[0] < important.stun_timer * 1000: #while stunned:    
            important.current_time = pygame.time.get_ticks() #current time is recorded
            bot() #bot can attack
            #for player attempts to take action, nothing happens
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d:
                        sounds.stunned.play()
                        print("Stunned")

                #if event.type == pygame.QUIT:
                    #pygame.quit

            if health > important.player1: #if taken damage (while stunned):
                #lose extra health
                important.player1 -= 1
                break #break out of while loop
        #player is no longer stunned
        important.stunned[0] = False

    #blocking
    #elif player holds "S":
    if pygame.key.get_pressed()[pygame.K_s]:
        #if player also holds *key*:
        if pygame.key.get_pressed()[pygame.K_a]:
            #print("blocking left")
            important.Block = [True, False, False]
            visuals.Block_Keys = [True, False, False]
        elif pygame.key.get_pressed()[pygame.K_d]:
            #print("blocking right")
            important.Block = [False, False, True]
            visuals.Block_Keys = [False, False, True]
        else:
            #print("blocking middle")
            important.Block = [False, True, False]
            visuals.Block_Keys = [False, True, False]

    #attacking
    #if enough time has passed (current time - last time attacked)
    elif important.current_time - important.last_attack[0] >= important.attack_time[0] * 1000:
        #for when action is allowed (pygame.event.get())
        n = 3
        for event in pygame.event.get():
            #if the player tries to attack:
            if event.type == pygame.KEYDOWN:
                #if the player presses *key*:
                if event.key == pygame.K_a: #'A'
                    n = 0
                elif event.key == pygame.K_w: #'W'
                    n = 1
                elif event.key == pygame.K_d: #'D'
                    n = 2

                if n < 3:
                    #attack[number] is enable
                    important.animation_timer[0] = important.current_time
                    visuals.Attack_Keys[n] = True

                    #while animation is playing:
                    #while important.current_time - important.animation_timer[0] < important.animation_duration:
                    #    important.current_time = pygame.time.get_ticks()
                        #bot has a chance to take action/ block
                    #    bot()
                    if important.Bot_Block[n]:
                        important.stunned[0] = True
                        important.when_stunned[0] = important.current_time
                        sounds.block.play()
                        print("BLOCKED!")

                    if not important.stunned[0]:
                        important.player2 -= 1
                        sounds.punch.play()
                        sounds.hurt.play()
                        print(f"Bot: {important.player2}")
            
            important.last_attack[0] = important.current_time
    
    #not blocking
    #elif if not holding "S":
    if not pygame.key.get_pressed()[pygame.K_s]:
        #all blocks = False
        important.Block = [False, False, False]
        visuals.Block_Keys = [False, False, False]

#bot
def bot():
    #stunned
    if important.stunned[1]: #if stunned:
        health = important.player2 #health recorded for bonus damage
        while important.current_time - important.when_stunned[1] < important.stun_timer * 1000: #while stunned:    
            important.current_time = pygame.time.get_ticks() #current time is recorded
            important.last_attack[0] = important.attack_time[0]
            pygame.event.get() #resets what keys are being pressed, else player forever holds block..
            player()  # This allows the player to take actions while the bot is stunned
            
            if health > important.player2: #if taken damage (while stunned)
                #lose extra health
                important.player2 -= 1
                print(f"Bonus hit! {important.player2}")
                break #break out of while loop

        #player is no longer stunned
        important.stunned[1] = False
    
    r = random.randrange(1, 101) #pick a number from 1 - 100 (numbers below 101)

    if important.current_time - important.last_attack[1] >= important.attack_time[1] * 1000:

        important.Bot_Block = [False, False, False]
        visuals.Bot_Block = [False, False, False]

    #blocking
        if 1 <= r <= 40:
            n = random.randrange(0, 3)
            important.last_attack[1] = important.current_time
            important.Bot_Block[n] = True
            visuals.Bot_Block[n] = True
        
    #attacking
        elif 40 < r <= 100:
                n = random.randrange(0, 3)
                important.animation_timer[1] = important.current_time
                visuals.Bot_Attack[n] = True

                #while important.current_time - important.animation_timer[1] < important.animation_duration:
                #    important.current_time = pygame.time.get_ticks()
                #    pygame.event.get()
                #    player()
                if important.Block[n]:
                    important.stunned[1] = True
                    important.when_stunned[1] = important.current_time
                    sounds.block.play()
                    print("BLOCKED THE BOT!")
                
                if not important.stunned[1]:
                    important.player1 -= 1
                    important.last_attack[1] = important.current_time
                    sounds.hurt.play()
                    print(f"Player: {important.player1}")
        
