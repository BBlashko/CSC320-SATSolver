import os
import sys
import string
import re
from methodCNF import generateRowCNF, generateColumnCNF, generate3X3CNF, generatePrefilledCNF, generateIndivCNF
from utils import convertBase9
from subprocess import call

#-----parseFile(filename)-----#
#Purpose: encodes input file into one string
def parseFile(filename):
  try:
    open_file = open(filename)
  except:
    print("Error: File not found")
    print("Unable to open file: " + filename)
    sys.exit(-1)

  content = open_file.readlines()
  encodedLine = ""
  for line in content:
    encodedLine += ''.join(line.split())

  encodedLine = encodedLine.replace('.', '*').replace('0', '*').replace('?', '*')
  return encodedLine

#-----genGrid(filename)-----#
#Purpose: create a 2 by 2 array of the input puzzle
def genGrid(string):
  arr = [[0 for x in range(9)] for x in range(9)]
  for i in range(9):
    for j in range(9):
      arr[i][j] = string[ i * 9 + j ]
  return arr


#-----MAIN-----#
#Purpose: Controls the main flow of the program

print("Starting the SAT Solver!\n")
if len(sys.argv) < 2:
  print("Error: Incorrect arguments")
  print("To run: python main.py <input>")
  sys.exit(-1)

line = parseFile(sys.argv[1])
grid = genGrid(line) #generate grid

#generate minimal clauses
clauses = 0
f = open('tempOutput.txt', 'w')
clauses += generatePrefilledCNF(f, grid) #generate prefilled stuff
clauses += generateIndivCNF(f, grid) #generate individual stuff
clauses += generateColumnCNF(f, grid) #generate a list of columns
clauses += generateRowCNF(f, grid) #generate a list of rows
clauses += generate3X3CNF(f, grid) #generate a list of boxes (3x3)
f.close()

f = open('tempOutput.txt','r')
temp = f.read()
f.close()

f = open('tempOutput.txt', 'w')
f.write("p cnf 729 " + str(clauses) + "\n")

f.write(temp)
f.close()

# input into minisat
call(["minisat", "tempOutput.txt", "SATOutput.txt"])

# Decode output file
f = open('SATOutput.txt','r')
sat = f.readline().strip()

print("\nInput puzzle:\n")

# print input puzzle
open_file = open("SolvedPuzzle.txt", 'w')
open_file.write("SAT Solver: Sudoku!\n\n")
open_file.write("\nInput puzzle:\n")
for x in range(0, 9):
  line = ''
  for y in range(0, 9):
    line = line + grid[x][y] + " "
  print(line + "\n")
  open_file.write(line + "\n")

open_file.write("\n\n")

# output solved sudoku solver.
if(sat == 'SAT'):
  print('\nProblem is Satisfiable!')
  print('\nSolved Puzzle:\n')
  numbers = f.readline()
  asArr = numbers.split(' ')

  for i in range(len(asArr)):
    asArr[i] = int(asArr[i])

  open_file.write("Solved Puzzle: \n")

  for y in range(9):
    line = ''
    for x in range(9):
      for z in range(9):
        if(asArr[y*81 + 9*x + z] >= 0):
          line = line + str(z + 1) + ' '
          break
    print(line + '\n')
    open_file.write(line + '\n')

else:
  print('\nProblem is unsatisfiable.')
  open_file.write("'\nProblem is unsatisfiable.'")
