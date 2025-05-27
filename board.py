import pygame
from consts import *
from cell import Cell

CELL_SIZE = 50
neighbours = [(-1,-1), (0,-1),(1,-1),(1,1), (0,1),(-1,1), (-1,0),(1,0)]
first_cell_press = True
class Board():
    def __init__(self):
        self.cells = []
        self.init_cells()
    
    def on_cell_pressed(self, cell):
        global first_cell_press
        if first_cell_press:
            first_cell_press = False
            cell.clear_bomb()
        
    def init_cells(self):
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            self.cells.append([])
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j].append(Cell(i,j,CELL_SIZE,CELL_SIZE,"B",action=self.on_cell_pressed))
                # Button(self.x * CELL_SIZE - 1,y * CELL_SIZE - 1,CELL_SIZE-1,CELL_SIZE - 1, "B")
                

    def draw(self,screen):
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j][i].draw(screen)
                
    def handle_event(self,event):
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j][i].handle_event(event)
        

    
    
                