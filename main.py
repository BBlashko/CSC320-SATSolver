import os
import sys
import string
from methodCNF import generateRowCNF, generateColumnCNF, generate3X3CNF

#-----parseFile(filename)-----#
#Purpose: encodes input file into one string
def parseFile(filename):
    try:
        open_file = open(filename)
    except:
        print("unable to open file: " + filename)

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


#-----MAIN-----#
line = parseFile(sys.argv[1])
grid = genGrid(line) #generate grid

columnList = generateColumnCNF(grid) #generate a list of columns
generate3X3CNF(grid)
