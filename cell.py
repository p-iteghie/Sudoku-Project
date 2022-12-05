from constants import *
import pygame

class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value # value will be numbers 0-9
    self.row = row
    self.col = col
    self.screen = screen
    self.value_font = pygame.font.Font("Luciole-Regular.ttf", 50)
    self.value_drawn = self.value_font.render(str(value), True, TEXT_COLOR)
    self.cell = pygame.Rect(self.col * CELL_DIM, self.row * CELL_DIM, CELL_DIM, CELL_DIM)
    self.color = CELL_BORDER_UNHIGHLIGHTED
    self.sketch = 0
    if value != 0:
      self.editable = False
    else:
      self.editable = True


  def set_cell_value(self, value):
    self.value = value
    self.value_drawn = self.value_font.render(str(self.value), True, TEXT_COLOR)

  '''def set_sketched_value(self, value):
    self.value = value'''

  def draw(self):
    pygame.draw.rect(self.screen, self.color, self.cell, int(CELL_BORDER / 2))
    sketch_font = pygame.font.Font("Luciole-Regular.ttf", 30)
    sketch_drawn = sketch_font.render(str(self.sketch), True, SKETCH_COLOR)

    if self.value != 0:
      self.screen.blit(self.value_drawn, (self.col * CELL_DIM + (36 / 2), self.row * CELL_DIM + (34 / 2)))
    if self.sketch != 0:
      self.screen.blit(sketch_drawn, (self.col * CELL_DIM + 3, self.row * CELL_DIM + 3))

