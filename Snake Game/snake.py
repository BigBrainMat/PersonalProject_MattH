#imports
import pygame
import time
import random

#inital use
pygame.init()

#sets a cool caption for our game
pygame.display.set_caption('Snake game made by Matt') 

#creates a clock
clock = pygame.time.Clock()

#setes colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
blue = (50, 153, 213)
red = (213, 50, 80)
green = (0, 255, 0)
 
#sets display things
disp_width = 600
disp_height = 400

#sets display stuff
display = pygame.display.set_mode((disp_width, disp_height))

#sets some other varables and fonts
snake_block = 10
snake_speed = 15 
font_style = pygame.font.SysFont("calibri", 20)
score_font = pygame.font.SysFont("timesnewroman", 30)

#lets you send a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [disp_width / 6, disp_height / 3])

#Creats a list for the snake game
def sSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

#sets a display for the score
def my_score(score):
    
    value = score_font.render("Your Score: " + str(score), True, red)
    display.blit(value, [0, 0])
 
#makes the game loop so the game can run
def gameLoop():
    
    #sets a bunch of diffrent varaibles
    game_over = False
    game_close = False
    x1 = disp_width / 2
    y1 = disp_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    sLength = 1

    #creats the snake food
    food2 = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
    food1 = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
 
 #whats runs when the game is not over
    while not game_over:

 # what runs with the game is over
        while game_close == True:
            
            #tells us we lost
            --message("NEEDS TO BE FIXED", red)--

            #sets colour
            display.fill(blue)
            
            #Changes the score
            my_score(sLength - 1)

            #updates the game
            pygame.display.update()
 
 # checks what key is pressed so you can play again
            for event in pygame.event.get():
               
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_q:
                        
                        game_over = True
                        game_close = False
                    
                    if event.key == pygame.K_r:
                        
                        gameLoop()

#checks to see what keys are pressed to move snake
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                game_over = True

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                   
                    y1_change = -snake_block
                    x1_change = 0

                elif event.key == pygame.K_DOWN:
                   
                    y1_change = snake_block
                    x1_change = 0

                elif event.key == pygame.K_LEFT:
                    
                    x1_change = -snake_block
                    y1_change = 0
                
                elif event.key == pygame.K_RIGHT:
                   
                    x1_change = snake_block
                    y1_change = 0
                
 #checks if your out of bounds
        if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
            game_close = True
        
        y1 += y1_change
        x1 += x1_change
        
        #sets colur again
        display.fill(green)
        
        #draws the food
        pygame.draw.rect(display, red, [food2, food1, snake_block, snake_block])
        
        #values used to make snake longer and shorter
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        #checks if the snake has tuched its self
        if len(snake_List) > sLength:
            del snake_List[0]
 
         #checks if the snake has tuched its self
        for x in snake_List[:-1]:
            
            if x == snake_Head:
                
                game_close = True
 
#sets current snake and score values 
        sSnake(snake_block, snake_List)
        my_score(sLength - 1)
 
 #updates the game
        pygame.display.update()

#Creating more food 
        if x1 == food2 and y1 == food1:
            food2 = round(random.randrange(0, disp_width - snake_block) / 10.0) * 10.0
            food1 = round(random.randrange(0, disp_height - snake_block) / 10.0) * 10.0
            sLength += 1
 #messes with the snakes speed
        clock.tick(snake_speed)
 
 #exits the game
    pygame.quit()
    quit()
 
 #ends the loop
gameLoop()