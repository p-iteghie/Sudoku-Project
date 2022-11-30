import sudoku_generator as sg
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