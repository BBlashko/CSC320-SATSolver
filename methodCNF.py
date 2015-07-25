def generateRowCNF(grid):
  return 1

#-----generateColumnCNF(grid)-----#
#Purpose:
def generateColumnCNF(grid):
  columnslist = []
  for x in range(9):
    column = []
    for y in range(9):
      column.append(grid[x][y])
    columnslist.append(column)
  return columnslist

def generate3X3CNF(grid):
  return 1
