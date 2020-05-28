fIn = open("test.txt", "r")
fOut = open("210王品智.txt", "w")

inPut = fIn.readlines()
outPut = str(inPut[0])

for i in range(1, len(inPut)):
  line = inPut[i].split( )
  line.sort()
  for j in range(len(line)):
    outPut += '%s ' % line[j]
  outPut += '\n'

fOut.write(outPut)

fIn.close()
fOut.close()
