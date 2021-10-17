##import text
f = open("in.txt")
data = f.read()

##process into list structure
listy = data.rsplit('\n')

#part 1
def part1(I):
	visited = []
	
	curLine = 0
	accumulator = 0

	while curLine not in visited:
		if I[curLine][0:3] == "nop":
			visited.append(curLine)
			curLine = curLine +1
		
		elif I[curLine][0:3] == "acc":
			accumulator = accumulator + int(I[curLine][4:len(I[curLine])])
			visited.append(curLine)
			curLine = curLine +1
		
		elif I[curLine][0:3] == "jmp":
			visited.append(curLine)
			curLine = curLine +int(I[curLine][4:len(I[curLine])])
		
		else:
			print("ERROR!!!: " + I[curLine][0:3])
	
	return accumulator

#part 2
def part2(I):
	iterate = 0
	for x in I:
		if x[0:3] == "nop" or x[0:3] == "jmp":
			if x[0:3] == "nop":
				I[iterate] = x.replace("nop", "jmp")
			
			else:
				I[iterate] = x.replace("jmp", "nop")

			curLine = 0
			accumulator = 0
			visited = []

			while curLine not in visited:
				if curLine >= len(I):
					return accumulator

				elif I[curLine][0:3] == "nop":
					visited.append(curLine)
					curLine = curLine +1
				
				elif I[curLine][0:3] == "acc":
					accumulator = accumulator + int(I[curLine][4:len(I[curLine])])
					visited.append(curLine)
					curLine = curLine +1
				
				elif I[curLine][0:3] == "jmp":
					visited.append(curLine)
					curLine = curLine +int(I[curLine][4:len(I[curLine])])
				
				else:
					print("ERROR!!!: " + I[curLine][0:3])			
			
			if x[0:3] == "jmp":
				I[iterate] = x.replace("nop", "jmp")
			
			else:
				I[iterate] = x.replace("jmp", "nop")

		iterate = iterate+ 1

	return("err")

ans1 = part1(listy)
ans2 = part2(listy)

print("Answers:")
print(ans1)
print(ans2)