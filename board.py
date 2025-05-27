import pygame
from consts import *
from cell import Cell

CELL_SIZE = 50
first_cell_press = True
class Board():
    def __init__(self):
        self.cells = []
        self.neighbours = [(-1,-1), (0,-1),(1,-1),(1,1), (0,1),(-1,1), (-1,0),(1,0)]

        self.init_cells()

    def num_bomb_neighbours(self, cell):
        num_bombs = 0
        for neighbour in self.neighbours:
            neighbour_x = cell.i + neighbour[0]
            neighbour_y = cell.j + neighbour[1]
            
            if neighbour_x >= 0 and neighbour_x < SCREEN_WIDTH // CELL_SIZE \
                and neighbour_y >= 0 and neighbour_y < SCREEN_HEIGHT:
                if self.cells[neighbour_y][neighbour_x].bomb == True:
                    num_bombs += 1
        return num_bombs
                  
            
    def on_cell_pressed(self, cell):
        
        global first_cell_press
        if first_cell_press:
            first_cell_press = False
            cell.clear_bomb()
        
        num_bombs = self.num_bomb_neighbours(cell)
        cell.num_neighbour_bombs = num_bombs
          
                
        
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
        

    
    
                