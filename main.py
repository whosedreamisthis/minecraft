import pygame
from consts import *
from board import Board
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Minecraft")
board = Board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    board.draw(screen)
    pygame.display.update()
            

pygame.quit()