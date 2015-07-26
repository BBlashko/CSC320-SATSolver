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

    encodedLine = encodedLine.replace('.', '0').replace('*', '0').replace('?', '0')
    return encodedLine


#-----MAIN-----#
line = parseFile(sys.argv[1])
print("\nencodedLine = " + line)
