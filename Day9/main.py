##import text
f = open("in.txt")
data = f.read()

##process into list structure
listy = data.rsplit('\n')

#part 1
def part1(I):
	Valids = I[0:25]
	I = I[25:len(I)]

	for x in I:
		good = False
		for y in Valids:
			for z in Valids:
				if int(x) == int(y) + int(z) and y != z:
					good = True
		
		Valids = Valids[1:len(Valids)]
		Valids.append(x)
		
		if good == False:
			return x
	
	return("err")

#part 2
def part2(I):
	ran = []
	while ran == []:
		tot = 0
		index = 0

		for x in I:
			index = index + 1
			if tot == 3199139634:
				ran = I[0:index-1]
				tot = tot+1111
			else:
				tot = tot + int(x)

		I = I[1:len(I)]

	return(int(min(ran)) + int(max(ran)))
	

ans1 = part1(listy)
ans2 = part2(listy)

print("Answers:")
print(ans1)
print(ans2)

