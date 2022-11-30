from constants import *
import pygame

class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value # value will be numbers 1-9
    self.row = row
    self.col = col
    self.screen = screen

  def set_cell_value(self, value):
    self.value = value

  def set_sketched_value(self, value):
    self.value = value

  def draw(self):
    # draw cell with value inside
    
    # display value in cell if the value is not zero

    # if the value is zero, do not display anything

    # outline cell in red if selected by user
  
if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Welcome to Sudoku")
  screen.fill(BG_COLOR)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    pygame.display.update()