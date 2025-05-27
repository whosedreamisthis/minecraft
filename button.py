import pygame
from consts import *
class Button:
    """
    A customizable button class for Pygame applications.
    Handles drawing, hover effects, and click actions.
    """
    def __init__(self, x, y, width, height, text, action=None,
                 normal_color = (1,0,200), hover_color = (200,200,200), pressed_color = (20,20,20),
                 font_size = 18, font_color=BLACK):
        """
        Initializes a button instance.

        Args:
            x (int): X-coordinate of the top-left corner of the button.
            y (int): Y-coordinate of the top-left corner of the button.
            width (int): Width of the button.
            height (int): Height of the button.
            text (str): The text string to display on the button.
            normal_color (tuple): RGB color tuple for the button's default state.
            hover_color (tuple): RGB color tuple for the button when hovered over.
            pressed_color (tuple): RGB color tuple for the button when clicked.
            font_size (int): Size of the font for the button text.
            font_color (tuple): RGB color tuple for the button text.
            action (callable, optional): A function to be called when the button is clicked.
                                        Defaults to None.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.font_color = font_color
        self.action = action

        # Initialize the font for rendering text
        # Using None for default Pygame font, you can specify a font file path here
        self.font = pygame.font.Font(None, font_size) 

        self.current_color = self.normal_color # Tracks the current color state
        self.is_hovered = False # True if mouse is over the button
        self.is_pressed = False # True if the button is currently being held down

    def draw(self, screen):
        """
        Draws the button on the specified Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame surface to draw the button on.
        """
        # Draw the main button rectangle with rounded corners for a modern look
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=0)

        # Render the text surface
        text_surface = self.font.render(self.text, True, self.font_color)
        
        # Get the rectangle for the text surface and center it on the button's rectangle
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Blit (draw) the text surface onto the screen
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
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
            if event.button == 1: # 1 is the left mouse button
                if self.is_hovered:
                    self.is_pressed = True
                    self.current_color = self.pressed_color # Change color to pressed color

        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the left mouse button was released
            if event.button == 1:
                # If the button was pressed and the mouse is still hovering (clicked)
                if self.is_pressed and self.is_hovered:
                    self.is_pressed = False
                    self.current_color = self.hover_color # Revert to hover color
                    if self.action:
                        self.action() # Execute the button's action function
                        return True # Indicate that the action was performed
                # Reset pressed state regardless of hover, to handle cases where mouse moves off while pressed
                self.is_pressed = False 
                # Set color back to normal or hover based on current mouse position
                self.current_color = self.normal_color if not self.is_hovered else self.hover_color
        return False