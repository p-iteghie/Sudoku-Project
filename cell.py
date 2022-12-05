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

  def set_CELL_value(self, value):
    self.value = value

  def set_sketched_value(self, value):
    self.value = value

  def draw(self):
    # draw cell with value inside
    cell = pygame.Rect(CELL_DIM, CELL_DIM, self.col * CELL_DIM, self.row * CELL_DIM)
    # display value in cell if the value is not zero
    #TEST BELOW SHOWS A VALUE JUST NOT IN RIGHT SPOT
    self.screen.blit(self.value_drawn, (self.col * CELL_DIM, self.row * CELL_DIM)
    # if the value is zero, do not display anything

    # outline cell in red if selected by user
