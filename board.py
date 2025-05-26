import pygame
from consts import *
from cell import Cell
CELL_SIZE = 50
class Board():
    def __init__(self):
        self.cells = []
        self.init_cells()
    
    def init_cells(self):
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            self.cells.append([])
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j].append(Cell(j,i))
                print(f"cell {i} {j} {self.cells[j][i]}")
                
    def draw(self,screen):
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j][i].draw(screen)

    
    
                