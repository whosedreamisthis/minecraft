import pygame
from consts import *
from cell import Cell

CELL_SIZE = 50
class Board():
    def __init__(self):
        self.cells = []
        self.neighbours = [(-1,-1), (0,-1),(1,-1),(1,1), (0,1),(-1,1), (-1,0),(1,0)]

        self.init_cells()
        self.game_over = False
        self.first_cell_press = True



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
             
    def reset(self):
        self.game_over = False
        self.first_cell_press = True
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j][i].reset()    
                
    def show_all_bombs(self):
        for j in range(SCREEN_HEIGHT//CELL_SIZE):
            for i in range(SCREEN_WIDTH//CELL_SIZE):
                self.cells[j][i].show_bomb()       
            
    def on_cell_pressed(self, cell):
        if self.first_cell_press:
            self.first_cell_press = False
            cell.clear_bomb()
            for neighbour in self.neighbours:
                neighbour_x = cell.i + neighbour[0]
                neighbour_y = cell.j + neighbour[1]
            
                if neighbour_x >= 0 and neighbour_x < SCREEN_WIDTH // CELL_SIZE \
                and neighbour_y >= 0 and neighbour_y < SCREEN_HEIGHT:
                    self.cells[neighbour_y][neighbour_x].clear_bomb()
                    
            
        if cell.bomb:
            self.game_over = True
        else:
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
        

    
    
                