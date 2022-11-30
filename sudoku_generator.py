import math,random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
      self.row_length = row_length
      self.removed_cells = removed_cells
      self.board = [[0] * row_length for i in range(0, row_length)]
      self.box_length = int(math.sqrt(row_length))

    def get_board(self):
      return self.board

    def print_board(self):
      print(self.board)

    def valid_in_row(self, row, num):
      for i in self.board[row]:
        if i == num:
          return False
      return True

    def valid_in_col(self, col, num):
      for current_row in range(self.row_length):
        if self.board[current_row][col] == num:
          return False
      return True

    def valid_in_box(self, row_start, col_start, num):
      for current_row in range(row_start, row_start + 3):
        for current_col in range(col_start, col_start + 3):
          if self.board[current_row][current_col] == num:
            return False
      return True
    
    def is_valid(self, row, col, num): 
      if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row // 3 * 3, col // 3 * 3, num) == True:
        return True
      else:
        return False

    def fill_box(self, row_start, col_start):
      numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      random.shuffle(numbers)
      i = 0
      for current_row in range(row_start, row_start + 3):
        for current_col in range(col_start, col_start + 3):
          self.board[current_row][current_col] = numbers[i]
          i += 1

    def fill_diagonal(self):
      self.fill_box(0, 0)
      self.fill_box(3, 3)
      self.fill_box(6, 6)

    def fill_remaining(self, row, col):  # Given to us
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # Given to us
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
      cells_to_remove = self.removed_cells
      while cells_to_remove > 0:
        current_row = random.randint(0, self.row_length - 1)
        current_col = random.randint(0, self.row_length - 1)
        if self.board[current_row][current_col] != 0:
          self.board[current_row][current_col] = 0
          cells_to_remove -= 1

def generate_sudoku(size, removed):  # Given to us
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
