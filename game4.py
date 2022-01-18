import pygame
x = pygame.init()

#Creating window
gameWindow = pygame.display.set_mode((1200, 500))  # screen size
pygame.display.set_caption("My First Game")  # for title

# Game specific variables
exit_game = False
game_over = False