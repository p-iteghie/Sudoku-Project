import sys

import sudoku_generator as sg
from cell import Cell
from board import Board
import pygame
from constants import *
# test file

def printBoardConsole(board):
  print('-'*29)
  for i, row in enumerate(board):
    print(row[:3], row[3:6], row[6:])
    if i % 3 == 2:
      print('-' * 29) 
  
def main():
  hi = sg.generate_sudoku(9, 1)
  printBoardConsole(hi)
  cell_list = []
  # for Board.draw()
  for row_num, row in enumerate(hi):
    for col_num, i in enumerate(row):
      cell_list.append(Cell(i, row_num, col_num, 5))
  for i in cell_list:
    print(i.value, i.row, i.col)

  '''pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Welcome to Sudoku!")
  screen.fill(BG_COLOR)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        print(event.unicode)
    pygame.display.update()'''


if __name__ == '__main__':
  main()



  
'''
bens mistake ignore this pls (he doesn't want to delete his embarrasment -pat)(i put too much work i cant just delete it... -ben)
print('---------------------------') 
i=0
while i<9:
  j=0
  while j<3:
    k = i % 3
    
    print(hi[j][(3*k):(3*(k+1))], end ='')
    j+=1
  print('\n---------------------------') if i%3 == 2 else print()
  i += 1
'''