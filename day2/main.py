##import text
f = open("in.txt")
data = f.read()

##process into data structure
listy = data.rsplit('\n')
goods = 0

for x in listy:
	indStr = x.rsplit(':')
	badlimCarStr = indStr[0].rsplit(' ')
	limCarStr = badlimCarStr[0].rsplit('-')
	limCarStr.append(badlimCarStr[1])
	limCarStr.append(indStr[1])

	##part a
	##	numTimes = limCarStr[3].count(limCarStr[2])
	##	if numTimes >= int(limCarStr[0]) and numTimes <= int(limCarStr[1]):
	##		goods = goods+1
	##		print("I am good boi: ")

	##part b 
	pos1 = limCarStr[2]==limCarStr[3][int(limCarStr[0])]
	pos2 = limCarStr[2]==limCarStr[3][int(limCarStr[1])]
	if pos1 != pos2:
		goods = goods +1
		print("I am good boi: ")
	print(x)

print(goods)

