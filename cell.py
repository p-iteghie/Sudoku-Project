from constants import *
import pygame

class CELL:
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
    # draw CELL with value inside
    CELL_with_value = pygame.Rect((WIDTH - CELL_WIDTH + CELL_BORDER) / 2, 400 + CELL_BORDER / 2, CELL_WIDTH - CELL_BORDER, CELL_HEIGHT - CELL_BORDER)
    # display value in CELL if the value is not zero
    #TEST BELOW SHOWS A VALUE JUST NOT IN RIGHT SPOT
    self.screen.blit(self.value_drawn, ((WIDTH - self.value_drawn.get_rect().width) / 2, 400 + (CELL_HEIGHT - self.value_drawn.get_rect().height) / 2))
    # if the value is zero, do not display anything

    # outline CELL in red if selected by user
