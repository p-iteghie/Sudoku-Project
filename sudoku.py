import sudoku_generator as sg
# test file

def main():
  hi = sg.generate_sudoku(9, 2)

  i=0
  print(hi)
  while i<8:
    print(hi[i][:3])
    print(hi[i][i])
    i+=1


if __name__ == '__main__':
  main()
  