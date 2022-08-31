# Imports pygame
import pygame

pygame.init()
# Sets display size
dis=pygame.display.set_mode((400,300))
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
 
pygame.quit()
quit()