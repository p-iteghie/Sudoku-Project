from constants import *
from cell import Cell
import pygame
import sudoku_generator as sg

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    if difficulty == 1:
      self.board = sg.generate_sudoku(9, 30)
    elif difficulty == 2:
      self.board = sg.generate_sudoku(9, 40)
    elif difficulty == 3:
      self.board = sg.generate_sudoku(9, 50)

    cell_list = []
    for row_num, row in enumerate(self.board):
      for col_num, i in enumerate(row):
        cell_list.append(Cell(i, row_num, col_num, self.screen))

  def draw(self):
    # test drawing
    pygame.draw.rect(self.screen, BUTTON_COLOR, [(WIDTH - BUTTON_WIDTH + BUTTON_BORDER) / 2, 400 + BUTTON_BORDER / 2, BUTTON_WIDTH - BUTTON_BORDER, BUTTON_HEIGHT - BUTTON_BORDER])