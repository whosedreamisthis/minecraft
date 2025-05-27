import pygame
from consts import *
from board import Board

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Minesweepwe")
board = Board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if board.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("reset board")
                    board.reset()
        else:
            board.handle_event(event)
    
    screen.fill(WHITE)
    if board.game_over:
        board.show_all_bombs()
    board.draw(screen)
    pygame.display.update()
            

pygame.quit()