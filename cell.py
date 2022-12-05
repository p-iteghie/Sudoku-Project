from constants import *
import pygame

class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value # value will be numbers 0-9
    self.row = row
    self.col = col
    self.screen = screen
    value_font = pygame.font.Font("Luciole-Bold.ttf", 50)
    self.value_drawn = value_font.render(str(value), True, TEXT_COLOR)
    self.cell = pygame.Rect(self.col * CELL_DIM, self.row * CELL_DIM, CELL_DIM, CELL_DIM)

  def set_cell_value(self, value):
    self.value = value

  def set_sketched_value(self, value):
    self.value = value

  def draw(self):
    # draw cell with value inside
    


    # color variable to see if cell is selected
    color = CELL_BORDER_UNHIGHLIGHTED
    active = False


    if active:
      color = CELL_BORDER_HIGHLIGHTED
    else:
      color = CELL_BORDER_UNHIGHLIGHTED
    
    pygame.draw.rect(self.screen, color, self.cell, CELL_BORDER)
    # display value in cell if the value is not zero
    #TEST BELOW SHOWS A VALUE JUST NOT IN RIGHT SPOT
    self.screen.blit(self.value_drawn, (self.col * CELL_DIM, self.row * CELL_DIM))
    # if the value is zero, do not display anything

    # outline cell in red if selected by user
