import pygame
from consts import *
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = "Covered"
        
    def draw(self,screen):
        pygame.draw.rect(screen,GRAY,(self.x * CELL_SIZE - 1,self.y * CELL_SIZE - 1, CELL_SIZE-1,CELL_SIZE-1))
    