#Generate the rows 
def generateRowCNF(grid):
	rows_list = []
	for y in range(GRID):
	rows = []
		for x in range(GRID):
		rows.append(grid[x][y])
		rows_list.append(rows)
	return rows_list

def generateColumnCNF(grid):
  return 1

def generate3X3CNF(grid):
  return 1
