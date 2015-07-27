from getNeededNumbers import getNeededNumbers

def generateRowCNF(grid):
  return 1

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
  return 1
