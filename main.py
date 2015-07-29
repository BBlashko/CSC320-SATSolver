import os
import sys
import string
import re
from methodCNF import generateRowCNF, generateColumnCNF, generate3X3CNF, generatePrefilledCNF, generateIndivCNF

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
#Purpose:
def genGrid(string):
  arr = [[0 for x in range(9)] for x in range(9)]
  for i in range(9):
    for j in range(9):
      arr[i][j] = string[ i * 9 + j ]
  return arr

#-----convertBase9(line)-----#
#Purpose: convert the encoded string to base 9 by subtracting 1 from all digits.
def convertBase9(x,y,z):
  return (x-1)*81 + (y-1)*9 + (z-1) + 1


#-----MAIN-----#
if len(sys.argv) < 2:
  print("Error: Incorrect arguments")
  print("To run: python main.py <input>")
  sys.exit(-1)

line = parseFile(sys.argv[1])
grid = genGrid(line) #generate grid

#All minimal (no extendid)
f = open('output.txt', 'w')
generatePrefilledCNF(f, grid) #generate prefilled stuff
generateIndivCNF(f, grid) #generate individual stuff
generateColumnCNF(f, grid) #generate a list of columns
generateRowCNF(f, grid) #generate a list of rows
generate3X3CNF(f, grid) #generate a list of boxes (3x3)
f.close()
