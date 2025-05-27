import pygame
from consts import *
from button import Button
import random
BOMB_COLOR = RED
EMPTY_CELL_COLOR = GREEN
class Cell:
    def __init__(self, x, y, width, height, text, action=None,
                 normal_color = (128,128,128), hover_color = (200,200,200), pressed_color = (120,120,120),
                 font_size = 18, font_color=BLACK):
        self.i = x
        self.j = y
        self.rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, width-2, height-2)
        self.text = ""
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.font_color = font_color
        self.action = action#self.pressed
        self.num_neighbour_bombs = -1

        # Initialize the font for rendering text
        # Using None for default Pygame font, you can specify a font file path here
        self.font = pygame.font.Font(None, font_size) 

        self.current_color = self.normal_color # Tracks the current color state
        self.is_hovered = False # True if mouse is over the button
        self.is_pressed = False
        self.enabled = True
        

        self.state = "Covered"
        self.color = GRAY
        self.bomb = random.choice([True,False])
        
    def draw(self,screen):
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=0)

        # Render the text surface
        if GOD_MODE:
            if self.bomb:
                self.text = "b"
        text_surface = self.font.render(self.text, True, self.font_color)
        
        # Get the rectangle for the text surface and center it on the button's rectangle
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Blit (draw) the text surface onto the screen
        screen.blit(text_surface, text_rect)
        
    def pressed(self):
        if not self.enabled:
            return
        self.text = ""
        
    
        if self.action:
            self.action(self) 
            
        if self.num_neighbour_bombs > 0:
            self.text = str(self.num_neighbour_bombs)
        self.enabled = False
        if self.bomb:
            self.normal_color = BOMB_COLOR
            self.hover_color = BOMB_COLOR
            self.pressed_color = BOMB_COLOR
            self.current_color = BOMB_COLOR
            self.text = "B"
        else:
            self.normal_color = EMPTY_CELL_COLOR
            self.hover_color = EMPTY_CELL_COLOR
            self.pressed_color = EMPTY_CELL_COLOR
            self.current_color = EMPTY_CELL_COLOR
            
        # self.button.normal_color = RED
        # self.button.pressed_color = RED
        
        if self.bomb:
            self.color = GREEN
    
    
    def clear_bomb(self):
        self.bomb = False
    def handle_event(self, event):
        if not self.enabled:
            return False
        """
        Handles Pygame events relevant to the button (mouse motion, mouse clicks).

        Args:
            event (pygame.event.Event): A Pygame event object from the event queue.

        Returns:
            bool: True if the button was clicked and its associated action was performed,
                  False otherwise.
        """
        if event.type == pygame.MOUSEMOTION:
            # Check if the mouse cursor is currently over the button
            if self.rect.collidepoint(event.pos):
                self.is_hovered = True
                # Change color to hover color only if not currently pressed
                if not self.is_pressed: 
                    self.current_color = self.hover_color
            else:
                self.is_hovered = False
                # Revert to normal color only if not currently pressed
                if not self.is_pressed: 
                    self.current_color = self.normal_color

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button was pressed down
            
            if event.button == 3 and self.rect.collidepoint(event.pos):
                self.text = "F" if self.text == "" else ""
                return True
            if event.button == 1: # 1 is the left mouse button
                if self.is_hovered:
                    self.is_pressed = True
                    self.current_color = self.pressed_color # Change color to pressed color

        # elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the left mouse button was released
            if event.button == 1:
                # If the button was pressed and the mouse is still hovering (clicked)
                if self.is_pressed and self.is_hovered:
                    self.is_pressed = False
                    self.current_color = self.hover_color # Revert to hover color
                    self.pressed()
                    # if self.action:
                    #     self.action() # Execute the button's action function
                    #     return True # Indicate that the action was performed
                # Reset pressed state regardless of hover, to handle cases where mouse moves off while pressed
                self.is_pressed = False 
                # Set color back to normal or hover based on current mouse position
                self.current_color = self.normal_color if not self.is_hovered else self.hover_color
        return False
    