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

  def set_cell_value(self, value):
    self.value = value

  def set_sketched_value(self, value):
    self.value = value

  def draw(self):
    self.screen.blit(self.value_drawn, ((WIDTH - self.value_drawn.get_rect().width) / 2, 400 + (BUTTON_HEIGHT - self.value_drawn.get_rect().height) / 2))
    # draw cell with value inside
    
    # display value in cell if the value is not zero

    # if the value is zero, do not display anything

    # outline cell in red if selected by user
