fIn = open("test.txt", "r")
fOut = open("210王品智.txt", "w")

inPut = fIn.readlines()
outPut = []

n = 0
for i in range(len(inPut[0])-1):
  n*=10
  n+=int(inPut[0][i])

for i in range(1,len(inPut)):
  line = []
  j=0
  while (j < len(inPut[i])-1):
    n=0
    while (inPut[i][j]>= '0' and inPut[i][j]<= '9' and j<len(inPut[i])):
      n*=10
      n+=int(inPut[i][j])
      j+=1
    j+=1
    line.append(n)
  line.sort()
  outPut.append(line)

text=str(inPut[0])
for i in range(len(outPut)):
  for j in range(len(outPut[i])):
    text+=str(outPut[i][j])
    text+=" "
  text+='\n'
fOut.write(text)

fIn.close()
fOut.close()
