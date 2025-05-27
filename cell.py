import pygame
from consts import *
from button import Button
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = "Covered"
        self.button = Button(self.x * CELL_SIZE - 1,y * CELL_SIZE - 1,CELL_SIZE-1,CELL_SIZE - 1, "B", action=self.pressed)
        self.color = GRAY
        
    def draw(self,screen):
        pygame.draw.rect(screen,GRAY,(self.x * CELL_SIZE - 1,self.y * CELL_SIZE - 1, CELL_SIZE-1,CELL_SIZE-1))
        self.button.draw(screen)
        
    def pressed(self):
        self.color = RED
        print(f"button pressed {self.x} {self.y}")
        
    def handle_event(self,event):
        self.button.handle_event(event)
    