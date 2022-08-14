# All my imports
import pygame
import time
import random

#initializes pygame
pygame.init()

#           screen and font

#makes a screen to use
screen = pygame.display.set_mode((720,720))
#sets a captio for the screen
pygame.display.set_caption("Reaction Time Test!!")

mainFont = pygame.font.SysFont("Roboto", 75)

# ALL DIFFRENT PAGES (in order of the actual game)
# Title
title = mainFont.render("Reaction Time Game", True, "red")
titleRect = title.get_rect(center=(360, 50))
# Click to start 
clickToStart = mainFont.render("Click here to Start", True, "yellow")
clickToStartRect = clickToStart.get_rect(center=(360, 360))
#waiting 
waiting = mainFont.render("Wait for just a bit", True, "grey")
waitingRect = waiting.get_rect(center=(360, 360))
# click 
clicked = mainFont.render("Click NOW!!!!!!", True, "grey")
clickedRect = clicked.get_rect(center=(360, 360))
# score 
score = mainFont.render("Score: 1000 ms", True, "red")
scoreRect = score.get_rect(center=(360, 360))

# game state
gameState = "Click here to Start"

#Times and clicks
startTime, endTime = 0, 0

#game loop
while True:
    #Any Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #checks if mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gameState == "Click here to Start":
                gameState = "Waiting"
            elif gameState == "Wait for just a bit":
                endTime = time.time()
                gameState = "Showing Results now"
            else:
                gameState = "Click here to Start"
    
    screen.fill("grey")
    
    #Puts title opn screen
    screen.blit(title, titleRect)

    #logic for game
    if gameState == "Click here to Start":
        #puts click to start text on screen
        screen.blit(clickToStart ,clickToStartRect)
    
    elif gameState == "Waiting":
        screen.fill("yellow")

        # Puts up waiting text
        screen.blit(waiting, waitingRect)
        pygame.display.update()

        # sets and times the delay between click and the next click
        delayTime = random.uniform(1, 10)
        time.sleep(delayTime)

        #starts test
        gameState = "Wait for just a bit"
        
        #put together our score
        startTime = time.time()
        #Checks if game is starting
    elif gameState == "Wait for just a bit":
        screen.fill("green")
        screen.blit(clicked, clickedRect)
        # showing results game state
    else:
        reaction = round((endTime - startTime) * 1000)
        # uses F string to pass the data into the final screen
        score = mainFont.render(f"Speed: {reaction} ms", True, "black")
        #sends all to screen
        screen.blit(score, scoreRect)
    # updates display
    pygame.display.update()