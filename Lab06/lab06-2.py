def mySort(arrIn):
  for i in range(len(arrIn)):
    for j in range(len(arrIn) - 1 - i):
      if(arrIn[j]>arrIn[j+1]):
        t = arrIn[j]
        arrIn[j] = arrIn[j+1]
        arrIn[j+1] = t
  return arrIn

fIn = open("test.txt", "r")
fOut = open("210王品智.txt", "w")

inPut = fIn.readlines()
outPut = str(inPut[0])

for i in range(1, len(inPut)):
  singalLine = inPut[i].split( )
  singalLine = mySort(singalLine)
  for j in range(len(singalLine)):
    outPut += str(singalLine[j])
    outPut += ' '
  outPut += '\n'

fOut.write(outPut)

fIn.close()
fOut.close()
