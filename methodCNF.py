#Import the needed numbers to find which number is required for each row in the grid.
from getNeededNumbers import getNeededNumbers


def generateRowCNF(grid):
  rows_list = []
  for x in range(9):
    rows = []
    for y in range(9):
      rows.append(grid[x][y])
    # Find the needed number for each of the rows, and once that is done, append the result of the rows into rows_list
    rows.append(getNeededNumbers(rows))
    rows_list.append(rows)
  return rows_list

#-----generateColumnCNF(grid)-----#
#Purpose:
def generateColumnCNF(grid):
  print("\ngetting needed numbers for generateColumnCNF \n")
  columnslist = []
  for y in range(9):
    column = []
    for x in range(9):
      column.append(grid[x][y])

    #calculate the needed number in each column.
    #Eg. '001100000' columns needs numbers 2 and 3
    column.append(getNeededNumbers(column))
    columnslist.append(column)

  return columnslist

def generate3X3CNF(grid):
  #Turn the grid into
  cnf = []
  for gridX in range(3):
    for gridY in range(3):
      tgrid = []
      for x in range(3):
        for y in range(3):
          xpos = gridX * 3 + x
          ypos = gridY * 3 + y
          tgrid.append(grid[x][y])
      cnf.append(getNeededNumbers(tgrid))
      cnf.append(tgrid)
  return cnf
