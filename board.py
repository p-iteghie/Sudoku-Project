from constants import *
from cell import Cell
import pygame
import sudoku_generator as sg

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.temp_board = sg.SudokuGenerator(9,0)
    if difficulty == 1:
      self.board = sg.generate_sudoku(9, 1)
    elif difficulty == 2:
      self.board = sg.generate_sudoku(9, 40)
    elif difficulty == 3:
      self.board = sg.generate_sudoku(9, 50)

    self.cell_list = []
    for row_num, row in enumerate(self.board):
      for col_num, i in enumerate(row):
        self.cell_list.append(Cell(i, row_num, col_num, self.screen))

  def draw(self):
    for y in range(3):
      for x in range(3):
        group = pygame.Rect(CELL_DIM * 3 * x, CELL_DIM * 3 * y, CELL_DIM * 3, CELL_DIM * 3)
        pygame.draw.rect(self.screen, TEXT_COLOR, group, CELL_BORDER)
            
    for i in self.cell_list:
      i.draw()
      
  def is_filled(self):
    for cell in self.cell_list:
      if cell.value == 0:
        return False
    return True

  def check_win(self):
    self.temp_board.board = self.board
    for cell in self.cell_list:
      self.temp_board.board[cell.row][cell.col] = int(cell.value)
    print(self.temp_board.board)

    for row_num, row in enumerate(self.temp_board.board):
      print(row)
      for col_num, num in enumerate(row):
        print(row_num, col_num)
        print(num)
        if not self.temp_board.is_valid(row_num, col_num, num):
          print('lose')
          # return False
    print('win')
    return True

    