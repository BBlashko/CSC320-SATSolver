#Import the needed numbers to find which number is required for each row in the grid.
from utils import convertBase9

def generateRowCNF(f, grid):
  rows_list = []
  for x in range(9):
    rows = []
    for y in range(9):
      rows.append(grid[x][y])
    # Find the needed number for each of the rows, and once that is done, append the result of the rows into rows_list
    rows.append(rows)
    rows_list.append(rows)
  return rows_list

#-----generateColumnCNF(grid)-----#
#Purpose:
def generateColumnCNF(f, grid):
  columnslist = []
  for y in range(9):
    column = []
    for x in range(9):
      column.append(grid[x][y])

    #calculate the needed number in each column.
    #Eg. '001100000' columns needs numbers 2 and 3
    column.append(column)
    columnslist.append(column)
  return columnslist

def generate3X3CNF(f, grid):
  #Turn the grid into
  cnf = []
  for gridX in range(0, 3):    #Grid (3x3 boxes) along the X axis
    for gridY in range(0, 3):  #Grid (3x3 boxes) along the Y axis
      for z in range(1, 10):    #Numbers from 0-8 (possible input values, in base 9)
        for x in range(1, 3):
          for y in range(1, 3):

            #Minimal clauses
            for k in range(y + 1, 4):
              a = gridX * 3 + x
              b = gridY * 3 + y
              c = gridX * 3 + k
              f.write('-' + convertBase9(a,b,z) + ' -' + convertBase9(a,c,z) + ' 0\n')

            for k in range (x + 1, 4):
              for l in range(1, 4):
                a = gridX * 3 + x
                b = gridY * 3 + y
                c = gridX * 3 + k
                d = gridY * 3 + l
                f.write('-' +  convertBase9(a,b,z) + ' -' + convertBase9(c,d,z) + ' 0\n')


#Generate prefilled
def generatePrefilledCNF(f, grid):
  for y in range(9):
    for x in range(9):
      if grid[x][y] != '*':
        f.write(convertBase9(x, y, int(grid[x][y]))+ ' 0\n') #Terminate with a 0


#Generate individual
def generateIndivCNF(f, grid):
  for y in range(9):
    for x in range(9):
      for z in range(9):
        f.write(convertBase9(x, y, z)
      f.write(' \0n') # Terminate with a 0















