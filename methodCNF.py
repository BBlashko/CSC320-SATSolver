#Import the needed numbers to find which number is required for each row in the grid.

from getNeededNumbers import getNeededNumbers

#Generate the rows 
def generateRowCNF(grid):
	rows_list = []
	for y in range(GRID):
	rows = []
		for x in range(GRID):
			rows.append(grid[x][y])
	# Find the needed number for each of the rows, and once that is done, append the result of the rows into rows_list		
	rows.append(getNeededNumbers(rows))
    	rows_list.append(rows)
    	
return rows_list

def generateColumnCNF(grid):
  return 1

def generate3X3CNF(grid):
  return 1
