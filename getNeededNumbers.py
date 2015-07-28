
#-----getNeededNumbers(sector)-----#
#Purpose: Given a single column, row, 9x9 box, determine what numbers are needed
#         outputs needed number into a string of 0's and 1's if number needed location in string is a 1
#         EG. returns "000011001" numbers needed are 5, 6, 8
def getNeededNumbers(sector):
  neededNumbers = ['1', '1', '1', '1', '1', '1', '1', '1', '1']

  print(sector)
  #for each character in sector determine if number is present. if so replace
  #numbers corresponding location with a '0'
  for character in sector:
    if(character == '0'):
      neededNumbers[0] = neededNumbers[0].replace('1', '0')
    elif(character == '1'):
      neededNumbers[1] = neededNumbers[1].replace('1', '0')
    elif(character =='2'):
      neededNumbers[2] = neededNumbers[2].replace('1', '0')
    elif(character == '3'):
      neededNumbers[3] = neededNumbers[3].replace('1', '0')
    elif(character == '4'):
      neededNumbers[4] = neededNumbers[4].replace('1', '0')
    elif(character == '5'):
      neededNumbers[5] = neededNumbers[5].replace('1', '0')
    elif(character == '6'):
      neededNumbers[6] = neededNumbers[6].replace('1', '0')
    elif(character == '7'):
      neededNumbers[7] = neededNumbers[7].replace('1', '0')
    elif(character == '9'):
      neededNumbers[8] = neededNumbers[8].replace('1', '0')

  #convert neededNumbers back into a string and return
  neededNumbers = "".join(neededNumbers)
  print(neededNumbers)
  return neededNumbers
