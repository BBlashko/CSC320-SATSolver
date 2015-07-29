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
for y in range(9):
		for z in range(9):
			for x in range(8):
				for (i=x+1 in range(9)):
					f.write(convertBase9(x, y, z)+ " "+  convertBase9(i, y, z) + "\0n")
					

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
  for gridX in range(3):
    for gridY in range(3):
      tgrid = []
      for x in range(3):
        for y in range(3):
          xpos = gridX * 3 + x
          ypos = gridY * 3 + y
          tgrid.append(grid[xpos][ypos])
      cnf.append(tgrid)
      cnf.append(tgrid)
  return cnf



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


					
		



void generateRowCNF(char *input)
{
	int x, y, z, i;
	char tempBuffer[TEMPBUFFERSIZE];
	
	sprintf(input, "c ***Clauses for Rows***\n");
	for (y=1; y<=9; y++)
	{
		for (z=1; z<=9; z++)
		{
			/*Generates the required minimal clauses*/
			for (x=1; x<=8; x++)
			{
				for (i=x+1; i<=9; i++)
				{
					sprintf(tempBuffer, "-%d -%d 0\n", convertNumber(x,y,z), convertNumber(i,y,z));
					strcat(input, tempBuffer);
					CLAUSECOUNT++;
				}
			}
			
			/*Generates the extended clauses*/
			if(SOLVINGMODE == EXTENDED)
			{
				sprintf(tempBuffer, "%d %d %d %d %d %d %d %d %d 0\n", convertNumber(1,y,z), convertNumber(2,y,z), convertNumber(3,y,z),
				 convertNumber(4,y,z), convertNumber(5,y,z), convertNumber(6,y,z), convertNumber(7,y,z), convertNumber(8,y,z),
				 convertNumber(9,y,z));
				strcat(input, tempBuffer);
				CLAUSECOUNT++;
			}
			
		}
	}
}













