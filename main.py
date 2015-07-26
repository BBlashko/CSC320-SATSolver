import os
import sys
import string

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


def genGrid(string):
    arr = [[0 for x in range(9)] for x in range(9)]
    for i in range(8):
        for j in range(8):
            arr[i][j] = string[ i * 9 + j ]
    return arr


#-----MAIN-----#
line = parseFile(sys.argv[1])
grid = genGrid(line)


print("\nencodedLine = " + line)
