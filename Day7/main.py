##import text
f = open("in.txt")
data = f.read()

##process into list structure
listy = data.rsplit('\n')

## for pt 1
def canContain(bag, bagDic):
	if "shiny gold" in bag:
		return True

	if "other" in bag:
		return False
	
	for x in bagDic[bag]:
		x = x[3:len(x)]

		if "bags" not in x:
			x  = x + 's'
		
		x  = x + ' '
		
		if canContain(x, bagDic):
			return True

	return False
		
## for pt 2
def FakeContain(bag, bagDic):
	total = 0
	if bag[1] == 'n':
		return 0
	
	for x in bagDic[bag]:
		if x[1] == 'n':
			return 0
		else:
			numBags = int(x[1])
			total = total + numBags

		x = x[3:len(x)]

		if "bags" not in x:
			x  = x + 's'
		
		x  = x + ' '

		print(x)
		print(total)
		
		total = total + FakeContain(x, bagDic)*numBags
	
	return total

#part 1
def part1(I):
	out = 0

	bagDic = {}
	
	for x in I:
		x = x.replace('.', '')
		prt1 = x.rsplit("contain")
		prt2 = prt1[1].rsplit(',')

		prt1 = prt1 
	
		bagDic[prt1[0]] = prt2

	for x in bagDic: 
		if canContain(x, bagDic) and "shiny gold" not in x:
			out = out + 1

	return out

#part 2
def part2(I):
	bagDic = {}
	
	for x in I:
		x = x.replace('.', '')
		prt1 = x.rsplit("contain")
		prt2 = prt1[1].rsplit(',')

		prt1 = prt1 
	
		bagDic[prt1[0]] = prt2

	return FakeContain("shiny gold bags ", bagDic)

ans1 = part1(listy)
ans2 = part2(listy)

print("Answers:")
print(ans1)
print(ans2)

