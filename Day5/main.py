import math

print("------")
##import text
f = open("in.txt")
data = f.read()

##process into data structure
listy = data.rsplit('\n')

#variables for next section
out = []
last = -1

def findLoc(dat, block):
	if len(block) < 2:
		return block[0]
	if dat[0] == 'F' or dat[0] == 'L':
		dat = dat[1:len(dat)]
		return(findLoc(dat, range(block[0], round((block[-1]+block[0]+1)/2))))
	if dat[0] == 'B' or dat[0] == 'R':
		dat = dat[1:len(dat)]
		return(findLoc(dat, range(round((block[-1]+block[0]+1)/2), block[-1]+1)))

##data processing
for x in listy:
	rowStr = x[0:7]
	posStr = x[7:10]

	row = findLoc(rowStr, range(128))
	pos = findLoc(posStr, range(8))

	passID = row * 8 + pos
	print(passID)

	out.append(passID)

print("Ans--------")
out.sort()
for x in out:
	if int(x) != int(last)+1:
		print(x-1)
	last = x
