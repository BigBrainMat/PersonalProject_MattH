# Imports
import pygame
import time

pygame.init()

# Sets colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Sets display size
dis=pygame.display.set_mode((800,600))

# Sets some values used later
x1 = 300
y1 = 300
x1_change = 0       
y1_change = 0
snake_block = 10
snake_speed = 15
disp_width = 800
disp_height  = 600
display = pygame.display.set_mode((disp_width, disp_width))

# Creates a font
font_style = pygame.font.SysFont(None, 50)

# Creates the message output
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [disp_width/2, disp_height/2])

# Makes a clock
clock = pygame.time.Clock()

# Updates the screen
pygame.display.update()

# Sets the caption for the 
pygame.display.set_caption('A pretty good snake game')

game_over = False

# A while loop and a for loop and a if telling us if the game is actualy over and closes it if so 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    if x1 >= disp_width or x1 < 0 or y1 >= disp_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, white, [x1, y1, snake_block *2, snake_block *2])
 
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("You lost",red)
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit()