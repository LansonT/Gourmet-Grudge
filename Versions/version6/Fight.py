import pygame
import important
import random
import sounds
import visuals

# pygame setup
pygame.init()
pygame.mixer.init()  # Initialize the mixer
screen = important.screen

#player health points
player1 = 20
player2 = 20

#variables for blocking attacks
block = [False, False, False, False, False, False] #player1 l,m,r, player2 l,m,r
blocktime = 0
block_num = 3
stun = [False, False]
stun_time = [0, 0]
health_check = [0, 0]

last_attack_time = [0, 0]  # To store the time of the last attack

def fight1(): #controls for player 1
    global player1, player2, block, blocktime, stun, stun_time, health_check, last_attack_time #health of player2/bot
    
    stun_secs = 5 #seconds for stun timer

    #Stunned
    if stun[0] == True: #if player1 is stunned
        while important.current_time - stun_time[0] < stun_secs * 1000:
            bot()  # This allows the bot to take actions while the player is stunned
            important.current_time = pygame.time.get_ticks()
            #The player will not move during this time, if the player tries to take action while stunned
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        sounds.stunned.play()
                        print("Stunned")
                    elif event.key == pygame.K_a:
                        sounds.stunned.play()
                        print("Stunned")
                    elif event.key == pygame.K_d:
                        sounds.stunned.play()
                        print("Stunned")

            #If the bot attacks the Player during the while loop, break the loop early and the player loses another point.
            if health_check[0] > player1:
                player1 -= 1
                print(f"Bonus hit! {player1}")
                break
        stun[0] = False #player is no longer stunned

    #Block/Defense
    #Players can block by holding the 'S' key. The player can also change where they're guarding by holding either the 'A' key or the 'D' key
    if pygame.key.get_pressed()[pygame.K_s]:
        if pygame.key.get_pressed()[pygame.K_a]:
            #print("blocking left")
            visuals.Block_Keys = [True, False, False]
            block[0] = True
            block[1] = False
            block[2] = False
        elif pygame.key.get_pressed()[pygame.K_d]:
            #print("blocking right")
            visuals.Block_Keys = [False, False, True]
            block[0] = False
            block[1] = False
            block[2] = True
        else:
            #print("blocking middle")
            visuals.Block_Keys = [False, True, False]
            block[0] = False
            block[1] = True
            block[2] = False


    #Attacking
    #register behavior of input, 1 click = 1 hit
    else:
        #Checks the last time user has attack. Should prevent players from spamming
        if important.current_time - last_attack_time[0] >= 1 * 1000: #seconds * 1000 milliseconds:
            # 'W', 'A', 'D' keys are used to attack the opponent. Unless the bot is blocking then the player gets stunned.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w: #'W'
                        print("Pressed: W")
                        visuals.Attack_Keys[1] = True
                        if block[4] == True:
                            stun[0] = True
                            health_check[0] = player1
                            stun_time[0] = important.current_time
                            sounds.block.play()
                            print("BLOCKED!")
                        else:
                            sounds.punch.play()
                            sounds.hurt.play()
                            player2 -= 1
                            print(f"player 2 = {player2}")
                        screen.fill((0,0,0))
                    elif event.key == pygame.K_a:
                        print("Pressed: A")
                        visuals.Attack_Keys[0] = True
                        if block[3] == True:
                            stun[0] = True
                            stun_time[0] = important.current_time
                            health_check[0] = player1
                            sounds.block.play()
                            print("BLOCKED!")
                        else:
                            sounds.punch.play()
                            sounds.hurt.play()
                            player2 -= 1
                            print(f"player 2 = {player2}")
                    elif event.key == pygame.K_d:
                        print("Pressed: D")
                        visuals.Attack_Keys[2] = True
                        if block[5] == True:
                            stun[0] = True
                            stun_time[0] = important.current_time
                            health_check[0] = player1
                            sounds.block.play()
                            print("BLOCKED!")
                        else:
                            sounds.punch.play()
                            sounds.hurt.play()
                            player2 -= 1
                            print(f"player 2 = {player2}")
                last_attack_time[0] = important.current_time #records when player last attack. Should prevent players from spamming
    
    #Block Reset
    #After the player stops blocking, Update the game to disable blocking
    if not pygame.key.get_pressed()[pygame.K_s]:
        visuals.Block_Keys = [False, False, False]
        block[0] = False
        block[1] = False
        block[2] = False


def bot():
    global player1, player2, last_attack_time, block, blocktime, block_num, stun, stun_time, health_check

    #modifiable variables
    secs = 2
    stun_secs = 5
    block_secs = 3
    number = random.randrange(0, 9) #generates a random number to decide it's next move

    displace = important.current_time - last_attack_time[1]

    #Stunned
    if stun[1] == True: #If the bot gets stunned
        while important.current_time - stun_time[1] < stun_secs * 1000:
            important.current_time = pygame.time.get_ticks()
            pygame.event.get() #resets what keys are being pressed, else player forever holds block..
            fight1()  # This allows the player to take actions while the bot is stunned
            if health_check[1] > player2:
                player2 -= 1
                print(f"Bonus hit! {player2}")
                break
        stun[1] = False

    #"read" feature of bot. blocks everything
    #for when the generated number from before is larger than a 6, block all attack.
    if block_num > 6:
        while important.current_time - blocktime < block_secs * 1000:
            important.current_time = pygame.time.get_ticks()
            #print(f"auto time: {important.current_time - blocktime} ") #DEBUG PURPOSES
            block[3] = True
            block[4] = True
            block[5] = True
            for event in pygame.event.get():
                if stun[0] == True:
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        sounds.block.play()
                        stun[0] = True
                        health_check[0] = player1
                        stun_time[0] = important.current_time
                        print("A")
                    elif event.key == pygame.K_w:
                        sounds.block.play()
                        stun[0] = True
                        health_check[0] = player1
                        stun_time[0] = important.current_time
                        print("W")
                    elif event.key == pygame.K_d:
                        sounds.block.play()
                        stun[0] = True
                        health_check[0] = player1
                        stun_time[0] = important.current_time
                        print("D")
            if stun[0] == True:
                break
        block[3] = False 
        block[4] = False 
        block[5] = False
        block_num = 3

    #for when the bot decides to block at a random direction.
    if block[block_num] == True:
        if important.current_time - blocktime >= block_secs * 1000:
            block[block_num] = False
            visuals.Bot_Block[block_num-3] = False
            print("end of bot block...")
    else:
        #after a certain amount of time has passed, make another move
        if displace >= secs * 1000:
            #attack
            if number < 3: #for when bot attacks but the player is blocking
                block_num = random.randrange(0, 3)
                visuals.Bot_Attack[block_num] = True
                if block[block_num] == True:
                    stun[1] = True
                    health_check[1] = player2
                    stun_time[1] = important.current_time
                    sounds.block.play()
                    print("BLOCKED!")
                else: #if the player isn't blocking, hit the player
                    sounds.punch.play()
                    sounds.hurt.play()
                    if block_num == 0:
                        print("Attack Left(A)")
                        player1 -= 1
                        print(f"player 1 = {player1}")
                    elif block_num == 1:
                        print("Attack Middle(W)")
                        player1 -= 1
                        print(f"player 1 = {player1}")
                    elif block_num == 2:
                        print("Attack Right(R)")
                        player1 -= 1
                        print(f"player 1 = {player1}")
            #blocking
            elif number >= 3 and number <= 6: #bot blocks at the a random direction
                block_num = random.randrange(3, 6) #to block at a random direction and disable the block before the next move
                block[block_num] = True
                print("Bot Block...")
                visuals.Bot_Block[block_num-3] = True
                blocktime = important.current_time #to record how much time has passed when blocking
            else: #auto block / block everything
                blocktime = important.current_time
                block_num = number
                print("auto block")

            # Update the last_attack_time to the current time
            last_attack_time[1] = important.current_time
